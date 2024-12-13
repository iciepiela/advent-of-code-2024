data =[]

with open("day12/input.txt","r") as file:
    for line in file:
        if line[-1] == '\n':
            data.append(line[:-1])
        else:
            data.append(line)


# data = ["RRRRIICCFF",
# "RRRRIICCCF",
# "VVRRRCCFFF",
# "VVRCCCJFFF",
# "VVVVCJJCFE",
# "VVIVCCJJEE",
# "VVIIICJJEE",
# "MIIIIIJJEE",
# "MIIISIJEEE",
# "MMMISSJEEE"]

n = len(data)
m = len(data[0])


map = [[0 for _ in range(m)] for _ in range(n)]
discovered = [[False for _ in range(m)] for _ in range(n)]
directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]
corners_dir = [(-1,1),(-1,-1),(1,-1),(1,1)]
result1 = 0


def find_area(i,j):
    if discovered[i][j]:
        return (0,0)
    elif map[i][j] !=0:
        return map[i][j]
    else:
        discovered[i][j] = True
        map[i][j]=(0,0)
        area = 0
        paramiters = 0
        for di, dj in directions:
            ni, nj = i + di, j + dj
            if 0 <= ni < n and 0 <= nj < m and data[i][j] == data[ni][nj]:
                area_and_par = find_area(ni,nj)
                area += area_and_par[0]
                paramiters += area_and_par[1]
            else:
                paramiters +=1
        map[i][j] = (area+1,paramiters)
        return map[i][j]

for i in range(n):
    for j in range(m):
        if map[i][j]==0:
            area_and_par = find_area(i,j)
            result1+= area_and_par[0] * area_and_par[1]


print("Answer for first part: ",result1)

result2 = 0
map = [[0 for _ in range(m)] for _ in range(n)]
discovered = [[False for _ in range(m)] for _ in range(n)]

def find_area_2(i, j):
    if discovered[i][j]:
        return (0, 0)

    if map[i][j] != 0:
        return map[i][j]

    discovered[i][j] = True
    map[i][j] = (0, 0)

    area = 0
    corners = 0
    adjacent_count = 0  
    corner_accum = 0  
    direction_index = 0  

    for di, dj in directions:
        ni, nj = i + di, j + dj

        if 0 <= ni < n and 0 <= nj < m and data[i][j] == data[ni][nj]:
            adjacent_count += 1

            if corner_accum > 0:
                corners += corner_accum - 1
                corner_accum = 0

            ci, cj = corners_dir[direction_index]
            corner_ni, corner_nj = i + ci, j + cj

            if adjacent_count == 2:
                if data[i][j] != data[corner_ni][corner_nj]:
                    corners += 1
                adjacent_count = 1

            neighbor_area, neighbor_corners = find_area_2(ni, nj)
            area += neighbor_area
            corners += neighbor_corners
        else:
            corner_accum += 1
            adjacent_count = 0

        direction_index += 1

    di, dj = directions[0]
    ni, nj = i + di, j + dj
    if not (0 <= ni < n and 0 <= nj < m and data[i][j] == data[ni][nj]):
        corner_accum += 1

    if corner_accum > 0:
        corners += corner_accum - 1
    if corner_accum == 4:
        corners += 1

    ci, cj = corners_dir[0]
    corner_ni, corner_nj = i + ci, j + cj
    if (adjacent_count == 1 and
        (0 <= ni < n and 0 <= nj < m and data[i][j] == data[ni][nj]) and
        data[i][j] != data[corner_ni][corner_nj]):
        corners += 1

    map[i][j] = (area + 1, corners)

    return map[i][j]




for i in range(n):
    for j in range(m):
        if map[i][j]==0:
            area_and_par = find_area_2(i,j)
            result2+= area_and_par[0] * area_and_par[1]


print("Answer for second part: ",result2)


