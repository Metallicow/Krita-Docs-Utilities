A Word About Digital Brushes
----------------------------

Krita ships with an extensive set of Brush Presets so you can get
started right away. In addition, some members of the world-wide Krita
community have kindly posted their own customized brush sets that you
can download from the `Resources page <Special:MyLanguage/Resources>`__.

However, as you advance you may find yourself wanting to create or
customize specific brushes, or perhaps an entire category, that more
specifically suit your own needs. This could be anything from a
color-blending airbrush with a sharp edge to a brush that mimics a
traditional artist's Camel-hair bristle brush to a Blender brush that
closely mimics a Blending Stump. You do this by modifying the brush
settings and parameters. These correlate to each of the different types
of available Krita Brush Engines. For instance, the settings for the
Pixel Brush type are different from those of a Particle Brush and those
differ from a Color-Smudge type and so on.

When thinking about digital “brushes” though it's important to keep in
mind that a brush is just collections of the settings and parameters
that, when taken together, make or effect a mark. They combine to
produce the effect of the analog tools of an artist; like an Airbrush,
Ink Pen, 2B Pencil, etc... They can also represent items that would only
be found in the digital world, like painting with “predefined” brushes,
such as leaves, trees, textures, etc... This is one of the strengths of
many drawing programs and you will find it here in Krita as well.

We'll go into this in details later. For now, it's important to keep in
mind that, ultimately, the settings, variables and parameters assigned
to a brush combine to produce an interpretation of what might exist in
the analog world. For instance, the settings for one 2B Pencil preset
will likely differ from the brush set created by one person from those
of another.

If you download a set of brushes from someone and they have one marked
as Wet Oil Brush, keep in mind that this is just their interpretation of
what that stroke would look like. Your own might be different. This is
where a part of the great flexibility of Krita comes in. With Krita you
are not stuck with what you get “out of the box”. So with that in mind
let's take a look...

The Brush Settings Editor
-------------------------

We won't be going into all the details of the Brush Settings Editor in
this section since that will be covered later on **need section for
this**. What we want to focus on now are the steps required to create a
new Brush Preset and save it for reuse.

To start, the panel can be accessed in the toolbar, between the button
on the right and the button on the left. Alternately, you can use the
function key <kbd>F5</kbd> to open it. With the panel open you can
right-click and detach it from the toolbar if you wish. This is useful
if you have dual monitors and want to leave it open for quick access. It
is also useful, although not required, if, with a dual monitor setup,
you want to use the Multi-use Brush option described later.

When you open Brush Settings Editor panel you will see something like
this:

.. figure:: Brush_Settings_-_Full.PNG
   :alt: Brush_Settings_-_Full.PNG

   Brush\_Settings\_-\_Full.PNG

The screen is divided into several functional sections.

Left Panel
    list of Brush Engines that Krita supports
Center
    All configurable settings and parameters for every type of Brush
    Engine. Every single Krita brush is made from a combination of the
    settings found here.
Right Panel
    Brush Preview and ScratchPad area
Top Panel
    Brush Presets

At the bottom, there's a few really useful options, they are:

Default
    This gives the default brush settings for this brush engine.
Save Tweaks to Current Preset
    This enables dirty presets. Dirty presets store the tweaks you make
    as long as this session of Krita is active. After that, the revert
    to default. Dirtied presets can be recognised by the icon in the
    top-left of the preset.
Change Eraser Switch Size
    This switches the brush to a separately stored size when using the
    eraser(<kbd>E</kbd>) key.
Change Eraser Switch Opacity
    Same as above, but then with Eraser opacity.
Instant Preview
    This allows you to toggle `instant
    preview <Special:MyLanguage/Instant_Preview>`__ on the brush.

The Brush Preview and Brush Preset panels can be hidden anytime by and
unchecking the view option.

.. raw:: mediawiki

   {{Note|Sadly, this was broken by QT5, so not available in 3.0}}

Notice that the name of the active Brush Preset is at the top and the
two buttons to the right have been disabled. This is the default
condition when you first open up the Brush Editor or when you select a
brush that has no modifications waiting to be saved. This will be
important later on.

Modifying Brush Presets
-----------------------

Krita allows you to modify brushes in a wide variety of ways. You can:

