import os

# file handling
fileDir = os.path.dirname(os.path.realpath('__file__'))

#For accessing the file in the same folder
filename = "2022_advent_9.input.txt"
# filename = "2022_advent_9.input.sample.txt"
path_to_file = fileDir + '/' + filename

file = open(os.path.expanduser(path_to_file))

# problem solution

position = {
    'occupancy': 'free',
    'tail_mark': False
}


line_pos = [position]
class MoveMatrix():
    head_pos_x = head_pos_y = 0
    max_tails = 9
    position_value = int
    position_value = 0
    def __init__(self):
        self.matrix = [line_pos]
        self.tails = []
        for i in range(self.max_tails):
            self.tails.append({'x': self.position_value, 'y': self.position_value})
#        self.tails[0]['x'] = 1
#        self.tails[1]['y'] = 2

    def move_head_one_step_right(self):
        max_column = len(self.matrix[0])
        if self.head_pos_x + 1 == max_column:
            # extend movement matrix, i.e. include one column
            for line in self.matrix:
                line.append({'occupancy': 'free', 'tail_mark': False})
        # move head one pos to right
        self.head_pos_x += 1
        # move tail accordingly
        self.move_tail()

    def move_head_multiple_steps_right(self, steps):
        for i in range(steps):
            self.move_head_one_step_right()

    def move_head_one_step_left(self):
        if self.head_pos_x == 0:
            # extend movement matrix, i.e. include one column from left
            for line in self.matrix:
                line.insert(0, {'occupancy': 'free', 'tail_mark': False})
            # adjust tail position to extend matrix
            for i in range(self.max_tails):
                self.tails[i]['x'] += 1
        else:
            # move head one pos to right
            self.head_pos_x -= 1
        # move tail accordingly
        self.move_tail()

    def move_head_multiple_steps_left(self, steps):
        for i in range(steps):
            self.move_head_one_step_left()
    def move_head_multiple_steps_up(self, steps):
        for i in range(steps):
            self.move_head_one_step_up()

    def move_head_one_step_up(self):
        if self.head_pos_y == len(self.matrix)-1:
            # extend movement matrix, i.e. include one row
            new_line = [{'occupancy': 'free', 'tail_mark': False}]
            for i in range(len(self.matrix[0])-1):
                new_line.append({'occupancy': 'free', 'tail_mark': False})
            self.matrix.append(new_line)
        self.head_pos_y += 1
        # move tail accordingly
        self.move_tail()

    def move_head_multiple_steps_down(self, steps):
        for i in range(steps):
            self.move_head_one_step_down()


    def move_head_one_step_down(self):
        if self.head_pos_y == 0:
            # extend movement matrix, i.e. include one row
            new_line = [{'occupancy': 'free', 'tail_mark': False}]
            for i in range(len(self.matrix[0])-1):
                new_line.insert(0, {'occupancy': 'free', 'tail_mark': False})
            self.matrix.insert(self.head_pos_y, new_line)
            # adjust tail_pos_pointer
            for i in range(self.max_tails):
                self.tails[i]['y'] += 1

        # move head one pos to down
        else:
            self.head_pos_y -= 1
        # move tail accordingly
        self.move_tail()

    def move_tail(self):
        # self.print_move_matrix()
        # case: same horizontal line
        if self.head_pos_y == self.tails[0]['y']:
            if self.tails[0]['x'] + 2 == self.head_pos_x:
                self.tails[0]['x'] += 1
            elif self.tails[0]['x'] - 2 == self.head_pos_x:
                self.tails[0]['x'] -= 1
        # case: same vertical line
        if self.head_pos_x == self.tails[0]['x']:
            if self.tails[0]['y'] + 2 == self.head_pos_y:
                self.tails[0]['y'] += 1
            elif self.tails[0]['y'] - 2 == self.head_pos_y:
                self.tails[0]['y'] -= 1

        # case: vertical shift two line
        if (self.tails[0]['x'] + 1 == self.head_pos_x) and (self.tails[0]['y'] + 2 == self.head_pos_y):
            self.tails[0]['x'] += 1
            self.tails[0]['y'] += 1
        elif (self.tails[0]['x'] - 1 == self.head_pos_x) and (self.tails[0]['y'] + 2 == self.head_pos_y):
            self.tails[0]['x'] -= 1
            self.tails[0]['y'] += 1
        elif (self.tails[0]['x'] + 1 == self.head_pos_x) and (self.tails[0]['y'] - 2 == self.head_pos_y):
            self.tails[0]['x'] += 1
            self.tails[0]['y'] -= 1
        elif (self.tails[0]['x'] - 1 == self.head_pos_x) and (self.tails[0]['y'] - 2 == self.head_pos_y):
            self.tails[0]['x'] -= 1
            self.tails[0]['y'] -= 1

        # case: vertical shift two lines
        if (self.tails[0]['x'] + 2 == self.head_pos_x) and (self.tails[0]['y'] + 1 == self.head_pos_y):
            self.tails[0]['x'] += 1
            self.tails[0]['y'] += 1
        elif (self.tails[0]['x'] - 2 == self.head_pos_x) and (self.tails[0]['y'] + 1 == self.head_pos_y):
            self.tails[0]['x'] -= 1
            self.tails[0]['y'] += 1
        elif (self.tails[0]['x'] + 2 == self.head_pos_x) and (self.tails[0]['y'] - 1 == self.head_pos_y):
            self.tails[0]['x'] += 1
            self.tails[0]['y'] -= 1
        elif (self.tails[0]['x'] - 2 == self.head_pos_x) and (self.tails[0]['y'] - 1 == self.head_pos_y):
            self.tails[0]['x'] -= 1
            self.tails[0]['y'] -= 1

