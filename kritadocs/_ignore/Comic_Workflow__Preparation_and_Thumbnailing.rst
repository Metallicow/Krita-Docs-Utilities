.. raw:: mediawiki

   {{Warning|Under construction}}

So, this is a bit of an odd page in this manual, as Krita isn’t a
writing program: It’s a drawing program. But comics start with a story
of sorts, and often it can be quite a task to figure out how to
structure a comic project. This page is here to give some ideas, as well
as ideas of how to bring it into Krita.

Folders:
--------

First things first. If you start a project like a comic, and it’ll take
more than two pages, chances are it’s actually quite a big project.

And big projects using the computer are started by making a folder.
Comics are peculiar in that even if you make everything digitally, you
will still make a lot of real-life doodles and notes. So buy a real-life
folder, or christen an old shoebox to become your project box.

Digitally, some file-browsers allow you to tag your files, and this can
be a good habit. It’ll allow you to find your files more easily when
storing the files on a backup drive, where it can be quite likely your
forgot how the backup drive’s folders were structured.

Many file browsers allow you to set the folder as a bookmarked folder
too, for easy access during saving.

<!--Add stuff about the reference docker here, maybe?-->

Further Organisation
--------------------

You’ll probably want to investigate how to order your text-documents.
That is, your character biographies, your worldbuilding notes.

There’s the old-fashioned note book, a moleskin, or one of those
notebooks where you can rip out the paper and add them to a folder.

Another solution is to use a wiki. The traditional full-featured
solution is mediawiki, but you can also use smaller solutions, like
evernote, or my personal favorite, Tiddlywiki.

If you have your files and documents organised, you can use the folder
bookmark to quickly save and load files into Krita. Right now, for
palettes, Krita only really supports GPL files.

Setting up a comic template
---------------------------

Templates are a feature in Krita that allows you to make any given
document into a raw template for multiple usages. For comics, you
obviously want to make your own comic template.

Comic templates are usually set up with four guides for the margins.

However, sometimes, you have a special effect, where the panel is open
and goes into the margins itself, beyond the page even. While for
digital comic creation, you can just export the page as a png and upload
it, for print it’s often difficult to tell where a page ends, because of
alignment and human error. Therefore, a good comic template has a little
bit of bleed as well.

This doesn’t have to be much, 2/3 mm is enough, but official comic
template guide-lines may make it much bigger, because the bleed is also
a convenient place to add notes!

So, let us make a template with both margins and a bleed. We will be
editing the kra-meta data to do this right.

.. figure:: Krita_comic_workflow_template_01.png
   :alt: Krita_comic_workflow_template_01.png

   Krita\_comic\_workflow\_template\_01.png

First, make a page of the size you want the final page to be in inches
or centimeters, and set it to 72 dpi. For my example, I’ll be taking a
A4 image.

Then, use <kbd>Shift</kbd>+<kbd>S</kbd> to set , and drag out the guides
from the Rulers, and snap them to the canvas borders.

Now, go to and set the unit to mm. Then, select the width number and
type +4 at the end. Do the same for height This’ll add 4 mm to the total
canvas size. That’s right, you can do maths in the input boxes! Anyway,
this’ll give us a bleed of 2 mm, horizontally and vertically.

.. figure:: Krita_comic_workflow_template_02.png
   :alt: Krita_comic_workflow_template_02.png

   Krita\_comic\_workflow\_template\_02.png

Now, if you hit ok, you will notice that the guides haven’t moved. This
is a bug. But that doesn’t matter, save the file as something
recognisable, like comic\_template and save it as a kra file.

We’re now going to hack the kra file and adjust it manually.

.. figure:: Krita_comic_workflow_template_03.png
   :alt: Krita_comic_workflow_template_03.png

   Krita\_comic\_workflow\_template\_03.png

Go to the folder you have your kra file. Copy it and rename the copy to
.zip.

.. figure:: Krita_comic_workflow_template_04.png
   :alt: Krita_comic_workflow_template_04.png

   Krita\_comic\_workflow\_template\_04.png

Open it with a unzipper (like the windows standard one) and open the
file ‘maindoc.xml’ with notepad or another simple text-editor. You will
see something like the following:

