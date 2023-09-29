count = 0

source = input("Source file name: ")

with open(source) as f:
    for line in f:
        if " for" in line:
            count += 1

print("For is in the file", count, "times")
