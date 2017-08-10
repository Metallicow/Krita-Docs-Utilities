Brushes are ordered alphabetically. The brush that is selected by
default when you start with Krita is the **Pixel Brush**. The pixel
brush is the traditional mainstay of digital art. This brush paints
impressions of the brush tip along your stroke with a greater or smaller
density.

.. figure:: Krita_Pixel_Brush_Settings_Popup.PNG
   :alt: Krita_Pixel_Brush_Settings_Popup.PNG

   Krita\_Pixel\_Brush\_Settings\_Popup.PNG

Let's first review these mechanics:

#. select a brush tip. This can be a generated brush tip (round, square,
   star-shaped), a predefined bitmap brush tip, a custom brush tip or a
   text.
#. select the spacing: this determines how many impressions of the tip
   will be made along your stroke
#. select the effects: the pressure of your stylus, your speed of
   painting or other inputs can change the size, the color, the opacity
   or other aspects of the currently painted brush tip instance -- some
   applications call that a “dab”.
#. depending on the brush mode, the previously painted brush tip
   instance is mixed with the current one, causing a darker, more
   painterly stroke, or the complete stroke is computed and put on your
   layer. You will see the stroke grow while painting in both cases, of
   course!

Available Parameters:

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
-  `Source <Special:myLanguage/Parameters#Source>`__
-  `Mix <Special:myLanguage/Parameters#Mix>`__
-  `Airbrush <Special:myLanguage/Parameters#Airbrush>`__
-  `Painting Mode <Special:myLanguage/Opacity_&amp;_Flow>`__
-  `Texture <Special:myLanguage/Texture>`__

Specific Parameters to the Pixel Brush Engine
---------------------------------------------

Darken
~~~~~~

Allows you to Darken the source colour with Sensors.

.. figure:: Krita_2_9_brushengine_darken_01.png
   :alt: Krita_2_9_brushengine_darken_01.png

   Krita\_2\_9\_brushengine\_darken\_01.png

The color will always become black in the end, and will work with Plain
Color, Gradient and Uniform random as source.

Hue, Saturation, Value
~~~~~~~~~~~~~~~~~~~~~~

These parameters allow you to do a HSV adjustment filter on the
`Source <Special:myLanguage/Parameters#Source>`__ and control it with
Sensors. |Krita\_2\_9\_brushengine\_HSV\_01.png|

Works with Plain Color, Gradient and Uniform random as source.

**Uses**

.. figure:: Krita_2_9_brushengine_HSV_02.png
   :alt: Krita_2_9_brushengine_HSV_02.png

   Krita\_2\_9\_brushengine\_HSV\_02.png

Having all three parameters on Fuzzy will help with rich color texture.
In combination with `Mix
Parameter <Special:myLanguage/Parameters#Mix>`__, you can have even
finer control.

`Category:Brush
Engines{{#translation:}} <Category:Brush_Engines{{#translation:}}>`__

.. |Krita\_2\_9\_brushengine\_HSV\_01.png| image:: Krita_2_9_brushengine_HSV_01.png

