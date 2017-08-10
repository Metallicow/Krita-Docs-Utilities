Krita's main goal is to help artists create digital painting from
scratch. Krita is used by comic artists, matte painters, texture
artists, and illustrators around the world. This section explains some
common workflow that artists use in Krita.

When you open a new document in Krita for the first time, you can start
painting instantly. The brush tool is selected by default and you just
have to paint on the canvas. However, let us look at what artists do in
Krita.

Below are some of the common workflows used in Krita:

Speed Painting and Conceptualizing
----------------------------------

Some artists work only on digital medium, sketching and visualizing
concepts in Krita from scratch. As the name suggests a technique of
painting done within matter of hours to quickly visualize the basic
scene , character, look and feel of the environment or to denote the
general mood and overall concept is called a **speed painting**.
Finishing and finer details are not the main goal of this type of
painting, but the representation of form value and layout is main goal.

Some artists set time limit to complete the painting while some paint
casually. Speed painting then can be taken forward by adding finer
details and polish to create a final piece.

Generally artists first block in the composition by adding patches and
blobs of flat colors, defining the silhouette etc . Krita has some
efficient brushes for this situation, for example the brush under
**Block Tag** like Block fuzzy, Block basic, layout\_block etc.

After the composition and a basic layout has been laid out the artists
add as much details as possible in the given limited time, this requires
a decent knowledge of forms, value perspective and proportions of the
objects. Below is an example of speed paint done by `David
Revoy <http://www.davidrevoy.com/>`__ done in an hours time.

.. figure:: Pepper-speedpaint-deevad.jpg
   :alt:  500px

    500px

Artwork by David Revoy, licence :
`CC-BY <http://creativecommons.org/licenses/by/3.0/>`__

You can view the recorded speed painting demo for the above image
`here <https://www.youtube.com/watch?v=93lMLEuxSLk>`__

Colorizing Line Art
-------------------

Often an artist for example a comic book colorist will need to take a
pencil sketch or other line art of some sort and use Krita to paint
underneath it. This can be either an image created digitally or
something that was done outside the computer and has been scanned.

Preparing the Lineart
~~~~~~~~~~~~~~~~~~~~~

If your images has a white or other single-tone background, you can use
either of the the following methods to prepare the art for coloring.:

Place the line-art at the top of the layer stack and set its layer
blending mode to Multiply

If you want to clean the lineart a bit you can press
<kbd>Ctrl</kbd>+<kbd>L</kbd> or go to <span class=“menuchoice”>Filters
-> Adjust -> levels </span>

`300px <File:Levels-filter.png>`__

You can clean the unwanted greys by moving the white triangle in the
input levels section to left and darken the black by moving the black
triangle to right.

If you draw in blue pencils and then ink your line art you may need to
remove the blue lines first to do that go to <span
class=“menuchoice”>Filter -> Adjust -> Color adjustment curves </span>
or press shortcut <kbd>Ctrl</kbd>+<kbd>M</kbd>.

.. figure:: Color-adjustment-cw.png
   :alt:  500px

    500px

now select **Red** from the drop-down, Click on the top right node on
the graph and slide it all the way down. Or you can click on the top
right node and enter **0** in the output field. Repeat this step for
**Green** too.

.. figure:: Color-adjustment-02.png
   :alt:  500px

    500px

Now the whole drawing will have a blue overlay, zoom in and check if the
blue pencil lines are still visible slightly, If you you still see them,
then go to *' Blue*' Channel in the color adjustment and shift the top
right node towards left a bit, Or enter a value around 190 ( one that
removes the remaining rough lines) in the input box.

.. figure:: Color-adjustment-03.png
   :alt:  500px

    500px

Now apply the color adjustment filter, yes we still have lots of blue on
the artwork be patient and move on to the next step. Go to <span
class=“menuchoice”>Filter -> Adjust -> Desaturate </span> or press
<kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>U</kbd> Now select **max**
from the list.

.. figure:: Color-adjustment-04.png
   :alt:  500px

    500px

