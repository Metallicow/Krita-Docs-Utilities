Tangent Normal
==============

The Tangent Normal Brush Engine is an engine that is specifically
designed for drawing normal maps, of the tangent variety. These are in
turn used in 3d programs and game engines to do all sorts of lightning
trickery. Common uses of normal maps include faking detail where there
is none, and to drive transformations(Flow Maps).

A Normal map is an image that holds information for vectors. In
particular, they hold information for Normal Vectors, which is the
information for how the light bends on a surface. Because Normal Vectors
are made up of 3 coordinates, just like colors, we can store and see
this information as colors.

Normals can be seen similar to the stylus on your tablet. Therefore, we
can use the tilt-sensors that are available to some tablets to generate
the colour of the normals, which can then be used by a 3d program to do
lighting effects.

In short, you will be able to paint with surfaces instead of colors.

The following options are available to the tangent normal brush engine:

-  `Brush Tips <Special:myLanguage/Brush_Tips>`__
-  `Blending Modes <Special:myLanguage/Blending_Modes>`__
-  `Opacity & Flow <Special:myLanguage/Opacity_&amp;_Flow>`__
-  `Size <Special:myLanguage/Parameters#Size>`__
-  `Spacing <Special:myLanguage/Parameters#Spacing>`__
-  `Mirror <Special:myLanguage/Parameters#Mirror>`__
-  `Softness <Special:myLanguage/Parameters#Softness>`__
-  `Sharpness <Special:myLanguage/Parameters#Sharpness>`__
-  `Rotation <Special:myLanguage/Parameters#Rotation>`__
-  `Scatter <Special:myLanguage/Parameters#Scatter>`__
-  `Airbrush <Special:myLanguage/Parameters#Airbrush>`__
-  `Painting Mode <Special:myLanguage/Opacity_&amp;_Flow>`__
-  `Texture <Special:myLanguage/Texture>`__

Specific Parameters to the Tangent Normal Brush Engine
------------------------------------------------------

Tangent Tilt
~~~~~~~~~~~~

These are the options that determine how the normals are calculated from
tablet input.

Tangent Encoding
    This allows you to set what each color channel means. Different
    programs set different coordinates to different channels, a common
    version is that the green channel might need to be inverted(-Y), or
    that the green channel is actually storing the x-value (+X).
Tilt Options
    Allows you to choose which sensor is used for the X and Y.
Tilt
    Uses Tilt for the X and Y.
Direction
    Uses the drawing angle for the X and Y and Tilt-elevation for the Z,
    this allows you to draw flowmaps easily.
Rotation
    Uses rotation for the x and y, and tilt-elevation for the Z. Only
    available for specialized Pens.
Elevation Sensitivity
    Allows you to change the range of the normal that are outputted. At
    0 it will only paint the default normal, at 1 it will paint all the
    normals in a full hemisphere.

Usage
-----

The Tangent Normal Map Brush Engine is best used with the Tilt Cursor,
which can be set in <span class=“menuchoice”>Settings &rarr; configure
Krita &rarr; general &rarr; Outline Shape &rarr; Tilt Outline</span>.

Normal Map authoring workflow
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#. Create an image with a background color of (128, 128, 255)
   blue/purple.

.. figure:: images/tangent_normal/krita-normals-tutorial_1.png
   :alt: images/tangent_normal/krita-normals-tutorial_1.png

   Setting up a background with the default color.

#. Set up group with a phongbumpmap-filter mask. Use the 'use normal
   map' checkbox on the filter to make it use normals.

.. figure:: images/tangent_normal/krita-normals-tutorial_2.png
   :alt: images/tangent_normal/krita-normals-tutorial_2.png

   Creating a phong bump map filterlayer, make sure to check 'use
   normalmap'.

.. figure:: images/tangent_normal/krita-normals-tutorial_3.png
   :alt: images/tangent_normal/krita-normals-tutorial_3.png

   These settings give a nice daylight-esque lighting setup, with light
   1 being the sun, light 3 being the light from the sky, and light 2
   being the light from the ground.

#. Make a 'normalize' filter layer or mask to normalize the normal map
   before feeding it into the phongbumpmap filter for the best results.
#. Then, paint on layers in the group to get direct feedback.

.. figure:: images/tangent_normal/krita-normals-tutoria_4.png
   :alt: images/tangent_normal/krita-normals-tutoria_4.png

   Paint on the layer beneath the filters with the tangent normal brush
   to have them be converted in real time.

#. Finally, when done, hide the phongbumpmap filter-layer(but keep the
   normalize filter layer!) , and export the normal map for use in 3d
   programs.

Drawing Direction Maps
~~~~~~~~~~~~~~~~~~~~~~

Direction maps are made with the 'Direction' option in the Tangent Tilt
options. These normal maps are used to distort textures in a 3d
program(to simulate for example, the flow of water) or to create maps
that indicate how hair and brushed metal is brushed. Krita can't
currently give feedback on how a given direction map will influence a
distortion or shader, but these maps are a little easier to read.

Just set the tangent-tilt option to direction, and draw. The direction
your brush draws in will be the direction that is encoded in the colors.

Only editing a single channel
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Sometimes you only want to edit a single channel. In that case set the
blending mode of the brush to 'copy <channel>', with <channel> replaced
with red, green or blue. These are under the misc section of the
blending modes.

So, if you want the brush to only affect the red channel, set the
blending mode to 'copy red'.

.. figure:: images/tangent_normal/Krita_Filter_layer_invert_greenchannel.png
   :alt: images/tangent_normal/Krita_Filter_layer_invert_greenchannel.png

   The copy red, green and blue blending modes also work on filter-layers.

This can also be done with filter layers. So if you
quickly want to flip a layer's green channel, make an invert filter
layer with 'copy green' above it.

Mixing Normal Maps
~~~~~~~~~~~~~~~~~~

For mixing two normal maps, Krita has the `Combine Normal
Map <special:myLanguage/Blending_Modes#Combine_Normal_Map>`__ blending
mode under 'misc'.


