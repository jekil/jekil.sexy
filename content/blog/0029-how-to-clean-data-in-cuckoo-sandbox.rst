How to clean data in Cuckoo Sandbox
###################################
:date: 2015-03-02 00:15
:author: jekil
:category: Tools
:tags: cuckoo
:slug: how-to-clean-data-in-cuckoo-sandbox
:status: published
:alias: /tools/how-to-clean-data-in-cuckoo-sandbox/

Starting with `Cuckoo Sandbox <http://cuckoosandbox.org/>`__ 1.2, which
will be released soon, the old data cleanup tool will be deprecated in
favor of a new cleanup method.

The old clean tool, still available, it is the clean.sh script in the
tools directory. It is a bash script used to delete the data inside the
storage directory (malware samples and reports), logs directory and db
directory. The downside is that if you are not using SQLite database but
 MySQL or PostgreSQL and if you enable the MongoDB reporting module to
store analysis results in MongoDB, clean.sh won't clean up that data,
leaving you in a dirty situation.

In Cuckoo 1.2 clean.sh has been deprecated and a new clean up method is
provided, using the *--clean* argument when calling cuckoo.py:

.. code-block:: console

    $ python cuckoo.py --clean

Running this command all the data will be deleted: storage directory
(malware samples and reports), logs directory, data inside any database
configured and MongoDB data if the related reporting module is enabled.

Easy peasy!
