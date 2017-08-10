Just like real life, there's many ways to mix colors. You have glossing,
scumbling, hatching, optical illusions. We can mimic most of these in a
digital medium as well, and each has a different effect.

Glossing
--------

.. figure:: Color_gloss.gif
   :alt: Color_gloss.gif

   Color\_gloss.gif

Glossing is the most important of all the mixing techniques.

Traditionally, it's overlaying many different semi-transparent layers
over one another to create visual mixtures. In digital painting, we can
also use it to mix colors on-canvas. We first lay down a
semi-transparent layer. Then, we pick the resultant color with
<kbd>ctrl</kbd>+(This can be configured in the canvas input settings),
and paint with that. Each layer we lay down, and each color we pick is
an avarage of the colors before it, leading to a nice mixture.

We can even more easily paint mix with glossing when we set the flow
low. `Flow <Special:MyLanguage/Opacity_%26_Flow>`__ is transparency per
dab instead of stroke, and it gives softer strokes without giving up
control.

Similarly, you can use blending modes like multiply to create nice
shadows.

.. figure:: Color_gloss_example_1.png
   :alt: Color_gloss_example_1.png

   Color\_gloss\_example\_1.png

We start with a plain base.

.. figure:: Color_gloss_example_2.png
   :alt: Color_gloss_example_2.png
   :width: 500px

   Color\_gloss\_example\_2.png

Then we set a semi-transparent brush to multiply and add two plain
colored layers over everything.

.. figure:: Color_gloss_example_3.png
   :alt: Color_gloss_example_3.png
   :width: 500px

   Color\_gloss\_example\_3.png

Then use a brush with low flow (0.30) to pick the resulting colors and
lay down layers. This'll give quite a painterly effect.

.. figure:: Color_gloss_example_4.png
   :alt: Color_gloss_example_4.png

   Color\_gloss\_example\_4.png

Continue with a lower opacity and flow to create smoother gradients.

Mixing and Smudging
-------------------

.. figure:: Color_mix.gif
   :alt: Color_mix.gif

   Color\_mix.gif

Mixing is done with the color smudge brush. The `color smudge
brush <Special:MyLanguage/Color_Smudge>`__ is a special brush engine
that allows you to mix the color you painting with, with the color under
the brush. It's a very powerful brush that gives a lovely painterly
effect, but it's a bit slower than the regular pixel brush.

If you remove all paint from a color smudge brush, you get a smudge
effect:

.. figure:: Color_smudge.gif
   :alt: Color_smudge.gif

   Color\_smudge.gif

Different smudge brushes have different effects, so be sure to try them
all out.

Scumbling
---------

Scumbling is when we, instead of having a semi-opaque layer, we use
layers of paint that are patterned. |Color\_scumble2.gif| Most painting
programs allow you to pick a `brush
tip <Special:MyLanguage/Brush_Tips>`__, which can be used to create a
textured effect like that of scumbling.

.. figure:: Color_scumble.gif
   :alt: Color_scumble.gif

   Color\_scumble.gif

Krita's brush engines also allows you to use the `texture
option <Special:MyLanguage/Texture>`__. This allows you to create
screentone like effects.

While glossing can get you pretty far, scumbling is the best method to
create texture and to break up big pasty flats in your drawing.

Other tips
----------

Mixing colors will often go far better in a `higher bit-depth like
16bit <Special:MyLanguage/Bit_Depth>`__, though it'll make the image
take up much more working memory(RAM). Furthermore, a `linear color
space <Special:MyLanguage/Gamma_and_Linear>`__ can often give far better
mixtures than a gamma-corrected one, though doing sketches and lineart
is easier to do in a gamma-corrected space.

Category:Color

.. |Color\_scumble2.gif| image:: Color_scumble2.gif

