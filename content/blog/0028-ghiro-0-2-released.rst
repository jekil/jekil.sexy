Ghiro 0.2 released
##################
:date: 2015-01-15 23:06
:author: jekil
:category: Tools
:tags: ghiro, image forensics
:slug: ghiro-0-2-released
:status: published
:alias: /tools/ghiro-0-2-released/

It took some time, but here we are, I am really happy to say: we
released **Ghiro 0.2**! We continuously love to improve Ghiro's feature
and our codebase, I hope you like we now release and any kind of
feedback will be appreciated. It follows the official release statement.

::

    Ghiro 0.2 has been released!

    Ghiro is an automated image forensics tool: sometimes forensic investigators
    need to process digital images as evidence. Dealing with tons of images is
    pretty easy, Ghiro is designed to scale to support gigs of images.
    All tasks are totally automated, you have just to upload you images and let
    Ghiro does the work. Understandable reports, and great search capabilities
    allows you to find a needle in a haystack. Ghiro is a multi user environment,
    different permissions can be assigned to each user. Cases allow you to group
    image analysis by topic, you can choose which user allow to see your case
    with a permission schema.

    It can be downloaded from http://getghiro.org  in both package and appliance
    ready-for-use.

    What’s new in Ghiro 0.2?

    * Added case deletion, you can now delete a case.
    * Added analysis deletion, you can now delete an analysis.
    * Added favorited images.
    * Added automatic update check and option to disable it.
    * Added filter to show only completed analysis in task panel.
    * Added an admin panel showing dependency status.
    * Added image’s hex view page.
    * Added PDF and HTML static report download.
    * Added image’s strings extraction and important string highlight.
    * Added requirements.txt for quick dependency setup with pip.
    * Added JSON API to create cases and submit images.
    * Added command to check for new releases via command line.
    * Added search only inside cases, now you can specify in which case search.
    * Added image’s tags, now you can tag an image.
    * Added image’s comments, now you can comment an image.
    * Added signatures count in Google Map and image thumbnails view.
    * Added URL upload, now you can upload an image from an URL.
    * Refactored image analyzer to be modular, rewritten all analysis features as
    modular plugins.
    * Fixed upload local folder feature, now unknown files are skipped.
    * Fixed a bug when logging an activity containing UTF-8 chars.
    * Updated Javascript libraries.
    * Many little refactorings.
    * Documentation update.
    * Bug fixes.
