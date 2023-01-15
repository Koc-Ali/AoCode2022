import os

path_to_file = "~/901_src/PycharmProjects/AoCode2022/2022_advent_4.input.txt"
file = open(os.path.expanduser(path_to_file))

totaloverlap = 0

for line in file:
    fields = line.strip().split(',')
    # print(fields)
    partner1 = fields[0]
    Start_partner1 = int(partner1.split('-')[0])
    End_partner1 = int(partner1.split('-')[1])

    partner2 = fields[1]
    Start_partner2 = int(partner2.split('-')[0])
    End_partner2 = int(partner2.split('-')[1])

    rangeP1 = range(Start_partner1, End_partner1+1, 1)
    rangeP2 = range(Start_partner2, End_partner2+1, 1)


    print('partner 1 =', partner1, 'partner 2= ', partner2, 'sp1 = ', Start_partner1, 'ep1 = ', End_partner1, 'sp2 = ', Start_partner2, 'ep2 = ', End_partner2)

    if ((Start_partner2 in rangeP1) or (End_partner2 in rangeP1)) or ((Start_partner1 in rangeP2) or (End_partner1 in rangeP2)):
        totaloverlap += 1
        #print(' ==> included')


print('totaloverlap =', totaloverlap)





