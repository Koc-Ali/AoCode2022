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
    def __init__(self):
        self.x_reg_stream = [x_reg_status]

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


myXStream = CRT()

myXStream.x_reg_stream[0]['cycle'] = 0
myXStream.x_reg_stream[0]['value'] = 1

for line in file:
    fields = line.strip().split()
    command = fields[0]
    command_value = fields[1] if command == 'addx' else 0

    myXStream.exec_command(command, command_value)

print('total signal strenghts = ', myXStream.calc_signal_strengths())

