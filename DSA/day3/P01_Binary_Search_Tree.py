from collections import deque

class Node:
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None
	


class BinarySearchTree:
	def __init__(self):
		self.__root = None
		self.__size = 0

	@property
	def size(self):
		return self.__size

	def is_empty(self):
		return self.__size == 0


	def print_tree(self):

		# 计算树的层数（递归）
		def get_layer( node):
			if node is None:
				return 0 
			else:
				left_depth = get_layer(node.left)
				right_depth = get_layer(node.right)
				return max(left_depth, right_depth) + 1
		
		layer = get_layer(self.__root)

		# 层序遍历并打印
		queue = deque([(self.__root, 1)])
		current_level = 1
		while queue:
			node, level = queue.popleft()
			if level > current_level:
				print()
				current_level += 1
			if node:
				print(f"{node.data:^{20 * layer // 2 ** (level - 1)}}", end="")
			else:
				print(f"{'N':^{20 * layer // 2 ** (level - 1)}}", end="")
			
			if level < layer:
				if node:
					queue.append((node.left, level + 1))
					queue.append((node.right, level + 1))
				else:
					queue.append((None, level + 1))
					queue.append((None, level + 1))
		print()

	# 查找节点，返回（节点，父节点）
	def __search_pos(self, item):
		parent = None
		current = self.__root
		while current:
			if current.data == item:
				break
			parent = current
			current = current.left if item < current.data else current.right
		return current, parent

	# 判断查找的元素是否在树中存在
	def search(self, item):
		return self.__search_pos(item)[0] is not None

	# 添加元素
	def add(self, item):
		node = Node(item)
		if self.is_empty():
			self.__root = node
			self.__size += 1
			return
		
		current, parent = self.__search_pos(item)
		if current:
			return
		else:
			if item < parent.data:
				parent.left = node
			else:
				parent.right = node
		
		self.__size += 1

	# 找到当前节点的最小子节点
	def __get_min(self, node):
		current = node
		while current:
			current = current.left
		return current
	
	def remove(self, item):
		# 查找元素在树中的位置
		current, parent = self.__search_pos(item)

		#如果元素不存在
		if not current:
			return

		#如果元素对应的是叶节点
		if not current.left and not current.next:
			# 判断元素对应的是不是根节点（唯一节点）
			if parent:
				if parent.left == current:
					parent.left = None
				else:
					parent.right = None
			else:
				self.__root = None

		#元素对应的节点有一个子节点（左或右）
		elif not current.left or not current.right:
			child = current.left if current.left else current.right

			if parent:
				if parent.left == current:
					parent.left = child
				else:
					parent.right = child
			else:
				self.__root = child

		# 元素对应的节点有两个子节点（左右都有)
		else:
			successor = self.__get_min(current.right)
			successor_data = successor.data
			self.remove(successor_data)
			current.data = successor_data
		
		self.__size -= 1

	def for_each(self, func, order="inorder"):
		"""遍历树，默认中序遍历"""
		match order:
			case "inorder":
				self.__inorder_traversal(func)
			case "preorder":
				self.__preorder_traversal(func)
			case "postorder":
				self.__postorder_traversal(func)
			case "levelorder":
				self.__levelorder_traversal(func)

	def __inorder_traversal(self, func):
		"""深度优先搜索：中序遍历"""
		def inorder(node):
			if node:
				inorder(node.left)
				func(node.data)
				inorder(node.right)

		inorder(self.__root)

	def __preorder_traversal(self, func):
		"""深度优先搜索：前序遍历"""

		def preorder(node):
			if node:
				func(node.data)
				preorder(node.left)
				preorder(node.right)

		preorder(self.__root)

	def __postorder_traversal(self, func):
		"""深度优先搜索：后序遍历"""

		def postorder(node):
			if node:
				postorder(node.left)
				postorder(node.right)
				func(node.data)

		postorder(self.__root)

	def __levelorder_traversal(self, func):
		"""广度优先搜索：层序遍历"""
		queue = deque()
		queue.append(self.__root)
		while queue:
			node = queue.popleft()
			func(node.data)
			if node.left:
				queue.append(node.left)
			if node.right:
				queue.append(node.right)


bst = BinarySearchTree()
bst.add(6)
bst.add(5)
bst.add(8)
bst.add(3)
bst.add(7)
bst.add(9)
bst.print_tree()
print("~~~~~~~")
bst.for_each(print, order="levelorder")

		