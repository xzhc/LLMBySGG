"""
This case demonstrates viewing subdirectories and files under a dictionary
"""

import os
# print(os.getcwd())

for root,dir, files in os.walk(os.getcwd()):
    print("Current path:", root)
    print("Directories:", dir)
    print("Files:", files)
    print()