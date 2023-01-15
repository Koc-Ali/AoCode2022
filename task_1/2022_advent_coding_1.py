import os


path_to_file = "~/901_src/PycharmProjects/AoCode2022/2022_advent_1.input.txt"
file = open(os.path.expanduser(path_to_file))
elf_list = []
sum = 0

#for line in file:
#    fields = line.strip().split()
#    #print(fields[0], fields[1], fields[2], fields[3])
#    print(fields[0])


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





