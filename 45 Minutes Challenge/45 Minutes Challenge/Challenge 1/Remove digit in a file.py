output = ''
count = 0

source = input("Source file name: ")
target = input("Target file name: ")

with open(source) as f:
    for line in f:
        if line[0].isdigit():
            output += line[1:]
            count += 1
        else:
            output += line

f = open(target, 'w')
f.write(output)
