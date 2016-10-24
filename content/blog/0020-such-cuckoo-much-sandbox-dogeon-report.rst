Such Cuckoo, much sandbox: dogeon report
########################################
:date: 2014-06-08 23:07
:author: jekil
:category: Tools
:tags: cuckoo, doge
:slug: such-cuckoo-much-sandbox-dogeon-report
:status: published
:alias: /tools/such-cuckoo-much-sandbox-dogeon-report

Several days ago I discovered one of the best projects of this year:
`dogeon <http://dogeon.org/>`__.

*DSON (Doge Serialized Object Notation) is a data-interchange format,
that is easy to read and write for Shiba Inu dogs. It is easy for
machines to parse and generate. It is designed to be as similiar as
possible to the `DogeScript Programming
Language <https://github.com/remixz/dogescript>`__. DSON is a text
format that is not language independent but uses conventions that are
familiar to a wide variety of japanese dog breeds. These properties make
DSON an ideal data-interchange language for everything that involves
Shiba Inu intercommunication.*

`Cuckoo <http://cuckoosandbox.org>`__ is such sandbox, lol malware,
 very sandbox. So, I did it.

First of all I found this `great
library <https://github.com/soasme/dogeon>`__ written in Python,
because of Shiba Inu code Python.

Writing modules in Cuckoo is amazingly easy, check out the documentation
about reporting
modules: \ http://docs.cuckoosandbox.org/en/latest/customization/reporting/

I used  json module as a starting point, changing just a few lines, I
imported dogeon library and used it to dump the Cuckoo results dict.
This is the code (available on
`Github <https://github.com/jekil/cuckoo-fu/blob/master/modules/reporting/dogeon.py>`__
too):

.. code-block:: python

    import os
    import dson
    import codecs

    from lib.cuckoo.common.abstracts import Report
    from lib.cuckoo.common.exceptions import CuckooReportError

    class DogeonDump(Report):

        def run(self, results):
            try:
                path = os.path.join(self.reports_path, "report.doge")
                report = codecs.open(path, "w", "utf-8")
                dson.dump(results, report, indent=4)
                report.close()
            except (UnicodeError, TypeError, IOError) as e:
                raise CuckooReportError("Failed to generate Dogeon report: %s" % e

To install this setup requirements with:

.. code-block:: console

    pip install dogeon

Copy the reporting module in reporting modules folder, in
/modules/reporting. Enable it adding the following lines to
reporting.conf, in /conf/reporting.conf:

.. code-block:: text

    [dogeon]
    enabled = yes

Run cuckoo and a report will be like:

.. code-block:: text

    such
        "info" is such
            "category" is "file",
            "package" is "",
            "started" is "2014-06-08 17:52:53",
            "custom" is "",
            "machine" is such
                "shutdown_on" is "2014-06-08 17:53:58",
                "label" is "cuckoo01",
                "manager" is "VirtualBox",
                "started_on" is "2014-06-08 17:52:53",
                "id" is 1,
                "name" is "cuckooosx"
            wow,
            "ended" is "2014-06-08 17:53:58",
            "version" is "1.2-dev",
            "duration" is 65,
            "id" is 1
        wow,
        "signatures" is so many,
        "static" is such wow,
        "dropped" is so
            such
                "yara" is so many,
    [snip...]

Please, use doge power with care.
