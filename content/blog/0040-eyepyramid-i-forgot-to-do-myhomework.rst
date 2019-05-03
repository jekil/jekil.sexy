EyePyramid: I forgot to do my homework!
#######################################
:date: 2017-01-11 02:59
:author: jekil
:category: Blog
:tags: malware, botnet, EyePyramid
:slug: eyepyramid-i-forgot-to-do-myhomework
:status: published

Today Italian news were surrounded by the story of brother and sister arrested in Italy for spying on top public officials, institutions and high profile VIPs.

The **EyePyramid** story has been `widely <http://english.sina.com/news/2017-01-10/detail-ifxzkfuh6792570.shtml>`_ `reported <http://www.telegraph.co.uk/news/2017/01/10/italian-brother-sister-arrested-cyber-espionage-operation-tapped/>`_ and probably it is going to monopolise Italian media for the next week. So I do not want to write about it.

The only official information available (right now) are in the `subpoena / arrest warrant <http://www.agi.it/pictures/pdf/agi/agi/2017/01/10/132733992-5cec4d88-49a1-4a00-8a01-dde65baa5a68.pdf>`_ (sorry, in Italian). It is filled of operational details about how the bad guys were running their business.

Technically speaking, they wrote a VB.NET malware with RAT / spyware features. They infected high level targets via spear-phishing and pivoted on their email to infect more high level targets. The whole thing was reporting and exfiltering data to a C&C.

`@phretor <https://twitter.com/phretor>`_ wrote a `digest <https://gist.github.com/phretor/c01945ec501480291d780bbec01da20e>`_  with all the available IoC and `@ReaQta <https://twitter.com/ReaQta>`_ guys are publishing some details from malware analysis.

So, there is no much to say. This is not so advanced to be dubbed as APT$foo or $barBear, although we understood how we do not need cutting edge malware to compromise high level targets.

Now the fun part: what about operational details? The arrest warrant is plenty of interesting suggestions by these malware operators:

* **Side channel over cloud storage or email**: why you should deploy a complex side channel if you can just push data to the cloud? They stole small files just sending them via email and large files uploading to some cloud storage sites.
* **Licensed software**: when writing malware, if you need a commercial library, be honest and fair. Buy a proper license using your real name.
* **Privacy Protect Everything**: for your C&C forgot fast flux and DGA, simply old stuff just works. With a bunch of domains and a whois privacy option you can rule the world!
* **Premium DSL support**: if you are in trouble with your internet link, just tell the support you are bot herding like a boss.
* **Buy chocolate flavoured smart cards**: so next time you can just eat them.

Do not care about your homework and be a great YOLO malware operator!
