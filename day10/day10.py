data =[]

with open("day10/input.txt","r") as file:
    for line in file:
        if line[-1] == '\n':
            data.append(line[:-1])
        else:
            data.append(line)


# data = ["89010123",
# "78121874",
# "87430965",
# "96549874",
# "45678903",
# "32019012",
# "01329801",
# "10456732"]



n = len(data)
m = len(data[0])

map = [[set() for _ in range(m)] for _ in range(n)]
result1 = 0

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

for step in range(9, -1, -1):
    for i in range(n):
        for j in range(m):
            if int(data[i][j]) == step:
                if step == 9:
                    map[i][j].add((i, j))
                else:
                    for di, dj in directions:
                        ni, nj = i + di, j + dj
                        if 0 <= ni < n and 0 <= nj < m and int(data[ni][nj]) == step + 1:
                            map[i][j].update(map[ni][nj])
                
                if step == 0:
                    result1 += len(map[i][j])


print("Answer for first part: ",result1)

result2 = 0

map = [[ 0 for _ in range(m)] for _ in range(n)]

for step in range(9, -1, -1):
    for i in range(n):
        for j in range(m):
            if int(data[i][j]) == step:
                if step == 9:
                    map[i][j] = 1
                else:
                    for di, dj in directions:
                        ni, nj = i + di, j + dj
                        if 0 <= ni < n and 0 <= nj < m and int(data[ni][nj]) == step + 1:
                            map[i][j] += map[ni][nj]
                
                if step == 0:
                    result2 += map[i][j]

print("Answer for second part: ",result2)
