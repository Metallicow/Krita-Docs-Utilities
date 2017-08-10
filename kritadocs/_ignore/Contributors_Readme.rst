Welcome to our new wiki!

We're moving from userbase.kde.org to docs.krita.org because we felt
that we needed a bit more flexibility.

The new wiki will include:

A reference manual for Krita
    This one is probably what everyone is expecting when they type in
    docs.krita.org. Dry, basic, 'what does this button do' type of
    information.
General concept tutorials.
    We've found over the past two years that for certain of users, a
    reference manual, even with some examples, just isn't enough. The
    manual should provide fast and concise explanations for things, and
    provide a basic workflow for preparing an image for the web. But we
    also have found that certain concepts, such as color management and
    layer handling is far more advanced in Krita than that the average
    artist is used to. Krita is free and many of its users will not have
    formal training in digital artwork. So there's no pre-existing
    artist-focused knowledge on how to use color management or filter
    layers. In addition there are systems that are unique to Krita, for
    example the brush system, the transform masks, the alpha inheritance
    and the perspective assistants. Finally, there are users who aren't
    familiar with even standard painting workflows, and are not flexible
    enough to understand how to port a tutorial for Sai or Photoshop to
    Krita.
A list of known tutorials and video tutorials
    Apparantly, one of the great things about Krita's team is how we
    connect with artists and acknowledge that they're doing cool stuff.
    The same should count for tutorials, especially because there's ways
    of using Krita and ways of approaching painting that are unique and
    we should encourage people to share their knowledge.
krita.org tutorials
    There's been a bunch of tutorials on the krita.org and the
    krita-foundation.tumblr.com, the former focussing on explaining how
    to use a new feature and the later stimulated by user request.
FAQ
    This one is already online and a merger of the different FAQs that
    we had. It's currently being translated and we hope to keep this one
    the primary one to update.

For first timers
----------------

You make your account via identity.kde.org, this account can also be
used on the forum and phabricator as well as a lot of other KDE
infrastructure(bugzilla being a notable exception).

Unlike userbase, we don't use openID anymore, which means that permanent
login works now.

If you are new I recommend you to go to preferences and check out the
editor settings. There's AJAX based instant preview type stuff available
as well as a slightly better rich text editor, and these are very useful
for getting comfortable in mediawiki.

General philosophy
------------------

Demographics and target audience(s)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

We cannot talk about a demographic in the sense that we know all Krita
users are 55 year old men. Krita is used by a hugely different amount of
people, and we are actually kind of proud that we have such a varied
userbase.

Despite that, we know a couple of things about our users:

-  They are artists. This is explicitly the type of users that we
   target.

   -  Therefore, we know they prefer pretty pictures.
   -  They are visual.
   -  And that they are trying to achieve pretty pictures. Therefore,
      the implicit goal of each page would be to get the feature used
      for pretty pictures.

Other than that, we've observed the following groups:

-  High-school and college students trying out drawing software for
   illustrations. These usually have some previous experience with
   drawing software, like Painttool Sai or Photoshop, but need to be
   introduced to possibilities. This group's strength is that they share
   a lot of information with each other like tips and tricks and
   tutorials.
-  Professionals, people who earn their money with digital drawing
   software. The strength of this group is that they have a lot of
   know-how and are willing to donate to improve the program. These come
   in two types:

   -  Non technical professionals. These are people who do not really
      grasp the more mathematical bits of a piece of software, but have
      developed solid workflows over the years and work with software
      using their finely honed instincts. These tend to be illustrators,
      painters and people working with print.
   -  Technical professionals. These are people who use Krita as part of
      a pipeline, and care about the precise maths and pixel pushing.
      These tend to be people working in the games and VFX industry, but
      occasionally there's a scientist in there as well.

-  Adult and elderly hobbyists. This group doesn't know much about
   computers, and they always seem to get snagged on that one little
   step missing from a tutorial. Their strength as a group is that they
   adapt unconventional workflows from real life that the student
   wouldn't know about and the professional has no time for and create
   cool stuff with that, as well as that they have a tempering effect on
   the first group in the larger community.

