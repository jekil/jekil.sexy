Website defacement detection techniques
#######################################
:date: 2009-10-14 00:22
:author: jekil
:category: Research
:tags: defacement, detection, website monitoring
:slug: website-defacement-detection-techniques
:status: published
:alias: /paper/website-defacement-detection-techniques

Table of Contents
-----------------

| 1. Website defacement
| 2. Anomaly detection systems
| 2.1 Checksum comparison
| 2.2 Diff comparison
| 2.3 DOM tree analysis
| 2.4 Complex algorithms
| 3. Signature detection
| 4. Thresholds and worst cases

1. Website defacement
---------------------

| A website defacement is the unauthorized substitution of a web page or
  a part of it by a system cracker. A defacement is generally meant as a
  kind of electronic graffiti, although recently it has become a means
  to spread messages by politically motivated cyber protesters or
  hacktivists.
| This is a very common form of attack that seriously damages the trust
  and the reputation of a website.
| Detecting web page defacements is one of the main services for the
  security monitoring system.
| A lot of time ago I wrote a small & smart application to detect web
  site defacements in large scale with the ability to monitor a lot
  (thousands) of websites. This was a test to collect some statistics,
  so I tried to do it in a short time: I wrote it in a few days.
| So I was asking me about what techniques and technologies I can use to
  get the highest detection rate with the minimum effort.
| I choose Ruby, Ruby on Rails for the user interface and Event Machine
  to speed up the performances.
| With only few days of development I can't struggle with complex
  algorithms to detect defacements, but I choose some very simple
  techniques, that after some months of tests, seemed to be very
  effective. The performance and detection rate of this "poor man"
  techniques are comparable to some others commercial monitoring
  systems.
| The key feature of the proposed techniques is that it does not require
  the installation of a component (like an HIDS) or a participation of
  the site maintainers. It require only the URL of the web site to
  monitor.
| Today I want to share this brainstorming about web site detection
  techniques.

2. Anomaly detection systems
----------------------------

| Anomaly detection refers to detecting patterns in a given data set
  that do not conform to an established normal behavior. The patterns
  thus detected are called anomalies and often translate to critical and
  actionable information in several application domains.
| The defacement monitoring application needs to detect a change in a
  web page and detect if it's "normal" or it's an "anomaly".
| To create a set of "normal" a preliminary learning phase builds a
  profile of the monitored web page, then the web site can be monitored
  for "anomaly" changes.
| The detection of a defacement is based on a dynamic threshold, if the
  web page changed over this threshold the system treat it as defaced
  and throw a defacement alert.
| This threshold is updated to avoid the obsolescence of his value and
  the learning set.

2.1 Checksum comparison
-----------------------

| The simplest way to detect a change in some text-formatted data, like
  a HTML page, is to compute and check his checksum with a hash
  algorithm like MD5 or SHA1.
| Only a little change in the monitored web page generate a different
  checksum, so you can detect a defacement.
| This works well for "best of '90s" web sites which uses only static
  content, but for today's web pages with contents that change at every
  reload this technique is quite obsolete.
| For example a web page with a counter or a timers inside changes his
  content at every reload and the checksum is continually different.
| Moreover this type of check cannot observe a threshold based system
  because it's a comparison with a true or false result.

2.2 Diff comparison
-------------------

| There are some libraries in python and ruby implementing the widely
  known unix tool diff, using it we can get the difference between two
  web pages.
| We can use a threshold based system learning the usual difference
  percentage of a web page and check if a changeset is under the usual
  threshold.
| This is a very fast but very effective technique which works well in
  most dynamic sites.

2.3 DOM tree analysis
---------------------

| This is a similar strategy to the diff comparison, but is used the DOM
  tree instead of the plain HTML content for the comparison.
| The layout of a website changes, tags and properties, have little
  changes during time. Using this fact you can build up a threshold
  based system as above.

2.4 Complex algorithms
----------------------

You can design a lot of algorithms, or use some of the already known,
but this is a very expensive work. I haven't used any complex logic or
algorithm but if you want to follow this way you can find a lot of
academic papers about this field.

3. Signature detection
----------------------

The web pages are examined for pre-configured and predetermined attack
patterns known as signatures. Many attacks today have distinct
signatures. The collection of these signatures must be constantly
updated to mitigate emerging threats. I used the wide database of
`Zone-h <http://www.zone-h.org>`__ to build a signature set always
updated.

4. Thresholds and worst cases
-----------------------------

| The bigger effort is design the engagement rules and tuning good
  thresholds.
| The percentage of changes in a website can change during time, an
  evaluation of both anomaly detection and signature detection
  techniques, using a weighted logic can help to reduce false positives.
| You must remember that you need to deal with website restyling, layout
  changes, widgets and banners that can be removed or added.
| As today there are some worst cases that causes false negatives:
  defacement done via javascript (levaraging on a XSS vulnerability) or
  via CSS, or partial defacements (do you remember the securityfocus.com
  defacement?) where only a part, like an image or a banner, of the
  website changes.
