import os

# file handling
fileDir = os.path.dirname(os.path.realpath('__file__'))

#For accessing the file in the same folder
filename = "2022_advent_9.input.txt"
path_to_file = fileDir + '/' + filename



file = open(os.path.expanduser(path_to_file))

# problem solution

class RopeMove:
    Head = None
    Tail = None
    Start = None

    def __init__(self, Right=None, Left=None, Up=None, Down=None):
        self.Tail_Marked = False
        self.Right = None
        self.Left = None
        self.Up = None
        self.Down = None

        if Right is not None:
            self.Right = Right
        if Left is not None:
            self.Left = Left
        if Up is not None:
            self.Up = Up
        if Down is not None:
            self.Down = Down

    def move_tail_right_single(self):
        print(self)

        if (self.Head == self.Tail.Right):
            self.Tail_Marked = True
            return

        if (self.Tail.Right is not None) and (self.Head == self.Tail.Right.Right):
            self.Tail = self.Tail.Right
        elif (self.Tail.Up.Right is not None) and (self.Head == self.Tail.Up.Right.Right):
            self.Tail = self.Tail.Up.Right
        elif (self.Tail.Right.Up is not None) and (self.Head == self.Tail.Right.Up.Up):
            self.Tail = self.Tail.Right.Up
        elif (self.Tail.Down is not None) and (self.Head == cls.Tail.Down.Down):
            self.Tail = self.Tail.Down
        self.Tail.Tail_Marked = True

    def move_head_right_single(self):
        # if right element does not exists create RopMove object
        if self.Right is None:
            self.Right = RopeMove()
        # move head & tail
        self.Head = self.Right
        self.move_tail_right_single()

    def move_head_right_multiple(self, steps):
        for i in range(steps):
            self.move_head_right_single()

    def print_movement_matrix(self):
        print('self: ', 'ojb id', self, 'Head =', self.Head, 'Tail =', self.Tail, 'Start =', self.Start, 'tail mark = ', self.Tail_Marked)
        # print all right elements

        print('--- right elements ---')
        if (self.Right is not None):
            self.Right.print_movement_matrix()
        # print all left elements
        print('--- left elements ---')
        if (self.Left is not None):
            self.Left.print_movement_matrix()
        # print all upper elements
        print('--- up elements ---')
        if (self.Up is not None):
            self.Up.print_movement_matrix()
        # print all down elements
        print('--- down elements ---')
        if (self.Down is not None):
            self.Down.print_movement_matrix()



myRope = RopeMove()
myRope.Head = myRope
myRope.Tail = myRope
myRope.Start = myRope
myRope.move_head_right_single()
print(myRope.Head, myRope.Tail)
myRope.print_movement_matrix()
myRope.move_head_right_multiple(4)
print(myRope.Head, myRope.Tail)
myRope.print_movement_matrix()



