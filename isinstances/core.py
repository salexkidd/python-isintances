# -*- coding:utf-8 -*-
"""
This is core module of isinstances
"""


class DifferentObjectError(Exception):
    """
    DifferentObject Error Class
    """
    def __init__(self, obj_list):
        self.obj_list = obj_list

    def __str__(self):
        return "Different object error"


def _isinstances_with_objects(object_list=[], klass=None):
    """
    Check instances type
    """
    diff_flg = True
    diff_obj_list = []

    for obj in object_list:
        if isinstance(obj, klass) is False:
            diff_obj_list.append(obj)
            diff_flg = False

    return diff_flg, diff_obj_list


def isinstances(object_list=[], klass=None):
    """
    isinstances function
    """
    ret_flg, diff_objs = _isinstances_with_objects(object_list, klass)
    return ret_flg, diff_objs


def isinstances_with_raise(object_list=[], klass=None):
    """
    isinstances_with_raise function
    """
    ret_flg, diff_objs = _isinstances_with_objects(object_list, klass)

    if ret_flg == False:
        raise DifferentObjectError(obj_list=diff_objs)