-  take an existing Krita brush and modify it to meet you needs, saving
   it back for future use. This is the most typical way to create a
   custom brush.

-  tweak a brush for your needs at the moment. An very simple example
   would be adjusting the Diameter of the Brush Tip on a Pixel Brush to
   flatten it out, providing a less spherical tip. However, if you don't
   overwrite the settings then you can revert it back to the original by
   reloading the brush.

-  create your own brushes from scratch. This is probably not necessary
   for most people but Krita makes if fairly easy if you're so inclined.

-  load brushes created for Gimp or Photoshop. You can assign them to
   new Brush Presets and even customize them especially for Krita.

Creating a New Preset
---------------------

The easiest way to create a new preset is by editing the settings of an
existing one. In a nutshell, you choose an existing brush that has at
least something in common with what you're looking to create. For
instance, there would be little point in creating a new Airbrush variant
by starting with a Block Marker preset. In this case you would want to
start with an Airbrush preset and then give it a new name, customize the
things you want to change, modify the Preview Image and then overwrite
the preset. Of course, there are exceptions, but this a good, simple
workflow.

Naming the New Brush Preset
---------------------------

When you first load a brush into the Brush Setting Editor you will see
something at the top similar to:

.. figure:: Preset_Name_-_Inactive_Overwrite_Button.PNG
   :alt: Preset_Name_-_Inactive_Overwrite_Button.PNG

   Preset\_Name\_-\_Inactive\_Overwrite\_Button.PNG

This show the name of the currently loaded Brush Preset. As soon as you
make any change to the settings, the two buttons, Overwrite Preset and
Reload, will be enabled.

.. figure:: Preset_Name_-_Active_Overwrite_Button.PNG
   :alt: Preset_Name_-_Active_Overwrite_Button.PNG

   Preset\_Name\_-\_Active\_Overwrite\_Button.PNG

The first step in creating a new Brush Preset is to type the name of the
new preset (eg. Camel Oil Brush) in the **Name** field where you see the
existing brush name. As soon as you click into the Name field and make a
change to one or more characters then the button configuration changes
to:

.. figure:: Preset_Name_-_Active_Save_Preset_Button.PNG
   :alt: Preset_Name_-_Active_Save_Preset_Button.PNG

   Preset\_Name\_-\_Active\_Save\_Preset\_Button.PNG

Enter the name you want to give your new Brush Preset and click on <span
class=“menuchoice”>Save to Presets</span>. Now you are ready you safely
make changes and experiment without the danger of affecting the existing
brush you used as a template.

However, if you wanted to make changes to the settings of the existing
brush and have them be a part of the permanent configuration, then you
would not click in the **Name** field. Instead you would click the <span
class=“menuchoice”>Overwrite Preset</span> button when you have
completed your change(s) and are ready to save.

If, at any time, you want to reload the default settings of the
currently loaded brush then you can click the Reload button.

Creating a Preview Image of the New Brush
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The preview of your preset is generated from the square dotted line area
in the scratchpad on the right of the Brush Settings Editor. If you
don't see this vertically rectangular panel then right-click anywhere on
the Brush Settings Editor and make sure you have Show ScratchPad clicked
on as shown below.

.. figure:: Show_ScratchPad_dialog.PNG
   :alt: Show_ScratchPad_dialog.PNG

   Show\_ScratchPad\_dialog.PNG

Whatever you put in the square at the top of the panel will be the image
that is used in the Brush Presets docker and the Brush Presets, accessed
from the toolbar or by pressing <kbd>F5</kbd>. This can really be
anything you want to represent the meaning of this brush. Some people
create graphic images that represent analog tools (Pens, Pencils,
Brushes, Sponges, etc...), others prefer to show a representative stroke
if applicable. A third type is the texture brush which we'll be using as
an example later on.

Saving the New Preset
~~~~~~~~~~~~~~~~~~~~~

When you have made all your changes you can use the Overwrite Preset
button to save your new brush (remember that you gave it a new name
earlier so now it is safe to overwrite the settings.) This can be
tricky. If you didn't give the preset a new name earlier then clicking
the Overwrite Preset button will overwrite the setting for your original
brush. Much like Monty Python's Dead Parrot, it will “cease to be”.

.. figure:: Krita_Brush_Settings_Dialog.PNG
   :alt: Krita_Brush_Settings_Dialog.PNG

   Krita\_Brush\_Settings\_Dialog.PNG

