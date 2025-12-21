"""
    This case demonstrates the basic operations of dictionaries
"""

#create a dictionary object
# dict1 = {}
# dict2 = dict()
# dict3 = {"a": 1, "b": 2, "c": 3}
# dict4 = dict(a=1, b=2, c=3)
# dict5 = dict([("a",1), ("b",2), ("c",3)])
# dict6 = {i: i * 2 for i in range(5)}
# print(dict1, type(dict1))
# print(dict2, type(dict2))
# print(dict3, type(dict3))
# print(dict4, type(dict4))
# print(dict5, type(dict5))
# print(dict6, type(dict6))

#Access dictionary elements
# dict1 = {"name":"xzh", "age":26, "gender":"male"}
# print(dict1["name"])
# print(dict1["age"])
# print(dict1["gender"])
# print(dict1["add"]) #if there is no corresponding key, an error will occur

# print(dict1.get("name"))
# print(dict1.get("age"))
# print(dict1.get("gender"))
# print(dict1.get("add")) # if there is no corresponding key, return none


#Adding elements to a dictionary and modifying elements
# dict1 = {"name": "xzh", "age": 18, "gender": "male"}
# dict1["name"] = "lhc"
# dict1["age"] = 18
# dict1["gender"] = "female"
# print(dict1)

#determine if a key exists in a dictionary
# dict1 = {"name": "xzh", "age": 18, "gender": "male"}
# print("name" in dict1)
# can not determine by value
# print("xzh" in dict1)

#get the length of a dictionary
# print(len(dict1))

dict1 = {"swk":"六小龄童","bj":"马德华","shs":"闫怀礼","ts":"迟重瑞"}
#Iterate over all keys in a dictionary
# keys = dict1.keys()
# print(keys)
# for key in keys:
#     print(key)

#Iterate all values in a dictionary
# values = dict1.values();
# print(values)
# for v in values:
#     print(v)

#Iterate over key-value pairs simultaneously --Method1
# keys = dict1.keys()
# for k in keys:
#     print(f"{k}------{dict1[k]}")

#Iterate over key-value pairs simultaneously --Method2
# items = dict1.items()
# print(items)
# print(type(items))
# for item in items:
    # print(item)

# Delete elements from a dictionary
# del dict1["swk"]
#Clear a dictionary
# dict1.clear()
# print(dict1)

#Obtain the value corresponding to the key and delete key-value pair at the same time; a default value can be set
# print(dict1.pop("bj"))
# print(dict1)

#Retrieve the last inserted key-value pair from the dictionary; if the dictionary is empty,an error will be raised
# print(dict1.popitem())
# print(dict1)

#Update the key-value pairs from dict2 to dict1
dict2 = {"nz": "哪吒"}
# dict1.update(dict2)
# print(dict1)

# Get the value corresponding to the key in the dictionary,
# and a default value can be set.If the key does not exist in the dictionary,
# the key will be added and its value will be set to the default value
# dict2.setdefault("tslj", "太上老君")
# print(dict2)

#Create a new dictionary using the elements in the sequence seq as the dictionary's keys,
# and a default value foe the values can be set.
dict3 = dict2.fromkeys(range(5), dict2["nz"])
print(dict3)