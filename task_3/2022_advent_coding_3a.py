import os

path_to_file = "~/901_src/PycharmProjects/AoCode2022/2022_advent_3.input.txt"
file = open(os.path.expanduser(path_to_file))

sum_priorities = 0

def get_item_in_both_compartments (first_compartment, second_compartment):
    first_compartment = set(first_compartment)
    second_compartment = set(second_compartment)

    common_item = first_compartment.intersection(second_compartment)
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
    fields = line.strip()
    amount_of_items = len(fields)
    print(amount_of_items)
    first_compartment = fields[0:(amount_of_items//2)]
    second_compartment = fields[amount_of_items//2:amount_of_items]
    common_item = get_item_in_both_compartments(first_compartment, second_compartment)
    item_priority = calc_item_priority(common_item)
    print("item = ", amount_of_items, "first = ", first_compartment, "second = ", second_compartment, "common item =", common_item, "com item prio =", item_priority)
    sum_priorities += item_priority

print(sum_priorities)









