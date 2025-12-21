"""
This case demonstrates importing modules from packages
"""

#Global import
# import graphic.circle
# import graphic.rectangle
# Create Circle instance and call area method
# c = graphic.circle.Circle(5)
# print(c.area())
#Create Rectangle instance and call area method
# r = graphic.rectangle.Rectangle(3,4)
# print(r.area())

#Local import - import a module from a package
# from graphic import circle
# print(circle.Circle(5).area())

#Local import - import a member from a specific module in a package
# from graphic.circle import Circle
# c = Circle(5)
# print(c.area())

#Local import - from package import *

from graphic import *
c = circle.Circle(5)
r = rectangle.Rectangle(3,4)
print(c.area())
print(r.area())