| ``<?xml version=``\ “``1.0``”\ `` encoding=``\ “``UTF-8``”\ ``?>``
| ``<!DOCTYPE DOC PUBLIC '-//KDE//DTD krita 2.0//EN' '``\ ```http://www.calligra.org/DTD/krita-2.0.dtd`` <http://www.calligra.org/DTD/krita-2.0.dtd>`__\ ``'>``
| ``<DOC xmlns=``\ “```http://www.calligra.org/DTD/krita`` <http://www.calligra.org/DTD/krita>`__”\ `` syntaxVersion=``\ “``2``”\ `` editor=``\ “``Krita``”\ ``>``
| `` <IMAGE width=``\ “``606``”\ `` x-res=``\ “``72``”\ `` name=``\ “``comic_template``”\ `` y-res=``\ “``72``”\ `` proofing-model=``\ “``CMYKA``”
| ``proofing-profile-name=``\ “``Coated_Fogra39L_VIGC_260.icc``”\ `` height=``\ “``853``”\ `` proofing-adaptation-state=``\ “``1``”
| ``profile=``\ “``sRGB-elle-V2-srgbtrc.icc``”\ `` proofing-intent=``\ “``3``”\ `` proofing-depth=``\ “``U8``”
| ``mime=``\ “``application/x-kra``”\ `` colorspacename=``\ “``RGBA``”\ `` description="">``
| `` <layers>``
| ``  <layer selected=``\ “``true``”\ `` name=``\ “``Layer``\ `` ``\ ``1``”\ `` collapsed=``\ “``0``”\ `` visible=``\ “``1``”\ `` filename=``\ “``layer2``”
| ``compositeop=``\ “``normal``”\ `` uuid=``\ “``{49e69678-14bd-45d2-8269-e242c381499f}``”\ `` opacity=``\ “``255``”\ `` x=``\ “``6``”
| ``colorlabel=``\ “``0``”\ `` nodetype=``\ “``paintlayer``”\ `` channellockflags=``\ “``"``\ `` ``\ ``channelflags=``”\ ``" y=``\ “``6``”
| ``locked=``\ “``0``”\ `` colorspacename=``\ “``RGBA``”\ ``/>``
| `` </layers>``
| `` <ProjectionBackgroundColor ColorData=``\ “``o7/R/w==``”\ ``/>``
| `` <ProofingWarningColor>``
| ``  <RGB r=``\ “``0``”\ `` space=``\ “``sRGB-elle-V2-srgbtrc.icc``”\ `` g=``\ “``0``”\ `` b=``\ “``0``”\ ``/>``
| `` </ProofingWarningColor>``
| `` <guides>``
| ``  <showGuides value=``\ “``1``”\ `` type=``\ “``value``”\ ``/>``
| ``  <snapToGuides value=``\ “``0``”\ `` type=``\ “``value``”\ ``/>``
| ``  <lockGuides value=``\ “``1``”\ `` type=``\ “``value``”\ ``/>``
| ``  <horizontalGuides type=``\ “``array``”\ ``>``
| ``   <item_0 value=``\ “``0``”\ `` type=``\ “``value``”\ ``/>``
| ``   <item_1 value=``\ “``842``”\ `` type=``\ “``value``”\ ``/>``
| ``  </horizontalGuides>``
| ``  <verticalGuides type=``\ “``array``”\ ``>``
| ``   <item_0 value=``\ “``0``”\ `` type=``\ “``value``”\ ``/>``
| ``   <item_1 value=``\ “``595``”\ `` type=``\ “``value``”\ ``/>``
| ``  </verticalGuides>``
| `` </guides>``
| `` <animation>``
| ``  <framerate value=``\ “``24``”\ `` type=``\ “``value``”\ ``/>``
| ``  <range from=``\ “``0``”\ `` type=``\ “``timerange``”\ `` to=``\ “``100``”\ ``/>``
| ``  <currentTime value=``\ “``0``”\ `` type=``\ “``value``”\ ``/>``
| `` </animation>``
| ``</IMAGE>``
| ``</DOC>``

This is the heart of a kra file. It is XML, which means that the layers
and meta-data is stored like an HTML file. For our interest, we need to
look at the “Guides” section.

So, if you look at the top <image> tag, the full width and heigh of the
image are 606 and 853 pixels.

The horizontal guides are at 0 and 842 pixels, and the vertical guides
are at 0 and 595 pixels.

We want to do two things: first, we want to move the guides so they take
the bleeds into account, and then we want to add a new set of guides for
the inner set.

