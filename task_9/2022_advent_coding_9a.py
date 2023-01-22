import os

# file handling
fileDir = os.path.dirname(os.path.realpath('__file__'))

#For accessing the file in the same folder
filename = "2022_advent_9.input.txt"
path_to_file = fileDir + '/' + filename



file = open(os.path.expanduser(path_to_file))

# problem solution

position = {
    'occupancy': 'free',
    'tail_mark': False
}

new_position = {
    'occupancy': 'free',
    'tail_mark': False
}

line_pos = [position]
class MoveMatrix():
    head_pos_x = head_pos_y = 0
    tail_pos_x = tail_pos_y = 0
    def __init__(self):
        self.matrix = [line_pos]
        print(self)

    def move_head_one_step_right(self):
        max_column = len(self.matrix[0])
        if self.head_pos_x + 1 == max_column:
            # extend movement matrix, i.e. include one column
            for line in self.matrix:
                line.append(new_position)
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
                line.insert(0, new_position)
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
        if self.head_pos_y == 0:
            # extend movement matrix, i.e. include one row
            new_line = [new_position]
            for i in range(len(self.matrix[0])-1):
                new_line.append(new_position)
            self.matrix.insert(self.head_pos_y, new_line)
        # move head one pos to right
        else:
            self.head_pos_y -= 1
        # move tail accordingly
        self.move_tail()

    def move_head_multiple_steps_down(self, steps):
        for i in range(steps):
            self.move_head_one_step_down()


    def move_head_one_step_down(self):
        max_row = len(self.matrix)
        if self.head_pos_y + 1 == max_row:
            # extend movement matrix, i.e. include one row
            new_line = [new_position]
            for i in range(len(self.matrix[0])-1):
                new_line.append(new_position)
            self.matrix.append(new_line)
        # move head one pos to down
        self.head_pos_y += 1
        # move tail accordingly
        self.move_tail()

    def move_tail(self):
        print('empty move tail')

    def print_move_matrix(self):
        for line in self.matrix:
            str_line = ''
            for pos in line:
                str_line += 'M' if pos['tail_mark'] == True else '.'
            print(str_line)

myMoveMatrix = MoveMatrix()
# Set StartingPosition
myMoveMatrix.matrix[0][0]['tail_mark'] = True

myMoveMatrix.move_head_multiple_steps_right(2)
print(myMoveMatrix)


myMoveMatrix.move_head_multiple_steps_left(5)
print(myMoveMatrix)

myMoveMatrix.move_head_multiple_steps_up(3)
print(myMoveMatrix)

myMoveMatrix.move_head_multiple_steps_down(4)
print(myMoveMatrix)

myMoveMatrix.print_move_matrix()










