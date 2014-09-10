reStructuredText Refactored
###########################

..  _reST:  http://docutils.sourceforge.net/rst.html
..  _reStructuredText:  http://docutils.sourceforge.net/rst.html
..  _Sphinx:            http://sphinx-doc.org
..  _docutils:          http://docutils.sourceforge.net/index.html
..  _Grako:             https://pypi.python.org/pypi/grako/3.4.1

reStructuredText_ is a nice markup language for writing documentation. In fact,
`reST` as it is sometimes called, together with the docutils_ package, written
by David Goodger, and Sphinx_, written by Georg Brandl, are the current
standard tools for documenting Python_ itself. reST_ is being used  and by
thousands of programmers to create very nice looking documentation. Some have
even said that reST_ and Sphinx_ have made writing documentation fun, and that
motivates them to write more. Good!

I have been using Sphinx_ to produce lecture materials for classes I teach at
|ACC| in Austin, Texas for several years, and have been reasonably happy with
them. However, as my writings got more extensive, I began to have problems
managing things. In particular, I discovered that I wanted a better system to
organize my writings and associated support materials. As I studied the systems
more, I discoverd that the code was not that well documented (IMHO), surprising
for tools that support documentation!

In the end, I decided to study the markup language in depth, and work on a new
tool that supports my writing work. In addition, I wanted a system that I could
use to develop my own version of Donald Knuth's :term:`Literate Programming`.
The new tool is named pyLit, a contraction for Python Literate Programming. I
started naming my work on these concepts while working on a second Master's
degree at Texas State in 2003.

..  note::

    There is another project using the name pylit which has been pretty active
    for several years. However, I believe my use of the name predates their
    work, and I do own the domains pylit.org and co-pylit.org. (Notice the
    aeronautical slant to this? I am an aviator, by the way, with degrees in
    Aerospace Engineering and Computer Science.)

The PyLit program will be a Flask web application. It will use Grako_ to parse
the new markup, and other standard libraries for the fundamental components of
the system. As much as possible all parts of the system will be designed to be
replaced with newer tools as they become available. 


