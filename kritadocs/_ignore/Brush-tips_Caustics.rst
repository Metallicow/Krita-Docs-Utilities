Question
    Could you do a tutorial on how to recreate the look of light
    refracting in water?

Sure, caustics, it’s not like it’s the most complicated effect known to
CG graphics… Okay, so the first thing is that light effects never work
in isolation: you need to be spot on with colors and other effects to
make it work. So we first need to recreate the suroundings a bit.
|Krita-brushtips-caustics\_01.png| We set up something simple with
gradients. Some radial, some linear. The eraser mode works with
gradients as well, so use that to your advantage!

We create a simple smudge brush by taking *smudge\_soft* and adding
scattering to it, as well as an s-curve on the smudge length.
|Krita-brushtips-caustics\_02.png| And then we build up a quick base:
|Krita-brushtips-caustics\_03.gif| Note how the smudge brush here is
used not just to mix areas, but also to create definition of borders by
lowering the scatter.(If you reverse the pressure curve on the scatter,
this’ll be easily done by increasing the pressure on the stylus)

Now for the real magic. Caustics are a bit hairy, which means it’s a
good candidate for the sketch brush engine.
|Krita-brushtips-caustics\_04.png| Take *sketch\_ink\_big*, and add
pressure to the ‘line-width’ while setting ‘density’ under the
brush-size to 100%. This makes it extra hairy.
|Krita-brushtips-caustics\_05.png| Set the brush blending mode to ‘Color
Dodge’, and select the color of our caustics. Color dodge will cause a
move towards white by applying special dodge color maths to our brush
dabs instead of the ‘normal’ avaraging color maths.

Outside of pressure for making varying strokes, glowiness for the light
and extra density, we also want to have the size of the line decrease
the further away it is…

.. figure:: Krita-brushtips-caustics_06.png
   :alt: Krita-brushtips-caustics_06.png

   Krita-brushtips-caustics\_06.png

Then, use the assistant editor tool to add a perspective grid. It
doesn’t need to be perfectly in perspective, because we’ll only use it
for the perspective sensor.

.. figure:: Krita-brushtips-caustics_07.png
   :alt: Krita-brushtips-caustics_07.png

   Krita-brushtips-caustics\_07.png

This will cause the brush to give smaller lines the further it registers
on the perspective assistant.(It only works per single perspective
assistant, making it not very good for chaining, but for our purpose
this is good.)

Then you start slowly building up your lines. (Make sure to make a copy
of the layer)(The color dodge blending doesn’t work well on a seperate
layer, so do it on one that also has the ground on it).

.. figure:: Krita-brushtips-caustics_08.png
   :alt: Krita-brushtips-caustics_08.png

   Krita-brushtips-caustics\_08.png

Make sure to try and follow the shapes you made.(I failed at this) The
great thing about the sketch brush is that it causes those little
‘melt-togethers’ where two lines cross. This is only per stroke, so make
a lot of long ongoing strokes with this brush to make use of it.

.. figure:: Krita-brushtips-caustics_09.png
   :alt: Krita-brushtips-caustics_09.png

   Krita-brushtips-caustics\_09.png

Then take the gradient tool, and set the blending mode to color and the
paint tool to a light blue, so we can get in the bluish atmospheric
effect.

.. figure:: Krita-brushtips-caustics_10.png
   :alt: Krita-brushtips-caustics_10.png

   Krita-brushtips-caustics\_10.png

Then use the airbrush\_pressure with the line tool to make some
light-shafts of different sizes on a separate layer. (Don’t forget you
can use the eraser mode to for subtle erasing with the line-tool as
well)

.. figure:: Krita-brushtips-caustics_11.png
   :alt: Krita-brushtips-caustics_11.png

   Krita-brushtips-caustics\_11.png

Set the blending mode to color dodge and lower the opacity.

.. figure:: Krita-brushtips-caustics_12.png
   :alt: Krita-brushtips-caustics_12.png

   Krita-brushtips-caustics\_12.png

Finally, polish the piece with the airbush tool and some local color
picking. |Final result.|

Category:krita-Brush-tips

.. |Krita-brushtips-caustics\_01.png| image:: Krita-brushtips-caustics_01.png
.. |Krita-brushtips-caustics\_02.png| image:: Krita-brushtips-caustics_02.png
.. |Krita-brushtips-caustics\_03.gif| image:: Krita-brushtips-caustics_03.gif
.. |Krita-brushtips-caustics\_04.png| image:: Krita-brushtips-caustics_04.png
.. |Krita-brushtips-caustics\_05.png| image:: Krita-brushtips-caustics_05.png
.. |Final result.| image:: Krita-brushtips-caustics_13.png
   :width: 800px
