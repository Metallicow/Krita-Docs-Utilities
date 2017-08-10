Selections allow you to pick a specific area of your artwork to change.
There are many selection tools available that select in different ways.
Once an area is selected most tools will stay inside that area. On that
area you can draw or use gradients to quickly get colored and/or shaded
shapes with hard edges.

Creating Selections
-------------------

The most common selection tools all exist at the bottom of the toolbox.
Each tool selects things slightly differently. The links for each tool
go into a more detailed description with how to use it.

+-------------------------------------------------------------------+-------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `Rectangular Selection Tool <Rectangular_Selection_Tool>`__       | .. raw:: mediawiki                  | Select the shape of a square.                                                                                                                                              |
|                                                                   |                                     |                                                                                                                                                                            |
|                                                                   |    {{ToolIcon|rectangle-select}}    |                                                                                                                                                                            |
+-------------------------------------------------------------------+-------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `Elliptical Selection Tool <Elliptical_Selection_Tool>`__         | .. raw:: mediawiki                  | Select the shape of a circle.                                                                                                                                              |
|                                                                   |                                     |                                                                                                                                                                            |
|                                                                   |    {{ToolIcon|ellipse-select}}      |                                                                                                                                                                            |
+-------------------------------------------------------------------+-------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `Polygonal Selection Tool <Polygonal_Selection_Tool>`__           | .. raw:: mediawiki                  | Click where you want each point of the Polygon to be. Double click to end your polygon and finalize your selection area. Use <kbd>Shift + Z</kbd> to undo last point.      |
|                                                                   |                                     |                                                                                                                                                                            |
|                                                                   |    {{ToolIcon|polygon-select}}      |                                                                                                                                                                            |
+-------------------------------------------------------------------+-------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `Outline Selection Tool <Outline_Selection_Tool>`__               | .. raw:: mediawiki                  | Outline/Lasso tool is used for a rough selection by drawing the outline.                                                                                                   |
|                                                                   |                                     |                                                                                                                                                                            |
|                                                                   |    {{ToolIcon|outline-select}}      |                                                                                                                                                                            |
+-------------------------------------------------------------------+-------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `Similar Color Selection Tool <Similar_Color_Selection_Tool>`__   | .. raw:: mediawiki                  | Similar Color Selection Tool                                                                                                                                               |
|                                                                   |                                     |                                                                                                                                                                            |
|                                                                   |    {{ToolIcon|similar-select}}      |                                                                                                                                                                            |
+-------------------------------------------------------------------+-------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `Contiguous Selection Tool <Contiguous_Selection_Tool>`__         | .. raw:: mediawiki                  | Contiguous or “Magic Wand” selects a field of color, adjust the fuzziness to allow more changes in the field of color, by default limited to the current layer.            |
|                                                                   |                                     |                                                                                                                                                                            |
|                                                                   |    {{ToolIcon|contiguous-select}}   |                                                                                                                                                                            |
+-------------------------------------------------------------------+-------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `Bezier Curve Selection Tool <Bezier_Curve_Selection_Tool>`__     | .. raw:: mediawiki                  | Path select an area based on a vector path, click to get sharp corners or drag to get flowing lines and close the path with enter or connecting back to the first point.   |
|                                                                   |                                     |                                                                                                                                                                            |
|                                                                   |    {{ToolIcon|path-select}}         |                                                                                                                                                                            |
+-------------------------------------------------------------------+-------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. raw:: mediawiki

   {{Note|You can also use the transform tools on your selection, a great way to try different proportions on parts of your image. }}

Editing Selections
------------------

The tool options for each selection tool gives you the ability to modify
your selection.

+-------------+--------------------------+----------------+
| Action      | Modifier                 | Shortcut       |
+-------------+--------------------------+----------------+
| Replace     | <kbd>Ctrl</kbd>          | -              |
+-------------+--------------------------+----------------+
| Intersect   | <kbd>Shift + Alt</kbd>   | -              |
+-------------+--------------------------+----------------+
| Add         | <kbd>Shift</kbd>         | <kbd>A</kbd>   |
+-------------+--------------------------+----------------+
| Subtract    | <kbd>Alt</kbd>           | <kbd>S</kbd>   |
+-------------+--------------------------+----------------+

