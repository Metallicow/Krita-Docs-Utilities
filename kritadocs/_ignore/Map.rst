Filters that are signified by them mapping the input image.

Small Tiles
~~~~~~~~~~~

Tiles the input image, using it's own layer as output.

Phong Bumpmap
~~~~~~~~~~~~~

.. figure:: Krita-normals-tutoria_4.png
   :alt: Krita-normals-tutoria_4.png

   Krita-normals-tutoria\_4.png

Uses the input image as a height-map to output a 3d something, using the
phong-lambert shading model. Useful for checking one's height maps
during game texturing. Checking the box will make it use all channels
and interpret them as a normal map.

Round Corners
~~~~~~~~~~~~~

Adds little corners to the input image.

Normalize
~~~~~~~~~

This filter takes the input pixels, puts them into a 3d vector, and then
normalizes(makes the vector size exactly 1) the values. This is helpful
for normal maps and some minor image-editing functions.

Gradient Map
~~~~~~~~~~~~

Maps the lightness of the input to the selected gradient. Useful for
fancy artistic effects.

Category:Internal_filters
