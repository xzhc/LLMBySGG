"""
该案例演示了大O表示法
"""

#提供一个函数，完成对list中元素的求和
#通过执行绝对时间衡量算法的好坏
import time
def sum(nums):
	start_time = time.time()
	res = 0
	i = -1
	while  (i:= i + 1) < len(nums):
		res += nums[i]

	end_time = time.time()
	print(f'总耗时{end_time - start_time}')
	return res 

print(sum([x for x in range(10000000)]))