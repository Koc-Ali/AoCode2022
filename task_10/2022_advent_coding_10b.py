import os

# file handling
fileDir = os.path.dirname(os.path.realpath('__file__'))

# For accessing the file in the same folder
filename = "2022_advent_10.input.txt"
# filename = "2022_advent_10.input.sample.txt"
# filename = "2022_advent_10.input.sample2.txt"

path_to_file = fileDir + '/' + filename

file = open(os.path.expanduser(path_to_file))

# problem solution

x_reg_status = {
    'cycle': 0,
    'value': 0
}


# x_reg_stream = [x_reg_status]

class CRT():
    current_cycle = 0
    current_sprite_pos = 1
    max_row = 40
    max_cycle = 240

    def __init__(self):
        self.x_reg_stream = [x_reg_status]
        self.CRT_drawing = []

    def exec_command(self, command, command_value):
        current_cycle = len(self.x_reg_stream) - 1
        current_value = self.x_reg_stream[current_cycle]['value']
        if command == 'noop':
            # extend x_reg_stream
            self.x_reg_stream.append({'cycle': current_cycle + 1, 'value': current_value})
        elif command == 'addx':
            # extend x_reg_stream
            self.x_reg_stream.append({'cycle': current_cycle + 1, 'value': current_value})
            new_value = current_value + int(command_value)
            self.x_reg_stream.append({'cycle': current_cycle + 2, 'value': new_value})
            # value END of cycle! Value of current cycle is value of previous cycle

    def x_reg_value_in_cycle(self, cycleNr):
        stream_len = len(self.x_reg_stream)
        assert cycleNr > 0
        assert cycleNr <= stream_len

        return self.x_reg_stream[cycleNr - 1]['value']

    def calc_signal_strengths(self):
        total_signal_strenghts = 0

        for cycleNr in (20, 60, 100, 140, 180, 220):
            total_signal_strenghts += cycleNr * self.x_reg_value_in_cycle(cycleNr)
            print(cycleNr, total_signal_strenghts)
        return (total_signal_strenghts)

    def draw_CRT_picture(self):
        # for each clock cycle, check whether pixel is visible or not
        for cycle in range(1, int(self.max_cycle)+1):
            # if in current cycle x_register_value is part of sprite (current_pos, +1, +2 ) ==> visible
            # check whether to move to new line
            line_cycle = cycle % self.max_row
            if line_cycle in (self.current_sprite_pos, self.current_sprite_pos+1, self.current_sprite_pos+2):
                drawing_item = '#'      # visible
            else:
                drawing_item = '.'      # invisble
            self.CRT_drawing.append(drawing_item)
            if cycle < self.max_cycle:
                self.current_sprite_pos = self.x_reg_value_in_cycle(cycle+1)
                # chef if sprite_pos is -1; this leads to error at the end of 40 cycles
    def print_CRT_picture(self):
        max_column = int(self.max_cycle / self.max_row)

        for column in range(max_column):
            print(self.CRT_drawing[column*self.max_row:(column+1)*self.max_row])

myXStream = CRT()

myXStream.x_reg_stream[0]['cycle'] = 0
myXStream.x_reg_stream[0]['value'] = 1

for line in file:
    fields = line.strip().split()
    command = fields[0]
    command_value = fields[1] if command == 'addx' else 0

    myXStream.exec_command(command, command_value)

print('total signal strenghts = ', myXStream.calc_signal_strengths())
myXStream.draw_CRT_picture()
myXStream.print_CRT_picture()
