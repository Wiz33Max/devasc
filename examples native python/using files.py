items = []

try:
    with open("C:/py_files/sample.txt", "r") as f:
        items.append(f.read())
except Exception as e:
    print("Error:", e)

print ("_"*50+"\nFIGHTING GAMES ARE:\n")
print(items[0])

fgx = input("\nAdd Fighting game or C to cancel : ")

if fgx!= "C":
    try:
        with open("C:/py_files/sample.txt", "a+") as f:
            f.write(fgx)
    except Exception as e:
        print("Error:", e)