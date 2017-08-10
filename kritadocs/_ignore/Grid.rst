The grid brush engine draws shapes on a grid. It helps you produce retro
and halftone effects.

If you're looking to setup a grid for snapping, head to `Grids and
Guides Docker <Special:MyLanguage/Grids_and_Guides>`__.

Reference
=========

Parameters
----------

-  `Brush Size <#Brush_Size>`__
-  `Particle Type <#Particle_Type>`__
-  `Blending Modes <Special:MyLanguage/Blending_Modes>`__
-  `Color Options <#Color_Options>`__
-  `Painting Mode <Special:MyLanguage/Opacity_&amp;_Flow>`__

Brush Size
----------

Grid Width
    Width of the cursor area
Grid Height
    Height of the cursor area
Division
    Subdivides the cursor area and uses the resulting area to draw the
    particles.
Division by pressure
    The more you press, the more subdivisions. Uses Division as the
    finest subdivision possible.
Scale
    Scales up the area.
Vertical Border
    Forces vertical borders in the particle space, between which the
    particle needs to squeeze itself.
Horizontal Border
    Forces a horizontal borders in the particle space, between which the
    particle needs to squeeze itself.
Jitter Borders
    Randomizes the border values with the Border values given as
    maximums.

Particle Type
-------------

Decides the shape of the particle.

Ellipse
    Fills the area with a ellipse.
Rectangle
    Fills the area.
Line
    Draws lines from the lower left to the upper right corner of the
    particle
Pixel
    Looks like an aliased line on high resolutions.
    Anti-aliased Pixel
    Fills the area with little polygons.

Color Options
-------------

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

`Category:Brush
Engines{{#translation:}} <Category:Brush_Engines{{#translation:}}>`__