From these four groups...

-  there's only one that is technical. Which is why we need the concept
   pages, so that we can create a solid base to write our manual texts
   on top of.
-  three of them likely have previous experience with software and may
   need migration guides and be told how.
-  two of them need to know how to get Krita to cooperate with other
   software.
-  two of them have no clue what they are doing and may need to be
   guided through the most basic of steps.

From that we can get the followig rules:

General
~~~~~~~

Use American English if possible.
    We use American English in the manual, in accordance to Krita's UI
    being American English by default.
Keep the language polite, but do not use academic language.
    As a community, we want to be welcoming to the users, so we try to
    avoid language that is unwelcoming. Swearing is already not condoned
    by KDE, but going to the far other end, an academic style where
    neither writer nor reader is acknowledged might give the idea that
    the text is far more complex than necessary, and thus scare away
    users.
Avoid using gifs.(up to debate)
    The reason is that people with epilepsy may be affected by fast
    moving images. Similarly, gifs can sometimes cary too much of the
    burden of explanation. If you can't help but use gifs, at the least
    notify the reader of this in the introduction of the page.
Keep it translation compatible
    See below.

Regarding photos and paintings
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  I would like to dis-encourage photos and traditional paintings in the
   manual if they are not illustrating a concept. The reason is that it
   is very silly and a little dishonest to show Rembrand's work inside
   the Krita GUI, when we have so many modern works that were made in
   Krita. All of the pepper&carrot artwork was made in Krita and the
   original files are available, so when you do not have an image handy,
   start there. Photos should be avoided because Krita is a painting
   program. Too many photos can give the impression Krita is trying to
   be a solution for photo retouching, which really isn't the focus.
-  Of course, we still want to show certain concepts in play in photos
   and master paintings, such as glossing or indirect light. In this
   case, add a caption that mentions the name of the painting or the
   painter, or mention it's a photograph.
-  Photos can still be used for photobashing and the like, but only if
   it's obviously used in the context of photobashing.

Regarding images in general
~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  Avoid text in the images and use the caption instead. Like
   <nowiki>`caption <file:filename.png>`__\ </nowiki>.
-  If you do need to use text, make either an SVG, so the text inside
   can be manipulated easier, or try to minimize the amount of text.
-  Try to make your images high quality/cute. Let's give people the idea
   that they are using a program for drawing!

Translation and further Typography
----------------------------------

(under construction)

-  wikilinks will need to be prepended with Special:myLanguage so,
   Special:myLanguage/KritaFAQ for example.
-  Keyboard shortcuts go between <tt><nowiki><kbd></kbd></nowiki></tt>
   tags. So <tt><nowiki><kbd>Ctrl</kbd>+<kbd>S</kbd></nowiki></tt>
   becomes <kbd>Ctrl</kbd>+<kbd>S</kbd>.
-  Similarly, options on the menu go inbetween <tt><nowiki><span
   class=“menuchoice”></span><</nowiki></tt> So <tt><nowiki><span
   class=“menuchoice”>settings -> configure Krita ->
   display</span></nowiki></tt> becomes <span
   class=“menuchoice”>settings -> configure Krita -> display</span>.
   Note the space between the arrows.

   -  Optionally, use <tt>&amp;rarr;</tt>, which'll become &rarr;, so
      <span class=“menuchoice”>settings &rarr; configure Krita &rarr;
      display</span>. You can get these symbols from the special
      characters in the advanced markup editor which needs to be set in
      preferences.
   -  Use the template instead to prevent your fingers from getting
      tired: <tt><nowiki></nowiki></tt> then becomes

Templates
---------

<code><nowiki></nowiki></code> <code><nowiki></nowiki></code>
<code><nowiki></nowiki></code>

<code><nowiki> + + + </nowiki></code>

becomes: + + +

Other things to be discussed:

-  General outline of a reference page.
-  General outline of a tutorial.
-  Other issues.
