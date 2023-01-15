import os

path_to_file = "~/901_src/PycharmProjects/AoCode2022/2022_advent_2.input.txt"
file = open(os.path.expanduser(path_to_file))
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



    if selber == 'X': # lose
        if gegner == "A":
            new_selber = 'Z'
        if gegner == "B":
            new_selber = 'X'
        if gegner == "C":
            new_selber = 'Y'

    if selber == 'Y': # draw
        if gegner == "A":
            new_selber = 'X'
        if gegner == "B":
            new_selber = 'Y'
        if gegner == "C":
            new_selber = 'Z'

    if selber == 'Z': # win
        if gegner == "A":
            new_selber = 'Y'
        if gegner == "B":
            new_selber = 'Z'
        if gegner == "C":
            new_selber = 'X'

    print ('original selber =', selber, ' new selber =', new_selber)
    selber = new_selber

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





