import os

# file handling
fileDir = os.path.dirname(os.path.realpath('__file__'))

#For accessing the file in the same folder
filename = "2022_advent_1.input.txt"
path_to_file = fileDir + '/' + filename

file = open(os.path.expanduser(path_to_file))

# problem solution

elf_list = []
sum = 0

for line in file:
    line = line.strip() #preprocess line
    #print(line)
    if line == '':
        elf_list.append(sum)
        print(sum)
        sum = 0
    else:
        print(line)
        sum = sum + int(line)
        print(sum)

print(elf_list)
max_cal = max(elf_list)
print(max_cal)
max_elf = elf_list.index(max(elf_list))
print(max_elf-1)


# Second part of task

print(('--- sorted list ---'))
elf_list.sort(reverse=True)
print(elf_list)
print('--- calories three Elves carrying most Calories = ', elf_list[0]+elf_list[1]+elf_list[2])

#    print(line)





