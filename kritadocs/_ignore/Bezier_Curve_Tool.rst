.. raw:: mediawiki

   {{ToolIcon|path-select}}

This tool, represented by a ellipse with a dashed border and a curve
control, allows you to make a selection of an area by drawing a path
around it. Click where you want each point of the path to be. Click and
drag to curve the line between points. Finally click on the first point
you created to close your path.

Hotkeys and Sticky keys
-----------------------

-  <kbd>R</kbd> sets the selection to 'replace' in the tool options,
   this is the default mode.
-  <kbd>A</kbd> sets the selection to 'add' in the tool options.
-  <kbd>S</kbd> sets the selection to 'subtract' in the tool options.
-  <kbd>Shift</kbd> + sets the subsequent selection to 'add'. You can
   release the <kbd>Shift</kbd> key while dragging, but it will still be
   set to 'add'. Same for the others.
-  <kbd>Alt</kbd> + sets the subsequent selection to 'subtract'.
-  <kbd>Ctrl</kbd> + sets the subsequent selection to 'replace'.
-  <kbd>Shift</kbd> + <kbd>Alt</kbd> + sets the subsequent selection to
   'intersect'.

.. raw:: mediawiki

   {{Warning|Selection modifiers don't quite work yet with the path tool, as shift breaks the path}}

.. raw:: mediawiki

   {{Note|You can switch the behaviour of the Alt key to use Ctrl instead by toggling the switch in the [[Special:MyLanguage/General_Settings#Tool_options|general settings]]}}

Tool Options
------------

.. figure:: Bezier_Curve_Selection_Tool_Options.PNG
   :alt: Bezier_Curve_Selection_Tool_Options.PNG

   Bezier\_Curve\_Selection\_Tool\_Options.PNG

Anti-aliasing
    This toggles whether or not to give selections feathered edges. Some
    people preffer hard-jagged adges for their selections.

Category:Toolbox
