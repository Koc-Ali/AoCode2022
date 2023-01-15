import os

# file handling
fileDir = os.path.dirname(os.path.realpath('__file__'))

#For accessing the file in the same folder
filename = "2022_advent_5.input.txt"
path_to_file = fileDir + '/' + filename

file = open(os.path.expanduser(path_to_file))

# problem solution

stack_header = ['', '', '', '', '', '', '', '', '']
header_index = 0
stack_1 = []
stack_2 = []
stack_3 = []
stack_4 = []
stack_5 = []
stack_6 = []
stack_7 = []
stack_8 = []
stack_9 = []
stacks = [stack_1, stack_2, stack_3, stack_4, stack_5, stack_6, stack_7, stack_8, stack_9]
header_finished = False

def move_crates(source, target, amount):
    temp_stack = []

    # move required crates to temp stack
    for step in range(amount):
        crate_to_be_moved = source.pop()    # get the top element from source
        temp_stack.append(crate_to_be_moved)    # add element on source as top element

    for step in range(amount):
        crate_to_be_moved = temp_stack.pop()    # get the top element from source
        target.append(crate_to_be_moved)    # add element on source as top element


def move_crates_1 (source, target, amount):
    for step in range(amount):
        crate_to_be_moved = source.pop()  # get the top element from source
        target.append(crate_to_be_moved)  # add element on source as top element


def print_stack():
    print('stack 1 = ', stacks[0])
    print('stack 2 = ', stacks[1])
    print('stack 3 = ', stacks[2])
    print('stack 4 = ', stacks[3])
    print('stack 5 = ', stacks[4])
    print('stack 6 = ', stacks[5])
    print('stack 7 = ', stacks[6])
    print('stack 8 = ', stacks[7])
    print('stack 9 = ', stacks[8])

for line in file:
    #fields = line.strip().split(',')
    fields = line.strip().split(' ')
  #  oneline = line.strip()

    print(fields)
    if fields[0] != 'move' and fields[0] != '':
        if line[1] != ' ':
            stacks[0].append(line[1])
        if line[5] != ' ':
            stacks[1].append(line[5])
        if line[9] != ' ':
            stacks[2].append(line[9])
        if line[13] != ' ':
            stacks[3].append(line[13])
        if line[17] != ' ':
            stacks[4].append(line[17])
        if line[21] != ' ':
            stacks[5].append(line[21])
        if line[25] != ' ':
            stacks[6].append(line[25])
        if line[29] != ' ':
            stacks[7].append(line[29])
        if line[33] != ' ':
            stacks[8].append(line[33])
    if fields[0] == 'move':
        if header_finished == False:
            header_finished = True
            stacks[0].reverse()
            stacks[1].reverse()
            stacks[2].reverse()
            stacks[3].reverse()
            stacks[4].reverse()
            stacks[5].reverse()
            stacks[6].reverse()
            stacks[7].reverse()
            stacks[8].reverse()
        amount_of_crate = fields[1]
        source_stack = fields[3]
        target_stack = fields[5]


        print('steps = ', amount_of_crate, 'source stack =', source_stack, 'target stack =', target_stack)
        print_stack()
        move_crates(stacks[int(source_stack)-1], stacks[int(target_stack)-1], int(amount_of_crate))
        print('--- moved ones ---')
        print_stack()


    # print_stack()



print('---- resultat stack ----')
print_stack()
resultet_string = []
lang_s = len(stacks[0])
print('stacks_länge = ', lang_s)

for i in range(len(stacks)):
    last_element = len(stacks[i])-1
    resultet_string.append(stacks[i][last_element])
print('resultet string =', resultet_string)
resultet_string = ''.join(resultet_string)
print('resultet string =', resultet_string)







