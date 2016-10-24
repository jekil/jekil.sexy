Continuous Integration Services I Like
######################################
:date: 2015-07-20 17:28
:author: jekil
:category: Blog
:tags: CI, development
:slug: continuous-integration-services-i-like
:status: published
:alias: /blog/continuous-integration-services-i-like

The term **"continuous integration (CI)"** refers to a process that
builds, assess and tests code on a frequent basis.

Today continuous integration is a starting point for agile developers
and widely used.

Every project I'm working on starts with a setup of continuous
integration pipeline. I'm a big fan of agile developing, that's why I
was always searching for tools or services to help me develop my
projects better and faster.

Here is a brief summary of services, selected over the years, I use in
my projects, all of them are free, provide a badge you can embed in your
website and are really easy to use. As example I will show the services
I use on `Ghiro <http://www.getghiro.org/>`__, an open source image
forensics tool.

Coveralls.io
~~~~~~~~~~~~

`Coveralls.io <https://coveralls.io/>`__ is a service to help you track
your code coverage over time, and ensure that all your new code is fully
covered.

This is of great help to focus you on writing tests (yep, I will do...)

For example, this is the dashboard you get for
`Ghiro <http://www.getghiro.org/>`__:

|Screen Shot 2015-07-16 at 23.52.44|

DRONE.IO
~~~~~~~~

`Drone.io <https://drone.io/>`__ is another continuous integration tool,
I think it is more customizable than Travis-CI although I use both.

Landscape.io
~~~~~~~~~~~~

`Landscape.io <https://landscape.io/>`__ is a code quality service, it
monitors your codebase for metrics and trends. It runs checks against
your code to look for errors, code smells and deviations from stylistic
conventions. It finds potential problems before they're problems, to
help you decide what and when to refactor.

It is a good service, although it is not so much configurable (i.e. you
can't mark false positives), it could help to keep a code quality in
your projects.

For example, this is the dashboard you get for
`Ghiro <http://www.getghiro.org/>`__, there are same false positives I
can't mark as accepted:

|Screen Shot 2015-07-16 at 23.07.53|

Requires.io
~~~~~~~~~~~

`Requires.io <https://requires.io/>`__ monitors the requirements of your
project and notify you whenever a dependency is outdated, all Python
dependencies are monitored: you are notified if you are using an old
library or an insecure one.

I love this service, I found it of great help. Remember: it is mandatory
to keep track of insecure dependencies in your project!

For example, this is the dashboard you get for
`Ghiro <http://www.getghiro.org/>`__:

|Screen Shot 2015-07-16 at 22.49.09|

Travis CI
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

`Travis-CI <https://travis-ci.org/>`__ is the best continuous
integration and building services you will get, any description is
pointless, and it is free. Kudos to these guys.

For example, this is the build report you get for
`Ghiro <http://www.getghiro.org/>`__:

|Screen Shot 2015-07-16 at 23.57.36|

 
.. |Screen Shot 2015-07-16 at 23.52.44| image:: {filename}/images/2015/07/Screen-Shot-2015-07-16-at-23.52.44.png
   :width: 300px
   :height: 62px
   :target: {filename}/images/2015/07/Screen-Shot-2015-07-16-at-23.52.44.png
.. |Screen Shot 2015-07-16 at 23.07.53| image:: {filename}/images/2015/07/Screen-Shot-2015-07-16-at-23.07.53.png
   :width: 300px
   :height: 117px
   :target: {filename}/images/2015/07/Screen-Shot-2015-07-16-at-23.07.53.png
.. |Screen Shot 2015-07-16 at 22.49.09| image:: {filename}/images/2015/07/Screen-Shot-2015-07-16-at-22.49.09.png
   :width: 300px
   :height: 209px
   :target: {filename}/images/2015/07/Screen-Shot-2015-07-16-at-22.49.09.png
.. |Screen Shot 2015-07-16 at 23.57.36| image:: {filename}/images/2015/07/Screen-Shot-2015-07-16-at-23.57.36.png
   :width: 300px
   :height: 280px
   :target: {filename}/images/2015/07/Screen-Shot-2015-07-16-at-23.57.36.png
