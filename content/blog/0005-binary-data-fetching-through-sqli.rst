Binary data fetching through SQLi
#################################
:date: 2009-02-23 22:45
:author: jekil
:category: Research
:tags: binary data, blob, data casting, SQL Injection
:slug: binary-data-fetching-through-sqli
:status: published
:alias: /paper/binary-data-fetching-through-sqli

Table of contents
-----------------

| 1. Introduction
| 2. How BLOB storage works
| 3. Casting binary data
| 3.1 MySQL
| 3.2 PostgreSQL
| 3.3 SQL Server
| 4. References

1. Introduction
---------------

Exploiting a SQL injection flaw in a web application can give the
attacker full control of the remote DBMS. One of the major consequences
of exploiting consists in fetching all or part of the data stored in the
database.

In several cases, like a web application that stores images on the
database, the attacker has to deal with binary data.

Follows some techniques to fetch binary data via a SQL injection flaw.

2. How BLOB storage works
-------------------------

According to Wikipedia a BLOB[1] is:

    A binary large object, also known as a blob, is a collection of
    binary data stored as a single entity in a database management
    system. Blobs are typically images, audio or other multimedia
    objects, though sometimes binary executable code is stored as a
    blob. Database support for blobs is not universal.

    Blobs were originally just amorphous chunks of data invented by Jim
    Starkey at DEC, who describes them as "the thing that ate
    Cincinnati, Cleveland, or whatever". Later, Terry McKiever, a
    marketing person for Apollo felt that it needed to be an acronym and
    invented the backronym Basic Large Object. Then Informix invented an
    alternative backronym, Binary Large Object. Today many people
    believe that blob was originally intended as an acronym for
    something.

The BLOB data can be stored in the DBMS tables or as usual file system
files linked by a pointer in the data table.  The BLOB storage engine 
is built with one or a combination of these techniques to get the best
performances.

The BLOB storage is handled by the DBMS engine that provides high level
SQL statement to the user.

3. Casting Binary data
----------------------

The idea behind the hack is to cast the BLOB data to another data-type
that can be fetched via SQLi. For example: cast a BLOB to a string
containing the BLOB encoded in base64, so we can use a string
representation of binary object that acts as middleware to fetch data
over any type of SQL injection.

As far as I know there are no public automatic SQL injection tools that
can fetch binary data from a vulnerable web application.

3.1 MySQL
---------

