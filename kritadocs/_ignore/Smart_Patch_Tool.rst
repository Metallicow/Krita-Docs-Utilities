.. raw:: mediawiki

   {{ToolIcon|smart_patch}}

The smart patch tool allows you to seamlessly remove elements from the
image. It does this by letting you draw the area which has the element
you wish to remove, and then it will attempt to use patterns already
existing in the image to fill the blank.

You can see it as a smarter version of the clone brush.

.. figure:: Smart-patch.gif
   :alt: Smart-patch.gif

   Smart-patch.gif

The smart patch tool has the following tool options:

.. figure:: Tool-options-smartpatch.png
   :alt: Tool-options-smartpatch.png

   Tool-options-smartpatch.png

Accuracy
--------

Accuracy indicates how many samples, and thus how often the algorithm is
run. A low accuracy will do few samples, but will also run the algorithm
fewer times, making it faster. Higher accuracy will do many samples,
making the algorithm run more often and give more precise results, but
because it has to do more work, it is slower.

Patch size
----------

Patch size determines how big the size of the pattern to choose is. This
will be best explained with some testing, but if the surrounding image
has mostly small elements, like branches, a small patch size will give
better results, while a big patch size will be better for images with
big elements, so they get reused as a whole.

<!---->

Category:Toolbox `Category:Unstable
Features <Category:Unstable_Features>`__
