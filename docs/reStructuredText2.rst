..  restructuredtext-syntax:

reStructuredText Syntax Specification
#####################################

This note formally defines the syntax of reStructuredText as used in the PyLIT
project. As much as possible, the notation conforms to the original
specification published by David Goodger: `reStructuredText Markup
Specification
<http://docutils.sourceforge.net/docs/ref/rst/restructuredtext.html>`_.

Character Set
*************

RST2 uses unicode charater sets defined according to the unicode standards. The first line of every RST2 document must be a line identifying the language being used.

This version of reStructuredText eliminates some notation that does not seem
necessary, and leads to difficulties in parsing. Since the resulting notation
will not be 100% compliant with David Goodger's notation, files using this
notation should be named with an extension of `rst2`.

Whitespace
**********

Tabs are expanded to spaces, and tab stops default to 4 spaces, consistent with
common practices in the programming profession. Although it is not intended
that this markup be used exclusively by computer professionals, using the tab
character with a default setting of eight characters leads to text documents
that display oddly when viewed in different settings. 

Other whitespace characters are converted to spaces:

    * form feeds chr(12)]
    * vertical tabs [chr(11)]

When indenting text, spaces are required. 

..  note::

    These rules are not compliant with the original RST markup
   
Blank Lines
***********

Blank lines serve as separators between block elements. Multiple blank lines
are treated as a single blank line in this context, and are not displayed in
rendered documents. In literal text blocks, multiple blank lines are preserved.

Adornments
**********

Adornments are lines consisting of multiple instances of a single adornment
character. They are used to mark headings, and may appear both above and below
heading text. If the length of the adornment line does not match the length of
the heading line, a warning will be issued. (not an error as with the RST
processors) Adornments must begin in column 1 of the document.

Headings
********

Headings are lines of text with an adornment below the heading line, and an optional adornment above .


