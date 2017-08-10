<languages/> <translate> <!--T:116--> If this is your first foray into
digital painting, this page should give you a brief introduction about
the basic but important concepts required for getting started with
digital painting in Krita.

<!--T:117--> This page is very, very long because it tries to cover all
the important things you should know Krita is capable of, and Krita is
really powerful. So this page can also be considered a guide through
Krita's most important functionality. Hopefully it will help you grasp
what buttons are for, even if you don't know the exact purpose of them.

Raster and Vector
-----------------

<!--T:118-->

<!--T:119--> Even though Krita is primarily a raster based application,
it has some vector editing capabilities as well. If you are new to
Digital painting medium, it is necessary that you know the concepts of
raster and vector.

<!--T:120--> In digital imaging, a pixel (Picture Element) is a basic
and lowest element of an Image. It is basically a grid of points each
displaying specific color. Raster editing is manipulating and editing
these pixels. For example when you take a 1-pixel brush which is colored
black and painting on the white canvas in Krita you are actually
changing the color of the pixel beneath your brush from white to
black.When you zoom in and see a brush stroke you can notice many small
squares with colors, these are pixels

<!--T:121--> |Pixels-brushstroke.png|\ <!--replace this image if
translating, I guess(upload as Pixels-brushstoke-languagecode.png and
replace the image link)-->

<!--T:122--> In contrast, vector graphic work is based on mathematical
expressions. They are independent of the pixel. For example, when you
draw a rectangle on a vector layer in Krita you are actually drawing
paths passing through points called nodes which are located on specific
co-ordinates on the 'x' and 'y' axes. When you re-size or move these
points the computer calculates and redraws the path and displays the
newly formed shape to you. Hence you can re-size the vector shape to any
extent without any loss in quality.

<!--T:123--> In Krita everything which is not on a vector layer is
raster based.

Images, Views and Windows
-------------------------

<!--T:124-->

<!--T:125--> In a painting program, there are three major containers
that make up your work-space.

Image
~~~~~

<!--T:126-->

<!--T:127--> The most important one is the *Image*.

<!--T:128--> This is a individual copy of the image you opened or made
via the file dialog, and where you edit your file. Krita can allow you
to open the file as a new copy via the file menu, or to save it as a new
file, or make an incremental save. An image contains layers, a colour
space, a canvas size and meta-data such as creator, data created, and
DPI. Krita can open multiple images at once, you can switch between them
via the <span class=“menuchoice”>window</span> menu.

<!--T:129--> Because the image is a working copy of the image on the
hard drive, you can do a lot of little saving tricks with it:

<!--T:130-->

New
    Makes a new image. When you press <span
    class=“menuchoice”>save</span>, you make a new file on the hard
    drive.
Open
    Makes an internal copy of an existing image. When you press <span
    class=“menuchoice”>save</span> you will overwrite the original
    existing image with your working copy.
Open existing image as new
    Similar to Open, however, <span class=“menuchoice”>save</span> will
    request you to specify a saving location: you're making a new copy.
    This is similar to <span class=“menuchoice”>import</span> in other
    programs.
Create Copy From Current Image
    Similar to <span class=“menuchoice”>Open Existing Image as
    new</span> but with the currently selected image.
Save incremental
    Allows you to quickly make a snapshot of the current image by making
    a new file with a versioning number added to it.

<!--T:131--> These options are great for people doing production work,
who need to switch between files quickly, or have backup files in case
they do something extreme. Krita also has a file backup system in the
form of auto-saves and back files and crash recovery. You can configure
these in the general settings.

<!--T:132--> You view the image via a *View*.

View
~~~~

<!--T:133-->

<!--T:134--> A view is the window onto your image. Krita allows you to
have multiple views, and you can manipulate the view to zoom, rotate and
mirror and modify the colour of the way you see an image without editing
the image itself. This is very useful for artists, as changing the way
they view the image is a common way to diagnose mistakes, like skewing
to one side. Mirroring with <kbd>m</kbd> makes such skewing easy to
identify.

