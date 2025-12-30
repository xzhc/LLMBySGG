"""
This example demonstrates the Stack data structure
"""

# Define the Stack class
class Stack:
	# Constructor: initialize the stack
	def __init__(self):
		# Use a dynamic array (python list) to store stack elements
		self.__items = []
		# Number of elements in the stack
		self.__size = 0

	def __str__(self):
		res = "["
		for i in range(self.__size):
			res += str(self.__items[i])
			if i != self.__size - 1:
				res += ','
		res += ']'
		return res


	# Property decrator to get the size of the stack
	@property
	def size(self):
		"""Return the number of elements in the stack """
		# Return the current size
		return self.__size

	# Method to check if the stack is empty
	def is_empty(self):
		"""Check if the stack is empty"""
		# Return True if size is 0, otherwise False
		return self.__size == 0

	# Method to push an element onto the stack
	def push(self, item):
		"""Push: Add an element to the top of the stack"""
		# Append the item to the end of the list(top of stack)
		self.__items.append(item)
		# Increment the size counter
		self.__size += 1

	# Method to pop an element from the stack
	def pop(self):
		"""Pop: Remove and return the top element from the stack"""
		# Check if the stak is empty
		if self.is_empty():
			# Raise an exception if stack is empty
			raise Exception('Stack is empty')
		
		# Get the top element (last item in list)
		item = self.__items[self.__size - 1]
		# Delete the top element from the list
		del self.__items[self.__size - 1]
		# Decrement the size counter
		self.__size -= 1
		# Return the popped item
		return item
	

	# Method to peek at the top element without removing it
	def peek(self):
		# Check if the stack is empty
		if self.is_empty():
			raise Exception('Stack is empty')
		# Return the top element
		return self.__items[self.__size - 1]

# Create a new Stack instance
s1 = Stack()
# Push some elements onto stack
s1.push(1)
s1.push(2)
s1.push(3)
# Print the current size of the stack
print(s1.size)
# Pop the top element from the stack
s1.pop()
print(s1)
print(s1.peek())

	