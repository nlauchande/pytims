'''This module implements  a specialized linked lists container datatypes providing
alternatives to Python's general purpose built-in containerslist

* LinkedList   factory function for creating tuple subclasses with named fields

'''

__all__ = ['LinkedList']

class Node:
	
	def __init__(self,data):
		self.next=None
		self.data = data

	def __repr__(self):
		return self.data

	def __eq__(self, obj):
		return isinstance(obj, Node) and obj.data == self.data
		
class LinkedList:

	def __init__(self):
		self._current = None
		self._head = None
	
	def insert(self, data):
		current = Node(data)

		if self._head != None:
			current.next = self._head
		
		self._head = current

		current = self._head

	def remove(self, data):

		nodeToFind = Node(data)

		if self._head == nodeToFind:
			self._head = self._head.next			
		else:
			current = self._head
			while current.next!=nodeToFind  and current.next!=None :
				current = current.next
			
			if current.next==nodeToFind:
				current.next = current.next.next
				return True
			else:
				return False

	def __iter__(self):
		self._current = self._head
		return self

	def __next__(self):

		if self._current == None:
			  raise StopIteration

		result = self._current

		self._current = self._current.next

		return result

if __name__ == "__main__":
	linked_list = LinkedList()
	
	linked_list.insert("10")
	linked_list.insert("30")
	linked_list.insert("15")
	linked_list.insert("40")
	linked_list.insert("50")

	print("After insertion: \n")
	for i in iter(linked_list) :
		print(i)

	print("Remove 40: \n")
	linked_list.remove("40")

	for i in iter(linked_list) :
		print(i)
