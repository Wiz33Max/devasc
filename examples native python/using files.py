import sys

current_dir = sys.path[0]
filePath = (current_dir+"\\sample.txt")

with open(filePath, "r") as f:
    print(f.read())