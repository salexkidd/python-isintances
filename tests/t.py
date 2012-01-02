#!/usr/bin/env python
# -*- coding:utf-8 -*-
import unittest
from core import *


class isinstancesTestClass(unittest.TestCase):
    def setUp(self):
        self.same_obj = {
            'obj_list': [1, 2, 3, 4, ],
            'type': int
            }
        self.diff_obj = {
            'obj_list': [1, 'aaa', 2, 'bbb', ],
            'type': int,
            }

    def tearDown(self):
        pass

    def test_isinstances(self):
        diff_flg, same_obj_list = \
            isinstances(self.same_obj['obj_list'],
                        self.same_obj['type'],)
        assert diff_flg == True, "Why it is False!?"

        diff_flg, diff_obj_list = \
            isinstances(self.diff_obj['obj_list'],
                        self.diff_obj['type'])
        assert diff_flg == False, "Why it is True!?"

    def test_isinstances_with_raise(self):
        with self.assertRaises(DifferentObjectError) as cm:
            isinstances_with_raise(
                self.diff_obj['obj_list'],
                self.diff_obj['type'])

    def test_stres(self):
        with self.assertRaises(DifferentObjectError) as cm:
            isinstances_with_raise(
                self.diff_obj['obj_list'],
                self.diff_obj['type'])


class isinstancesTestSuite(unittest.TestSuite):
    def __init__(self):
        tests = ('test_isinstances',
                 'test_isinstances_with_raise',
                 'test_stres',
                 )
        unittest.TestSuite.__init__(
            self,
            map(isinstancesTestClass, tests)
            )


if __name__ == "__main__":
    alltests = isinstancesTestSuite()
    unittest.TextTestRunner(verbosity=2).run(alltests)
