import os
top_calorie = []

filepath = os.getcwd()
with open(filepath+"\\Day_1\\input.txt", "r") as file:
    current_calorie = 0
    for line in file.readlines():
        if line != "\n":
            current_calorie += int(line)
        else:
            top_calorie.append(current_calorie)
            current_calorie = 0
    top_calorie.sort()
    print(sum(top_calorie[-3:]))