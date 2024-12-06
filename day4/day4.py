import re
# load and prepare data
data =[]

with open("day4/input.txt","r") as file:
    for line in file:
        if line[-1] == '\n':
            data.append(line[:-1])
        else:
            data.append(line)


# data = ["MMMSXXMASM",
# "MSAMXMSMSA",
# "AMXSXMAAMM",
# "MSAMASMSMX",
# "XMASAMXAMM",
# "XXAMMXXAMA",
# "SMSMSASXSS",
# "SAXAMASAAA",
# "MAMMMXMMMM",
# "MXMXAXMASX"]

result1 = 0

def check_xmas(i, j, di, dj):
    pattern = "XMAS"
    for k in range(len(pattern)):
        if not (0 <= i + k * di < len(data) and 0 <= j + k * dj < len(data[0])):
            return False
        if data[i + k * di][j + k * dj] != pattern[k]:
            return False
    return True


for i in range(len(data)):
    for j in range(len(data[0])):
        if check_xmas(i, j, -1, -1):  
            result1 += 1
        if check_xmas(i, j, -1, 1):   
            result1 += 1
        if check_xmas(i, j, 1, -1):  
            result1 += 1
        if check_xmas(i, j, 1, 1):   
            result1 += 1
        if check_xmas(i,j,1,0):
            result1+=1
        if check_xmas(i,j,0,1):
            result1+=1
        if check_xmas(i,j,-1,0):
            result1+=1
        if check_xmas(i,j,0,-1):
            result1+=1
            

print("First half result: ",result1)

result2 = 0

def check_x_mas(i, j):
    diag1 = (data[i + 1][j + 1] == "M" and data[i - 1][j - 1] == "S") or \
            (data[i + 1][j + 1] == "S" and data[i - 1][j - 1] == "M")
    
    diag2 = (data[i + 1][j - 1] == "M" and data[i - 1][j + 1] == "S") or \
            (data[i + 1][j - 1] == "S" and data[i - 1][j + 1] == "M")
    
    return diag1 and diag2


for i in range(1,len(data)-1):
    for j in range(1,len(data[0])-1):
        if data[i][j] == "A" and check_x_mas(i,j):
            result2+=1

print("Second half result: ",result2)
