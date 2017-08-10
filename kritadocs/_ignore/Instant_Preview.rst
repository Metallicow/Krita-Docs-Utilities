Instant Preview(Previously known under the code name Level Of Detail/LOD
strokes) is Krita's special speed-up mechanism that was funded by the
2015 Kickstarter. Krita slows down with really large images due the
large amount of data it's crunching in painting these images. Instant
Preview works by taking a smaller version of the canvas, and drawing the
feedback on there while Krita calculates the real stroke in the
background. This means that if you have a 4k screen and are working on a
4k image at 100% zoom, you won't feel any speed up.

Activating Instant Preview
--------------------------

.. raw:: mediawiki

   {{Warning|Instant Preview requires OpenGL 3.0 support at minimum. So if you don't have ''high-quality'' scaling available in '''settings &amp;rarr; configure Krita &amp;rarr; display &amp;rarr; display scaling filter''', then you wont't be able to use Instant Preview either.}}

|The Global Instant Preview toggle is under the view menu| Instant
Preview is activated in two places: The view
menu(<kbd>shift</kbd>+<kbd>L</kbd>), and the settings of the given
paintop by default. This is because Instant Preview has different
limitations with different paint operations.

For example, the overlay mode in the color smudge brush will disable the
ability to have Instant Preview on the brush, so does using 'fade'
sensor for size.

Similarly, the auto-spacing, fuzzy sensor in size, use of density in
brush-tip and the use of texture paintops will make it more difficult to
determine a stroke, and thus will give a feeling of 'popping' when the
stroke is finished.

When you check the brush settings, the Instant Preview checkbox will
have a \* behind it. Hovering over it will give you a list of options
that are affecting the Instant Preview mode. |The Instant Preview
checkbox at the bottom of the brush settings editor will give you
feedback when there's settings active that can't be previewed right.
Hover over it to get more detail. In this case, the issue is that
auto-spacing is on.|

Tools that benefit from Instant Preview
---------------------------------------

The following tools benefit from Instant Preview:

-  The Freehand brush tool.
-  The geometric tools.
-  The Move Tool.
-  The Filters.
-  Animation.

`Category:Reference Manual <Category:Reference_Manual>`__

.. |The Global Instant Preview toggle is under the view menu| image:: Lod_position.png
.. |The Instant Preview checkbox at the bottom of the brush settings editor will give you feedback when there's settings active that can't be previewed right. Hover over it to get more detail. In this case, the issue is that auto-spacing is on.| image:: Lod_position2.png
   :width: 500px
