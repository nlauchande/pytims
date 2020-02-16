"""This module implements  a specialized linked lists container datatypes providing
alternatives to Python's general purpose built-in containerslist

* LinkedList   factory function for creating tuple subclasses with named fields

"""
from pyrithms.collections.tree import BSTTree
import pytest
import unittest


class TreeTest(unittest.TestCase):

    tree = BSTTree()
    tree.insert_element("10")
    tree.insert_element("30")
    tree.insert_element("15")
    tree.insert_element("40")
    tree.insert_element("50")

