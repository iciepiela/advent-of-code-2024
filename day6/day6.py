# load and prepare data
data =[]

with open("day6/input.txt","r") as file:
    for line in file:
        if line[-1] == '\n':
            data.append(line[:-1])
        else:
            data.append(line)

print(data)