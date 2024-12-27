import copy

map =[]
is_map = True
instructions = ""
with open("day15/input.txt","r") as file:
    for line in file:
        if line == '\n':
            is_map =False
        if is_map:
            if line[-1] == '\n':
                map.append(list(line[:-1]))
            else:
                map.append(list(line))
        else:
            if line[-1] == '\n':
                instructions+=line[:-1]
            else:
                instructions+=line


map = ["##########",
"#..O..O.O#",
"#......O.#",
"#.OO..O.O#",
"#..O@..O.#",
"#O#..O...#",
"#O..O..O.#",
"#.OO.O.OO#",
"#....O...#",
"##########"]
for i in range(len(map)):
    map[i] = list(map[i])

instructions = "<vv>^<v^>v>^vv^v>v<>v^v<v<^vv<<<^><<><>>v<vvv<>^v^>^<<<><<v<<<v^vv^v>^vvv<<^>^v^^><<>>><>^<<><^vv^^<>vvv<>><^^v>^>vv<>v<<<<v<^v>^<^^>>>^<v<v><>vv>v^v^<>><>>>><^^>vv>v<^^^>>v^v^<^^>v^^>v^<^v>v<>>v^v^<v>v^^<^^vv<<<v<^>>^^^^>>>v^<>vvv^><v<<<>^^^vv^<vvv>^>v<^^^^v<>^>vvvv><>>v^<<^^^^^^><^><>>><>^^<<^^v>>><^<v>^<vv>>v>>>^v><>^v><<<<v>>v<v<v>vvv>^<><<>^><^>><>^v<><^vvv<^^<><v<<<<<><^v<<<><<<^^<v<^^^><^>>^<v^><<<^>>^v<v^v<v^>^>>^v>vv>^<<^v<>><<><<v<<v><>v<^vv<<<>^^v^>^^>>><<^v>>v^v><^^>>^<>vv^<><^^>^^^<><vvvvv^v<v<<>^v<v>v<<^><<><<><<<^^<<<^<<>><<><^^^>^^<>^>v<>^^>vv<^v^v<vv>^<><v<^v>^^^>>>^^vvv^>vvv<>>>^<^>>>>>^<<^v>^vvv<>^<><<v>v^^>>><<^^<>>^v^<v^vv<>v^<<>^<^v^v><^<<<><<^<v><v<>vv>>v><v^<vv<>v^<<^"

for i in range(len(map)):
    if '@' in map[i]:
        fish_i = i
        fish_j = map[i].index('@')


directions = {
    '^': (-1, 0),
    'v': (1, 0),
    '<': (0, -1),
    '>': (0, 1)
}

def move(i,j,di,dj,map):
    if map[i+di][j+dj] == '.':
        map[i+di][j+dj] = map[i][j]
        map[i][j] = '.'
        return True

    elif map[i+di][j+dj] == 'O':
        if move(i+di,j+dj,di,dj,map):
            map[i+di][j+dj] = map[i][j]
            map[i][j] = '.'
            return True
    return False


map_copy = copy.deepcopy(map)

for instruction in instructions:
    di,dj = directions[instruction]
    if move(fish_i,fish_j,di,dj,map_copy):
        fish_i+=di
        fish_j+=dj
result1 = 0

for i in range(len(map_copy)):
    for j in range(len(map_copy[0])):
        if map_copy[i][j]=='O':
            result1+=100*i+j
    
# print("map")
# for line in map_copy:
#     print(line)

print(result1)

def move2(i,j,i2,j2,di,dj,map):
    if map[i+di][j+dj] == '.' and i2==0 and j2==0:
        map[i+di][j+dj] = map[i][j]
        if map[i][j] == ']':
            map[i][j] = '['
        elif map[i][j] == '[':
            map[i][j] = ']'
        else:
            map[i][j] = '.'
        return True
    
    elif map[i+di][j+dj] == '.' and map[i2+di][j2+dj]=='.':
        map[i+di][j+dj] = map[i][j] 
        map[i2+di][j2+dj] = map[i2][j2]
        map[i][j] = '.'
        map[i2][j2] = '.'
        return True
    
    elif map[i+di][j+dj] == '[' and map[i2+di][j2+dj]==']':
        if move2(i+di,j+dj,i2+di,j2+dj,di,dj,map):
            map[i+di][j+dj] = map[i][j] 
            map[i2+di][j2+dj] = map[i2][j2]
            map[i][j] = '.'
            map[i2][j2] = '.'
            return True
    
    elif (dj!=0 and (map[i+di][j+dj] == '[' or map[i+di][j+dj] == ']') 
          and (map[i+di*2][j+dj*2]==']' or map[i+di*2][j+dj*2]=='[')and i2==0 and j2==0):
        if move2(i+2*di,j+2*dj,0,0,di,dj,map):
            map[i+di*2][j+dj*2] = map[i+di][j+dj]
            map[i+di][j+dj] = map[i][j]
            map[i][j] = '.'
            return True
    elif dj == 0 and map[i+di][j+dj] == '['and i2==0 and j2==0:
        if move2(i+di,j+dj,i+di,j+dj+1,di,dj,map):
            map[i+di][j+dj] = '@'
            map[i][j] = '.'
            return True
    elif dj == 0 and map[i+di][j+dj] == ']'and i2==0 and j2==0:
        if move2(i+di,j-1+dj,i+di,j+dj,di,dj,map):
            map[i+di][j+dj] = '@'
            map[i][j] = '.'
            return True
    return False



map_scaled = [[]for _ in range(len(map))]

for i in range(len(map)):
    for j in range(len(map[0])):
        if map[i][j] == '#':
            map_scaled[i].append('#')
            map_scaled[i].append('#')
        elif map[i][j] == 'O':
            map_scaled[i].append('[')
            map_scaled[i].append(']')
        elif map[i][j] == '.':
            map_scaled[i].append('.')
            map_scaled[i].append('.')
        elif map[i][j] == '@':
            map_scaled[i].append('@')
            map_scaled[i].append('.')


for i in range(len(map_scaled)):
    if '@' in map_scaled[i]:
        fish_i = i
        fish_j = map_scaled[i].index('@')


map_copy = copy.deepcopy(map_scaled)
k =0
for instruction in instructions:
    k+=1
    di,dj = directions[instruction]
    if move2(fish_i,fish_j,0,0,di,dj,map_copy):
        fish_i+=di
        fish_j+=dj
    if k<25:
        print("move: ",instruction)
        for line in map_copy:
            print(line)

result2 = 0

for i in range(len(map_copy)):
    for j in range(len(map_copy[0])):
        if map_copy[i][j]=='[':
            result2+=100*i+j

print("map")
for line in map_copy:
    print(line)

print(result2)