<!--T:135--> If you have trouble drawing certain curves you will enjoy
using rotation for drawing, and of course there is zooming in and out
for precision and rough work. </translate>|<translate><!--T:136-->
Multiple views of the same image in Krita</translate>|\ <translate>
<!--T:137--> Multiple views are possible in Krita via <span
class=“menuchoice”>window &rarr; new view &rarr; image name</span>. You
can switch between them via the <span class=“menuchoice”>window</span>
menu, or <kbd>ctrl</kbd>+<kbd>tab</kbd>, or keep them in the same area
when *subwindow* mode is active in the
`settings <Special:myLanguage/GeneralSettings>`__, via <span
class=“menuchoice”>Window &rarr; Tile</span>.

Dockers
-------

<!--T:138-->

<!--T:139--> Dockers are little subwindows in `Krita's
interface <Special:MyLanguage/Navigation>`__. They contain useful tools,
like the color selector, layer stack, tool options etc.
</translate>|Dockers.png|\ <translate> <!--T:140--> The image above
shows some of the dockers in Krita

<!--T:141--> All the views and the dockers are held inside *Windows*

Window
~~~~~~

<!--T:142-->

<!--T:143--> If you've used a computer before, you know what windows
are: They are big containers for your computer programs.

<!--T:144--> Krita allows you to have multiple windows via <span
class=“menuchoice”>window->new window</span>. You can then drag this to
another monitor for multi-monitor use.

<!--T:145--> The image below shows an example of multiple windows in
Krita. </translate>|Multi-window.png|\ <translate>

Canvas in Krita
---------------

<!--T:146-->

<!--T:147--> When you create a new document in Krita for the first time
you will see a rectangular white area. This is called a canvas. You can
see it in the image below. The area marked by a red rectangle is a
canvas. <br> |Canvas-krita.png| When you save the painting as jpg , png
etc or take a print out of the painting, only the content inside this
area is taken into consideration. Anything beyond it is ignored. Krita
does store information beyond this area, you just won't be able to see
it. This data is stored in the *Layers*.

Layers and Compositing
----------------------

<!--T:148-->

<!--T:149--> Like a landscape painter will first paint the sky and then
the furthest away elements before slowly working his way to the
foreground elements, computers will do the same with all the things you
tell them to draw. So, if you tell them to draw a circle after a square
on the same spot, the circle will always be drawn later. This is called
the *Drawing Order*.

<!--T:150--> The layer stack is a way for you to separate elements of a
drawing and manipulate the drawing order by showing you which layers are
drawn when, and allowing you to change the order they are drawn in, and
all sorts of other effects. This is called *Compositing*.

<!--T:151--> This allows you to have line art above the colours, or
trees before the mountains, and edit each without affecting the other.

<!--T:152--> Krita has many layer-types, each doing a slightly different
thing:

<!--T:153-->

`Paint Layers <Special:MyLanguage/Paint_Layers>`__
    Also known as raster layers, and the most common layer type, you
    will be painting on these.
`Vector Layers <Special:MyLanguage/Vector_Layers>`__
    This is a layer type on which you draw vector graphics. Vector
    graphics are typically more simple than raster graphics and with the
    benefit that you can deform them with less blurriness.
`Group Layers <Special:MyLanguage/Group_Layers>`__
    These allow you to group several layers via drag and drop, so you
    can organize, move, apply masks and perform other actions on them
    together.
`Clone Layers <Special:MyLanguage/Clone_Layers>`__
    These are copies of the layer you selected when making them. They
    get updated automatically when changing the original.
`File Layers <Special:MyLanguage/File_Layers>`__
    These refer to an outside existing image, and update as soon as the
    outside image updates. Useful for logos and emblems that change a
    lot.
`Fill Layers <Special:MyLanguage/Fill_Layers>`__
    These layers are filled with something that Krita can make up on the
    fly, like colors or patterns.
`Filter Layers <Special:MyLanguage/Filter_Layers>`__
    Adding a filter in the layer-stack. We discuss these later on.

<!--T:154--> You can manipulate the content of the layers with *Tools*.

Tools
-----

<!--T:155-->

<!--T:156--> Tools help you manipulate the image data. The most common
one is of course, the freehand brush, which is the default when you open
Krita. There are roughly five types of tools in Krita:

<!--T:157-->

