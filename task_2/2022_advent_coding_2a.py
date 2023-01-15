import os

# file handling
fileDir = os.path.dirname(os.path.realpath('__file__'))

#For accessing the file in the same folder
filename = "2022_advent_2.input.txt"
path_to_file = fileDir + '/' + filename

file = open(os.path.expanduser(path_to_file))

# problem solution

totalscore = 0

score_win = 6
score_gleich = 3
score_lost = 0

score_paper = 2
score_rock = 1
score_scissors = 3


#for line in file:
#    fields = line.strip().split()
#    #print(fields[0], fields[1], fields[2], fields[3])
#    print(fields[0])


for line in file:
    fields = line.strip().split()
    gegner = fields[0]
    selber = fields[1]
    singlescore = 0

    if gegner == 'A': # Rock
        if selber == "X":    ## gleichstand
            singlescore = singlescore + score_gleich + score_rock
        if selber == "Y": # ich habe gewonnen
            singlescore = singlescore + score_win  + score_paper
        if selber == "Z": # ich habe verloren
            singlescore = singlescore + score_lost  + score_scissors

    if gegner == 'B': # Paper
        if selber =="X":  # ich habe verloren
            singlescore = singlescore + score_lost + score_rock
        if selber == "Y":  # gleichstand
            singlescore = singlescore + score_gleich + score_paper
        if selber =="Z":  # ich habe gewonnen
            singlescore = singlescore + score_win + score_scissors

    if gegner == 'C': # Scissor
        if selber == "X":  # ich habe gewonnen
            singlescore = singlescore + score_win + score_rock
        if selber == "Y":  # ich habe verloren
            singlescore = singlescore + score_lost + score_paper
        if selber == "Z":  # gleichstand
            singlescore = singlescore + score_gleich + score_scissors

    totalscore = totalscore + singlescore

    print(gegner, ' ', selber, 'singlescore =', singlescore, 'totalscore =', totalscore)

print('final totalscore =', totalscore)





