\_\_NEWSECTIONLINK\_\_ <languages/>

This page contains common problems people have with Krita

General
-------

General questions

Krita start with a black canvas and nothing changes when you try to draw/shows a black screen on my Windows system with an Intel GPU
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This is a bug in the Intel OpenGL driver. Update to 10.18.14 or later.
On Windows 8.0 and 8.1, you might need to manually install the driver.
Follow the instructions from the `Intel
Website <http://www.intel.com/support/graphics/sb/cs-022355.htm>`__. No,
we don’t know either why they made installing an updated driver so hard.

As an alternative turn off OpenGL under <span
class=“menuchoice”>settings &rarr; configure Krita &rarr; display</span>

Since January 2016 however, we've noticed that the Intel drivers broke
again. We hope to fix this issue in Krita 3.0.

Is it possible to use Krita in my own language, not English?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Unless you belong to a proud tribe of a minority language, YES it is
POSSIBLE! You can easily do this by going into

#. <span class=“menuchoice”>settings &rarr; switch application
   language</span>. An small window will appear.
#. click <span class="menuchoice>Primary language</span> and select your
   language.
#. click <span class="menuchoice>OK</span> to close the window.
#. restart krita and it will be displayed in your selected language!

<div class=“mw-collapsible mw-collapsed”> **<big>The List of Available
Languages in Krita</big>** <div class=“mw-collapsible-content”>

-  Afrikaans
-  Albanian
-  American English
-  Arabic
-  Asturian
-  Basque
-  Belarusian
-  Bosnian
-  Brazilian Portuguese
-  Breton
-  British English
-  Bulgarian
-  Catalan
-  Catalan (Valencian)
-  Chhattisgarhi
-  Chinese Simplified
-  Chinese Traditional
-  Croatian
-  Czech
-  Danish
-  Dutch
-  Esperanto
-  Estonian
-  Farsi (Persian)
-  Finnish
-  French
-  Frisian
-  Galician
-  German
-  Greek
-  Hebrew
-  Hindi
-  Hungarian
-  Icelandic
-  Interligua
-  Irish Garlic
-  Italian
-  Japanese
-  Maithili
-  Kazakh
-  Khmer
-  Korean
-  Lithuanian
-  Latvian
-  Low Saxon
-  Malay
-  Marathi
-  Norwegian Bokmål
-  Nepali
-  Northern Sami
-  Norwegian Nynorsk
-  Occitan
-  Polish
-  Portuguese
-  Romanian
-  Russian
-  Slovak
-  Slovenian
-  Spanish
-  Tajik
-  Tamil
-  Swedish
-  Thai
-  Ukrainian
-  Uyghur
-  Walloon
-  Weish
-  Turkish
-  Vietnamese
-  Xhosa</div>

</div>

Does Krita have layer clip or clipping mask?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Krita has no clipping mask, but it has a clipping feature called
**inherit alpha**. Let's see `**this
page** <Special:MyLanguage/Introduction_to_Layers_and_Masks#Inherit_Alpha_or_Clipping_layers>`__
and learn how to do clipping in Krita!

OBS can't record the Krita openGL canvas
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Apparantly the workaround for this is to either...

#. Turn off OpenGL in <span class=“menuchoice”>settings &rarr; configure
   Krita &rarr; display</span>.
#. Or don't use the hardware accelerated mode(game recording mode) in
   OBS, so capture the whole desktop instead of attempting to capture
   only Krita.

Where are the configuration files stored?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

On Windows, this is %APPDATA%\\krita or %LOCALAPPDATA%\\krita.

On Linux, .kde/share/config/krita or .kde4/share/config/krita (For 3.0
this is .config for the kritarc and .local/share/krita for the
resources)

My resource disappeared with installing 3.0! Did Krita delete them?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Don't worry, Krita nor the installer know how to delete your
brushes(unless you use the 'delete backup files' in the resource
manager)

Your old 2.9 brushes should be at

for Linux:

<code>home/.kde/share/krita</code>

for Windows:

<code>User\\AppData\\Roaming\\krita\\share\\apps\\krita\\</code>

