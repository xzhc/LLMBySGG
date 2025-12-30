"""
This example demonstrates the HashTable data structure
"""

# Define the Node class for the linked list (use for chaining)
class Node:
	""" Define a node class for the linked list in hash table"""
	# Constructor: initialize a node with key-value pair
	def __init__(self, key, value):
		# Store the key
		self.key = key
		# Store the value
		self.value = value
		# Reference to next node (for collision handling via chaining)
		self.next = None

# Define the HashTable class
class HashTable:
	# Constructor: initialize the hash tabl
	def __init__(self):
		# Number of elements in the hash table
		self.__size = 0
		# Initial capacity of the hash table array
		self.__capacity = 2
		# The array part of the hash table (initialized with None)
		self.__table = [None] * self.__capacity
		# Load factor threshold (element count / array capacity)
		self.__load_factor = 0.7

	# Private method to compute the hash index for a given key
	def __hash(self, key):
		# User Python's built-in hash function and modulo by capacity
		return hash(key) % self.__capacity
	
	# Property dectorator to get the size of the hash table
	@property
	def size(self):
		return self.__size

	# Method to check if the hash table is empty
	def is_empty(self):
		return self.__size == 0
	
	# Method to display the contents of the hash table
	def display(self):
		for i, node in enumerate(self.__table):
			print(f'Index:{i} ', end= '')
			current = node
			while current:
				print(f'{current.key}, {current.value} ->', end= '')
				current = current.next
			print('None')

	# Private method to grow / resize the hash table
	def __grow(self):
		self.__capacity *= 2
		self.__table, old_table = [None] * self.__capacity, self.__table
		self.__size = 0

		for node in old_table:
			current = node
			while current:
				self.put(current.key, current.value)
				current = current.next 


	# Method to add or update a key-value pair in the hash table
	def put(self, key, value):
		index = self.__hash(key)
		new_node = Node(key, value)
		
		if self.__table[index] is None:
			self.__table[index] = new_node
		else:
			current = self.__table[index]
			while current:
				if current.key == key:
					current.value = value
					return
				if current.next:
					current = current.next
				else:
					break
			current.next = new_node
		self.__size += 1

	# Method to remove an element by key
	def remove(self, key):
		index = self.__hash(key)
		current = self.__table[index]
		prev = None

		while current:
			if current.key == key:
				if prev:
					prev.next = current.next
				else:
					self.__table[index] = current.next
				self.__size -= 1
				return True
			prev = current
			current = current.next
		return False

	# Method to get a value by key
	def get(self, key):
		index = self.__hash(key)
		current = self.__table[index]
		while current:
			if current.key == key:
				return current.value
			current = current.next
		return None

	# Method to iterate over all elements in the hash table
	def for_each(self, func):
		for node in self.__table:
			current  = node
			while current:
				func(current.key, current.value)
				current = current.next

hs1 = HashTable()
hs1.put(1, 10)
hs1.put(2, 20)
hs1.put(3, 30)
hs1.put(4,40)
hs1.remove(3)
print(hs1.get(1))
hs1.display()
hs1.for_each(print)