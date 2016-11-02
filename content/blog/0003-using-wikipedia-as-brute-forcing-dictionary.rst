Using Wikipedia as brute forcing dictionary
###########################################
:date: 2009-01-08 04:23
:author: jekil
:category: Blog
:tags: brute forcer, brute forcing, dictionary, wikipedia, words
:slug: using-wikipedia-as-brute-forcing-dictionary
:status: published
:alias: /blog/using-wikipedia-as-brute-forcing-dictionary/

The success and the time elapsed in a `brute forcing
attack <http://en.wikipedia.org/wiki/Brute_force_attack>`__ depends by
the number of discovered brute forcing points, the quality of the tool
used (like `THC-hydra <http://freeworld.thc.org/thc-hydra/>`__,
`brutus <http://www.hoobie.net/brutus/>`__ or
`medusa <http://www.foofus.net/jmk/medusa/medusa.html>`__) and the
quality of the dictionary used.

Sometimes using a incremental dictionary is a waste of time, a good
dictionary can be the success key to a fast brute forcing attack. Get a
dictionary of common words and keep it updated is an hard work.

`Wikipedia <http://www.wikipedia.org>`__ is a free multilingual
encyclopedia, it currently contains
`2,683,099 <http://en.wikipedia.org/wiki/Special:Statistics>`__
articles. This is a really good database to generate a dictionary of
common words.

`Wikipedia <http://www.wikipedia.org>`__ offers free copies of all
available content to interested users. These databases can be used for
`mirroring <http://en.wikipedia.org/wiki/Wikipedia:Mirrors_and_forks>`__,
personal use, informal backups, or database queries. All text content is
licensed under the `GNU Free Documentation
License <http://en.wikipedia.org/wiki/Wikipedia:Text_of_the_GFDL>`__
(GFDL). Images and other files are available under `different
terms <http://en.wikipedia.org/wiki/Wikipedia:ICT>`__, as detailed on
their description pages.

The Wikipedia database download page is available here:
http://en.wikipedia.org/wiki/Wikipedia_database and the database dumps
are available here: http://download.wikimedia.org/backup-index.html

A good dictionary must contains the most common terms used in a current
language and also common words that can be used as password, an example
is "foo", "bar", "1234", "antani", etc.

We can create two types of dictionary, a dictionary containing all the
words inside wikipedia, a dictionary containing all article titles, a
dictionary containing all the words in the article titles.

After downloading a bunch of gigs we get the wikipedia database dump in
XML, the fields that we need to create our dictionary are <title> and
<text>.

Now you can create all the types of dictionary that you need: words,
titles, case sensitive or case insensitive.

To achieve better performances I used simple bash scripting for parsing
because using a DOM or SAX parser is too slow with these very big XMLs.

This dictionary contains all the article titles, so you can guess
password like names, cities, etc.

To create it you can use the following or you can edit it to fit your
needs, it's not beautiful but works:

.. code-block:: console

  grep -E '<title>(.*?)</title>' itwiki-20081206-pages-meta-current.xml | \
  cut -d '>' -f2| cut -d '<' -f1 | grep -v : | sed s/\(.*\)//g| sort | uniq

Word dictionary contains all the words in the wikipedia articles, you
can create it with a command similar to the above, I left it for your
homework ;)

Happy brute forcing!