Paint Tools
    These are tools for painting on paint layers. They describe shapes,
    like rectangles, circles and straight lines, but also freehand
    paths. These shapes then get used by the Brush engines to make
    shapes and drawing effects.
Vector Tools
    This is the upper row of tools, which are used to edit vectors.
    Interestingly enough, all paint tools except the freehand brush
    allow you to draw shapes on the vector layers. These don't get a
    brush engine effect applied to them, though.
Selection Tools
    Selections allow you to edit a very specific area of the layer you
    are working on without affecting the others. The selection tools
    allow you modify the current selection. This is not unlike using
    masking-fluids in traditional painting, but whereas using masking
    fluids and film is often messy and delicate, selections are far
    easier to use.
Guide Tools
    These are tools like grids and assistants.
Transform Tools
    These are tools that allow you to transform your image. More on that
    later.

<!--T:158--> All tools can be found in the toolbox, and information can
be found in the tools section of the manual.

Brush Engines
-------------

<!--T:159-->

<!--T:160--> Brush engines, like mentioned before, take a path and
tablet information and add effects to it, making a stroke.

<!--T:161--> Engine is a term programmers use to describe a complex
interacting set of code that is the core for a certain functionality,
and is highly configurable. In short, like the engine of your car drives
your car, and the type of engine and its configuration affects how you
use your car, the brush engine drives the look and feel of the brush,
and different brush engines have different results.

<!--T:162--> Krita has `a LOT of different brush
engines <Special:MyLanguage/Brush_Engines>`__, all with different
effects. | 800px \| center\|\ **Left:** pixel brush, **center:** color
smudge brush, **right:** sketch brush| For example, the pixel-brush
engine is simple and allows you to do most of your basic work, but if
you do a lot of painting, the color smudge brush engine might be more
useful. Even though it's slower to use than the Pixel Brush engine, its
mixing of colors allows you to work faster.

<!--T:163--> If you want something totally different than that, the
sketch brush engine helps with making messy lines, and the shape brush
engine allows you to make big flats quickly. There are a lot of cool
effects inside Krita's brush engines, so try them all out, and be sure
to check the chapters on each.

<!--T:164--> You can configure these effects via the Brush Settings
drop-down, which can be quickly accessed via <kbd>f5</kbd>. These
configurations can then be saved into presets, which you can quickly
access with <kbd>f6</kbd> or the Brush Presets docker.

<!--T:165--> Brushes draw with colors, but how do computers understand
colors?

Colors
------

<!--T:166-->

<!--T:167--> Humans can see a few million colors, which are combinations
of electromagnetic waves (light) bouncing off a surface, where the
surface absorbs some of it. </translate>|<translate><!--T:168-->
Subtractive CMY colors on the left and additive RGB colors on the right.
This difference means that printers benefit from color conversion before
printing</translate>|\ <translate> <!--T:169--> When painting
traditionally, we use pigments which also absorb the right light-waves
for the color we want it to have, but the more pigments you combine, the
more light is absorbed, leading to a kind of murky black. This is why we
call the mixing of paints *subtractive*, as it subtracts light the more
pigments you put together. Because of that, in traditional pigment
mixing, our most efficient primaries are three fairly light colors: Cyan
blue and Magenta red and Yellow (CMY).

<!--T:170--> A computer also uses three primaries and uses a specific
amount of each primary in a color as the way it stores color. However, a
computer is a screen that emits light. So it makes more light, which
means it needs to do *additive* mixing, where adding more and more
colored lights result in white. This is why the three most efficient
primaries, as used by computers are Red, Green and Blue (RGB).

<!--T:171--> Per pixel, a computer then stores the value of each of
these primaries, with the maximum depending on the bit-depth. These are
called the *components* or *channels* depending on who you talk to.
</translate>|<translate><!--T:172--> This is the red-channel of an image
of a red rose. As you can see, the petals are white here, indicating
that those areas contain full red. The leaves are much darker,
indicating a lack of red, which is to be expected, as they are
green.</translate>|\ <translate><!--T:173--> Though by default computers
use RGB, they can also convert to CMYK (the subtractive model), or a
perceptual model like LAB. In all cases this is just a different way of
indicating how the colors relate to each other, and each time it usually
has 3 components. The exception here is grayscale, because the computer
only needs to remember how white a color is. This is why grayscale is
more efficient memory-wise.

