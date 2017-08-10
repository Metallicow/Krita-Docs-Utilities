Accessing a Gradient
~~~~~~~~~~~~~~~~~~~~

The Gradients configuration panel is accessed by clicking the Gradients
icon (usually the icon next to the disk).

.. figure:: Gradient_Toolbar_Panel.PNG
   :alt: Gradient_Toolbar_Panel.PNG

   Gradient\_Toolbar\_Panel.PNG

Gradients are configurations of blending between colors. Krita provides
over a dozen preset dynamic gradients for you to choose from. In
addition, you can design and save your own.

Some typical uses of gradients are:

-  Fill for vector shapes.
-  Gradient tool
-  As a source of color for the pixel brush.

There is no gradients docker. They can only be accessed through the
gradient “quick-menu” in the toolbar.

Editing a Gradient
~~~~~~~~~~~~~~~~~~

\_\_NOTOC\_\_

Krita has two gradient types:

#. Segmented Gradients, which are compatible with GIMP, have many
   different features but are also a bit complicated to make.
#. Stop Gradients, which are saved as SVG files and similar to how most
   applications do their gradients, but has less features than the
   segmented gradient.

Initially we could only make segmented gradients in Krita, but in 3.0.2
we can also make stop gradients.

.. figure:: Krita_new_gradient.png
   :alt: Krita_new_gradient.png

   Krita\_new\_gradient.png

You can make a new gradient by going into the drop-down and selecting
the gradient type you wish to have. By default Krita will make a
stop-gradient.

Stop Gradients
^^^^^^^^^^^^^^

|Krita\_stop\_gradient.png| Stop gradients are very straight forward:

-  

   .. raw:: mediawiki

      {{MouseButton|left}}

   on the gradient to add a stop.

-  

   .. raw:: mediawiki

      {{MouseButton|left}}

   on the stops to select them, and drag to move them.

-  

   .. raw:: mediawiki

      {{MouseButton|right}}

   on the stops to remove them. A stop gradient will not allow you to
   remove stops if there's only two left.

.. figure:: Krita_move_stop.png
   :alt: Krita_move_stop.png

   Krita\_move\_stop.png

A selected stop can have it's color and transparency changed using the
color button and the opacity slider below.

.. figure:: Krita_stop_sudden_change.png
   :alt: Krita_stop_sudden_change.png

   Krita\_stop\_sudden\_change.png

As per SVG spec, you can make a sudden change between stops by moving
them close together. The stops will overlap, but you can still drag them
around.

Segmented Gradients
^^^^^^^^^^^^^^^^^^^

.. figure:: Krita_Editing_Custom_Gradient.PNG
   :alt: Krita_Editing_Custom_Gradient.PNG

   Krita\_Editing\_Custom\_Gradient.PNG

Segmented gradients are a bit more tricky. Instead of going from color
to color, it allows you to define segments, which each can have a begin
and end color.

.. raw:: mediawiki

   {{MouseButton|right}}

the gradient to call up this menu:

.. figure:: Krita_segment_gradient_options.png
   :alt: Krita_segment_gradient_options.png

   Krita\_segment\_gradient\_options.png

Split Segment
    This splits the current segment in two, using the white arrow, the
    segment middle as the place to split. It will also use the color at
    the white arrow to define the new colors in place in the new
    segments.
Duplicate segment
    Similar to split, but instead the two new segments are copies of the
    old one.
Mirror segment.
    Mirrors the segment colors.
Remove segment
    Removes the segment.

.. raw:: mediawiki

   {{MouseButton|left}}

+ dragging the black arrows will resize the segments attaching to those
arrows. + dragging the white arrows will change the mid point of that
segment, changing the way how the mixture is made.

At the bottom, you can set the color and transparency of either part of
the segment.

You can also set the blending. The first is the interpolation mode:

.. figure:: Krita_gradient_segment_blending.png
   :alt: Krita_gradient_segment_blending.png

   Krita\_gradient\_segment\_blending.png

#. Linear - Does a linear blending between both segments.
#. Curved - This causes the mix to ease-in and out faster.
#. Sine - Uses a sine function. This causes the mix to ease in and out
   slower.
#. Sphere, increasing - This puts emphasis on the later color during the
   mix.
#. Sphere, descreasing - This puts emphasis on the first color during
   the mix.

Finally, there's the model:

.. figure:: Krita_gradient_hsv_cw.png
   :alt: Krita_gradient_hsv_cw.png

   Krita\_gradient\_hsv\_cw.png

RGB
    Does the blending in RGB model.
HSV clockwise
    Blends the two colors using the HSV model, and follows the hue
    clockwise(red-yellow-green-cyan-blue-purple). The above screenshot
    is an example of this.
HSV counter-clock wise.
    Blends the color as the previous options, but then
    counter-clockwise.

`Category: Resource Management <Category:_Resource_Management>`__

.. |Krita\_stop\_gradient.png| image:: Krita_stop_gradient.png

