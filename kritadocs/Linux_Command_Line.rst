Linux Command Line
==================

:doc:`File Menu <File_Menu>`

As a native Linux program, Krita allows you to do operations on images
without opening the program when using the Terminal. This option is
disabled on Windows and OSX because it makes a DBUS connection which
triggers firewalls and virus scanners, and we don't want to scare
people.

This is primarily used in bash or shell scripts, for example, to mass
convert kra files into pngs.

Export
------

This allows you to quickly convert files via the terminal:

.. code-block:: text

   krita importfilename --export --export-filename exportfilename

krita
    This tells the terminal to use the program Krita.
importfilename
    Replace this with the filename of the file you want to manipulate.
``--export``
    This selects the export option.
``--exportfilename``
    This says that the following word is the filename it should be
    exported to.
exportfilename
    Replace this with the name of the output file. Use a different
    extension to change the fileformat.

Example:

.. code-block:: text

   krita final.png --export --export-filename final.jpg

This piece of code takes the file *file.png* and saves it as *file.jpg*.

PDF export
~~~~~~~~~~

Pdf export looks a bit different, using the ``--export-pdf`` option.

.. code-block:: text

   krita final.png --export-pdf --export-filename final.pdf

This exports the file *file.png* as a pdf file.

.. Warning::

   This has been removed from 3.1 because the results were incorrect.

Open with Custom Screen DPI
---------------------------

Open Krita with specified Screen DPI.

.. code-block:: text

   krita --dpi <dpiX,dpiY>

For example: 

.. code-block:: text

   krita --dpi <72,72>

Open template
-------------

Open krita and automatically open the given template(s). This allows you
to, for example, create a shortcut to Krita that opens a given template,
so you can get to work immidiately!

.. code-block:: text

   krita --template templatename.desktop

``--template``
    Selects the template option
templatename.desktop
    All templates are saved with the .desktop extension. You can find
    templates in the .kde/share/apps/krita/template or in the install
    folder of Krita.

.. code-block:: text

   krita --template BD-EuroTemplate.desktop

This opens the European BD comic template with Krita.

.. code-block:: text

   krita --template BD-EuroTemplate.desktop BD-EuroTemplate.desktop

This opens the European BD template twice, in seperate documents.

Print
-----

.. code-block:: text

   krita file.png --print

Prints the file.

