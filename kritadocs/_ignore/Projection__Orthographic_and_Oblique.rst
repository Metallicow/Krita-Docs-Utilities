So let's start with the basics...

Orthographic
------------

Despite the fancy name, you probably know what orthographic is. It is a
schematic representation of an object, draw undeformed. Like the
following example:

.. figure:: Projection-cube_01.svg
   :alt: Projection-cube_01.svg

   Projection-cube\_01.svg

This is a rectangle. We have a front, top and side view. Put into
perspective it should look somewhat like this:

.. figure:: Projection-cube_02.svg
   :alt: Projection-cube_02.svg

   Projection-cube\_02.svg

While orthographic representations are kinda boring, they're also a good
basis to start with when you find yourself in trouble with a pose. But
we'll get to that in a bit.

Oblique
-------

So, if we can say that the front view is the viewer looking at the
front, and the side view is the viewer directly looking at the side.
(The perpendicular line being the view plane it is projected on)
|Projection-cube\_03.svg| Then we can get a half-way view from looking
from an angle, no? |Projection-cube\_04.svg| If we do that for a lot of
different sides… |Projection-cube\_05.svg| And we line up the sides we
get a… |Projection-cube\_06.svg| But cubes are boring. I am suspecting
that projection is so ignored because no tutorial applies it to an
object where you actually might NEED projection. Like a face.

First, let's prepare our front and side views:

.. figure:: Projection_image_01.png
   :alt: Projection_image_01.png

   Projection\_image\_01.png

I always start with the side, and then extrapolate the front view from
it. Because you are using Krita, set up two parallel rulers, one
vertical and the other horizontal. To snap them perfectly, drag one of
the nodes after you have made the ruler, and press <kbd>Shift</kbd> to
snap it horizontal or vertical. In 3.0, you can also snap them to the
image borders if you have <span class=“menuchoice”>snap to image
borders</span> active via <kbd>Shift</kbd> + <kbd>S</kbd>

Then, by moving the mirror to the left, you can design a front-view from
the sideview, while the parallel preview line helps you with aligning
the eyes(which in the above screenshot are too low).

Eventually, you should have something like this:

.. figure:: Projection_image_02.png
   :alt: Projection_image_02.png

   Projection\_image\_02.png

And of course, let us not forget the top, it's pretty important:

.. figure:: Projection_image_03.png
   :alt: Projection_image_03.png

   Projection\_image\_03.png

Tip: When you are using Krita, you can just use transform masks to
rotate the side view for drawing the top-view.

The top view works as a method for debugging your orthos as well. If we
take the red line to figure out the orthographics from, we see that our
eyes are obviously too inset. Let's move them a bit more forward, to
around the nose.

.. figure:: Projection_image_04.png
   :alt: Projection_image_04.png

   Projection\_image\_04.png

If you want to do precision position moving in the tool options docker,
just select 'position' and the input box for the X. Pressing down then
moves the transformed selection left. With Krita 3.0 you can just use
the move tool for this and the arrow keys. Using transform here can be
more convenient if you also have to squash and stretch an eye.

.. figure:: Projection_image_05.png
   :alt: Projection_image_05.png

   Projection\_image\_05.png

We fix the top view now. Much better.

For faces, the multiple slices are actually pretty important. So
important even, that I have decided we should have these slices on
separate layers. Thankfully, I chose to colour them, so all we need to
do is go to <span class=“menuchoice”>layers &rarr; split layer</span>.

.. figure:: Projection_image_06.png
   :alt: Projection_image_06.png

   Projection\_image\_06.png

This'll give you a few awkwardly named layers… rename them by selecting
all and mass changing the name in the properties editor:

.. figure:: Projection_image_07.png
   :alt: Projection_image_07.png

   Projection\_image\_07.png

So, after some cleanup, we should have the following:

.. figure:: Projection_image_08.png
   :alt: Projection_image_08.png

   Projection\_image\_08.png

Okay, now we're gonna use animation for the next bit.

Set it up as following:

.. figure:: Projection_image_09.png
   :alt: Projection_image_09.png

   Projection\_image\_09.png

-  Both frontview and sideview are set up as 'visible in timeline' so we
   can always see them.
-  Frontview has it's visible frame on frame 0 and an empty-frame on
   frame 23.
-  Side view has it's visible frame on frame 23 and an empty view on
   frame 0.
-  The end of the animation is set to 23.

.. figure:: Projection_image_10.png
   :alt: Projection_image_10.png

   Projection\_image\_10.png

Krita can't animate a transformation on multiple layers on multiple
frames yet, so let's just only transform the top layer. Add a
semi-transparent layer where we draw the guide-lines.

Now, select frame 11(halfway), add new frames from frontview, sideview
and the guide-lines. And turn on the onion skin by toggling the lamp
symbols. We copy the frame for the top-view and use the transform tool
to rotate it 45°.

.. figure:: Projection_image_11.png
   :alt: Projection_image_11.png

   Projection\_image\_11.png

So, we draw our vertical guides again and determine a in-between...

.. figure:: Projection_image_12.png
   :alt: Projection_image_12.png

   Projection\_image\_12.png

This is about how far you can get with only the main slice, so rotate
the rest as well.

.. figure:: Projection_image_13.png
   :alt: Projection_image_13.png

   Projection\_image\_13.png

And just like with the cube, we do this for all slices…

.. figure:: Projection_image_14.png
   :alt: Projection_image_14.png

   Projection\_image\_14.png

Eventually, if you have the top slices rotate every frame with 15°, you
should be able to make a turn table, like this:

.. figure:: Projection_animation_01.gif
   :alt: Projection_animation_01.gif

   Projection\_animation\_01.gif

(Because our boy here is fully symmetrical, you can just animate one
side and flip the frames for the other half) (While it is not necessary
to follow all the steps in the theory section to understand the
tutorial, I do recommend making a turn table sometime. It teaches you a
lot about drawing 3/4th faces.

How about… we introduce the top view into the drawing itself?

`1 <Category:Projection>`__

.. |Projection-cube\_03.svg| image:: Projection-cube_03.svg
.. |Projection-cube\_04.svg| image:: Projection-cube_04.svg
.. |Projection-cube\_05.svg| image:: Projection-cube_05.svg
.. |Projection-cube\_06.svg| image:: Projection-cube_06.svg

