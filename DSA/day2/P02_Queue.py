"""
This example demonstrates implementing a Queue using a Linked List
"""

# Define the Node class for the linked list
class Node:
	# Constructor: initialize a node
	def __init__(self, data):
		# Store the data/element to this node
		self.data = data
		# Reference to the next node(initially None)
		self.next = None

# Define the Queue class
class Queue:
	# Constructor: initialize the queue
	def __init__(self):
		# Reference to the front/head of the queue
		self.__head = None
		# Reference to the rear/tail of the queue
		self.__tail = None
		# Number of elements in the queue
		self.__size = 0

	def __str__(self):
		res = []
		node = self.__head
		while node:
			res.append(str(node.data))
			node = node.next
		
		return '<-'.join(res)
	
	# Property decorator to get the size of the queue
	@property
	def size(self):
		return self.__size

	# Method to check if the queue is empty
	def is_empty(self):
		return self.__size == 0

	# Method to add an element to the queue
	def enqueue(self, data):
		new_node = Node(data)
		if self.is_empty():
			self.__head = new_node
			self.__tail = new_node
		else:
			self.__tail.next = new_node
			self.__tail = new_node
		self.__size += 1

	# Method to remove an element from the front element
	def dequeue(self):
		# Check if the queue is empty
		if self.is_empty():
			raise Exception('Queue is empty')

		dada = self.__head.data
		self.__head = self.__head.next
		self.__size -= 1
		return dada

	# Method to peek at the front element without removing it
	def peek(self):
		if self.is_empty():
			raise Exception('Queue is empty')
		return self.__head.data

q1 = Queue()

q1.enqueue(10)
q1.enqueue(20)
q1.enqueue(30)
print(q1.size)
print(q1)
q1.dequeue()
print(q1.size)
print(q1)
print(q1.peek())
print(q1.size)