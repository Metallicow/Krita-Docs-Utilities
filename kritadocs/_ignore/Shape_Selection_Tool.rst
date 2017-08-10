.. raw:: mediawiki

   {{ToolIcon|arrow}}

The shape selection tool used to be called the “default” tool. This had
to do with Krita beig part of an office suit once upon a time. But this
is no longer the case, so we renamed it to its purpose in Krita:
Selecting shapes!

The shape selection tool allows you to select shapes, group them, apply
boolean operations and change the shape look.

Selection
---------

Selecting shapes works as follows. You can click on a shape to select a
single shape. You can select multiple shapes with click drag.

There's two types of drag action, a \*blue\* one and a \*green\* one.
The blue one is created by dragging from left to right, and will only
select shapes that are fully covered by it. The green selection is
created from right to left and will select all shapes it touches.

Tool Options
------------

The tool options of this menu are quite involved, and separated over 3
tabs.

Geometry
~~~~~~~~

Geometry is the most basic tab. It allows you to precisely set the x, y,
width and height.

Anchor Lock
    This is not implemented at the moment.
Uniform scaling
    When enabled, it will scale the stroke width with the shape, when
    not enabled, the stroke with will stay the same.
Global coordinates
    Determines whether the width and height bars use the width and
    height of the object, while taking transforms into account.
Opacity
    The general opacity of the object.

Stroke
~~~~~~

The stroke tab determines how strokes should look.

The first setting is the fill of the stroke. This has the same features
as the fill of the shape, so scroll down a bit for details on that.

Then, there's the settings for the stroke style.

Thickness
    The width of the stroke is determined by this entry. When creating a
    shape, Krita will use the current brush size to determine the width
    of the stroke.
Cap and corner style
    If you press the button after the thickness entry, you will be able
    to set the stroke cap and the stroke corner style.
Line-style
    Determines whether the stroke is solid or uses dashes and dots.
Markers
    Which markers can be added to the stroke. Markers are little figures
    that will appear at the start, end or all the nodes in between
    depending on your configuration.

Fill
~~~~

The fill of the shape. As this has the same features as the fill of the
stroke, this is explained here as well.

A fill can be a flat color, a gradient or a pattern. Or it can be
nothing(transparent)

None
    No fill. It's transparent.
Color
    A flat color, you can select a new one by pressing the color button.
Gradient
    This one has a few more options.

    Type
        A linear or radial gradient.
    Repeat
        How the gradient repeats itself.
    Preset
        A quick menu for choosing a base gradient to edit.

    You can edit the gradient in two ways. The first one is the actual
    gradient in the docker that you can manipulate. Vectors always use
    stop-gradients.
    The other way to edit gradients is editing their position on canvas.
Patterns
    Patterns aren't implemented yet.

Rightclick menu
---------------

The shape selection tool has a nice right click menu that gives you
several features. It is called up the same way as the pop-up palette.

`Category: Unstable\_Features <Category:_Unstable_Features>`__
