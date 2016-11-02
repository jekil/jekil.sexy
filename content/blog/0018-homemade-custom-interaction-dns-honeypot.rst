Homemade custom interaction DNS honeypot
########################################
:date: 2014-04-02 20:30
:author: jekil
:category: Tools
:tags: dns, honeypot
:slug: homemade-custom-interaction-dns-honeypot
:status: published
:alias: /tools/homemade-custom-interaction-dns-honeypot/

| Time ago I needed a weird DNS honeypot with "some" level of
  interaction.
| I mean an honeypot which acts as a real DNS server, sending out DNS
  replies  for the first bunch of requests, and after it work as a
  sinkhole.
| I did it in Python and `Twisted <https://twistedmatrix.com/trac/>`__,
   named it with the worst name I was able to catch and published it on
  `Github <https://github.com/jekil/UDPot>`__.

I hope all setup steps are documented
in `README.md <https://github.com/jekil/UDPot/blob/master/README.md>`__,
anyway here is a quick recap.

Check it out from `Github <https://github.com/jekil/UDPot>`__ and
create a virtualenv (you have to install it for example with apt-get
install python-virtualenv):

.. code-block:: console

    $ git clone https://github.com/jekil/UDPot.git
    $ virtualenv ve_udpot

Enter in the virtualenv and in the application folder:

.. code-block:: console

    $ source ve_udpot/bin/activate
    $ cd UDPot

Setup all requirements (you need python headers, you can install it with
apt-get python-dev):

.. code-block:: console

    $ pip install -r requirements.txt

You can print the option list using the help -h option:

.. code-block:: console

    $ python dns.py -h
    usage: dns.py [-h] [-p DNS_PORT] [-c REQ_COUNT] [-t REQ_TIMEOUT] [-s] [-v] server

    positional arguments:
      server                DNS server IP address

    optional arguments:
      -h, --help            show this help message and exit
      -p DNS_PORT, --dns-port DNS_PORT
                            DNS honeypot port
      -c REQ_COUNT, --req-count REQ_COUNT
                            how many request to resolve
      -t REQ_TIMEOUT, --req-timeout REQ_TIMEOUT
                            how many request to resolve
      -s, --sql             database connection string
      -v, --verbose         print each request

And run the DNS honeypot using options you like, as:

.. code-block:: console

    $ python dns.py -v 8.8.8.8

Dns.py binds on port 5053, to reply on requests on port 53 without
running dns.py as root you need some iptables magic:

.. code-block:: console

    # iptables -t nat -A PREROUTING -i eth0 -p tcp --dport 53 -j REDIRECT --to-ports 5053
    # iptables -t nat -A PREROUTING -i eth0 -p udp --dport 53 -j REDIRECT --to-ports 5053

Honeypot data can be printed on stdout with -v option or you can read
them in sqlite database:

.. code-block:: console

    $ sqlite3 db.sqlite3
    SQLite version 3.7.13 2012-06-11 02:05:22
    Enter ".help" for instructions
    Enter SQL statements terminated with a ";"
    sqlite> SELECT * FROM __main___dns;


    1|94.23.212.82|30789|ahuyehue.info|ALL_RECORDS|IN|2014-04-02 10:35:43.378744
    2|94.23.212.82|30789|ahuyehue.info|ALL_RECORDS|IN|2014-04-02 10:35:43.374297
    3|94.23.212.82|30789|ahuyehue.info|ALL_RECORDS|IN|2014-04-02 10:35:43.370550
    4|94.23.212.82|30789|ahuyehue.info|ALL_RECORDS|IN|2014-04-02 10:35:43.366275
    5|94.23.212.82|30789|ahuyehue.info|ALL_RECORDS|IN|2014-04-02 10:35:43.358958
    6|94.23.212.82|37820|ahuyehue.info|ALL_RECORDS|IN|2014-04-02 10:35:32.104334
    7|94.23.212.82|37820|ahuyehue.info|ALL_RECORDS|IN|2014-04-02 10:35:32.099354
    8|94.23.212.82|37820|ahuyehue.info|ALL_RECORDS|IN|2014-04-02 10:35:32.094711
    9|94.23.212.82|37820|ahuyehue.info|ALL_RECORDS|IN|2014-04-02 10:35:32.086916