<!--T:174--> In fact, if you look at each channel separately, they also
look like grayscale images, but instead white just means how much Red,
Green or Blue there is.

<!--T:175--> Krita has a very complex color management system, which you
can read more about `here <Special:MyLanguage/Category:Color>`__.

Transparency
~~~~~~~~~~~~

<!--T:176-->

<!--T:177--> Just like Red, Green and Blue, the computer can also store
how transparent a pixel is. This is important for *compositing* as
mentioned before. After all, there's no point in having multiple layers
if you can't have transparency.

<!--T:178--> Transparency is stored in the same way as colors, meaning
that it's also a channel. We usually call this channel the *alpha
channel* or *alpha* for short. The reason behind this is because the
letter 'α' is used to represent it in programming.

<!--T:179--> Some older programs don't always have transparency by
default. Krita is the opposite: it doesn't understand images that don't
track transparency, and will always add a transparency channel to
images. When a given pixel is completely transparent on all layers,
Krita will instead show a checkerboard pattern, like the rose image to
the left.

`Blending modes <Special:MyLanguage/Blending_Modes>`__
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

<!--T:180-->

<!--T:181--> Because colors are stored as numbers you can do maths with
them. We call this *Blending Modes* or *Compositing Modes*.

<!--T:182--> Blending modes can be done per layer or per brush stroke,
and thus are also part of the compositing of layers.

<!--T:183-->

Multiply
    A commonly used blending mode is for example <span
    class=“menuchoice”>multiply</span> which multiplies the components,
    leading to darker colors. This allows you to simulate the
    subtractive mixing, and thus makes painting shadows much easier.
Addition
    Another common one is <span class=“menuchoice”>Addition</span>,
    which adds one layer's components to the other, making it perfect
    for special glow effects.
Erasing
    <span class=“menuchoice”>Erasing</span> is a blending mode in Krita.
    There is no eraser tool, but you can toggle on the brush quickly
    with <kbd>E</kbd> to become an eraser. You can also use it on
    layers. Unlike the other blending modes, this one only affects the
    alpha channel, making things more transparent.
Normal
    The <span class=“menuchoice”>normal</span> blend mode just averages
    between colors depending on how transparent the topmost color is.

<!--T:184--> Krita has 76 blending modes, each doing slightly different
things. Head over to the `Blending Modes
page <Special:MyLanguage/Blending_Modes>`__ to learn more.

<!--T:185--> Because we can see channels as grayscale images, we can
convert grayscale images into channels. Like for example, we can use a
grayscale image for the transparency. We call these *Masks*.

Masks
-----

<!--T:186-->

<!--T:187--> Masks are a type of sub-effect applied to a layer, usually
driven by a grayscale image.

<!--T:188--> The primary type of mask is a `transparency
mask <Special:MyLanguage/Transparency_Masks>`__, which allows you to use
a grayscale image to determine the transparency, where black makes
everything transparent and white makes the pixel fully opaque.

<!--T:189--> You can paint on masks with any of the brushes, or convert
a normal paint-layer to a mask. The big benefit of masks is that you can
make things transparent without removing the underlying pixels.
Furthermore, you can use masks to reveal or hide a whole group layer at
once!

<!--T:190--> For example, we have a white ghost lady here: </translate>|
800px \|center|\ <translate><!--T:191--> <!-- not sure what to do with
the ghost lady images yet, for now they're outside of the translation,
maybe they'll get added in later so that you may replace her with
something else -->

<!--T:192--> But you can't really tell whether she's a ghost lady or
just really really white. If only we could give the idea that she
floats... We right-click the layer and add a transparency mask. Then, we
select that mask and draw with a black and white linear gradient so that
the black is below. </translate>| 800px \|center|\ <translate>
<!--T:193--> Wherever the black is, there the lady now becomes
transparent, turning her into a real ghost!

<!--T:194--> The name mask comes from traditional masking fluid and
film. You may recall the earlier comparison of selections to traditional
masking fluid. Selections too are stored internally as grayscale images,
and you can save them as a local selection which is kind of like a mask,
or convert them to a transparency mask.

Filters
-------

<!--T:195-->