For the first, we look at how many pixels we added. So... <code>image
total - guide = 853 - 842 = 11</code> And <code>11/2 = 5.5</code>

So we set item\_0 in the horizontal guides from 0 to 5.5. For item\_1 we
set it to (853-5.5=847,5).

We do the same maths for the vertical guides. So, 606-595 = 11, meaning
that item\_0 should be 5.5 and item\_1 should be at 606-5.5=601.5.

| `` <guides>``
| ``  <showGuides value=``\ “``1``”\ `` type=``\ “``value``”\ ``/>``
| ``  <snapToGuides value=``\ “``0``”\ `` type=``\ “``value``”\ ``/>``
| ``  <lockGuides value=``\ “``1``”\ `` type=``\ “``value``”\ ``/>``
| ``  <horizontalGuides type=``\ “``array``”\ ``>``
| ``   <item_0 value=``\ “``5.5``”\ `` type=``\ “``value``”\ ``/>``
| ``   <item_1 value=``\ “``847.5``”\ `` type=``\ “``value``”\ ``/>``
| ``  </horizontalGuides>``
| ``  <verticalGuides type=``\ “``array``”\ ``>``
| ``   <item_0 value=``\ “``5.5``”\ `` type=``\ “``value``”\ ``/>``
| ``   <item_1 value=”601.5" type=``\ “``value``”\ ``/>``
| ``  </verticalGuides>``
| `` </guides>``
| `` ``

Now save.

For the second part, we’re going to add more items.

Let us assume we want a horizontal margin of 1cm and a vertical margin
of 1.5.

We first need to calculate how many pixels that is. So, we have a DPI of
72 pixels. Which means that every inch is 72 pixels. However, my units
are centimeters(because I am a dirty european). We first need to convert
our centimeters to inches:

1 inch is 2.54 cm. So 1 cm is 1/2.54 inch. And then, 1.5 cm is 1.5/2.54.
Then, we multiply those with 72...

| ``1 / 2.54 * 72 = 28.346456693 pixels``
| ``1.5/2.54 * 72 = 42.519685039 pixels``

So, we need new vertical guides at 5.5+28.346456693 = 33.846456693 and
601.5 - 28.346456693 = 573.153543307

For the horizontal, we’ll need new ones at 5.5 + 42.519685039 =
48.019685039 and 847.5 - 42.519685039 = 804.980314961.

Let’s add them:

| `` <guides>``
| ``  <showGuides value=``\ “``1``”\ `` type=``\ “``value``”\ ``/>``
| ``  <snapToGuides value=``\ “``0``”\ `` type=``\ “``value``”\ ``/>``
| ``  <lockGuides value=``\ “``1``”\ `` type=``\ “``value``”\ ``/>``
| ``  <horizontalGuides type=``\ “``array``”\ ``>``
| ``   <item_0 value=``\ “``5.5``”\ `` type=``\ “``value``”\ ``/>``
| ``   <item_1 value=``\ “``847.5``”\ `` type=``\ “``value``”\ ``/>``
| ``   <item_2 value=``\ “``48.019685039``”\ `` type=``\ “``value``”\ ``/>``
| ``   <item_3 value=``\ “``804.980314961``”\ `` type=``\ “``value``”\ ``/>``
| ``  </horizontalGuides>``
| ``  <verticalGuides type=``\ “``array``”\ ``>``
| ``   <item_0 value=``\ “``5.5``”\ `` type=``\ “``value``”\ ``/>``
| ``   <item_1 value=”601.5" type=``\ “``value``”\ ``/>``
| ``   <item_2 value=``\ “``33.846456693``”\ `` type=``\ “``value``”\ ``/>``
| ``   <item_3 value=``\ “``573.153543307``”\ `` type=``\ “``value``”\ ``/>   ``
| ``  </verticalGuides>``
| `` </guides>``

Now, save, close the zip file, and rename it back to a .kra file, and
open that in Krita.

.. figure:: Krita_comic_workflow_template_05.png
   :alt: Krita_comic_workflow_template_05.png

   Krita\_comic\_workflow\_template\_05.png

Now, you should have a perfectly set-up guided template!

Now, before we turn this into a template, there’s some other things you
might want to adjust.

Document Information
    The document information holds the default title of the document.
    You might want to strip it, or add something more descriptive than
    'template'
