import os
import sys


sys.setrecursionlimit(5000)

def check_duplicates(datastream_buffer: str):
    for i in datastream_buffer:
        count = datastream_buffer.count(i)
        if count > 1:
            return True
        
    return False
        
def factorial_search(string_list: list, current_idx) :
    if not check_duplicates(string_list[:4]):
        print(current_idx+4)
    else:
        string_list = string_list[1:]
        current_idx += 1
        factorial_search(string_list, current_idx)


filepath = os.getcwd()
sum_priorities = 0
with open(filepath+"\\AOC-2022\\Day_6\\input.txt", "r") as file:
    lines = [i.replace(" ", "") for i in file.read().strip().split("\n")]

datastream_buffer = lines[0]

factorial_search(datastream_buffer,0)