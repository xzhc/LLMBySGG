"""
This case demonstrates the with keyword(context manager)
"""

# try:
#     file = open('test.txt', 'w')
#     file.write(a)
#     file.close()
# finally:
#     print('Is file closed?', file.closed)

# try:
#     file = open('test.txt', 'w')
#     try:
#         file.write(a)
#     finally:
#         file.close()
# finally:
#     print('Is file closed?', file.closed)

# try:
#     with open('test.txt', 'w') as file:
#         file.write("hello world")
# finally:
#     print('Is file closed?', file.closed)