The layers
    Do you think all your comic pages should have one sketch layer, one
    inking layer, and one vector layer for text? Add them now, and
    they'll be added to the final template.
The softproofing configuration.
    This is a bit of an odd one, but you can set the soft-proofing
    already by going into image->image properties and setting the
    profile there. Some areas have standard profiles that get used
    often, so for example, American printing houses tend to use swop
    while European ones use fogra.
Grids and Assistants
    Some people enjoy setting a 5 mm grid, or setting up orthographic
    assistants. If you do that now, you can have them in all your comics
    quite quickly.

When you are done, go to and name your new template. You can even make a
cute icon for it.

.. figure:: Krita_comic_workflow_template_06.png
   :alt: Krita_comic_workflow_template_06.png

   Krita\_comic\_workflow\_template\_06.png

And now you can find your template in the new document dialog, ready for
action!

300 dpi template
^^^^^^^^^^^^^^^^

Why did I tell you to make a 72 dpi image? Because guides are stored in
72 dpi, meaning that even on a 300 dpi image we’d have these same values
You can in fact just change the dpi and the values in the image tag, and
then you end up with exactly the same image, but at a higher dpi.

So let's try that, make another copy of the kra file with guides and get
to the point you can change the maindoc.xml, now, we only need this bit:

| ``<IMAGE width=``\ “``606``”\ `` x-res=``\ “``72``”\ `` name=``\ “``comic_template``”\ `` y-res=``\ “``72``”\ `` proofing-model=``\ “``CMYKA``”
| ``proofing-profile-name=``\ “``Coated_Fogra39L_VIGC_260.icc``”\ `` height=``\ “``853``”\ `` proofing-adaptation-state=``\ “``1``”
| ``profile=``\ “``sRGB-elle-V2-srgbtrc.icc``”\ `` proofing-intent=``\ “``3``”\ `` proofing-depth=``\ “``U8``”
| ``mime=``\ “``application/x-kra``”\ `` colorspacename=``\ “``RGBA``”\ `` description="">``

change x-res and y-res to 300. And width and height need to be first
divided by 72, and then multiplied by 300:

| ``606 / 72 * 300 = 2525``
| ``853 / 72 * 300 = 3554~``

And then fill it into the image part:

