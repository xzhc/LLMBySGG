"""
	This example demonstrates a Linked List in python.
	Linked List Characteristics:
	- Linear data structure(Liked an array)
	- NOT stored contigously in memory(unlike an array)
	- Each element (Node) contains data and a reference to the next node
	- Dynamic size - can grow or shrinks as needed
	- No random access - must traverse from head to find elements
"""

# Node Class
class Node:
	"""
		Node Class: represents a single element in the linked list
		Each Node contains:
		- data: the actual value sotred
		- next: a pointer/reference to the next node(or None if it's the last node)
	"""

	def __init__(self, data, next = None):
		self.data = data # Store the data value in this Node
		self.next = next # Reference to the next node (default is None)
	

# Linked List Class
class LinkedList:
	"""
		LinkedList Class - a class linked list implementation
		Uses private attributes (__head __size) to encapsulate internal state.
	"""

	def __init__(self):
		"""Initialize an empty linked list"""
		self.__head = None # Head pointer: points to the first Node(None if the linked list is empty)
		self.__size = 0 # Track the bnumber of elements in the list
	
	def __str__(self):
		""" 
			Convert the linked list to a string for printing.
			Return a string like: "1->2->3->4"
		"""
		res = [] # Create an empty list to collect node values
		node = self.__head # Start from the head node
		while node: # Loop until node become None(end of list)
			res.append(str(node.data)) # Add current node's data as string
			node = node.next # Move to the next node
		return '->'.join(res) # Join all values with '->' separater


	@property
	def size(self):
		"""Property to get the number of elements in the list """
		return self.__size

	def is_empty(self):
		"""Check if the linked list is empty"""
		return self.__size == 0 # Return True if size is 0, False otherwise

	# Insert operation
	def insert(self, index, item):
		"""
		Insert an element at a specific position in the linked list
		Args:
			index: Position to insert (0 = head, size = tail)
			item: The data value to insert
		Time Complexity: O(n) - need to traverse to find the position
		"""
		# print(index)
		# print(self.__size)
		#Step1: Check if index is within valid range
		if index < 0 or index > self.__size:
			raise IndexError('Index out of bounds')

		#Step2: Handle insertion at head (index == 0)
		if index == 0:
			# Create new node whose 'next' points the current head
			# Then update head to point  to this new node
			# Example: insert(0, 10) on list [1->2->3]
			# Before: head -> 1 -> 2 -> 3 => None
			# After: head -> 10 -> 1 -> 2 -> 3 -> None
			self.__head = Node(item, self.__head)
		else:
			# Step3: Handle insertion at other position
			node = self.__head # Start from head
			for i in range(index - 1): #Traverse to the nod Before insert position
				node = node.next # Move to next node
			
			# Now 'node' is at position ( index - 1 )
			# Create a new node that points to node.next (the current node at index)
			# Then make the previous node point to our new node
			# Example: insert (2, 99) on list [1->2->3->4]
			# Before: [1] -> [2] -> [3] -> [4]
			# After: [1] -> [2] -> [99] -> [3] -> [4]
			node.next = Node(item, node.next)
		
		# Step4: Increment size
		self.__size += 1

	def append(self, item):
		"""
		Append an element to the end of the linked list
		Simply calls the insert() at position 'size'
		"""
		self.insert(self.__size, item)

	# Repmve operation
	def remove(self, index):
		"""
		Remove the element at a specific position
		Args:
			index: Position of element to remove (0-based)
		Time complexity: O(n) - need to traverse to find the position
		"""

		# Step1: check bounds
		if index < 0 or index >= self.__size:
			raise IndexError('Index out of bounds')
		
		# Step2: Handle removing head node (index == 0)
		if index == 0:
			# Simply move head to the second node
			# Example: remove(0) on list [1->2->3]
			# Before: head -> [1] -> [2] -> [3]
			# After: head -> [2] -> [3]
			self.__head = self.__head.next
		else:
			# Step3: Handle removing from other positions
			node = self.__head
			for i in range (index - 1): # Traverse to node Before the one to delete
				node = node.next

			# Skip over the node to be deleted by pointing to node.next.next
			# Example: remove(1) on list [1->2->3->4]
			# Before: [1] -> [2] -> [3] -> [4]
			# After: [1] -> [3] -> [4]
			node.next = node.next.next  

		# Step4: Decrement size
		self.__size -= 1

	# Update operation
	def set(self, index, item):
		"""
		Update the value at a specific position.
		Args:
			index: Position to update
			item: New value to set
		Time complexity: O(n) - need to traverse to the position
		"""
		# Check bounds
		if index < 0 or index >= self.__size:
			raise IndexError('Index out of bounds')
		
		# Traverse to the target node
		node = self.__head
		for i in range(index):
			node = node.next
		
		# Update the data
		node.data = item
	
	# Get operation
	def get(self, index):
		"""
		Get the value at a specific position
		Args:
			index: Position to access
		Return:
			The data value at that position
		
		Time complexity: O(n) - need to traverse to the position
		"""
		# Check bounds
		if index < 0 or index >= self.__size:
			raise IndexError('Index out of bounds')
		# Traverse to the target node
		node = self.__head
		for i in range(index):
			node = node.next
		
		# Return the data
		return node.data
	
	# Find operation

	def find(self, item):
		"""
		Check if an elements exists in the linked list.
		Args: 
			item: value to search for
		Returns: 
			True if found, False otherwise
		Time Complexity: O(n) - may need to check every node
		"""
		node = self.__head # Start from head
		while node: # Loop through all node
			if node.data == item: # Found a match
				return True 
			node = node.next # Move to next node
		return False # Searched entire list, not found

	def for_each(self, func):
		"""
		Apply a function to each element in the linked list
		Args:
			func: A funciton to apply to each element's data
		Example: llist.for_each(print) will print every element
		"""
		node = self.__head 
		while node:
			func(node.data)
			node = node.next


llist = LinkedList()
llist.append(1)
llist.append(2)
llist.append(3)
llist.append(4)
llist.insert(0, 10)
llist.insert(3, 20)
llist.remove(0)
llist.remove(3)
llist.set(0,6)
llist.set(3, 10)
print(llist)
print(llist.get(2))
print(llist.find(2))
print(llist.find(30))
llist.for_each(print)