Making a Simple Inking Brush
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

So, to demonstrate how to use this system, let's make a simple inking
brush: A nice round brush that uses your tablet's sensors and makes
pretty lines.

#. Press <kbd>f5</kbd> to open the brush settings editor.
#. Choose the <span class=“menuchoice”>Pixel Brush</span> engine. This
   is the most general of the brush engines.
#. Press the <span class=“menuchoice”>Default</span> button below.
   This'll reset the brush to the default for this brush engine.
#. Draw on the scratchpad to see what the current brush looks like. If
   done correctly you should have a 5px wide brush that has pressure set
   to opacity.
#. Let us turn off the opacity first. Click on the
   `opacity <special:myLanguage/Krita/Manual/BrushEngines/OpacitynFlow>`__
   option in the right-hand list. The settings should now be changed to
   a big curve. This is the sensor curve.
#. Untick the <span class=“menuchoice”>enable pen settings
   button</span>.
#. Test on the scratch pad... there still seems to be something
   affecting opacity. This is due the
   `flow <special:myLanguage/Krita/Manual/BrushEngines/OpacitynFlow>`__
   option.
#. Select the <span class=“menuchoice”>Flow</span> option from the list
   on the right hand. Flow is like Opacity, except that Flow is per dab,
   and opacity is per stroke.
#. Turn off the <span class=“menuchoice”>enable pen settings
   button</span> here as well. Test again.
#. Now you should be getting somewhere towards an inking brush. It is
   still too small however, and kinda grainy looking. Click `Brush
   Tip <special:myLanguage/Krita/Manual/BrushEngines/BrushTip>`__ in the
   brush engine options.
#. Here, diameter is the size of the brush-tip. You can touch the slider
   change the size, or right-click it and type in a value. Set it to 25
   and test again. It should be much better.
#. Now to make the brush feel a bit softer, turn down the <span
   class=“menuchoice”>fade</span> parameter to about 0.9. This'll give
   the *brush mask* a softer edge.
#. If you test again, you'll notice the fade doesn't seem to have much
   effect. This has to do with the spacing of the dabs: The closer they
   are together, the harder the line is. By default this is 0.1, which
   is a bit low. If you set it to 10 and test, you'll see what kind of
   effect spacing has. The
   `Auto <special:myLanguage/Krita/Manual/BrushEngines/MiscParameters#Spacing>`__
   tickbox changes the way the spacing is calculated, and Auto Spacing
   with a value of 0.8 is the best value for inking brushes. Don't
   forget that you can use right-click to type in a value.
#. Now, when you test, the fade seems to have a normal effect... except
   on the really small sizes, which look pixelly. To get rid of that,
   tick the <span class=“menuchoice”>anti-aliasing</span> checkbox. If
   you test again, the lines should be much nicer now.
#. Now, for saving. Doodle something into the square in the scratchpad.
   Then, type in a name into the text input above the settings, and
   press <span class=“menuchoice”>Save to presets</span> (If your name
   has already been picked, this text will say <span
   class=“menuchoice”>Overwrite Preset</span> instead).
#. If you check the preset docker, you brush should now be a part of it!

So that's how you create a basic inking brush. There's more options you
can make use of, like for example:

Changing the amount of pressure you need to put on a brush to make it
full size.
    To do this, select the
    `size <special:myLanguage/Krita/Manual/BrushEngines/MiscParameters#Size>`__
    option, and press the <span class=“menuchoice”>pressure</span>sensor
    from the list next to the curve. The curve should look like a
    straight line. Now if you want a brush that gets big with little
    pressure, tick on the curve to make a point, and drag the point to
    the upper-left. The more the point is to the upper-left, the more
    extreme the effect.
    If you want instead a brush that you have to press really hard on to
    get to full size, drag the dot to the lower-right. Such a brush is
    useful for fine details.
    Don't forget to save the changes to your brush when done.
Making the fine lines look even softer by using the flow option.
    To do this, select the <span class=“menuchoice”>flow</span> option,
    and turn back on the <span class=“menuchoice”>enable pen
    settings</span> check box. Now if you test this, it is indeed a bit
    softer, but maybe a bit too much. Click on the curve to make a dot,
    and drag that dot to the top-left, half-way the horizontal of the
    first square of the grid. Now, if you test, the thin lines are much
    softer, but the hard your press, the harder the brush becomes.