In MySQL SQL syntax the function HEX()[2] can be used to get the
hexadecimal value of one field of any data-type. The function
HEX(\`foo\`) returns a string representation of the hexadecimal value of
foo, where foo is a binary large object (BLOB). So we can cast a binary
data-type to a string data-type.

For example the following SQL statement returns the hexadecimal value of
the binary object stored in the field named blob:

.. code-block:: mysql

    SELECT HEX(`blob`) FROM footable;

Now we can use the hexadecimal BLOB representation to fetch data from
binary (BLOB) fields using the standard techniques to fetch data via SQL
injection or blind SQL injection.

Using HEX() we can deal a BLOB as a text string and use the common
techniques and tools.

Once we have fetched the binary data encoded as hexadecimal, we have to
restore the original binary data out of it. We can use the SQL UNHEX()
function, that get a hexadecimal string and outputs a BLOB object, a
command line utility or a few lines in you favorite programming language
can do the trick.

This is the easy way to get a textual representation of BLOB under
MySQL, the HEX() function is supported from MySQL 4.1.

4.2 PostgreSQL
--------------

PostgreSQL can not store values of more than several thousands bytes
within any data-type except large objects, nor can binary data be easily
entered within single quotes. Instead, large objects (BLOB) are used to
store very large values and binary data.

BLOB permits storage of any operating system file, including images or
large text files, directly into the database.

As you can see in the DBMS data-type comparison sheet[3] PostgreSQL
stores BLOB data in a data-type called OID that acts like a pointer to
the stored object on the file system.

For example using the psql client from command line you can load the
file into the database using lo\_import(), and retrieve it from the
database using lo\_export() which works only for local files[4].

.. code-block:: psql

    postgres=# CREATE TABLE foo (image OID);
    CREATE TABLE
    postgres=# INSERT INTO foo VALUES (lo_import('/tmp/bar.jpg'));
    INSERT 0 1

The lo\_import() function stores /tmp/bar.jpg into the database. The
function call returns an OID that is used to refer the imported large
object. This value is stored in foo.image as an integer.

If you want to read the foo.image value the lo\_export() function uses
the OID value to find the large object stored in the database, then
places the exported file into the output file.

Full path names must be used with large objects because the database
server runs in a different directory than the psql client. Files are
imported and exported by the postgres user, so postgres must have
permission to read the file for lo\_import() and directory write
permission for lo\_export().

There are others functions to manage large objects (BLOB) available
under PostreSQL[5].

Because large objects uses the local filesystem, users connecting over a
network can not use lo\_import() or lo\_export(). They can, however, use
psql's \\lo\_import and \\lo\_export commands.

If we are exploiting a SQL injection in a web application we can't use
the functions lo\_import() and lo\_export() but we need a way to get the
juice data on the vulnerable server.

From PostgreSQL documentation "String Functions and Operators"[6] we
catch the function ENCODE(data bytea, type text).

This function encodes binary data to an ASCII-only representation. The
supported types are: base64, hex, escape.

Now we have the function to convert a bytea data-type into a base64 or
hex string. We need only to convert the BLOB OID in a bytea.

The fastest way to do this is a two step recipe: first get the number of
OID that you need and after quering the system table pg\_largeobject.

.. code-block:: psql

    postgres=# SELECT image FROM foo;
    image
    ——-
    16387
    (1 row)
    postgres=# SELECT ENCODE(data, 'base64') FROM pg_largeobject WHERE LOID=16387;
    encode
    ——————————————————————————
    JVBERi0xLjINJeLjz9MNCjIwOSAwIG9iag08PCANL0xpbmVhcml6ZWQgMSAN
    IDYyOCA4NTEgXSANL0wgMjU4NDYxOCANL0UgMTI5NDg1IA0vTiAxNiANL
    DWVuZG9iag0gICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIC
    [snip..]
    M2I4MWJkNTdlOTNjNWVmNj5dDT4+DXN0YXJ0eHJlZg0xNzMNJSVFT0YN
    (1263 rows)

Now you get your goal and you can fetch a BLOB on PostgreSQL with only
two queries.

For further details on PostgreSQL BLOB functions you can refer to "SQLi:
Writing files to disk under PostgreSQL"[7].

3.3 SQL Server
--------------

SQL Server stores binary data in the following data-types: BINARY,
VARBINARY, IMAGE.

You can create a demo table for your test with:

.. code-block:: sql

    CREATE TABLE dbo.foo
    (
    image image NULL
    )  ON [PRIMARY]
    TEXTIMAGE_ON [PRIMARY]
    GO

You can insert the file foo.bmp with the following:

.. code-block:: sql

    INSERT INTO [tempdb].[dbo].[foo]
    ([image])
    SELECT * FROM
    OPENROWSET(BULK N'C:\foo.bmp', SINGLE_BLOB) AS i  
    GO

The binary data can be converted to a hex string injecting a stored
procedure in SQL Server. This is described in Microsoft kb104829[8].

.. code-block:: sql

    create procedure sp_hexadecimal  
    @binvalue varbinary(255)  
    as  
    declare @charvalue varchar(255)  
    declare @i int  
    declare @length int  
    declare @hexstring char(16)
    
    select @charvalue = '0x'  
    select @i = 1  
    select @length = datalength(@binvalue)  
    select @hexstring = "0123456789abcdef"
    
    while (@i <= @length)  
    begin
    
    declare @tempint int  
    declare @firstint int  
    declare @secondint int
    
    select @tempint = convert(int, substring(@binvalue,@i,1))  
    select @firstint = floor(@tempint16)  
    select @secondint = @tempint - (@firstint*16)
    
    select @charvalue = @charvalue +  
    substring(@hexstring, @firstint+1, 1) +  
    substring(@hexstring, @secondint+1, 1)
    
    select @i = @i + 1
    
    end
    
    select 'sp_hexadecimal'=@charvalue

3.4 Other DBMS
--------------

The same technique can be used in any other DBMS like Oracle, DB2,
Informix that have casting functions or BLOB conversion functions.

4. References
-------------

| [1] http://en.wikipedia.org/wiki/Binary_large_object
| [2] http://dev.mysql.com/doc/mysql/en/String_functions.html
| [3]
  http://www.lonerunners.net/1246-database-datatype-comparison-sheet.html
| [4]
  http://www.postgresql.org/files/documentation/books/aw_pgsql/node96.html
| [5] http://www.postgresql.org/docs/8.3/interactive/largeobjects.html
| [6]
  http://www.postgresql.org/docs/8.1/interactive/functions-string.html
| [7]
  http://lab.lonerunners.net/blog/sqli-writing-files-to-disk-under-postgresql
| [8] http://support.microsoft.com/kb/104829
