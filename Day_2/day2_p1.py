
#___________________________________
#|_____ENEMY______|_______ME_______|
#|   Rock (A)     |   Rock (X)     |
#|   Paper (B)    |   Paper (Y)    |
#|   Scissors (C) |   Scissors (Z) |
#|_________________________________|

# Scoring

# Rock = 1
# Paper = 2
# Scissors = 3

# Lose = 0
# Draw = 3
# Win = 6


import os

def get_result(enemy, me):
    
    enemy = ord(enemy)-64
    me = ord(me)-87
    points = me
    if(enemy == me):
        points += 3
    elif (enemy%3) == (me-1):
        points +=6
    return points

total_score = 0

filepath = os.getcwd()
with open(filepath+"\\AOC-2022\\Day_2\\input.txt", "r") as file:
    for line in file.readlines():
        enemy = line[0]
        me = line[2]
        total_score += get_result(enemy, me)

    print(total_score)
