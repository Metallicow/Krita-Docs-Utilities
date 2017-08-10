You can access the General Category of the preferences by first going to
<span class=“menuchoice”>Settings > Configure Krita </span>

.. figure:: Krita_Preferences_General.png
   :alt: Krita_Preferences_General.png

   Krita\_Preferences\_General.png

Cursor Settings
---------------

Customise the drawing cursor here:

Cursor Shape
~~~~~~~~~~~~

Select a cursor shape to use while the brush tools are used. This cursor
will always be visible on the canvas. It is usually set to a type
exactly where your pen nib is at. The available cursor types are shown
below.

Tool Icon
    Shows the currently selected tool icon,even for the freehand brush.

.. figure:: Settings_cursor_tool_icon.png
   :alt: Settings_cursor_tool_icon.png

   Settings\_cursor\_tool\_icon.png

Arrow
    Shows a generic cursor.

.. figure:: Settings_cursor_arrow.png
   :alt: Settings_cursor_arrow.png

   Settings\_cursor\_arrow.png

Crosshair
    Shows a precision reticule.

.. figure:: Settings_cursor_crosshair.png
   :alt: Settings_cursor_crosshair.png

   Settings\_cursor\_crosshair.png

Small circle
    Shows a small white dot with a black outline.

.. figure:: Settings_cursor_small_circle.png
   :alt: Settings_cursor_small_circle.png

   Settings\_cursor\_small\_circle.png

No Cursor
    Show no cursor, useful for tablet-monitors.

.. figure:: Settings_cursor_no_cursor.png
   :alt: Settings_cursor_no_cursor.png

   Settings\_cursor\_no\_cursor.png

Triangle Right-Handed.
    Gives a small white triangle with a black border.

.. figure:: Settings_cursor_triangle_righthanded.png
   :alt: Settings_cursor_triangle_righthanded.png

   Settings\_cursor\_triangle\_righthanded.png

Triangle Left-Handed.
    Same as above but mirrored.

.. figure:: Settings_cursor_triangle_lefthanded.png
   :alt: Settings_cursor_triangle_lefthanded.png

   Settings\_cursor\_triangle\_lefthanded.png

Black Pixel
    Gives a single black pixel.

.. figure:: Settings_cursor_black_pixel.png
   :alt: Settings_cursor_black_pixel.png

   Settings\_cursor\_black\_pixel.png

White Pixel
    Gives a single white pixel.

.. figure:: Settings_cursor_white_pixel.png
   :alt: Settings_cursor_white_pixel.png

   Settings\_cursor\_white\_pixel.png

Outline Shape
~~~~~~~~~~~~~

Select an outline shape to use while the brush tools are used. This
cursor shape will optionally show in the middle of a painting stroke as
well. The available outline shape types are shown below.(pictures will
come soon)

No Outline
    No outline.
Circle Outline
    Gives a circular outline approximating the brush size.
Preview Outline
    Gives an outline based on the actual shape of the brush.
Tilt Outline
    Gives a circular outline with a tilt-indicator.

Show Outline When Painting
    This option when selected will show the brush outline while a stroke
    is being made. If unchecked the brush outline will not appear during
    stroke making, it will show up only after the brush stroke is
    finished. This option works only when Brush Outline is selected as
    the Cursor Shape.

Window Settings
---------------

Multiple Document Mode
    This can be either tabbed like **GIMP** or **Painttool Sai**, or
    subwindows, like **Photoshop**.
Background image
    Allows you to set a picture background for subwindow mode.
Window Background
    Set the colour of the subwindow canvas area.
Don't show contents when moving subwindows.
    This gives an outline when moving windows to work around ugly
    glitches with certain graphics-cards.
Show on-canvas popup messages
    Whether or not you want to see the on-canvas pop-up messages that
    tell you whether you are in tabbed mode, rotating the canvas, or
    mirroring it.
Enable Hi-DPI support
    Attempt to use the Hi-DPI support. It is an option because we are
    still experiencing bugs on windows.
Allow only once instance of Krita
    An instance is a single entry in your system's task manager. Turning
    this option makes sure that Krita will check if there's an instance
    of Krita open already when you instruct it to open new documents,
    and then have your documents opened in that single instance. There's
    some obscure uses to allowing multiple instances, but if you can't
    think of any, just keep this option on.

Tool options
------------

In docker (default)
    Gives you the tool options in a docker.
In toolbar
    Gives you the tool options in the toolbar, next to the brush
    settings. You can open it with <kbd>\\ </kbd>

Switch ctrl/alt modifiers
    This switches the function of the ctrl and alt buttons when
    modifying selections. Useful for those used to Gimp instead of
    photoshop, or Lefties without a right-alt key on their keyboard.

Enable Touchpainting
    This allows fingerpainting with capacitive screens. Some devices
    have both capacitive touch and a stylus, and then this can
    interfere. In that case, just toggle this.

Miscellaneous
-------------

Autosave Every
    Here the user can specify how often Krita should autosave the file,
    you can tick the checkbox to turn it off. For Windows these files
    are saved in the %TEMP% directory. If you are on Linux it is stored
    in /home/'username'.
Compress \*.kra files more.
    This increases the zip compression on the saved Krita files, which
    makes them lighter on disk, but this takes longer to load.
Upon importing Images as Layers, convert to the image color space.
    This makes sure that layers are the same color space as the image,
    necessary for saving to PSD.
Undo Stack Size
    This is the number of undo commands Krita remembers. You can set the
    value to 0 for unlimited undos.
Favorite Presets
    This determines the amount of presets that can be used in the
    `pop-up
    palette <Special:MyLanguage/Krita/Manual/Interface#Pop-up_Palette>`__.
Create Backup File
    When selected Krita will try to save a backup file in case of a
    crash.
Hide splash screen on startup.
    This'll hide the splash screen automatically once Krita is fully
    loaded.
Enable Native File Dialog
    This allows you to use the system file dialog. By default turned off
    because we cannot seem to get native file dialogues 100% bugfree.
Maximum brush size
    This allows you to set the maximum brush size to a size of up to
    10.000 pixels. Do be careful with using this, as a 10.000 size pixel
    can very quickly be a full gigabyte of data being manipulated, per
    dab. In other words, this might be slow.
Recalculate animation cache in background.
    This allows you to set whether the animation is cached for playback
    in the background. Then, when animation is cached when pressing
    play, this caching will take less long. However, turning off this
    automatic caching can save power by having your computer work less.

`Category:Preferences{{#translation:}} <Category:Preferences{{#translation:}}>`__