.. raw:: mediawiki

   {{Info|It is good to use non-photo-blue pencils to create the blue lines as those are easy to remove. If you are drawing digitally in blue lines use #A4DDED color as this is closer to non-photo-blue color.}}

You can learn more about doing a sketch from blue sketch to digital
painting
`here <http://www.davidrevoy.com/article239/cleaning-blue-lines-sketch-in-krita>`__
in a tutorial by David Revoy.

After you have a clean black and white line-art you may need to erase
the white color and keep only black line-art, to achieve that go to
<span class=“menuchoice”>Filters->Color->Color to Alpha</span>. Use the
dialog box to turn all the white areas of the image transparent. The
Color Picker is set to White by default. If you have imported scanned
art and need to select another color for the paper color then you would
do it here.

.. figure:: Color-to-alpha.png
   :alt: Color-to-alpha.png

   Color-to-alpha.png

This will convert the white color in your line-art to alpha i.e. it will
make the white transparent leaving only the lineart. Your line-art can
be in grey-scale color space, this is a unique feature in Krita which
allows you to keep a layer in a color-space independent from the image.

Laying in Flat Colors
~~~~~~~~~~~~~~~~~~~~~

There are many ways to color a line art in Krita, but generally these
three are the common among the artists

#. Paint blocks of color directly with block brushes
#. Fill with Flood fill Tool
#. Use one of the GMIC colorise comics filters.

Blocking with brush
    The first is the more traditional method of taking a shape brush or
    using the geometric tools to lay in color. This would be similar to
    using an analog marker or brush on paper. There are various block
    brushes in Krita, you can select **Block** Tag from the dro-pdown in
    the brush presets docker and use the brushes listed there.

    Add a layer underneath your lineart layer and start painting with
    the brush, If you want to correct any area you can press
    <kbd>E</kbd> and convert the same brush into an eraser. You can also
    use a layer each for different colors for more flexibility.

Filling with Flood Fill tool
    The second method is to use the Flood fill tool to fill large parts
    of your line-art quickly. This method generally requires closed gaps
    in the line-art. To begin with this method place your line-art on a
    separate layer. Then activate the flood fill tool and set the grow
    selection to 2px, un-check limit to current layer if previously
    checked.

.. figure:: Floodfill-krita.png
   :alt:  600px

    600px

    Choose a color from color elector and just click on the area you
    want to fill the color. As we have expanded the fill with grow
    seclection the color will be filled slightly underneath the line-art
    thus giving us a clean fill.

GMIC Colorise [Interactive]
    The third method is to use take advantage of the integrated G'Mic
    filters. These are powerful filters that can dramatically improve
    your workflow and cut your down on your production time.
    To begin coloring with the GMIC colorize interactive, go to <span
    class=“menuchoice”>FIlter -> GMIC </span>. Choose <span
    class=“menuchoice”>Filter -> G'Mic -> Black & white ->
    Colorize[interactive]</span> from the list of filters. Then select
    **Line-art for Input type, Image + Colors (2 Layers)** for output
    type, set the view resolution according to your need. If you have
    any specific color palette to use for coloring add the path for it
    in additional color palette. The example of the filter window with
    the required inputs is shown below

.. figure:: GMIC-colorize-interactive-krita.png
   :alt: GMIC-colorize-interactive-krita.png
   :width: 600px

   GMIC-colorize-interactive-krita.png

    Press **Apply** to begin the coloring, this will open a color
    selector **palette** window and a window showing your lineart.
    Choose the color from the palette and click on the areas that needs
    to be filled with color like the example shown below.

.. figure:: Krita-GMIC-colorize-interactive.png
   :alt: Krita-GMIC-colorize-interactive.png
   :width: 600px

   Krita-GMIC-colorize-interactive.png

    If you feel that the dots are a bit distracting you can press
    <kbd>Tab</kbd> to reduce the size or hide the dots. to zoom out you
    can press <kbd>Ctrl</kbd>+<kbd>down arrow</kbd> and
    <kbd>Ctrl</kbd>+<kbd>up arrow</kbd> vice versa. Panning is done by
    +<kbd>drag</kbd>. Press <kbd>Spacebar</kbd> to generate the colors.
    If you want to replace a color select the color by and pressing
    <kbd>R</kbd> then you can select an alternate color from the
    palette.

    Once you have finished adding the desired flat colors you can press
    <kbd>Enter</kbd> to apply the filter. Then don't forget to press
    <span class=“menuchoice”>Ok</span> in the GMIC dialog box.

    The flats colors will be placed on a separate layer. You can check
    `this <http://www.davidrevoy.com/article240/gmic-line-art-colorization>`__
    tutorial by David Revoy to know more about this technique.

GMIC Colorize [comics]
    Krita provides one more option to prepare flat colors through GMIC
    colorize comics filter. This technique needs some preparations
    before you run the GMIC filter. This layer extrapolates the color
    spots that you input below the lineart

    You have to create two layers below the line art, one for the color
    spots indicating which color you need to be filled in the region and
    one for the final extrapolated output of the filter. Mark some
    colors spots in the layer beneath the lineart. The layer setup can
    be seen in the image below.

.. figure:: Colorize-krita.png
   :alt: Colorize-krita.png

   Colorize-krita.png

    The colors spots are marked in red in the image

    Now go to <span class=“menuchoice”>Filter -> G'Mic -> Black & white
    -> Colorize[comics]</span>. In the GMIC dialog box, select all for
    input and inplace(default) for output, select Lineart + color spots
    + extrapolated layers for both input and output layers on the right
    hand side. Smoothness is for filling gap tolerance and details the
    default is 0.5 you can adjust it according to your line art.

.. figure:: Colorise-comics-setting.png
   :alt:  600px

    600px

    Press <span class=“menuchoice”>Apply</span> and <span
    class=“menuchoice”>Ok</span> to apply and exit the GMIC dialog.
    You'll now have flat colors beneath you lineart.
    More details about this technique can be found in the tutorial
    `here <http://timotheegiet.com/blog/comics/gmic-colorize-comics-working-in-krita.html>`__.

Painting
--------

Starting from chaos
~~~~~~~~~~~~~~~~~~~

Here, you start by making a mess through random shapes and texture, then
taking inspirations from the resulting chaos you can form various
concepts. It is kind of like making things from clouds or finding
recognizable shapes of things in abstract and random textures. Many
concept artist work with this technique.

You can use brushes like the shape brush, or the spray brush to paint a
lot of different shapes, and from the resulting noise, you let you brain
pick out shapes and compositions.

.. figure:: Chaos2.jpg
   :alt: Chaos2.jpg
   :width: 400px

   Chaos2.jpg

You then refine these shapes to look more like shapes you think they
look, and paint them over with a normal paintbrush.

This method is best done in a painting environment.

Starting from a value based underground
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This method finds it's origins in old oil-painting practice: You first
make an under-painting and then paint over it with colour, having the
dark underground shine through.

With Krita you can use blending modes for this purpose. Choosing the
Color blending mode on a layer on top allows you to change the colours
of the image without changing the relative luminosity. This is useful,
because humans are much more sensitive to tonal differences than
difference in saturation and hue. This'll allow you to work in greyscale
before going into colour for the polishing phase.

You can find more about this technique
`here <http://www.davidrevoy.com/article185/tutorial-getting-started-with-krita-1-3-bw-portrait>`__.

Preparing Tiles and Textures
----------------------------

Many artists use Krita to create textures for 3d assets used for games
animation etc. Krita has many texture template for you to choose and get
started with creating textures. These template have common sizes, bit
depth and color profiles that are used for texturing workflow.

Krita also has a real-time seamless tile mode to help texture artist
prepare tiles and texture easily and check if it is seamless on the fly.
The tiled mode is called wrap around mode , to activate this mode you
have press <kbd>W</kbd>. No when you paint the canvas is tiled in
real-time allowing you to create seamless pattern and texture, it is
also easy to prepare interlocking patterns and motifs in this mode.

Starting from 2.9.7 Krita now has a new brush engine to support painting
normal maps you can read more about it
`here <Special:MyLanguage/Tangent_Normal>`__

Creating Pixel Art
------------------

Krita can also be used to create high definition pixel painting. The
pixel art look can be achieved by using Index color filter layer and
overlaying dithering patterns. The general layer stack arrangement is as
shown below

.. figure:: Layer-docker-pixelart.png
   :alt: Layer-docker-pixelart.png

   Layer-docker-pixelart.png

The index color filter maps specific user selected colors to the grey
scale value of the artwork. You can see the example below, the strip
below the black and white gradient has index color applied to it so that
the black and white gradient gets the color selected to different
values.

.. figure:: Gradient-pixelart.png
   :alt: Gradient-pixelart.png

   Gradient-pixelart.png

You can choose the required colors and ramps in the index color filter
dialog as shown below

.. figure:: Index-color-filter.png
   :alt: Index-color-filter.png

   Index-color-filter.png

Dithering can be used to enhance the look of the art and to ease the
banding occurred by the index color filter. Krita has a variety of
dithering patterns by default, these can be found in pattern docker. You
can use these patterns as fill layer , then set the blend mode to
**overlay** and adjust the opacity according to your liking. generally
an opacity range of 10% - 25% is ideal.

Paint the artwork in grey-scale and add a index color filter layer at
the top then add the dithering pattern fill layer below the index color
filter but above the artwork layer, as shown in the layer stack
arrangement above. You can paint or adjust the artwork at any stage as
we have added the index color filter as a filter layer.

You can add different groups for different colors and add different
dithering patterns for each group.

Below is an example painted with this layer arrangement

.. figure:: Kiki-pixel-art.png
   :alt: Kiki-pixel-art.png

   Kiki-pixel-art.png

Category:Tutorials