For 3.0, these should go to

Linux: <code>home/.local/share/krita</code>

Windows:

<code>user\\Appdata\\Roaming\\krita</code>

Just copy the files over!

Resetting Krita configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can reset the Krita configuration in two ways: <!--\* Press
<kbd>Shift</kbd>+<kbd>Alt</kbd>+<kbd>Ctrl</kbd> while starting Krita.
This should show a pop-up asking if you want to reset the
configuration.-->

-  For Krita 2.9: Delete/rename the kritarc (not krita.rc) file in
   .kde/config/ on Linux or %APPDATA%\\Roaming\\krita\\ on Windows.
-  For Krita 3.0: Delete/rename the kritarc file in .config/ on Linux or
   %APPDATA%\\Local\\krita\\ on Windows.

If the config was causing a crash, don't delete but instead rename and
send us the file so we can figure out what caused the crash.

Krita tells me it can't find the configuration files and then closes, what should I do?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

First, search your filesystem for kritarc. If it's nowhere to be found,
then that is the main problem.

Causes for this could be the following:

-  It might be that your download got corrupted and is missing
   files(common with bad wifi and bad internet connection in general),
   in that case, try to find a better internet connection before trying
   to download again. Krita should be around 80 to 100 mb big when
   downloading.
-  It might be something went wrong during installation. Check if your
   harddrive isn't full. If not, and the problem still occurs, there
   might be something odd going on with your device and it's recommended
   to find an computer expert to diagnose what is going on.
-  Some unzippers don't unpack our zipfiles correctly. The native ones
   on windows, OSX and most linux distributions should be just fine, and
   we recommend using them.

What Graphics Cards does Krita support?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Krita can use OpenGL to accelerate painting and canvas zooming, rotation
and panning. Nvidia and recent Intel GPUs give the best results. Make
sure your OpenGL drivers support OpenGL 3.2 as the minimum. AMD/ATI
GPU’s are known to be troublesome, especially with the proprietary
drivers on Linux. However, it works perfectly with the radeon free
driver on linux for supported AMD GPU.

I can't edit text from PSD files created by photoshop
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

There is no text support for psd file yet. The text will appear
rasterized and converted into paint layer.

How much memory does my image take?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

For simple images, that’s pretty simple: you mulitply width \* height \*
channels \* size of the channels (so, for a 1000×1000 16 bit integer
rgba image: 1000 x 1000 x 4 x 2). You multiply this by the number of
layers plus two (one for the image, one for the display). If you add
masks, filter layers or clone layers, it gets more complicated.

Why do I get a checkerboard pattern when I use the eraser?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You’re probably used to Gimp or Photoshop. The background, that is
default or first layer in these applications doesn’t have an alpha
channel by default. so, on their background layer, the eraser paints in
the background color.

In Krita, all layers have an alpha channel, so if you want to paint in
the background color, you should do that, instead of erasing. You get
the same effect in, say, gimp, if you create new image, add an alpha
channel and then use the eraser tool. Most Krita users actually on
starting a sketch in Krita add a new blank layer first thing they do
(the INSert key is a useful shortcut here.) That doesn’t use extra
memory, since a blank layer or a layer with a default color just takes
one pixel worth of memory.

Can I use Krita with sandboxie on Windows?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

No, this is not recommended. Sandboxie causes stuttering and freezes due
to the way it intercepts calls for resources on disk.

Can krita work with 8 bit (indexed) images?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

No. Krita has been designed from the ground up to use real colors, not
indexed palettes. There are no plans to support indexed color images,
though Krita can export to some indexed color image formats, such as
GIF. However, Krita does not offer detailed control over pixel values.

How do I export gifs with Krita?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Currently, Krita 3.0 doesn't have gif, apng or spritesheet export yet.
This is because gif export in particular needs dedicated time for us to
figure out the indexed-colors that gif requires. Krita 3.1 will have gif
export. Until then we recommend exporting your animation as a png
sequence, and then inputtng that into a frames-to-gif creator, or using
the frames in ImageMagick or Gimp to turn it into a gif.

