data =[]
lines = []

with open("day7/input.txt","r") as file:
    lines = file.readlines()

lines = ["190: 10 19",
"3267: 81 40 27",
"83: 17 5",
"156: 15 6",
"7290: 6 8 6 15",
"161011: 16 10 13",
"192: 17 8 14",
"21037: 9 7 18 13",
"292: 11 6 16 20"]

for line in lines:
    sum, values = line.split(":", 1)  
    value_list = values.split()   
    data.append(value_list) 

result1=0

for line in data:
    num_operators = len(line) - 1
    masks = [bin(i)[2:].zfill(num_operators) for i in range(2**num_operators)]
    for mask in masks:
        for operator in mask:
            pass