import os

def get_priority(input_string):
    priority_list = []
    for char in input_string:
        priority = ord(char)-96
        if priority < 0:
            priority += 58
        priority_list.append(priority)
    return priority_list

filepath = os.getcwd()
with open(filepath+"\\AOC-2022\\Day_3\\input.txt", "r") as file:
    lines = [i.replace(" ", "") for i in file.read().strip().split("\n")]
    counter = 0
    new_list_3 = []
    temp_list = []
    for line in lines:
        if counter ==2:
            counter = 0
            temp_list.append(get_priority(line))
            new_list_3.append(temp_list)
            temp_list = []
        else:
            counter += 1
            temp_list.append(get_priority(line))
    sum_priorities = 0
    for group in new_list_3:
        group1 = group[0]
        group2 = group[1]
        group3 = group[2]
        sum_priorities += (set(group1) & set(group2) & set(group3)).pop()
    print(sum_priorities)