How can I produce a backtrace on Windows?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you experience a crash on Windows, and can reproduce the crash, the
bug report will be much more valuable if you can create a backtrace. A
backtrace is somewhat akin to an airplane's blackbox, in that they tell
what set of instructions your computer was running when it was
crashing(where the crash happened), making it very useful to figure out
why the crash happened. First you need to install DrMingw, which is a
debugger application:

https://github.com/jrfonseca/drmingw

Then you need a special version of Krita, one with debugging
information. The latest development builds with all the latest bug fixes
are here:

-  http://files.kde.org/krita/3/windows/debugbuilds/krita3-x64-dbg-latest.zip
-  http://files.kde.org/krita/3/windows/debugbuilds/krita3-x86-dbg-latest.zip

You can download the right file, unzip it and double-click on the krita
link in the unzipped folder. If you now reproduce the crash, Windows
will ask you whether you want to debug it; answer yes, and DrMingw will
pop up and after some time show you a lot of text. You can paste that
into your bug report.

Tablets
-------

What tablets does Krita support?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Krita isn’t much fun without a pressure sensitive tablet. If the tablet
has been properly configured, Krita works with Wacom, Huion and other
uc-logic based tablets, on Windows and Linux (look below for more
information on Huion Linux support). Genius tablets are know to have
problems.

If you're looking for information about tablets like the iPad or Android
tablets, look
`here <Special:MyLanguage/KritaFAQ#Can_I_get_Krita_for_iPad.3F_for_Android.3F>`__.

What if your tablet is not recognized by Krita?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Linux
^^^^^

We would like to see the full output of the following commands:

#. lsmod
#. xinput
#. xinput list-props <id-of-your-tablet> (id can be fetched from the
   item 2)
#. Get the log of the tablet events (if applicable):

   #. Open a console application (e.g. Konsole on KDE)
   #. Set the amount of scrollback to 'unlimited' (for Konsole: <span
      class=“menuchoice”>Settings &rarr; Edit Current Profile &rarr;
      Scrolling &rarr; Unlimited Scrollback</span>)
   #. Start Krita by typing 'krita' and create any document :)
   #. Press <kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>T</kbd>, you will see
      a message box telling the logging is started
   #. Try to reproduce your problem
   #. The console is now filled with the log. Attach it to a bug report
      or paste using services like paste.kde.org

#. Attach all this data to a bugreport using public paste services like
   paste.kde.org

Windows
^^^^^^^

If you have any kind of problems with Windows and your tablet, we cannot
help you without a tablet log.

#. Install
   `DebugView <http://technet.microsoft.com/en-us/sysinternals/bb896647.aspx>`__
   from the official Microsoft site
#. Start DebugView
#. Start Krita
#. Press <kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>T</kbd>, you will see a
   message box telling the logging is started
#. Try to reproduce your problem
#. Go back to DebugView and save its output to a file. Attach this file
   to a bug report or paste using services like paste.kde.org.

How to fix a tablet offset on multiple screen setup on Windows
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you see that your tablet pointer has an offset when working with
Krita canvas, it might be highly probable, that Krita got incorrect
screen resolution from the system. That problem happens mostly when an
external monitor is present and when either of monitor or a tablet was
connected after the system boot.

Now there is a simple solution to fix this data manually.

#. Lay you stylus aside
#. Start Krita without using a stylus, that is using a mouse or a
   keyboard
#. Press Shift key and hold it
#. Touch a tablet with your stylus so Krita would recognize it

You will see a special dialog asking for real screen resolution. Choose
the correct value or enter it manually and press OK.

If you have a dual monitor setup and only the top half of the screen is
reachable, you might have to enter the total width of both screens plus
the double height of your monitor in this field.

Microsoft Surface Pro and NTrig
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Make sure to do all of the updates that Microsoft wants when you start
using it. Go to the Start Menu and type “Check for Updates”. This will
fix a lot of issues with how Krita looks when you use it.

