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
sum_priorities = 0
with open(filepath+"\\AOC-2022\\Day_3\\given_input.txt", "r") as file:
    lines = [i.replace(" ", "") for i in file.read().strip().split("\n")]
    for line in lines:
        length = int(len(line) / 2)
        compartment1 = line[:length]
        priority_1 = get_priority(compartment1)
        compartment2 = line[length:]
        priority_2 = get_priority(compartment2)
        sum_priorities += (set(priority_1) & set(priority_2)).pop()
    print(sum_priorities)