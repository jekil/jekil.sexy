Virtual host and DNS names enumeration techniques
#################################################
:date: 2009-01-24 19:36
:author: jekil
:category: Research
:tags: discovery, dns alias, dns name, enumeration, hostmap, virtual host
:slug: virtual-host-and-dns-names-enumeration-techniques
:status: published
:alias: /paper/virtual-host-and-dns-names-enumeration-techniques/

Table of Contents
-----------------

| 1. Why you need to enumerate
| 2. Techniques
| 2.1 DNS enumeration techniques
| 2.2 Banner grabbing
| 2.3 SSL/TLS Protocol enumeration techniques
| 2.4 HTTP Protocol enumeration techniques
| 2.5 Passive web enumeration techniques
| 2.6 Active web enumeration techniques

1. Why you need to enumerate
----------------------------

The host name discovery phase is an information gathering act to get a
complete and detailed view of target resources and attack points.

During an attack or a penetration test, the attacker needs to known  as
much information as possible about the entry points to attack. An entry
point can be identified with an IP address, a service port, and some
application level information, like the virtual host name in the case of
a web server hosting several sites.

2. Techniques
-------------

There are several techniques that can be used to discover host names and
virtual hosts associated with a IP address.

Some techniques described here are implemented (and the others will be
implemented soon) in hostmap, a tool that I wrote to discover virtual
hosts and DNS names of a given IP address. As of today, the tool is
private (it does not depend on me) but I hope to release it to the
public domain soon.

2.1 DNS enumeration techniques
------------------------------

The following enumeration techniques are based on the DNS protocol and
are:

* **Reverse DNS lookup**: Performs a PTR request to get the host name
  from IP address.
* **Name servers record lookup**: Get the authoritative name server for
  the target host.
* **Mail exchange record lookup**: Get the MX records for the target
  host domain.
* **DNS AXFR zone transfer**: The name server that serve the target
  machine's domain zone can be prone to a zone transfer attack. This
  allows an attacker to perform an AXFR DNS request to retrieve all of the
  DNS records served.
* **Host name brute forcing**: Using a brute-forcing technique to guess
  a host name on the enumerated domain that resolve as the target ip
  address.

2.2 Banner grabbing
-------------------

The services exposed by the target host can disclose a host name in the
response banner. You need to simply telnet in all open ports and wait
for a response banner (or negotiate the application protocol). For
example this is the response banner of a SMTP server running Postfix:

.. code-block:: console

    $ telnet 10.0.0.1 25
    Trying 10.0.0.1...
    Connected to 10.0.0.1.
    Escape character is '^]'.
    220 mail.example.lan ESMTP Postfix

As you can see in the response banner you get the host name.

2.3 SSL/TLS Protocol enumeration techniques
-------------------------------------------

The following enumeration techniques are based on the SSL/TLS protocol
and is:

* **X.509 Certificate**: Often the target machine exposes an HTTP over
  SSL service. A connection is tried to the common HTTP service ports and
  is tried to negotiate an SSL/TLS connection, if the remote server supply
  a X.509 certificate the host name is taken from the Common Name (CN)
  field.

2.4 HTTP Protocol enumeration techniques
----------------------------------------

*  **Virtual host brute-forcing**: The web server can be brute-forced to
   guess a website served by the target host.
*  **Following redirects**: It is possible to guess another website
   served by the target host following redirects (HTTP code 301 and
   302).
*  **With error pages**: If you try to get an error page (code 500)
   sometimes you can get an error page showing a banner with the host
   name.

2.5 Passive web enumeration techniques
--------------------------------------

The following enumeration techniques are based on third party web sites
and are:

* **Search engines**: The following search engines can be used and
  queried using the target IP address:

  * Microsoft Live (with the dork "ip:"): [http://search.msn.com]

* **GPG/PGP key databases**: The following public databases can be used:

  * MIT gpg key server: [http://pgp.mit.edu:11371]

* **DNS/WHOIS databases**: Public whois information databases like RIPE,
  or DNS snapshot database can be used to passively enumerate host name
  and track his history.

The following is a partial list of public databases that can be used:

* Domainsdb: [http://www.domainsdb.net/]
* Fbk.de: [http://www.bfk.de/]
* Gigablast: [http://www.gigablast.com]
* Netcraft: [http://searchdns.netcraft.com]
* Robtex: [http://www.robtex.com]
* Tomdns: [http://www.tomdns.net]
* Web hosting: [http://whois.webhosting.info/]
* Web-max: [http://www.web-max.ca]

2.6 Active web enumeration techniques
-------------------------------------

*  **Crawling**: All published websites can be crawled for links to
   other sites and checked (if they resolve as the target IP address) to
   get other sites hosted on the target. This technique is very time
   consuming.

**UPDATE**: hostmap is a free, automatic, hostnames and virtual hosts
discovery tool written in Python. hostmap has been released in may and
you can get it at
`http://hostmap.lonerunners.net/ <http://hostmap.sourceforge.net/>`__
