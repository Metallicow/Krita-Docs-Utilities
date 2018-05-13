Particle
========

A brush that draws wires using parameters. These wires always get more
random and crazy over drawing distance. Gives very intricate lines best
used for special effects.

Reference
---------

Parameters
~~~~~~~~~~

-  `Brush size <#Brush_size>`__
-  `Blending Modes <Special:MyLanguage/Blending_Modes>`__
-  `Airbrush <Special:MyLanguage/Parameters#Airbrush>`__
-  `Painting Mode <Special:MyLanguage/Opacity_&amp;_Flow>`__

Brush Size
~~~~~~~~~~

Particles
    How many particles there's drawn.
Opacity Weight
    The Opacity of all particles. Is influenced by the painting mode.
Dx Scale (Distance X Scale)
    How much the horizontal cursor distance affects the placing of the
    pixel. Is unstable on negative values. 1.0 is equal.
Dy Scale (Distance Y Scale)
    How much the vertical cursor distance affects the placing of the
    pixel. Is unstable on negative values. 1.0 is equal.
Gravity
    Multiplies with the previous particle's position, to find the new
    particle's position.
Iterations
    The higher, the higher the internal acceleration is, with the
    furthest away particle from the brush having the highest
    acceleration. This means that the higher iteration is, the faster
    and more randomly a particle moves over time, giving a messier
    result.

