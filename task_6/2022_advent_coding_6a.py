import os

# file handling
fileDir = os.path.dirname(os.path.realpath('__file__'))

#For accessing the file in the same folder
filename = "2022_advent_6.input.txt"
path_to_file = fileDir + '/' + filename

file = open(os.path.expanduser(path_to_file))

# problem solution

data_window_size = 14 # instead of 4

def isUniqueChars(string):
  uchars = []
  for c in string:
    if c in uchars:
      return False
    else:
      uchars.append(c)
  return True

stream_position = 0

for line in file:
    #fields = line.strip().split(',')
    # data_ = line.strip()

    print(line)
    length_data_stream = len(line)
    print(length_data_stream)
    req_iteration = length_data_stream - data_window_size

    for i in range(req_iteration+1):
        data_window = line[i:i+data_window_size]
        if isUniqueChars(data_window) == True:
            print('code detected at position =', i+data_window_size, 'code =', data_window)
            break


