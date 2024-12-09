import copy
data =[]

with open("day8/input.txt","r") as file:
    for line in file:
        if line[-1] == '\n':
            data.append(list(line[:-1]))
        else:
            data.append(list(line))


# data = ["............",
# "........0...",
# ".....0......",
# ".......0....",
# "....0.......",
# "......A.....",
# "............",
# "............",
# "........A...",
# ".........A..",
# "............",
# "............"]


# for i in range(len(data)):
#     data[i] = list(data[i])

antinode_map = copy.deepcopy(data)
result1 = 0

for i in range(len(data)):
    for j in range(len(data[i])):
        if data[i][j] not in ('.', '#'):
            value = data[i][j]  
            for ii in range(i, len(data)):
                matching_indices = [k for k, x in enumerate(data[ii]) if x == value and k != j]

                for jj in matching_indices:
                    diff_i = ii - i
                    diff_j = jj - j

                    ni, nj = i - diff_i, j - diff_j
                    if 0 <= ni < len(data) and 0 <= nj < len(data[0]) and antinode_map[ni][nj] != '#':
                        antinode_map[ni][nj] = '#'
                        result1 += 1

                    ni, nj = i + 2 * diff_i, j + 2 * diff_j
                    if 0 <= ni < len(data) and 0 <= nj < len(data[0]) and antinode_map[ni][nj] != '#':
                        antinode_map[ni][nj] = '#'
                        result1 += 1


# for line in antinode_map:
#     print(line)

print("Answer for the first part: ",result1)

result2 = 0
antinode_map = copy.deepcopy(data)

for i in range(len(data)):
    for j in range(len(data[i])):
        if data[i][j] not in ('.', '#'):
            value = data[i][j] 
            exist_sec = False
            for ii in range(i, len(data)):
                matching_indices = [k for k, x in enumerate(data[ii]) if x == value and k != j]

                for jj in matching_indices:
                    if antinode_map[i][j] !='#':
                        antinode_map[i][j] = '#'
                        result2+=1
                        
                    diff_i = ii - i
                    diff_j = jj - j
                    iloraz = 1

                    while 0 <= i - diff_i*iloraz < len(data) and 0 <= j - diff_j*iloraz < len(data[0]):
                        ni, nj = i - diff_i*iloraz, j - diff_j*iloraz
                        if antinode_map[ni][nj] != '#':
                            antinode_map[ni][nj] = '#'
                            result2 += 1
                        iloraz+=1

                    iloraz = 1
                    while 0 <= i + iloraz * diff_i < len(data) and 0 <= j + iloraz * diff_j < len(data[0]):
                        ni, nj = i + diff_i*iloraz, j + diff_j*iloraz
                        if antinode_map[ni][nj] != '#':
                            antinode_map[ni][nj] = '#'
                            result2 += 1
                        iloraz+=1

# for line in antinode_map:
#     print(line)
print("Answer for the second part: ",result2)
