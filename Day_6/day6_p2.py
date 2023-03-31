import os
import sys


def check_duplicates(datastream_buffer: str):
    for i in datastream_buffer:
        count = datastream_buffer.count(i)
        if count > 1:
            return True
        
    return False

filepath = os.getcwd()
with open(filepath+"\\AOC-2022\\Day_6\\input.txt", "r") as file:
    lines = [i.replace(" ", "") for i in file.read().strip().split("\n")]

datastream_buffer = lines[0]

current_idx = 0
while(check_duplicates(datastream_buffer[:14])):
    datastream_buffer = datastream_buffer[1:]
    current_idx += 1

print(current_idx+14)