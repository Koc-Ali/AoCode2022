import os

class Monkeys():
    calc_round = 0
    global_div_factor = 1

    def __init__(self):
        self.monkeys = []

    def create_new_monkey(self, lines):
    #    lines = file.readlines()[0:20]
        print(lines)

        # get Monkey Nummer in line 1
        MNummer = lines[0].strip().split()[1]
        MNummer = MNummer[:-1]  # remove :

        # get items in line 2
        items = lines[1].strip().split()[2:]
        for index, item in enumerate(items, start=0):
            if item[len(item) - 1] == ',':
                items[index] = items[index][:-1]  # remove ,

        # get operator in line 2
        operator = lines[2].strip().split()[4]
        # get opFactor in line 2
        opFactor = lines[2].strip().split()[5]
        # get divFactor in line 3
        divFactor = lines[3].strip().split()[3]
        # get trueReceiver in line 4
        trueReceiver = lines[4].strip().split()[5]
        # get falseReceiver in line 5
        falseReceiver = lines[5].strip().split()[5]

        # create a monkey
        self.monkeys.append({'number': MNummer,
                             'items': items,
                             'inspected_items': 0,
                            'operation': operator,
                            'OPfactor': opFactor,
                            'divisible_factor': divFactor,
                            'true_receiver': trueReceiver,
                            'false_receiver': falseReceiver })


    def exec_rounds(self, rounds):
        self.calc_global_div_factor()
        for i in range(rounds):
            self.exec_one_round()
            print('round = ', i, self.monkeys)

    def exec_one_round(self):

        # calc for each monkey worry level of an item
        for monkey in self.monkeys:
            # calc worry level for each item
            for item in monkey['items']:
                new_worry_level = item
                if monkey['operation'] == '*':
                    if monkey['OPfactor'] == 'old':
                        new_worry_level = int(item) * int(item)
                    else:
                        new_worry_level = int(item) * int(monkey['OPfactor'])
                if monkey['operation'] == '+':
                    new_worry_level = int(item) + int(monkey['OPfactor'])
                div_factor = int(monkey['divisible_factor'])
                new_worry_level = int(new_worry_level)
#                new_worry_level = new_worry_level // 3
                new_worry_level = new_worry_level % self.global_div_factor
                divisible = new_worry_level % div_factor
                new_receiver = 0
                if divisible == 0:
                    new_receiver = int(monkey['true_receiver'])
                else:
                    new_receiver = int(monkey['false_receiver'])
                self.monkeys[new_receiver]['items'].append(new_worry_level)
                monkey['inspected_items'] += 1

            # remove items
            monkey['items'] = []

    def calc_monkey_business_level(self):
        # idendify two highest items checked
        inspected_items = []
        for monkey in self.monkeys:
            inspected_items.append(monkey['inspected_items'])
        print(inspected_items)
        inspected_items.sort(reverse=True)
        return(inspected_items[0]*inspected_items[1])

    def calc_global_div_factor(self):
        self.global_div_factor = 1
        for monkey in self.monkeys:
            self.global_div_factor *= int(monkey['divisible_factor'])
        print(self.global_div_factor)
def main():
    # file handling
    fileDir = os.path.dirname(os.path.realpath('__file__'))

    # For accessing the file in the same folder
    filename = "2022_advent_11.input.txt"
    # filename = "2022_advent_11.input.sample.txt"

    path_to_file = fileDir + '/' + filename

    file = open(os.path.expanduser(path_to_file))

    # problem solution

    myMonkeys = Monkeys()

    # read all lines in file
    all_lines = file.readlines()
    amount_of_monkey_entries = int((len(all_lines)+1)/7)

    # create initial monkey list
    for m_index in range(amount_of_monkey_entries):
        myMonkeys.create_new_monkey(all_lines[m_index*7:(m_index+1)*7])

    # exec one round
    myMonkeys.exec_rounds(10000)

    m_business_level = myMonkeys.calc_monkey_business_level()
    print(m_business_level)

if __name__ == "__main__":
    main()




