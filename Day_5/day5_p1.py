import os

filepath = os.getcwd()
with open(filepath+"\\AOC-2022\\Day_5\\input.txt", "r") as file:
    lines = file.readlines()

rows = []
for line in lines:
    if "1" not in line:
        rows.append(list(line.replace("    ", "[ ]").replace("\n", "").replace(" ", "").replace("[]", "[ ]").replace("[", "").replace("]", "")))
    else:
        break

columns = list(map(list, zip(*rows)))

commands = []
got_to_1 = False
for line in lines:
    if got_to_1 == True and line != "\n":
        move, to = line.split("from")
        move_ammount = int(move.replace("move", "").replace(" ", ""))
        from_column, to_column = to.split("to")
        from_column = int(from_column.replace(" ", "").replace("\n", ""))
        to_column = int(to_column.replace(" ", "").replace("\n", ""))
        commands.append([move_ammount,from_column,to_column])
    elif "1" in line:
        got_to_1 = True

columns[0].insert(0, " ")

for idx,column in enumerate(columns):
    columns[idx] = [i for i in column if i != " "]

# now to do the commands
for command in commands:
    num_to_move = command[0]
    column_from = command[1]-1
    column_to = command[2]-1
    in_move = columns[column_from][:num_to_move]
    for char in in_move:
        columns[column_from].pop(0)
        columns[column_to].insert(0,char)

message = ""
for column in columns:
    if column:
        message += str(column[0])

print(message)