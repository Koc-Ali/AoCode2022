import os

# path_to_file = "~/901_src/PycharmProjects/AoCode2022/2022_advent_8.small.input.txt"
path_to_file = "~/901_src/PycharmProjects/AoCode2022/2022_advent_8.input.txt"
file = open(os.path.expanduser(path_to_file))

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
        trees[0][index] = (tree[0], 'V', 0)

    # all lines, excluding last line are N
    for line_index, line_tree in enumerate(trees[1:], start=1):
        for index, tree in enumerate(trees[line_index], start=0):
     #       print(line_index, index, tree)
            trees[line_index][index] = (tree[0], 'N', 0)
            if index == 0 or index == (last_column-1):
                trees[line_index][index] = (tree[0], 'V', 0)

    # set last line V
    for index, tree in enumerate(trees[last_row-1], start=0):
    #    print(index, tree)
        trees[last_row-1][index] = (tree[0], 'V', 0)

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

        for index, tree in enumerate(trees[line_index], start=0):
            if int(tree[0]) > talest_tree_hight:
                talest_tree_hight = int(tree[0])
                trees[line_index][index] = (tree[0], 'V', tree[2])
        # reverse items.
        line_tree.reverse()

        talest_tree_hight = int(trees[line_index][0][0])

        for index, tree in enumerate(trees[line_index], start=0):
            if int(tree[0]) > talest_tree_hight:
                talest_tree_hight = int(tree[0])
                trees[line_index][index] = (tree[0], 'V', tree[2])
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

        for index, tree in enumerate(trees[line_index], start=0):
            if int(tree[0]) > talest_tree_hight:
                talest_tree_hight = int(tree[0])
                trees[line_index][index] = (tree[0], 'V', tree[2])
        # reverse items.
        line_tree.reverse()

        talest_tree_hight = int(trees[line_index][0][0])
        # print('boarder talest number =', talest_tree_hight)

        for index, tree in enumerate(trees[line_index], start=0):
            if int(tree[0]) > talest_tree_hight:
                talest_tree_hight = int(tree[0])
                trees[line_index][index] = (tree[0], 'V', tree[2])
        # reverse items.
        line_tree.reverse()

    trans_trees = matrixTranspose(trees)
    trees = trans_trees
    # print('--- trans trees ---')
    # print(trans_trees)

    return(trees)

def calc_total_score(stored_score, act_score):
    total_score = 0
    if (stored_score == 0) and (act_score == 0):
        total_score = 0
    if (stored_score == 0) and (act_score != 0):
        total_score = act_score
    if (stored_score != 0) and (act_score == 0):
        total_score = stored_score
    if (stored_score != 0) and (act_score != 0):
        total_score = stored_score * act_score
    return total_score


def calc_scenic_score(trees):
    last_row = len(trees)
    last_column = len(trees[0])
    left_score, right_score, top_score, down_score = 0, 0, 0, 0

    print('---- calc score - start ----')
    print_forest(trees)

    # calculate score for all rows
    for line_index, line_tree in enumerate(trees, start=0):
        # for each raw ...
        left_score = 0
        for index, tree in enumerate(line_tree, start=0):
            # for each tree
            issued_tree_hight = int(tree[0])
            left_score = 0
            for r_index, r_tree in enumerate(line_tree[index+1:], start=0):
                if int(r_tree[0]) < issued_tree_hight:
                    left_score += 1
                elif (int(r_tree[0]) == issued_tree_hight) or (int(r_tree[0]) > issued_tree_hight):
                    left_score += 1
                    break
                else:
                    break
            # store first score
            current_score = int(tree[2])
            total_score = calc_total_score(current_score, left_score)
            print('tree =', tree, 'current score = ', current_score, 'left score =', left_score, 'total score = ', total_score)
            trees[line_index][index] = (tree[0], tree[1], total_score)

        print('---- calc score - left to right ----')
        print_forest(trees)

        # reverse items.
        line_tree.reverse()

        for index, tree in enumerate(line_tree, start=0):
            # for each tree
            issued_tree_hight = int(tree[0])
            left_score = 0
            for r_index, r_tree in enumerate(line_tree[index + 1:], start=0):
                if int(r_tree[0]) < issued_tree_hight:
                    left_score += 1
                elif (int(r_tree[0]) == issued_tree_hight) or (int(r_tree[0]) > issued_tree_hight):
                    left_score += 1
                    break
                else:
                    break
            # store first score
            current_score = int(tree[2])
            total_score = calc_total_score(current_score, left_score)
            print('tree =', tree, 'current score = ', current_score, 'left score =', left_score, 'total score = ', total_score)
            trees[line_index][index] = (tree[0], tree[1], total_score)

        #        # reverse items.
        line_tree.reverse()

        print('---- calc score - +++ right to left ----')
        print_forest(trees)

    trans_trees = matrixTranspose(trees)
    trees = trans_trees

    # calculate score for all rows
    for line_index, line_tree in enumerate(trees, start=0):
        # for each raw ...
        left_score = 0
        for index, tree in enumerate(line_tree, start=0):
            # for each tree
            issued_tree_hight = int(tree[0])
            left_score = 0
            for r_index, r_tree in enumerate(line_tree[index+1:], start=0):
                if int(r_tree[0]) < issued_tree_hight:
                    left_score += 1
                elif (int(r_tree[0]) == issued_tree_hight) or (int(r_tree[0]) > issued_tree_hight):
                    left_score += 1
                    break
                else:
                    break
            # store first score
            current_score = int(tree[2])
            total_score = calc_total_score(current_score, left_score)
            print('tree =', tree, 'current score = ', current_score, 'left score =', left_score, 'total score = ', total_score)
            trees[line_index][index] = (tree[0], tree[1], total_score)

        print('---- calc score - +++ trans left to right  ----')
        print_forest(trees)

        # reverse items.
        line_tree.reverse()

        for index, tree in enumerate(line_tree, start=0):
            # for each tree
            issued_tree_hight = int(tree[0])
            left_score = 0
            for r_index, r_tree in enumerate(line_tree[index + 1:], start=0):
                if int(r_tree[0]) < issued_tree_hight:
                    left_score += 1
                elif (int(r_tree[0]) == issued_tree_hight) or (int(r_tree[0]) > issued_tree_hight):
                    left_score += 1
                    break
                else:
                    break
            # store first score
            current_score = int(tree[2])
            total_score = calc_total_score(current_score, left_score)
            print('tree =', tree, 'current score = ', current_score, 'left score =', left_score, 'total score = ', total_score)
            trees[line_index][index] = (tree[0], tree[1], total_score)
        #        # reverse items.
        line_tree.reverse()

        print('---- calc score - +++ trans right to left  ----')
        print_forest(trees)

    trans_trees = matrixTranspose(trees)
    trees = trans_trees

    print('---- calc score - end ----')
    print_forest(trees)

    return(trees)

def find_highest_score(trees):
    highest_score = 0

   # all lines, excluding last line are N
    for line_index, line_tree in enumerate(trees, start=0):
        for index, tree in enumerate(trees[line_index], start=0):
            if int(tree[2]) > highest_score:
                highest_score = int(tree[2])
    return highest_score


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

s_forest = calc_scenic_score(m_forest)
print('---- s_forest forest ----')
print_forest(s_forest)

print('highest score = ', find_highest_score(s_forest))


