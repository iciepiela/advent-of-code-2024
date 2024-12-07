data =[]
lines = []

with open("day7/input.txt","r") as file:
    lines = file.readlines()

# lines = ["190: 10 19",
# "3267: 81 40 27",
# "83: 17 5",
# "156: 15 6",
# "7290: 6 8 6 15",
# "161011: 16 10 13",
# "192: 17 8 14",
# "21037: 9 7 18 13",
# "292: 11 6 16 20"]

for line in lines:
    total, values = line.split(":", 1)  
    value_list = [int(value) for value in values.split()]
    new_line = [int(total)] + value_list
    data.append(new_line)



result1=0

for line in data:
    num_operators = len(line) - 2
    masks = [bin(i)[2:].zfill(num_operators) for i in range(2**num_operators)]

    for mask in masks:
        current_res = line[1]  

        for i in range(1,len(line)-1):
            if mask[i-1] == '1':  
                current_res *= line[i + 1]
            else:  
                current_res += line[i + 1]
            if current_res>line[0]:
                break
        if current_res == line[0]:

            result1+=current_res
            break


print("Answer for the first part: ", result1)


result2 = 0


for line in data:
    num_operators = len(line) - 2
    masks = [
        ''.join(map(str, [(i // (3**j)) % 3 for j in range(num_operators)][::-1]))
        for i in range(3**num_operators)
    ]
    for mask in masks:
        current_res = line[1]  

        for i in range(1, len(line) - 1):
            if mask[i - 1] == '1': 
                current_res *= line[i + 1]
            elif mask[i - 1] == '2':  
                current_res = current_res*10**len(str(line[i+1])) + line[i+1]
            else:  
                current_res += line[i + 1]
            
            if current_res > line[0]:  
                break
        
        if current_res == line[0]:  
            result2 += current_res  
            break

print("Answer for the second part: ", result2)