<!--T:196--> We mentioned earlier that you can do maths with colors. But
you can also do maths with pixels, or groups of pixels or whole layers.
In fact, you can make Krita do all sorts of little operations on layers.
We call these operations *Filters*.

<!--T:197--> Examples of such operations are:

<!--T:198-->

Desaturate
    This makes all the pixels turn grey.
Blur
    This averages the pixels with their neighbours, which removes sharp
    contrasts and makes the whole image look blurry.
Sharpen
    This increases the contrast between pixels that had a pretty high
    contrast to begin with.
Color to Alpha
    A popular filter which makes all of the chosen color transparent.

</translate>|<translate><!--T:199--> Different filter brushes being used
on different parts of the image.</translate>|\ <translate> <!--T:200-->
Krita has many more filters available: read about them
`here <Special:MyLanguage/Filters>`__.

Filter Brush Engine
~~~~~~~~~~~~~~~~~~~

<!--T:201-->

<!--T:202--> Because many of these operations are per pixel, Krita
allows you to use the filter as part of the `filter brush
engine <Special:MyLanguage/Filter_Brush>`__.

<!--T:203--> In most image manipulation software, these are separate
tools, but Krita has it as a brush engine, allowing much more
customisation than usual.

<!--T:204--> This means you can make a brush that desaturates pixels, or
a brush that changes the hue of the pixels underneath.

Filter Layers, Filter Masks and Layerstyles
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

<!--T:205-->

<!--T:206--> Krita also allows you to let the Filters be part of the
layer stack, via `Filter Layers <Special:MyLanguage/Filter_Layers>`__
and `Masks <Special:MyLanguage/Filter_Masks>`__. Filter Layers affect
all the layers underneath it in the same hierarchy. Transparency and
transparency masks on Filter Layers affect where the layer is applied.

<!--T:207--> Masks, on the other hand, can affect one single layer and
are driven by a grayscale image. They will also affect all layers in a
group, much like a transparency mask.

<!--T:208--> We can use these filters to make our ghost lady look even
more ethereal, by selecting the ghost lady's layer, and then creating a
clone layer. We then right click and add a filter mask and use gaussian
blur set to 10 or so pixels. The clone layer is then put behind the
original layer, and set to the blending mode **Color Dodge**, giving her
a definite spooky glow. You can keep on painting on the original layer
and everything will get updated automatically! </translate>| 800px \|
center |\ <translate> <!--T:209--> Layer Effects or Layer Styles are
**Photoshop's** unique brand of Filter Masks that are a little faster
than regular masks, but not as versatile. They are available by right
clicking a layer and selecting 'layer style'.

Transformations
---------------

<!--T:210-->

<!--T:211--> *Transformations* are kind of like filters, in that these
are operations done on the pixels of an image. We have regular image and
layer wide transformations in the image and layer top menus, so that you
may resize, flip and rotate the whole image.

<!--T:212--> We also have the `crop
tool <Special:MyLanguage/Crop_Tool>`__, which only affects the canvas
size, and the `move tool <Special:MyLanguage/Move_Tool>`__ which only
moves a given layer. However, if you want more control, Krita offers a
`transform tool <Special:MyLanguage/Transform_Tool>`__. </translate>|
800px \| center|\ <translate> <!--T:213--> With this tool you can rotate
and resize on the canvas, or put it in perspective. Or you can use
advanced transform tools, like the warp, cage and liquefy, which allow
you to transform by drawing custom points or even by pretending it's a
transforming brush.

`Deform brush Engine <Special:MyLanguage/Deform>`__
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

<!--T:214-->

<!--T:215--> Like the filter brush engine, Krita also has a Deform Brush
Engine, which allows you to transform with a brush. The deform is like a
much faster version of the Liquefy transform tool mode, but in exchange,
its results are of much lower quality. </translate>| thumb\| 600px \|
center \| <translate><!--T:216--> Apple transformed into a pear with
liquefy on the left and deform brush on the right.</translate>
|\ <translate> <!--T:217--> Furthermore, you can't apply the deform
brush as a non-destructive mask.

`Transform Masks <Special:MyLanguage/Transformation_Masks>`__
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

<!--T:218-->

