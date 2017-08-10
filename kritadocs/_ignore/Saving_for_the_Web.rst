Krita's default saving format is the
`\*.kra <Special:MyLanguage/*.kra>`__ format. This format saves
everything Krita can manipulate about an image: Layers, Filters,
Assistants, Masks, Color spaces, etc. However, that's a lot of data, so
\*.kra files are pretty big. This doesn't make them very good for
uploading to the internet. Imagine how many people's data-plans hit the
limit if they only could look at \*.kra files! So instead, we optimise
our images for the web.

There's a few steps involved:

#. Save as a .kra. This is your working file and serves as a backup if
   you make any mistakes.
#. Flatten all layers. This turns all your layers into a single one.
   Just go to <span class=“menuchoice”>Layer &rarr; Flatten Image</span>
   or press <kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>E</kbd>. Flattening
   can take a while, so if you have a big image, don't be scared if
   Krita freezes for a few seconds. It'll become responsive soon enough.
#. Convert the color space to 8bit sRGB(if it isn't yet). This is
   important to lower the filesize, and PNG for example can't take
   higher than 16bit. <span class=“menuchoice”>Image &rarr; Convert
   Image Color Space</span> and set the options to **RGB**, **8bit** and
   **sRGB-elle-v2-srgbtrc.icc** respectively. If you are coming from a
   linear space, uncheck <span class=“menuchoice”>little CMS
   optimisations</span>
#. Resize! Go to <span class=“menuchoice”>image &rarr; scale image to
   new size</span> or use <kbd>Ctrl</kbd>+<kbd>Alt</kbd>+<kbd>I</kbd>.
   This calls up the resize menu. A good rule of thumb for resizing is
   that you try to get both sizes to be less than 1200 pixels. (This
   being the size of HD formats). You can easily get there by setting
   the <span class=“menuchoice”>Resolution</span> under <span
   class=“menuchoice”>Print Pize</span> to **72** dots per inch. Then
   press <span class=“menuchoice”>OK</span> to have everything resized.
#. Save as a web-safe image format. There's three that are especially
   recommended:

`JPG <Special:MyLanguage/*.jpg>`__
    Use this for images with a lot of different colors, like paintings.
`PNG <Special:MyLanguage/*.png>`__
    Use this for images with few colours or which are black and white,
    like comics and pixel-art. Select 'save indexed if possible' to
    optimise even more.
`GIF <Special:MyLanguage/*.gif>`__
    Only use this for animation(will be supported this year) or images
    with a super low color count, because they will get indexed.

Saving with Transparency
~~~~~~~~~~~~~~~~~~~~~~~~

|Save\_with\_transparency.png| Saving with transparency is only possible
with gif and png. First, make sure you see the transparency
checkers(this can be done by simply hiding the bottom layers, changing
the projection color in , or by using . Then, save as PNG and tick

Save your image, upload, and show it off!

Category:Tutorials

.. |Save\_with\_transparency.png| image:: Save_with_transparency.png