Krita uses Wintab drivers to fix things like pressure sensitivity.
Download the latest WinTab drivers from the Microsoft site. Do an
internet search for “surface pro Wintab drivers”. The other files that
are really large are part of Windows updates, so you shouldn't have to
worry about those.

Take care to download the 32 bits version of the drivers, even if you
use the 64 bits version of Krita and a 64 bits version of Windows. The
64 bits drivers do not work.

In a moment of inanity, Microsoft decided not to package the MSVC 2010
runtime with the drivers. If you haven't got those runtimes on your
Surface, the drivers still don't work. You can download the runtime
separate:

https://www.microsoft.com/en-us/download/details.aspx?id=5555

Note that for the 32 bits driver, you need to install the the x86
runtime.

If you still don't have pressure sensitivity after installing the 32
bits drivers, you can try to install and uninstall the Photoshop CC
trial, apparently Adobe replaces some Windows system libraries with
versions that unbreak the wintab drivers.

How to make my Huion tablet work with Krita on Linux?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This applies to Huion models: H610 (maybe others too? report your model
here..)

First, if you use a linux kernel version 3.13 or above, remove the buggy
huion driver with this command line:

<code>rmmod hid-huion</code>

or, depending on your distribution:

<code>modprobe -r hid-huion</code>

Then build and install the `correct kernel
driver <https://github.com/DIGImend/huion-driver>`__.

(note that you’ll have to redo those steps after each kernel update,
until this driver is included in mainline kernel.)

Now you should have a working tablet in Krita and Gimp (sadly, it
doesn’t work with current mypaint version, probably because of GTK3..)
But as by default the whole tablet area is mapped to the whole screen,
depending on your screen ratio you may want to adapt the active area of
the tablet to have the same proportions.

For this, first you need to install xinput-calibrator (check in your
package manager it may be named a bit differently, with – or \_ in the
middle…)

Now, you’ll need the name or ID of your device, so list devices with
this command line:

<code>xinput\_calibrator --list \| grep H610</code>

Then I noticed the huion report two different devices with the same
name, just different ID. So to find out which is the one corresponding
to the actual stylus tablet area, get devices values with this command
line:

<code>xinput\_calibrator --device 10</code>

(adapt id number the the values you found on previous step…)

It will open a sort of calibration window, don’t click the crosses, just
press any key to abort. Then you can see the default values of the
device appeared in the console. One devices has much bigger max values
(0 40000 0 25000), this is the one you should get the ID number. (in my
case here was ID 10 )

Then calculate the values to set the active area to the same ratio as
screen.. For example, for a 1920×1080 screen, I did this operation:
40000\*1080/1920=22500

And finally set the calibration values (TopX BottomX TopY BottomY) like
this:

<code>xinput set-prop 10 “Evdev Axis Calibration” 0 40000 0 22500</code>

Toolbox
-------

Toolbox missing
~~~~~~~~~~~~~~~

You either reset the workspace by pressing the right most button on the
toolbar, the workspace switcher, and clicking a workspace from the list.

Or you try to select the toolbox from the docker dialogue. (2.9.7 and
onward only)

Tool icons size is too big
~~~~~~~~~~~~~~~~~~~~~~~~~~

Right click the toolbox to set the size.

Krita can't get maximized
~~~~~~~~~~~~~~~~~~~~~~~~~

This is due to the toolbox being too big, for example, when it's
accidentally made 1-columns wide. Resize it to make it 2 columns wide.

Resources
---------

Is there a way to restore a default brush that I have mistakenly overwritten with new settings to default?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Yes. First go to the resource folder, which is

-  Linux: .local/share/krita
-  Windows: %APPDATA%\\Roaming\\krita
-  OSX: ~/Library/Application Support/Krita

You can easily do this by going into <span class=“menuchoice”>settings
&rarr; manage resources &rarr; open resource folder</span>.

Then go into the paintoppressets folder and remove the latest created
file that you made of your preset.

Then go back to the resources folder and edit the blacklist file to
remove the previous paintop preset so Krita will load it. (Yes, it is a
bit of a convoluted system, but at the least you don't lose your
brushes)

