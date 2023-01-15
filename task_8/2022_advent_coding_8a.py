import os

# file handling
fileDir = os.path.dirname(os.path.realpath('__file__'))

#For accessing the file in the same folder
filename = "2022_advent_8.input.txt"
# filename = "2022_advent_8.small.input.txt" # for testing

path_to_file = fileDir + '/' + filename

file = open(os.path.expanduser(path_to_file))

# problem solution
tree_colums = []
trees = [tree_colums]
forest = list()

# Transpose from Stackoverflow
def matrixTranspose(matrix):
    if not matrix: return []
    return [[row[i] for row in matrix] for i in range(len(matrix[0]))]

# Transpose defined by me
def matrixTranspose2(matrix):
    new_matrix = []

    for i in range(len(matrix[0])):
        new_column = []
        for row in matrix:
            new_column += row[i]
        new_matrix += [new_column]

    return(new_matrix)

# init trees
def init_trees(trees):
    last_row = len(trees)
    last_column = len(trees[0])

    # first line is V
    for index, tree in enumerate(trees[0], start=0):
    #    print(index, tree)
        trees[0][index] = (tree[0], 'V')

    # all lines, excluding last line are N
    for line_index, line_tree in enumerate(trees[1:], start=1):
        for index, tree in enumerate(trees[line_index], start=0):
     #       print(line_index, index, tree)
            trees[line_index][index] = (tree[0], 'N')
            if index == 0 or index == (last_column-1):
                trees[line_index][index] = (tree[0], 'V')

    # set last line V
    for index, tree in enumerate(trees[last_row-1], start=0):
    #    print(index, tree)
        trees[last_row-1][index] = (tree[0], 'V')

    return(trees)


def mark_visible_trees(trees):
    last_row = len(trees)
    last_column = len(trees[0])

    # first line is and last lines are all visible!
    # start with line 1 until last-row - 1
    # skipp borders; start with borders

    # check rows from left
    # print('visible form left and right')
    for line_index, line_tree in enumerate(trees[1:], start=1):
        talest_tree_hight = int(trees[line_index][0][0])
        # print('boarder talest number =', talest_tree_hight)

        for index, tree in enumerate(trees[line_index], start=0):
            # print(line_index, index, tree)
            # print('tree =', tree)
            # print('tree - index  =', tree[0])
            # print('tree - index - value =', tree[index][0])
            if int(tree[0]) > talest_tree_hight:
                talest_tree_hight = int(tree[0])
                # print('talest number =', talest_tree_hight)
                trees[line_index][index] = (tree[0], 'V')
        # reverse items.
        line_tree.reverse()

        talest_tree_hight = int(trees[line_index][0][0])
        # print('boarder talest number =', talest_tree_hight)

        for index, tree in enumerate(trees[line_index], start=0):
            # print(line_index, index, tree)
            # print('tree =', tree)
            # print('tree - index  =', tree[0])
            # print('tree - index - value =', tree[index][0])
            if int(tree[0]) > talest_tree_hight:
                talest_tree_hight = int(tree[0])
                # print('talest number =', talest_tree_hight)
                trees[line_index][index] = (tree[0], 'V')
        # reverse items.
        line_tree.reverse()

    trans_trees = matrixTranspose(trees)
    trees = trans_trees
    # print('--- trans trees ---')
    # print(trans_trees)

    # check rows from left
    #print('visible form left and right')
    for line_index, line_tree in enumerate(trees[1:], start=1):
        talest_tree_hight = int(trees[line_index][0][0])
        # print('boarder talest number =', talest_tree_hight)

        for index, tree in enumerate(trees[line_index], start=0):
            # print(line_index, index, tree)
            # print('tree =', tree)
            # print('tree - index  =', tree[0])
            # print('tree - index - value =', tree[index][0])
            if int(tree[0]) > talest_tree_hight:
                talest_tree_hight = int(tree[0])
                # print('talest number =', talest_tree_hight)
                trees[line_index][index] = (tree[0], 'V')
        # reverse items.
        line_tree.reverse()

        talest_tree_hight = int(trees[line_index][0][0])
        # print('boarder talest number =', talest_tree_hight)

        for index, tree in enumerate(trees[line_index], start=0):
            # print(line_index, index, tree)
            # print('tree =', tree)
            # print('tree - index  =', tree[0])
            # print('tree - index - value =', tree[index][0])
            if int(tree[0]) > talest_tree_hight:
                talest_tree_hight = int(tree[0])
                # print('talest number =', talest_tree_hight)
                trees[line_index][index] = (tree[0], 'V')
        # reverse items.
        line_tree.reverse()

    trans_trees = matrixTranspose(trees)
    trees = trans_trees
    # print('--- trans trees ---')
    # print(trans_trees)

    return(trees)

def count_visible(trees):
    visible_trees = 0

    # all lines, excluding last line are N
    for line_index, line_tree in enumerate(trees, start=0):
        for index, tree in enumerate(trees[line_index], start=0):
            if tree[1] == 'V':
                visible_trees += 1

    return visible_trees

def print_forest(trees):
    # all lines, excluding last line are N
    for line_index, line_tree in enumerate(trees, start=0):
        print('row = ', line_index, 'values = ', line_tree)

row_index = 0

for line in file:
    #fields = line.strip().split(',')
    data = line.strip()
    row_trees = list()

    print(data)
    if data != '':
        for i in range(len(data)):
            data_set = (data[i], 'N')
            row_trees.append(data_set)
        row_index += 1
        forest.append(row_trees)


print('---- read in forest ----')
print_forest(forest)

forest = init_trees(forest)
print('---- initial forest ----')

print_forest(forest)

m_forest = mark_visible_trees(forest)
print('---- marked forest ----')

print_forest(m_forest)
visible_t = count_visible(m_forest)
print('# visible = ', visible_t)