<!--T:219--> Like filters, transforms can be applied as a non
destructive operation that is part of the layer stack. Unlike filter and
transparency masks however, transform masks can't be driven by a
grayscale image, for technical reasons.

<!--T:220--> You can use transform masks to deform clone and file layers
as well.

`Animation <Special:MyLanguage/Animation>`__
--------------------------------------------

.. figure:: Introduction_to_animation_walkcycle_02.gif
   :alt: Introduction_to_animation_walkcycle_02.gif

   Introduction\_to\_animation\_walkcycle\_02.gif

In 3.0, Krita got raster animation support. You can use the timeline,
animation and onionskin dockers, plus Krita's amazing variety of brushes
to do raster based animations, export those, and then turn them into
movies or gifs.

Assistants, Grids and Guides
----------------------------

<!--T:221-->

<!--T:222--> With all this technical stuff, you might forget that Krita
is a painting program. Like how a illustrator in real life can have all
sorts of equipment to make drawing easier, Krita also offers a variety
of tools: </translate>|<translate><!--T:223--> Krita's vanishing point
assistants in action</translate>|\ <translate>

<!--T:224-->

`Grids and Guides <Special:MyLanguage/Grids_and_Guides>`__
    Very straightforward guiding tools which shows a grids or guiding
    lines that can be configured.
`Snapping <Special:MyLanguage/Snapping>`__
    You can snap to all sorts of things. Grids, guides, extensions,
    orthogonals, image centers and bounding boxes.
`Assistants <Special:MyLanguage/Painting_With_Assistants>`__
    Because you can hardly put a ruler against your tablet to help you
    draw, the assistants are there to help you draw concentric circles,
    perspectives, parallel lines and other easily forgotten but tricky
    to draw details. Krita allows you to snap to these via the tool
    options as well.

<!--T:225--> These guides are saved into Krita's native format, which
means you can pick up your work easily afterwards.

Customisation
-------------

<!--T:226-->

<!--T:227--> This leads to the final concept: Customisation.

<!--T:228--> In addition to rearranging the dockers according to your
preferences, Krita provides and saves your configurations as
`workspaces <Special:MyLanguage/Workspaces>`__. This is the button at
the top right.

<!--T:229--> You can also configure the toolbar via , as well as the
shortcuts under both and . </translate>

`Category:Getting
Started{{#translation:}} <Category:Getting_Started{{#translation:}}>`__

.. |Pixels-brushstroke.png| image:: Pixels-brushstroke.png
.. |<translate><!--T:136--> Multiple views of the same image in Krita</translate>| image:: Krita_multiple_views.png
   :width: 800px
.. |Dockers.png| image:: Dockers.png
   :width: 800px
.. |Multi-window.png| image:: Multi-window.png
   :width: 800px
.. |Canvas-krita.png| image:: Canvas-krita.png
   :width: 450px
.. | 800px \| center\|\ **Left:** pixel brush, **center:** color smudge brush, **right:** sketch brush| image:: Krita_example_differentbrushengines.png
.. |<translate><!--T:168--> Subtractive CMY colors on the left and additive RGB colors on the right. This difference means that printers benefit from color conversion before printing</translate>| image:: Krita_basics_primaries.png
   :width: 800px
.. |<translate><!--T:172--> This is the red-channel of an image of a red rose. As you can see, the petals are white here, indicating that those areas contain full red. The leaves are much darker, indicating a lack of red, which is to be expected, as they are green.</translate>| image:: Krita_basic_channel_rose.png
   :width: 300px
.. | 800px \|center| image:: Krita_ghostlady_1.png
.. | 800px \|center| image:: Krita_ghostlady_2.png
.. |<translate><!--T:199--> Different filter brushes being used on different parts of the image.</translate>| image:: Krita_basic_filter_brush.png
   :width: 300px
.. | 800px \| center | image:: Krita_ghostlady_3.png
.. | 800px \| center| image:: Krita_transforms_free.png
.. | thumb\| 600px \| center \| <translate><!--T:216--> Apple transformed into a pear with liquefy on the left and deform brush on the right.</translate> | image:: Krita_transforms_deformvsliquefy.png
.. |<translate><!--T:223--> Krita's vanishing point assistants in action</translate>| image:: Krita_basic_assistants.png
   :width: 800px
