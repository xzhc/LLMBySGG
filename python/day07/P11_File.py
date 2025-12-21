"""
This case demonstrates file read and write operations
"""

#Open the file(establish a channel between the program and the file)
f = open('test.txt', 'w')

#Write  data to a file
f.write('hello world \n')
f.write('nihao python \n')

#Close the established channel with the file
f.close()

#Read data from a file
#Open the file(establish a channel between the program and the file)
f = open('test.txt', 'r')
#Read data from the file:read() read all data by default
# print(f.read())
#Read data of the specified byte size from the file
# print(f.read(5))
# print(f.read(8))

#Read one line of data
# print(f.readline())
# print(f.readline())


#Read all line
print(f.readlines())

#Close the established channel with the file
f.close()