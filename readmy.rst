======================================================================
python-isinstances by salexkidd (http://twitter.com/salexkidd)
======================================================================

.. toctree::

About
____________________________________
python-isinsntances provide a Check the class of instances.

Example
____________________________________
>>> from isinstances import isinstances
>>> isinstances([1, 2, 3,], int)
True
>>> isinstances([1, 2, 3, "a",], int)
(False, ['a'])

>>> from isinstances import isinstances_with_raise
>>> isinstances_with_raise([1, 2, 3,], int)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "isinstances/core.py", line 48, in isinstances_with_raise
    raise DifferentObjectError(obj_list=diff_objs)
isinstances.core.DifferentObjectError: Different object error