How do I set favourite presets?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Right-click a brush in the brush docker and assign it a tag. Then when
clicking the lower-right settings icon you can pick you tag.

Can Krita load Photoshop Brushes?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Yes, but there are limitations. You can load ABR files by using the Add
Brush button in the predefined brush tab in the brush editor. Since
Adobe hasn’t disclosed the file format specification, we depend on
reverse-engineering to figure out what to load, and currently that’s
limited to basic features.

Krita is slow
-------------

There is a myriad of reasons why this might be:

Slow start-up
~~~~~~~~~~~~~

You probably have too many resources installed. Deactivate some bundles
under <span class=“menuchoice”>settings &rarr; manage resources</span>

Slow Brushes
~~~~~~~~~~~~

-  Check if you accidentally turned on the stabilizer in the tool
   options docker.
-  Try an other display filter like trilinear. <span
   class=“menuchoice”>settings &rarr; configure Krita &rarr;
   display</span>
-  Try a lower color space value then 16-bit.
-  For NVidia, try a 16-bit floating point color space.
-  For AMD (Krita 2.9.10 and above), turn off the vector optimizations
   that are broken on AMD CPUs. <span class=“menuchoice”>settings &rarr;
   configure Krita &rarr; performance</span>
-  It's a fairly memory hungry program, so 2GB of ram is the minimum,
   and 4 gig is the preferable minimum.

Slowdown after a while of working
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Once you have the slowdown, click on the image-dimensions in the status
bar. It will tell you how much Krita is using, and if it's hit the
limit, whether it's started swapping. Swapping can slow down a program a
lot, so either work on smaller images or turn up the maximum amount of
ram in <span class=“menuchoice”>settings &rarr; configure Krita &rarr;
performance</span>

Tools
-----

Why does the Transform Tool give a good result and then get blurry upon finalizing?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The transform tool makes a preview that you edit before computing the
finalized version. As this preview is using the screen resolution rather
than the image resolution, it may feel that the result is blurry
compared to the preview. See
https://forum.kde.org/viewtopic.php?f=139&t=127269 for more info.

License, rights and the Krita foundation
----------------------------------------

What is Krita?
~~~~~~~~~~~~~~

This is our vision for the development of Krita:

<blockquote>Krita is a KDE program for sketching and painting, offering
an end–to–end solution for creating digital painting files from scratch
by masters. Fields of painting that Krita explicitly supports are
concept art, creation of comics and textures for rendering. Modeled on
existing real-world painting materials and workflows, Krita supports
creative working by getting out of the way and with a snappy
response.</blockquote>

Note that when we say “Krita is a KDE program”, that doesn’t mean you
need to run the Plasma Desktop to run Krita. It means that Krita as a
project is proud to be part of the wonderful KDE community and uses the
great framework technology that the KDE community develops.. You can run
Krita on Windows, Gnome, XFCE, and if you spend some effort even on OSX.

There are three versions of Krita: Krita Sketch, for touch devices,
Krita Desktop for desktop systems and finally Krita Gemini, available
through `Steam <http://steamcommunity.com/app/280680/>`__.

Who owns Krita?
~~~~~~~~~~~~~~~

The Stichting Krita Foundation owns the Krita trademark.

Is there professional support available for Krita?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Yes, the Krita Foundation offers support for Krita through the
`development fund <https://krita.org/support-us/donations/>`__,
sponsoring opportunities, consultancy and `dedicated development
contracts <https://krita.org/support-us/commercial/>`__.

Who and what is Kiki?
~~~~~~~~~~~~~~~~~~~~~

Kiki is a squirrel. She’s our mascot and has been designed by Tyson Tan.
We choose a squirrel when we discovered that ‘krita’ is the Albanian
word for Squirrel.

Why is Krita Free?
~~~~~~~~~~~~~~~~~~

Krita is developed as `free software <http://www.gnu.org/>`__ within the
KDE community. We believe that good tools should be available for all
artists. Krita Gemini will be available on Valve’s Steam platform and
will cost money, but will still be open source.