| ``<?xml version=``\ “``1.0``”\ `` encoding=``\ “``UTF-8``”\ ``?>``
| ``<!DOCTYPE DOC PUBLIC '-//KDE//DTD krita 2.0//EN' '``\ ```http://www.calligra.org/DTD/krita-2.0.dtd`` <http://www.calligra.org/DTD/krita-2.0.dtd>`__\ ``'>``
| ``<DOC xmlns=``\ “```http://www.calligra.org/DTD/krita`` <http://www.calligra.org/DTD/krita>`__”\ `` syntaxVersion=``\ “``2``”\ `` editor=``\ “``Krita``”\ ``>``
| `` <IMAGE width=``\ “``2525``”\ `` x-res=``\ “``300``”\ `` name=``\ “``comic_template``”\ `` y-res=``\ “``300``”\ `` proofing-model=``\ “``CMYKA``”\ `` ``
| ``proofing-profile-name=``\ “``Coated_Fogra39L_VIGC_260.icc``”\ `` height=``\ “``3554``”\ `` proofing-adaptation-state=``\ “``1``”\ `` ``
| ``profile=``\ “``sRGB-elle-V2-srgbtrc.icc``”\ `` proofing-intent=``\ “``3``”\ `` proofing-depth=``\ “``U8``”\ `` mime=``\ “``application/x-kra``”\ `` ``
| ``colorspacename=``\ “``RGBA``”\ `` description="">``
| ``  <layers>``
| ``   <layer selected=``\ “``true``”\ `` name=``\ “``Layer``\ `` ``\ ``1``”\ `` collapsed=``\ “``0``”\ `` visible=``\ “``1``”\ `` filename=``\ “``layer2``”\ `` compositeop=``\ “``normal``”\ `` ``
| ``uuid=``\ “``{49e69678-14bd-45d2-8269-e242c381499f}``”\ `` opacity=``\ “``255``”\ `` x=``\ “``6``”\ `` ``
| ``colorlabel=``\ “``0``”\ `` nodetype=``\ “``paintlayer``”\ `` channellockflags=""``
| ``channelflags=``\ “``"``\ `` ``\ ``y=``”\ ``6" locked=``\ “``0``”\ `` colorspacename=``\ “``RGBA``”\ ``/>``
| ``  </layers>``
| ``  <ProjectionBackgroundColor ColorData=``\ “``o7/R/w==``”\ ``/>``
| ``  <ProofingWarningColor>``
| ``   <RGB r=``\ “``0``”\ `` space=``\ “``sRGB-elle-V2-srgbtrc.icc``”\ `` g=``\ “``0``”\ `` b=``\ “``0``”\ ``/>``
| ``  </ProofingWarningColor>``
| ``<guides>``
| ``  <showGuides value=``\ “``1``”\ `` type=``\ “``value``”\ ``/>``
| ``  <snapToGuides value=``\ “``0``”\ `` type=``\ “``value``”\ ``/>``
| ``  <lockGuides value=``\ “``1``”\ `` type=``\ “``value``”\ ``/>``
| ``  <horizontalGuides type=``\ “``array``”\ ``>``
| ``   <item_0 value=``\ “``5.5``”\ `` type=``\ “``value``”\ ``/>``
| ``   <item_1 value=``\ “``847.5``”\ `` type=``\ “``value``”\ ``/>``
| ``   <item_2 value=``\ “``48.019685039``”\ `` type=``\ “``value``”\ ``/>``
| ``   <item_3 value=``\ “``804.980314961``”\ `` type=``\ “``value``”\ ``/>``
| ``  </horizontalGuides>``
| ``  <verticalGuides type=``\ “``array``”\ ``>``
| ``   <item_0 value=``\ “``5.5``”\ `` type=``\ “``value``”\ ``/>``
| ``   <item_1 value=``\ “``601.5``”\ `` type=``\ “``value``”\ ``/>``
| ``   <item_2 value=``\ “``33.846456693``”\ `` type=``\ “``value``”\ ``/>``
| ``   <item_3 value=``\ “``573.153543307``”\ `` type=``\ “``value``”\ ``/>   ``
| ``  </verticalGuides>``
| `` </guides>  <animation>``
| ``  <framerate value=``\ “``24``”\ `` type=``\ “``value``”\ ``/>``
| ``  <range from=``\ “``0``”\ `` type=``\ “``timerange``”\ `` to=``\ “``100``”\ ``/>``
| ``  <currentTime value=``\ “``0``”\ `` type=``\ “``value``”\ ``/>``
| ``  </animation>``
| `` </IMAGE>``
| ``</DOC>``

Now, save this as another template. You will be using both!

Thumbnailing/Storyboarding
~~~~~~~~~~~~~~~~~~~~~~~~~~

Now, there's many ways to do storyboards and thumbnails. The regular
method is to use a real-life notebook, or use a pdf annotator, like
Xournal. From there you can export or scan in your drawings as PDF or
PNG/JPG. You can also just use Krita's animation timeline as a simple
page-system.

.. figure:: Krita_thumbnailing_animation.png
   :alt: Krita_thumbnailing_animation.png

   Krita\_thumbnailing\_animation.png

PDFs
^^^^

You can open PDFs in Krita regularly. You will need to choose how big
the pages are interpreted, and how many:

.. figure:: Krita_pdf_import.png
   :alt: Krita_pdf_import.png

   Krita\_pdf\_import.png

The pages will be opened as layers, which can be a bit cumbersome to
work with. Therefore, put all the layers into a group, and convert the
group-layer to animation via

.. figure:: Krita_pdf_import_2.png
   :alt: Krita_pdf_import_2.png

   Krita\_pdf\_import\_2.png

.. raw:: mediawiki

   {{Note|You will need to inverse the layer order first to get them to align correctly to the time}}

This will convert the layers to an animation. While still not ideal to
work with, it'll allow you to start sketching and cleaning up, and
generally preparing the pages.

When done, you can select the frames and export the animation via ,
where they'll be neatly numbered upon export.

To get the files into the comic template we just created, you open the
template, and then import the page in question, ready for sketching!

.. raw:: mediawiki

   {{Info|Moritz Molch made a very lovely comic-page creator for Krita. It is a separate application, and can be found here: https://moritzmolch.com/2165 }}

<!-- TODO: If the multi-page workflow stuff ever gets out, rewrite to
make it use that.-->

`0 <Category:_Comic_Workflow>`__
