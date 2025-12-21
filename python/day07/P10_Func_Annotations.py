"""
This case demonstrates function annotations
"""

#Ordinary custom function
def dog1(name,age,species):
    return (name,age,species)

#Custom function with annotations added:
def dog2(name:str, age:(1,99), species:"breed of the dog") -> tuple :
    return (name,age,species)

print(dog1.__annotations__)
print(dog2.__annotations__)