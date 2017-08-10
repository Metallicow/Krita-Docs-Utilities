How to generate the docs
========================
In a console/terminal simply type...

```
make html
```

This should generate the html docs in "kritadocs/_build/html" directory.


Prerequisites
-------------

* https://www.python.org/ because it's the best!
* http://sphinx-doc.org/ for generating the docs.
  ``pip install sphinx``
  or see http://www.sphinx-doc.org/en/stable/install.html
* https://pandoc.org/
  (Optional) for conversion of the .mediawiki syntax to .rst. `See scripts directory <https://github.com/Metallicow/Krita-Docs-Utilities/blob/master/kritadocs/scripts/krita_mediawiki_utilities.py>`_.
  You will need to set the pandoc.exe path in the script.