#        print('tail 0: ', self.tails[0]['y'], ' ', self.tails[0]['x'])
        self.matrix[self.tails[0]['y']][self.tails[0]['x']]['tail_mark'] = True

    def print_move_matrix(self):
        # print lines in reverse order
        print_lines = ['']
        for line_index, line in enumerate(self.matrix, start=0):
            str_line = ''
            for pos_index, pos in enumerate(line, start=0):
                if line_index == self.tails[0]['y'] and pos_index == self.tails[0]['x']:
                    str_line += 'T'
                elif line_index == self.head_pos_y and pos_index == self.head_pos_x:
                    str_line += 'H'
                else:
                    str_line += '#' if pos['tail_mark'] else '.'
            print_lines.insert(0, str_line)
        # mark start position with S
        print_lines[len(print_lines)-2] = print_lines[len(print_lines)-2][:0] + 'S' + print_lines[len(print_lines)-2][0 + 1:]
        # print in reverse order
        for line in print_lines:
            print(line)

    def calc_marker(self):
        total_marker = 0
        for line_index, line in enumerate(self.matrix, start=0):
            for pos_index, pos in enumerate(line, start=0):
                if pos['tail_mark']:
                    total_marker += 1
        return(total_marker)


myMoveMatrix = MoveMatrix()
# Set StartingPosition
myMoveMatrix.matrix[0][0]['tail_mark'] = True

for line in file:
    fields = line.strip().split()
    move_dir = fields[0]
    move_steps = fields[1]

    # myMoveMatrix.print_move_matrix()
    print(fields)

    if move_dir == 'R':
        myMoveMatrix.move_head_multiple_steps_right(int(move_steps))
    if move_dir == 'L':
        myMoveMatrix.move_head_multiple_steps_left(int(move_steps))
    if move_dir == 'U':
        myMoveMatrix.move_head_multiple_steps_up(int(move_steps))
    if move_dir == 'D':
        myMoveMatrix.move_head_multiple_steps_down(int(move_steps))

    # myMoveMatrix.print_move_matrix()

print('total marked tiles = ', myMoveMatrix.calc_marker())







