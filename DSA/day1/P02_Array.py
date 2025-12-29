"""
    该案例演示了Python中的数组
    注意：python的内建中没有提供数组类型
    但是在python的array模块中提供了数组，另外在后续要用到的numpy模块中也提供了数组
    数组数据结构特点：
        线性的
        连续存储的，在内存中分配一片连续的存储空间
        只能存储相同数据类型的元素
        数组中的每一个元素都有下标，下标从0开始，可以通过下标访问数组元素
        数组容量一旦确定，就不能改变，如果需要扩容，需要通过额外的方法实现
"""
# import array
# arr1 = array.array('i', [1,2,3])
# print(id(arr1[0]))
# num = 1
# print(id(num))

# size()	返回数组中元素个数
# is_empty()	判断数组是否为空
# insert(index, item)	在指定位置插入元素
# append(item)	在末尾插入元素
# remove(index)	删除指定位置的元素
# set(index, item)	修改指定位置的元素
# get(index)	获取指定位置的元素
# find(item)	查找数组中某个元素的位置
# for_each(func)	遍历数组

class MyArray:
	def __init__(self):
		#数组容量
		self.__capacity = 8 # 私有：容量不能随便改
		#数组中元素的个数
		self.__size = 0 # 私有：只能通过 insert/remove 改变
		#数组底层用存储数据的list
		self.__items = [0] * 8
	
	def __str__(self):
		res = "["
		for i in range(self.__size):
			res += str(self.__items[i])
			if i != self.__size - 1:
				res += ","
		res += "]"
		return res

	@property
	def size(self):
		#获取数组中元素的个数
		return self.__size
	
	#判断数组是否为空
	def is_empty(self):
		return self.__size == 0

	#扩容数组
	def __grow(self):
		self.__capacity *= 2 #容量翻倍
		new_items = [0] * self.__capacity #创建新的更大的列表
		for i in range(self.__size): #把旧的数据复制到新的列表
			new_items[i] = self.__items[i]
		self.__items = new_items #指向新列表

	def insert(self, index, item):
		#第一步，检查小标边界
		if index < 0 or index > self.__size:
			raise IndexError('Index out of range')
		#第二步，检查是否需要扩容（数组是否满了）
		if self.__size == self.__capacity:
			self.__grow()
		#第三步：从右向左移动元素（为待插入元素腾出位置）
		for i in range(self.__size, index, -1): #i: size -> index + 1
			self.__items[i] = self.__items[i - 1] #每个元素都往后移动一位
		#第四步，在index处插入新的数据
		self.__items[index] = item
		#第五步：更新size
		self.__size +=1

	#在末尾处追加元素	
	def append(self,item):
		self.insert(self.__size, item) #在末尾处插入等于在size处插入

	#删除元素
	def remove(self, index):
		#第一步，检查是否越界
		if index < 0 or index > self.__size - 1:
			raise IndexError('index out of range')
		#第二步，从左向右前移元素覆盖要被删除的元素
		for i in range(index, self.__size - 1): #size: index -> size -2
			self.__items[i] = self.__items[i + 1]
		#第三步，更新size
		self.__size -= 1
	
	#修改元素
	def set(self, index, item):
		if index < 0 or index >= self.size: #检查越界
			raise IndexError('index out of range')
		self.__items[index] = item #直接覆盖

	#获取元素
	def get(self, index):
		if index < 0 or index >= self.__size: #检查越界
			raise IndexError('index out of range')
		return self.__items[index]

	#查找元素
	def find(self, item):
		for i in range(0, self.__size): #遍历所有有效元素
			if item == self.__items[i]: #找到匹配的
				return  i #返回下标
		return -1 #找不到就返回-1

	#遍历数组
	def for_each(self, func):
		for i in range(0, self.__size):
			func(self.__items[i])	

	
arr1 = MyArray()
arr1.append(1)
arr1.append(2)
arr1.append(3)
arr1.append(4)
arr1.remove(3)
arr1.set(1, 5)
arr1.append(6)
arr1.append(7)
arr1.append(8)
arr1.find(7)
print(arr1)
print(arr1.size)
print(arr1.is_empty())
print(arr1.get(1))
print(arr1.find(7))
arr1.for_each(print)
arr1.for_each(lambda x: print(x * 2))
