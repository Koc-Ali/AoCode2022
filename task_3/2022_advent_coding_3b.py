import os

path_to_file = "~/901_src/PycharmProjects/AoCode2022/2022_advent_3.input.txt"
file = open(os.path.expanduser(path_to_file))

sum_priorities = 0

first_rucksack = ''
second_rucksack = ''
third_rucksack = ''

def get_item_in_three_rucksack (first_RS, second_RS, third_RS):
    first_RS = set(first_RS)
    secon_RS = set(second_RS)
    third_RS = set(third_RS)

    common_item = first_RS.intersection(second_RS, third_RS)
    common_item = ''.join(common_item)
#    print("common item = ", common_item)
    return common_item

def calc_item_priority (item):
    item_priority = ord(item)
    if item_priority >= 97 and item_priority <= 122: # klein a bis klein z
        item_priority = item_priority - 97 + 1
    if item_priority >= 65 and item_priority <= 90: # groß A bis groß Z
        item_priority = item_priority - 65 + 1 + 26

    return item_priority

for line in file:
    line = line.strip()

    if (first_rucksack == ''):
        first_rucksack = line
    else:
        if (second_rucksack == ''):
            second_rucksack = line
        else:
            if (third_rucksack == ''):
                third_rucksack = line
                print ('--------')
                print ('1st =', first_rucksack, '2nd = ', second_rucksack, '3rd =', third_rucksack)
                common_item = get_item_in_three_rucksack(first_rucksack, second_rucksack, third_rucksack)
                item_priority = calc_item_priority(common_item)
                print("common item =", common_item, "com item prio =", item_priority)
                sum_priorities += item_priority
                first_rucksack = ''
                second_rucksack = ''
                third_rucksack = ''

print(sum_priorities)









