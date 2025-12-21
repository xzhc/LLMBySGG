"""
This case demonstrates an introduction to exceptions h
"""
try:
    result = 3 / 0
    print(result)
except:
    print("An error occurred during division.")

print("Program continues...")