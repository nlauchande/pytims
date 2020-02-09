"""This module implements  a specialized linked lists container datatypes providing
alternatives to Python's general purpose built-in containerslist

* LinkedList   factory function for creating tuple subclasses with named fields

"""
from pyrithms.collections.linked_list import LinkedList
import pytest
import unittest


class LinkedListTest(unittest.TestCase):
    def test_insertion(self):
        linked_list = LinkedList()

        linked_list.insert("10")
        linked_list.insert("30")
        linked_list.insert("15")
        linked_list.insert("40")
        linked_list.insert("50")
        result = []
        for i in iter(linked_list):
            result.append(i.data)

        assert result == ["50", "40", "15", "30", "10"]
