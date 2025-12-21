"""
This case demonstrates the ways of parameter passing
"""


"""
Required parameters: Match according to the position of parameters.
Requirement: the number of parameters must be consistent,
and the order of parameters must be same
"""

# def func(a,b,c):
#     print(a,b,c)
# func(1,2,3)

"""
keyword arguments(passing by name): When passing arguments to a function call, 
specify the parameter names and match with formal parameters by name.
The order of formal and actual parameters can be different
"""

# def func(name, age):
#     print(f"Current user:{name}, age:{age}")
# func("xzh", 18)
# func(age=26, name="John")

"""
Default parameter values: Assign default values to parameters when defining a function.
"""

# def func(name, age=18):
#     print(f"Current user:{name}, age:{age}")
#
# func("cyh")
# func("cyh", 20)

"""
Variable-length parameters
Parameters prefiexed with an asterisk * will be imported as a tuple,
storing all unnamed variable parameters.
If variable-length parameters appear in formal parameters, 
when calling the function,first match the required parameters by position,
then the parameters after the variable-length parameters must be matched by keyword arguments
"""

# def func(num, *args, num1):
#     print(num)
#     print(args)
#     print(num1)
#
# func(1,2,3,4,5, num1=6)

#args is a tuple, but kwargs is a dict.
# def func(num, **kwagrs):
#     print(num)
#     print(kwagrs)
#
# func(1, a=2,b=3,c=4,d=5)

"""
Unpacking arguments: Unpack sequence/dictionary type parameters before passing to the function
"""

# def func(a,b,c):
#     print(a+b+c)
# func(1,2,3)
# func(*(1,2,3)) #unpack tuple to pass arguments
# func(**{"a":1,"b":2,"c":3})#unpack dictionary to pass arguments


"""
Variable-length parameters combined with argument unpacking
"""
def func(num, *args):
    print(num)
    print(args)

func(3, *(100,200,300))

#Dictionary unpacking for keyword argument
def func(name,age):
    print(name,age)
func(**{"name":"xzh", "age":26})

"""
Parameters before / must be passed by position, parameters after * must be passed by keywords 
"""

def func(a,b,/,c,d,e,f,*,g,h):
    print(a,b,c,d,e,f,g,h)
func(1,2,3,4,5,6,g=7,h=8)