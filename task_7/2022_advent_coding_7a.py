import os

fileDir = os.path.dirname(os.path.realpath('__file__'))
print(fileDir)

#For accessing the file in the same folder
filename = "2022_advent_7.input.txt"
path_to_file = fileDir + '/' + filename
print(path_to_file)

file = open(os.path.expanduser(path_to_file))


dir_list = [(0, 'none')]

class dir_item:
   # def __init__(self, n_name, n_dir, n_size, n_main_dir):
    def __init__(self, n_name, n_dir, n_size, n_main_dir=None):
        self.name = n_name
        self.dir = n_dir
        self.size = n_size
        self.main_dir = n_main_dir
        self.file_items = []
        self.dir_items = []

    def get_main_dir(self):
        return self.main_dir
    def get_dir(self, dir_name):
        for X in self.dir_items:
            if X.name == dir_name:
                return X
    def get_upper_folder(self):
        return self.main_dir

    def add_file_item(self, n_file_item):
        self.file_items.append(n_file_item)

    def add_dir_item(self, n_dir_item):
        self.dir_items.append(n_dir_item)

    def calc_file_size_in_dir(self):
        if self.dir != True:            # item is a file
            return self.size
        if self.dir == True:            # item is a dir
            size_files_in_dir = 0
            size_files_in_sub_dir = 0
            for X in self.file_items:   # size of file in current directory
                size_files_in_dir += int(X.calc_file_size_in_dir())
            for Y in self.dir_items:     # size of files in sub directories
                size_files_in_sub_dir += int(Y.calc_file_size_in_dir())
            dir_total_size = size_files_in_sub_dir + size_files_in_dir
            current_dir = (dir_total_size, self.name)
            dir_list.append(current_dir)
            return dir_total_size
#    def __repr__(self):
#       rep = 'dir: name = ' + self.name + 'dir =' + 'size =' + str(self.size)
#       return rep




def read_file_info(file_info):
    ls_results = False
    col_file_ls_results = []
    col_dir_ls_results = []

    # main_dir = dir_item('/', True, 0, '')
    main_dir = dir_item('/', True, 0)
    current_dir = ''

    for line in file:
        fields = line.strip().split(' ')

        print(fields)

        if fields[0] == '$' and fields[1] == 'cd' and fields[2] == '/':
            current_dir = file_info
        elif fields[0] == '$' and fields[1] == 'cd' and fields[2] == '..':
            current_dir = current_dir.get_upper_folder()  # einen Ordner hoch gehen
        elif fields[0] == '$' and fields[1] == 'cd':
            current_dir = current_dir.get_dir(fields[2]) # in den Unterordner gehen
        if fields[0] == '$' and fields[1] == 'ls':
            # nothing to do!
            print('ls command: ', fields)
        if fields[0] == 'dir':
            print('dir ls: ', fields)
            new_dir = dir_item(fields[1], True, 0, current_dir)
            current_dir.add_dir_item(new_dir)
        if fields[0].isdigit() == True:
            print('file ls: ', fields)
            new_file = dir_item(fields[1], False, fields[0], current_dir)
            current_dir.add_file_item(new_file)

    return file_info

def print_sub_dir_list(file_info):
    counter = 0
    print('START dir list: ', file_info.name)
    for X in file_info.dir_items:
        print_dir_info(X)
    print('END dir list: ')

    print('START file list: ', file_info.name)
    for X in file_info.file_items:
        print_file_info(X)
    print('END file list: ')

    print('START SUB dir list: ')
    for X in file_info.dir_items:
        counter += 1
        print (' level = ', counter)
        print_sub_dir_list(X)
    print('END SUB dir list: ')
    counter = 0

    dir_size = file_info.calc_file_size_in_dir()
    print('dir name =', file_info.name, 'dir size =', dir_size)
    if dir_size <= 100000:
        print('below 100k dir name =', file_info.name, 'dir size =', dir_size)

def print_sub_file_list(file_info):
    print('START file list: ', file_info.name)
    for X in file_info.file_items:
        print_file_info(X)
    print('END file list: ')

def print_dir_info(dir_info):
    print('DIR = ', dir_info.name, ' MAIN DIR = ', dir_info.main_dir.name)

def print_file_info(file_info):
    print('item info: MAIN DIR = ', file_info.main_dir.name, ' FILE = ', file_info.name, ' FILE SIZE = ', file_info.size)

def find_smalest_dir(file_info, min_size):
    found_dir_name = ''
    found_dir_size = 70000000
    dirs = file_info.dir_items
    for item in dirs:
        size = find_smalest_dir(item, min_size)
        if size >= min_size:
            if found_dir_size > size:
                found_dir_size = size
            else:
                found_dir_size = size
    return(found_dir_size)

def find_min_dir_size(dir_list_result, min_size):
    def takeSecond(elem):
        return elem[0]

    # sort list with key
    dir_list_result.sort(key=takeSecond)
    print(dir_list_result)

    for i in dir_list_result:
        # print(i, ' ', i[0])
        if int(i[0]) > min_size:
            print(i[0])
            return int(i[0])

file_info = dir_item('/', True, 0)
file_info = read_file_info(file_info)
print_sub_file_list(file_info)
print_sub_dir_list(file_info)

total_size = file_info.calc_file_size_in_dir()
print(total_size)
required_free_space = 30000000-(70000000-total_size)
print(required_free_space)
smalest_size_calculated = find_smalest_dir(file_info, required_free_space)
print(smalest_size_calculated)
find_min_dir_size(dir_list, required_free_space)
#print(smalest_size_calculated)
#print(dir_list)










