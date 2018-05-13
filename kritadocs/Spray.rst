Spray
=====

A brush that can spray particles around in it's brush area.

Reference
---------

Parameters
~~~~~~~~~~

-  `Spray Area <#Spray_Area>`__
-  `Spray Shape <#Spray_Shape>`__
-  `Brush-tips <Special:MyLanguage/Brush_Tips>`__ (Used as particle if
   spray shape is not active)
-  `Opacity and Flow <Special:MyLanguage/Opacity_&amp;_Flow>`__
-  `Size (Parameter) <Special:MyLanguage/Parameters#Size>`__
-  `Blending Modes <Special:MyLanguage/Blending_Modes>`__
-  `Shape Dynamics <#Shape_Dynamics>`__
-  `Color Options <#Color_Options>`__
-  `Rotation (Parameter) <Special:MyLanguage/Parameters#Rotation>`__
-  `Airbrush <Special:MyLanguage/Parameters#Airbrush>`__
-  `Painting
   Mode <Special:MyLanguage/Opacity_&amp;_Flow#Painting_Mode>`__

Spray Area
~~~~~~~~~~

The area in which the particles are sprayed.

Diameter
    The size of the area.
Aspect Ratio
    It's aspect ratio: 1.0 is fully circular.
Angle
    The angle of the spray size: works nice with aspect ratios other
    than 1.0.
Scale
    Scales the diameter up.
Spacing
    Increases the spacing of the diameter's spray.

Particles
^^^^^^^^^

Count
    Use a specified amount of particles.
Density
    Use a % amount of particles.
Jitter Movement
    Jitters the spray area around for extra randomness.
Gaussian Distribution
    Focusses the particles to paint in the center instead of evenly
    random over the spray area.

Spray Shape
~~~~~~~~~~~

If activated, this will generate a special particle. If not, the
brush-tip will be the particle.

Shape
    Can be...

-  Ellipse
-  Rectangle
-  Anti-aliased Pixel
-  Pixel
-  Image

Width & Height
    Decides the width and height of the particle.
Proportional
    Locks Width & Height to be the same.
Texture
    Allows you to pick an image for the <menu choice>image shape.

Shape Dynamics
~~~~~~~~~~~~~~

Random Size
    Randomizes the particle size between 1x1 px and the given size of
    the particle in brush-tip or spray shape.
Fixed Rotation
    Gives a fixed rotation to the particle to work from.
Randomized Rotation
    Randomizes the rotation.
Follow Cursor Weight
    How much the pressure affects the rotation of the particles. At 1.0
    and high pressure it'll seem as if the particles are exploding from
    the middle.
Angle Weight
    How much the spray area angle affects the particle angle.

Color Options
~~~~~~~~~~~~~

Random HSV
    Randomize the HSV with the strength of the sliders. The higher, the
    more the color will deviate from the foreground color, with the
    direction indicating clock or counter clockwise.
Random Opacity
    Randomizes the opacity.
Color Per Particle
    Has the color options be per particle instead of area.
Sample Input Layer.
    Will use the underlying layer as reference for the colors instead of
    the foreground color.
Fill Background
    Fills the area before drawing the particles with the background
    color.
Mix with background color.
    Gives the particle a random color between foreground/input/random
    HSV and the background color.