Loading / Sharing / Downloading Presets through the User Interface
------------------------------------------------------------------

Brush presets can be loaded, shared online or downloaded from the
internet using the `Preset Docker <Special:MyLanguage/Brush_Presets>`__
(<span class=“menuchoice”>Settings &rarr; Dockers &rarr; Brush Preset
Docker</span>) or by the Preset drop-down.

Preset Drop-down:

.. figure:: 800px-Krita_Brush_Mode_Dialog.PNG
   :alt: 800px-Krita_Brush_Mode_Dialog.PNG

   800px-Krita\_Brush\_Mode\_Dialog.PNG

The preset drop-down is where you can delete brushes, and is a quick and
easy way to get to brushes. You can use <kbd>F6</kbd> to open it
quickly!

The icons at the bottom (from left to right) do the following:

-  Open a new preset saved on your computer
-  Delete a preset
-  See presets shared by other users online and install the one(s) you
   like
-  Share your preset with other users online

Preset Docker (<span class=“menuchoice”>Settings &rarr; Dockers &rarr;
Preset Docker</span>):

.. figure:: 300px-Krita_Brush_Preset_Docker.png
   :alt: 300px-Krita_Brush_Preset_Docker.png

   300px-Krita\_Brush\_Preset\_Docker.png

Loading preset packs manually
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Occasionally you'll come across a user sharing a whole pack of presets /
brushes online, usually in the form of a <tt>zip</tt> / <tt>tar.gz</tt>
file. These can be installed all at once by doing the following:

-  Unzip the file
-  Copy any presets (<tt>.kpp</tt> files) to (you can find this folder
   via <span class=“menuchoice”>settings &rarr; manage resources &rarr;
   open resource folder</span>)
-  Copy any brushes (usually .gbr/.gih/.png/.gih/.jpg/ files) to (also
   found via opening the resource folder)
-  Restart **Krita**

From version 2.9 Krita has a new format for handling resources, it is
called **Bundle**. It is just a compressed zip folder containing all the
resources together, you can load and save new Bundles from Krita's
inbuilt resource manager. You can check the Resource management page for
more information.

Example: Loading a Photoshop Brush (\*.ABR)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

For some time Photoshop has been using the ABR format to compile brushes
into a single file. Krita can read and load .ABR files, although there
are certain features. For this example we will use an example of an .ABR
file that contains numerous images of types of trees and ferns. We have
two objectives. The first is to create a series of brushes that we an
quickly access from the Brush Presets dock to easily put together a
believable forest. The second is to create a single brush that we can
change on the fly to use for a variety of flora, without the need to
have a dedicated Brush Preset for each type.

#. First up is download the file (.ZIP, .RAR,...) that contains the .ABR
   file and any licensing or other notes. Be sure to read the license if
   there is one!
#. Extract the .ABR file into Krita's home directory for brushes.
#. In your Brush Presets dock, select one of your brushes that uses the
   Pixel Brush Engine. An Ink Pen or solid fill type should do fine.
#. Open the Brush Settings Editor (<kbd>F5</kbd>)
#. Click on the tab “Predefined” next to “Auto”. This will change the
   editor to show a scrollable screen of thumbnail images, most will be
   black on a white background. At the bottom of the window are two
   icons:

.. figure:: 600px-BSE_-_Predefined_Window.PNG
   :alt: 600px-BSE_-_Predefined_Window.PNG

   600px-BSE\_-\_Predefined\_Window.PNG

#. Click on the blue file folder on the left and then navigate to where
   you saved your .ABR file and open it.
#. If everything went fine you will see a number of new thumbnails show
   up at the bottom of the window. In our case, they would all be
   thumbnails representing different types of trees. Your job now is to
   decide which of these you want to have as Brush Presets (Just like
   your Pencil) or you think you'll only use sporadically.
#. Let's say that there is an image of an evergreen tree that we're
   pretty sure is going to be a regular feature in some of our paintings
   and we want to have a dedicated brush for it. To do this we would do
   the following:
#. Click on the image of the tree we want
#. Change the name of the brush at the very top of the Brush Editor
   Settings dialog. Something like “Trees - Tall Evergreen” would be
   appropriate.
