The Animation Curve docker allows you to edit tweened sections by means
of interpolation curves. As of this time of writing, it can only edit
opacity.

The idea is that sometimes what you want to animated can be expressed as
a value. This allows the computer to do maths on the values, and
automate tasks, like interpolation, also known as 'Tweening'. Because
these are values, like percentage opacity, and animation happens over
time, that means we can visualise the way the values are interpolated as
a curve graph, and also edit the graph that way.

But, when you first open this docker, there's no curves visible! You
will first need to add opacity keyframes to the active animation layer.
You can do this by using the animation docker and selection 'add new
opacity frame'.

.. figure:: Animation_curves_1.png
   :alt: Animation_curves_1.png

   Animation\_curves\_1.png

Opacity should create a bright red curve line in the docker. On the
left, in the layer list, you will see that the active layer has an
outline of it's properties: A red 'opacity' has appeared. Pressing the
red dot will hide the current curve, which'll be more useful in the
future when more properties can be animated.

.. figure:: Animation_curves_2.png
   :alt: Animation_curves_2.png

   Animation\_curves\_2.png

If you select a dot of the curve, you can move it around to shift it's
place in the time-line or it's value.

On the top, you can select the method of smoothing:

Hold Value
    This keeps the value the same until there's a new keyframe.
Linear Interpolation (Default)
    This gives a straight interpolation between two values.
Custom interpolation
    This allows you to set the section after the keyframe node as one
    that can be modified. +dragging on the node allows you to drag out a
    handler node for adjusting the curving.

So, for example, making a 100% opacity keyframe on frame 0 and and a 0%
opacity one on frame 24 gives the following result:

.. figure:: Ghost_linear.gif
   :alt: Ghost_linear.gif

   Ghost\_linear.gif

If we select frame 12 and press A new opacity keyframe is added on that
spot. We can set this frame to 100% and set frame 0 to 0% for this
effect.

.. figure:: Ghost_linear_in-out.gif
   :alt: Ghost_linear_in-out.gif

   Ghost\_linear\_in-out.gif

Now, if we want easing in, we select the node on frame 0 and press the
button at the top. This will enable custom interpolation on the curve
between frames 0 and 12. Doing the same on frame 12 will enable custom
interpolation between frames 12 and 24. Drag from the node to add a
handle, which in turn you can use to get the following effects:

|Ghost\_ease\_in-out.gif| |Animation\_curves\_3.png|

The above shows an ease-in curve.

And convex/concave examples:

|Ghost\_concave\_in-out.gif|\ |Animation\_curves\_4.png|

|Ghost\_convex\_int-out.gif|\ |Animation\_curves\_5.png|

As you may be able to tell, there's quite a different 'texture', so to
speak, to each of these animations, despite the difference being only in
the curves. Indeed, a good animator can get quite some tricks out of
interpolation curves, and as we develop Krita, we hope to add more
properties for you to animate this way.

.. raw:: mediawiki

   {{Info|Opacity has currently 255 as maximum in the curve editor, as that's how opacity is stored internally}}

Category:Dockers

.. |Ghost\_ease\_in-out.gif| image:: Ghost_ease_in-out.gif
.. |Animation\_curves\_3.png| image:: Animation_curves_3.png
.. |Ghost\_concave\_in-out.gif| image:: Ghost_concave_in-out.gif
.. |Animation\_curves\_4.png| image:: Animation_curves_4.png
.. |Ghost\_convex\_int-out.gif| image:: Ghost_convex_int-out.gif
.. |Animation\_curves\_5.png| image:: Animation_curves_5.png

