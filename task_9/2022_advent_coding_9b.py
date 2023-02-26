import os

# file handling
fileDir = os.path.dirname(os.path.realpath('__file__'))

#For accessing the file in the same folder
filename = "2022_advent_9.input.txt"
# filename = "2022_advent_10.input.sample.txt"
# filename = "2022_advent_10.input.sample2.txt"
path_to_file = fileDir + '/' + filename

file = open(os.path.expanduser(path_to_file))

# problem solution
position_value = int
position_value = 0

position = {
    'tm': position_value
}

line_pos = [position]
class MoveMatrix():
    head_pos_x = head_pos_y = 0
    max_tails = 9
    tail_marker = 9

    def __init__(self):
        self.matrix = [line_pos]
        self.tails = []
        for i in range(self.max_tails):
            self.tails.append({'x': position_value, 'y': position_value})

    def move_head_one_step_right(self):
        max_column = len(self.matrix[0])
        if self.head_pos_x + 1 == max_column:
            # extend movement matrix, i.e. include one column
            for line in self.matrix:
                line.append({'tm': position_value})
        # move head one pos to right
        self.head_pos_x += 1
        # move tail accordingly
        self.move_tail()

    def move_head_multiple_steps_right(self, steps):
        for i in range(steps):
            self.move_head_one_step_right()
#        self.matrix[self.head_pos_y][self.head_pos_x]['tm'] = self.tail_marker
    def move_head_one_step_left(self):
        if self.head_pos_x == 0:
            # extend movement matrix, i.e. include one column from left
            for line in self.matrix:
                line.insert(0, {'tm': position_value})
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
            new_line = [{'tm': position_value}]
            for i in range(len(self.matrix[0])-1):
                new_line.append({'tm': position_value})
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
            new_line = [{'tm': position_value}]
            for i in range(len(self.matrix[0])-1):
                new_line.insert(0, {'tm': position_value})
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
        # move tail 0 according to head
        self.move_tail_one_tail(self.head_pos_y, self.head_pos_x, 0)

        # move ather tails
        for i in range(self.max_tails-1):
            self.move_tail_one_tail(self.tails[i]['y'], self.tails[i]['x'], i+1)

    def move_tail_one_tail(self, y_pos_head, x_pos_head, tailnr):

        assert tailnr <= self.max_tails

        current_tail_x = self.tails[tailnr]['x']
        current_tail_y = self.tails[tailnr]['y']

        # case: same horizontal line
        if y_pos_head == current_tail_y:
            if self.tails[tailnr]['x'] + 2 == x_pos_head:
                self.tails[tailnr]['x'] += 1
            elif self.tails[tailnr]['x'] - 2 == x_pos_head:
                self.tails[tailnr]['x'] -= 1
        # case: same vertical line
        if x_pos_head == current_tail_x:
            if self.tails[tailnr]['y'] + 2 == y_pos_head:
                self.tails[tailnr]['y'] += 1
            elif self.tails[tailnr]['y'] - 2 == y_pos_head:
                self.tails[tailnr]['y'] -= 1

        # case: vertical shift two line
        if (self.tails[tailnr]['x'] + 1 == x_pos_head) and (self.tails[tailnr]['y'] + 2 == y_pos_head):
            self.tails[tailnr]['x'] += 1
            self.tails[tailnr]['y'] += 1
        elif (self.tails[tailnr]['x'] - 1 == x_pos_head) and (self.tails[tailnr]['y'] + 2 == y_pos_head):
            self.tails[tailnr]['x'] -= 1
            self.tails[tailnr]['y'] += 1
        elif (self.tails[tailnr]['x'] + 1 == x_pos_head) and (self.tails[tailnr]['y'] - 2 == y_pos_head):
            self.tails[tailnr]['x'] += 1
            self.tails[tailnr]['y'] -= 1
        elif (self.tails[tailnr]['x'] - 1 == x_pos_head) and (self.tails[tailnr]['y'] - 2 == y_pos_head):
            self.tails[tailnr]['x'] -= 1
            self.tails[tailnr]['y'] -= 1

        # case: vertical shift two lines
        if (self.tails[tailnr]['x'] + 2 == x_pos_head) and (self.tails[tailnr]['y'] + 1 == y_pos_head):
            self.tails[tailnr]['x'] += 1
            self.tails[tailnr]['y'] += 1
        elif (self.tails[tailnr]['x'] - 2 == x_pos_head) and (self.tails[tailnr]['y'] + 1 == y_pos_head):
            self.tails[tailnr]['x'] -= 1
            self.tails[tailnr]['y'] += 1
        elif (self.tails[tailnr]['x'] + 2 == x_pos_head) and (self.tails[tailnr]['y'] - 1 == y_pos_head):
            self.tails[tailnr]['x'] += 1
            self.tails[tailnr]['y'] -= 1
        elif (self.tails[tailnr]['x'] - 2 == x_pos_head) and (self.tails[tailnr]['y'] - 1 == y_pos_head):
            self.tails[tailnr]['x'] -= 1
            self.tails[tailnr]['y'] -= 1

        # case: diagonal movement
        if (self.tails[tailnr]['x'] + 2 == x_pos_head) and (self.tails[tailnr]['y'] + 2 == y_pos_head):
            self.tails[tailnr]['x'] += 1
            self.tails[tailnr]['y'] += 1
        elif (self.tails[tailnr]['x'] - 2 == x_pos_head) and (self.tails[tailnr]['y'] + 2 == y_pos_head):
            self.tails[tailnr]['x'] -= 1
            self.tails[tailnr]['y'] += 1
        elif (self.tails[tailnr]['x'] + 2 == x_pos_head) and (self.tails[tailnr]['y'] - 2 == y_pos_head):
            self.tails[tailnr]['x'] += 1
            self.tails[tailnr]['y'] -= 1
        elif (self.tails[tailnr]['x'] - 2 == x_pos_head) and (self.tails[tailnr]['y'] - 2 == y_pos_head):
            self.tails[tailnr]['x'] -= 1
            self.tails[tailnr]['y'] -= 1

        # mark tail visited
        if tailnr+1 == self.tail_marker:
            self.matrix[self.tails[tailnr]['y']][self.tails[tailnr]['x']]['tm'] = self.tail_marker
        assert tailnr <= self.max_tails

    def print_move_matrix(self):
        print_matrix = []
        y_max = len(self.matrix)
        x_max = len(self.matrix[0])
        for j in range(y_max):
            print_line = []
            for i in range(x_max):
                print_line.append(0)
            print_matrix.append(print_line)
        print_matrix[self.head_pos_y][self.head_pos_x] = 'H'
        for index, tail in enumerate(self.tails, start=0):
            if print_matrix[tail['y']][tail['x']] == 0:
                print_matrix[tail['y']][tail['x']] = index+1
        reverse_print = []
        for line in print_matrix:
            reverse_print.insert(0, line)
        for line in reverse_print:
            print(line)
        return

    def calc_marker(self):
        total_marker = 0
        for line_index, line in enumerate(self.matrix, start=0):
            for pos_index, pos in enumerate(line, start=0):
                if pos['tm'] == self.tail_marker:
                    total_marker += 1
        return(total_marker)


myMoveMatrix = MoveMatrix()
# Set StartingPosition
myMoveMatrix.matrix[0][0]['tm'] = myMoveMatrix.tail_marker  # Start-position

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

    myMoveMatrix.print_move_matrix()

print('total marked tiles = ', myMoveMatrix.calc_marker())







