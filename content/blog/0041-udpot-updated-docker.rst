UDPot updated and new docker
############################
:date: 2020-04-25 23:25
:author: jekil
:category: Tools
:tags: honeypot, udpot
:slug: udpot-updated-and-new-docker
:status: published

`UDPot <https://github.com/jekil/UDPot>`__ is a littel script to run
an honeypot which acts as a real DNS server, sending out DNS replies 
for the first bunch of requests, and after it work as a sinkhole.

In the last days I refreshed the code, updated the requirements and more
spring cleaning.

Now a docker image is available on `DockerHub <https://hub.docker.com/r/jekil/udpot>`__,
you can run it with:

.. code-block:: console

    $ docker run --name udpot -p 5053:5053/udp -p 5053:5053/tcp -d jekil/udpot

It will run UDPot on port 5053 UDP and TCP, if you want to use it on another port you
can bind it with docker or redirect it with iptables.