Removing Selections
-------------------

If you want to delete the entire selection, the easiest way is de-select
everything. <span class=“menuchoice”>Select > Deselect</span>. Shortcut
<kbd>Ctrl + Shift + A</kbd>.

Display Modes
-------------

In the bottom left hand corner of the status bar there is a button to
toggle how the selection is displayed. The two display modes are the
following: (Marching) Ants and Mask. The red color with Mask can be
changed in the preferences. You can edit the color under <span
class="menuchoice>Settings > Configure Krita > Display > Selection
Overlay</span>. If there is no selection, this button will not do
anything.

.. figure:: ants-displayMode.jpg
   :alt: ants-displayMode.jpg

   ants-displayMode.jpg

Ants display mode (default) is best if you want to see the un-selected
area.

.. figure:: mask-displayMode.jpg
   :alt: mask-displayMode.jpg

   mask-displayMode.jpg

Mask display mode is good if you are interested in seeing the various
transparency levels for your selection. For example, you can create a
selection with a gradient.

Global Selection Mask (Painting a Selection)
--------------------------------------------

The global Selection Mask is your selection that appears on the layers
docker. By default this is hidden, so you will need to make it visible
<span class=“menuchoice”>Select > Show Global Selection Mask</span>.

.. figure:: Global-selection-mask.jpg
   :alt: Global-selection-mask.jpg

   Global-selection-mask.jpg

Once the global Selection Mask is shown, you will need to create a
selection. The benefit of using this is that you can paint your
selection using any of the normal painting tools. The information is
saved as greyscale. You might want to switch to the Mask display mode if
it is difficult to see the results.

Selection from layer transparency
---------------------------------

You can create a selection based on a layer's transparency by
right-clicking on the layer in the layer docker and selecting “Select
Opaque” from the context menu.

Pixel and Vector Selection Types
--------------------------------

Vector selections allow you to modify your selection with vector anchor
tools. Pixel selections allow you to modify selections with pixel
information. They both have their benefits and disadvantages. You can
convert one type of selection to another.

.. figure:: vector-pixel-selections.jpg
   :alt: vector-pixel-selections.jpg

   vector-pixel-selections.jpg

When creating a selection, you can select what type of selection you
want from the Mode in the selection tool options: Pixel or Vector.

Vector selections can can modify as any other vector shape with the
“Shape Handle” tool, if you try to paint on a vector selection it will
be converted into a pixel selection. Pixel selections can be painted
with any tool. You can also convert vector shapes to selection. In turn,
vector selections can be made from vector shapes, and vector shapes can
be converted to vector selections using the options in the selections
menu. Krita will add a new vector layer for this shape.

`vector-selection-example.jpg <vector-selection-example.jpg>`__ One of
the most common reasons to use vector selections is that they give you
the ability to move and transform a selection. Moving the selection with
a pixel selection will move the content on the layer. Moving the
selection on a vector selection will only move the selection. You can
also use the path editing tool to change the anchor points in the
selection

If you started with a pixel selection, you can still convert it to a
vector selection to get these benefits. Go to <span
class=“menuchoice”>Select > Convert to Vector Selection</span>.

.. raw:: mediawiki

   {{Note|If you have multiple levels of transparency when you convert a selection to vector, you will lose the grey values. }}

Common Shortcuts while Using Selections
---------------------------------------

-  Copy - <kbd>Ctrl + C</kbd> or <kbd>Ctrl + Ins</kbd>
-  Paste - <kbd>Ctrl + V</kbd> of <kbd>Shift + Ins</kbd>
-  Cut - <kbd>Ctrl + X</kbd>, <kbd>Shift + Del</kbd>
-  Copy From All Layers - <kbd>Ctrl + Shift + C</kbd>
-  Copy Selection to New Layer - <kbd>Ctrl + Alt + J</kbd>
-  Cut Selection to New Layer - <kbd>Ctrl + Shift + J</kbd>
-  Display or hide selection with <kbd>Ctrl + H</kbd>

`Category:User Manual <Category:User_Manual>`__
