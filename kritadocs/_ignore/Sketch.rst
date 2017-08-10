A line based brush engine, based on the Harmony brushes. Very messy and
fun.

Reference
=========

Parameters
----------

Has the following parameters:

-  `Brush-tips <Special:MyLanguage/Brush_Tips>`__
-  `Brush size <#Brush_size>`__
-  `Blending Modes <Special:MyLanguage/Blending_Modes>`__
-  `Opacity and Flow <Special:MyLanguage/Opacity_&amp;_Flow>`__ (Only
   opacity)
-  `Size <Special:MyLanguage/Parameters#Size>`__
-  `Rotation <Special:MyLanguage/Parameters#Rotation>`__
-  `Line Width <#Line_Width>`__
-  `Offset Scale <#Offset_Scale>`__
-  `Density <#Density>`__
-  `Airbrush <Special:MyLanguage/Parameters#Airbrush>`__
-  `Painting Mode <Special:MyLanguage/Opacity_&amp;_Flow>`__

Brush Size
----------

Line Width
~~~~~~~~~~

The width of the rendered lines.

.. figure:: Krita_2_9_brushengine_sketch_linewidth.png
   :alt: Krita_2_9_brushengine_sketch_linewidth.png

   Krita\_2\_9\_brushengine\_sketch\_linewidth.png

Offset Scale
~~~~~~~~~~~~

When curve lines are formed, this value roughly determines the distance
from the curve lines to the connection lines:

-  This is a bit misleading, because a value of 0% and a value of 100%
   give similar outputs, as do a value of say 30% and 70%. You could
   think that the actual value range is between 50% and 200%.
-  0% and 100% correspond to the curve lines touching the connection
   lines exactly.
-  Above 100%, the curve lines will go further than the connection
   lines, forming a fuzzy effect.

.. figure:: Krita_2.9_brushengine_sketch_offset.png
   :alt: Krita_2.9_brushengine_sketch_offset.png

   Krita\_2.9\_brushengine\_sketch\_offset.png

.. figure:: Krita-sketch_offset_scale2.png
   :alt: Krita-sketch_offset_scale2.png

   Krita-sketch\_offset\_scale2.png

Density
~~~~~~~

The density of the lines. This one is highly affected by the Brush-tip,
as determined by the Distance Density toggle.

.. figure:: Krita_2.9_brushengine_sketch_density.png
   :alt: Krita_2.9_brushengine_sketch_density.png

   Krita\_2.9\_brushengine\_sketch\_density.png

Use Distance Density
    the further the line covered is from the center of the area of
    effect, the less the density of the resulting curve lines.
Magnetify
    Magnetify is *on* by default. It's what causes curve lines to form
    between two close line sections, as though the curve lines are
    attracted to them like magnets.
    With Magnetify *off*, the curve line just forms on either side of
    the current active portion of your connection line. In other words,
    your line becomes fuzzier when another portion of the line is
    nearby, but the lines don't connect to said previous portion.
Random RGB
    Causes some slight RGB variations.
Random Opacity
    The curve lines get random opacity. This one is barely visible, so
    for the example I used line width 12 and 100% opacity.
Distance Opacity
    ???
Simple Mode
    this mode exists for performance reasons, and doesn't affect the
    output in a visible way. Check this for large brushes or thick lines
    for faster rendering.
Paint Connection Line
    What appears to be the connection line is usually made up of an
    actual connection line and many smaller curve lines. The many small
    curve lines make up the majority of the line. For this reason, the
    only time this option will make a visible difference is if you're
    drawing with 0% or near 0% density, and with a thick line width. The
    rest of the time, this option won't make a visible difference.

`Category:Brush
Engines{{#translation:}} <Category:Brush_Engines{{#translation:}}>`__