Can I use Krita commercially?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Yes. What you create with Krita is your sole property. You own your work
and can license your art however you want. Krita’s GPL license applies
to Krita’s source code. Krita can be used commercially by artists for
any purpose, by studios to make concept art, textures, or vfx, by game
artists to work on commercial games, by scientists for research, and by
students in educational institutions.

If you modify Krita itself, and distribute the result, you have to share
your modifications with us. Krita’s GNU GPL license guarantees you this
freedom. Nobody is ever permitted to take it away.

Can I get Krita for iPad? for Android?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Krita will never be available for iOS (iPad, iPhone, iPad Pro) because
Apple's Appstore's terms and conditions add restrictions that are
incompatible with free software licensed under the GNU Public License.
Krita has had over 600 contributors who would all have to agree to
relicensing their code to something that Apple likes, and that is not
going to happen.

As for Android, there are no such problems, and we would like to see a
version for Android, but we currently do not have the time to work on
that.

Who translates Krita and are there translations available?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Krita is a `KDE application <http://www.kde.org/>`__ — and proud of it!
That means that Krita’s translations are done by `KDE localization
teams <http://i18n.kde.org/>`__. If you want to help out, join the team
for your language! There is another way you can help out making Krita
look good in any language, and that is join the development team and fix
issues within the code that make Krita harder to translate.

The translations are easy to install on any linux distribution. On
Windows they are bundled and you can set them via settings->change
application language. On OSX, we are working to make them work similarly
to windows, but there are a few bugs preventing the translations work
correctly at the time of writing.

Why is Krita part of the Calligra Suite?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

It is no longer part of Calligra. Krita started out as KImageShop inside
KOffice because the KOffice libraries gave us things for free we would
have to code ourselves otherwise, like filter handling, a really cool
rich text tool and so on. The current stable version is Krita 3.0. which
is developed in its `own
repository <https://phabricator.kde.org/diffusion/KRITA/>`__.

What are Krita’s Development Goals?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Krita is primarily a painting program, although it has image processing
capabilities. This means that Krita is intended for creative people who
desire to paint and draw with computer software as they do with
real-world tools in an art studio.

If you are looking for a tool primarily to apply effects to existing
images or photos, to catalog images, or to view images other software
(such as Digikam) may be more suitable.If you want to work on collage,
photo editing or print production work, Gimp might be more suitable.
Ease of use and power as a painting application will always have a
higher priority in Krita’s ongoing development.

Would you like bug reports?
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Definitely. Please take care to include backtraces if you’ve got a
crash, and if there’s an image that breaks Krita for you, try to attach
the image to the report. If it’s too big, contact me (that’s ‘boud’) on
irc: #krita, or directly via email. Adding new wishes to bugzilla isn’t
terribly useful, I’m afraid. We have a lot on our TODO already, and to
create a new feature, we need to engage in some deep interaction with
you, so drop by on the forum, mailing or irc instead. You can report
bugs at the KDE bug tracker. We try to reply to bug reports within a
week.

If you find signing up to KDE’s bugzilla too much of a bother, or aren’t
sure you found a real bug, don’t hesitate, and drop by on the forum or
on `IRC <https://krita.org/irc/>`__.

Can I join the fun?
~~~~~~~~~~~~~~~~~~~

Yes.The best thing you can do is use and enjoy Krita! Learn to use Krita
and teach others. Create tutorials and sample files, create artwork to
show off what Krita can do and spread the good word. And if you want to
be more directly involved, well, I didn’t know any C++ when I started
hacking on Krita and I managed. You can do it, too! Check the `Join
Krita page <https://krita.org/get-involved/overview/>`__ for more
information.

And if you don’t feel like hacking C++ — well, there’s the manual that
needs someone attending to it, a set of tutorials would be nice, we are
everlastingly needing more artwork for interface elements, and finally,
we really appreciate reports from people using it, telling me about
their work flow and what hampers or helps them.

Reference
---------

https://answers.launchpad.net/krita-ru/+faqs

`Category:Documentation{{#translation:}} <Category:Documentation{{#translation:}}>`__
