import os

filepath = os.getcwd()
with open(filepath+"\\Day_1\\input.txt", "r") as file:
    max_calorie = 0
    current_calorie = 0
    for line in file.readlines():
        if line != "\n":
            current_calorie += int(line)
        else:
            if current_calorie > max_calorie:
                max_calorie = current_calorie
            current_calorie = 0
    print(max_calorie)