#. Click the “Save to Presets” button
#. Now that you have a “Tall Evergreen” brush safely saved you can
   experiment with the settings to see if there is anything you would
   like to change, for instance, by altering the size setting and the
   pressure parameter you could set the brush to change the tree size
   depending on the pressure you were using with your stylus (assuming
   you have a stylus!).
#. Once you're satisfied with your brush and it's settings you need to
   do one last thing (but click Overwrite Preset first!)

It's time now to create the Brush Preview graphic. The simplest and
easiest way to do this for a brush of this type is to clear out the
ScratchPad using the “Reset” button. Now, center your cursor in the
Brush Preview square at the top of the ScratchPad and click once. You
should see an image of your texture (in this case it would be the
evergreen tree. In order to work correctly though the entire image
should fit comfortably within the square. This might mean that you have
to tweak the size of the brush. Once you have something you are happy
with then click the **Overwrite Preset** button and your brush and it's
preview image will be saved.

An alternative method that requires a little more work but gives you
greater control of the outcome is the following:

Locate the Brush Preview thumbnail .KPP file in Krita and open it to get
a 200x200 file that you can edit to your wishes.

.. raw:: mediawiki

   {{ResourcePath|paintoppresets}}

You're ready to add the next texture! From here on it's just a matter of
wash, rinse and repeat for each texture where you want to create a
dedicated Brush Preset.

Resource Bundles
~~~~~~~~~~~~~~~~

Resource bundles are also zip-files, but they contain a lot of
extra-information, like creator, date, version of Krita, and they can be
used by Krita to mass-install resources and also to mass-uninstall.

You can make a resource bundle by going to <span
class=“menuchoice”>settings->manage resources</span> and selecting <span
class=“menuchoice”>Create Bundle</span>, A new window will pop-up. To
the left, you can fill in the meta-data, the icon, and where the bundle
ought to be saved to. The bundle name will be used to tag it, and the
rest will be used in the description. Select a resource type in the
drop-down to the top-right, and then select the resources you want to
use in the list. Press the button pointing to the right to put them in
the *selected* list. You can select multiple items at once using
<kbd>shift</kbd> or <kbd>ctrl</kbd>, and then use the right button to
add them to the selected list all at once. You can have multiple
resource-types in a single bundle, just select a new resource type, and
move the resources to the selected list.

When you are done, press OK, and the bundle will be generated at the
place where you told it to. That bundle can be shared.

To install a bundle, go to <span class=“menuchoice”>settings->manage
resources</span> and select <span class=“menuchoice”>import
resource</span> and set the file-browser filter to 'resource bundle'.
Navigate to where the bundle is, and click <span
class=“menuchoice”>open</span>. The bundle is now installed, and it's
contents have been tagged with the bundle name.

You can deactivate a bundle by selecting it from the 'active' list, and
pressing the 'right arrow' to the 'inactive' list. Reinstalling bundles
can be done in a similar manner, by selecting them from the *inactive*
list and pressing the 'left arrow' to move it to the *active* list.

Activating and deactivating bundles can help manage Krita's start-up
time.

Removing Presets
~~~~~~~~~~~~~~~~

Deleting a brush preset in Krita blacklists it for future recovering, to
delete it permanently you have to remove the file with a separate file
manager see
`Resources <Special:MyLanguage/Category:Resource_Management>`__.

Creating a Multi-use Texture Brush
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you are familiar with GIMP or Photoshop then you are familiar with
the idea of changing the brush texture on-the-fly rather than having a
dedicated brush for each texture. This is just a way of emulating this
capability and giving the artist access to more options more quickly for
certain types of work.

#. Create a texture brush following the steps above.
#. Suppose now that you want to paint with multiple textures changing
   them frequently, similar to our example of building up a forest made
   up of different types of trees. All you need to do is open the Brush
   Settings Editor or press <kbd>F5</kbd> each time you want to apply a
   different texture to your brush. Select any texture from the options
   in the predefined tab and come back to the canvas to start painting.

When you are ready to swap out for another texture, follow step 2 again.
In this way you can use a single texture brush to just swap textures in
and out without having to dedicate a Brush Preset to every texture.

`Category:User
Manual{{#translation:}} <Category:User_Manual{{#translation:}}>`__
