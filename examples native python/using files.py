import sys
import os
currentDir = sys.path[0]

files = os.listdir(currentDir)

for file in files:
    print(file)
    if file.endswith(".txt"):
        with open(file, "r") as f:
            print(f.read())
print (currentDir)

try:
    with open("sample.txt", "r") as f:
        print(f.read())

except Exception as e:
    print("Error:", e)