.. figure:: Krita_Undo_History_Docker.png
   :alt: Krita_Undo_History_Docker.png

   Krita\_Undo\_History\_Docker.png

This docker allows you to quickly shift between undo states, and even go
back in time far more quickly that rapidly reusing
<kbd>CTRL</kbd>+<kbd>Z</kbd>

Cumulative Undo
---------------

.. raw:: mediawiki

   {{MouseButton|right}}

an item in the undo-history docker to enable cumulative undo. again to
change the parameters:

Start merging time
    The amount of seconds required to consider a group of strokes to be
    worth one undo step.
Group time
    According to this parameter -- groups are made. Every stroke is put
    into the same group till two consecutive strokes have a time gap of
    more than T seconds. Then a new group is started.
Split strokes.
    A user may want to keep the ability of Undoing/Redoing his last N
    strokes. Once N is crossed -- the earlier strokes are merged into
    the group's first stroke.

`Category:Dockers{{#translation:}} <Category:Dockers{{#translation:}}>`__
