import os

def convert_elf_to_list(elf):
    start, stop = elf.split("-")
    start = int(start)
    stop = int(stop)
    new_elf = []
    while stop >= start:
        new_elf.append(start)
        start += 1
    return new_elf

filepath = os.getcwd()
with open(filepath+"\\AOC-2022\\Day_4\\input.txt", "r") as file:
    lines = [i.replace(" ", "") for i in file.read().strip().split("\n")]
    num_fully_contained = 0
    for line in lines:
        elf_1, elf_2 = line.split(",")
        elf_1 = convert_elf_to_list(elf_1)
        elf_2 = convert_elf_to_list(elf_2)
        if (set(elf_1).issubset(set(elf_2)) or set(elf_2).issubset(set(elf_1))):
            num_fully_contained += 1

    print(num_fully_contained)