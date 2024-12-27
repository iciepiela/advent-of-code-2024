# load and prepare data
import copy


data =[]

with open("day6/input.txt","r") as file:
    for line in file:
        if line[-1] == '\n':
            data.append(list(line[:-1]))
        else:
            data.append(list(line))

# data = ["....#.....",
# ".........#",
# "..........",
# "..#.......",
# ".......#..",
# "..........",
# ".#..^.....",
# "........#.",
# "#.........",
# "......#..."]

# for i in range(len(data)):
#     data[i] = list(data[i])

for i in range(len(data)):
    if '^' in data[i]:
        guard_i = i
        guard_j = data[i].index('^')



directions = {
    '^': (-1, 0, '>'),
    'v': (1, 0, '<'),
    '<': (0, -1, '^'),
    '>': (0, 1, 'v')
}

def move(guard_i,guard_j,map):
    in_map = True
    distinct_positions = 1
    moves = 0
    while in_map and moves<len(map)*len(map[0]):
        moves+=1
        current_cell = map[guard_i][guard_j]
        if current_cell in directions:
            di, dj, next_direction = directions[current_cell]

            map[guard_i][guard_j] = 'X'

            guard_i += di
            guard_j += dj

            if not (0 <= guard_i < len(map) and 0 <= guard_j < len(map[0])):
                return distinct_positions
            else:

                new_cell = map[guard_i][guard_j]
                if new_cell == '.':
                    distinct_positions += 1
                    map[guard_i][guard_j] = current_cell
                elif new_cell == 'X':
                    map[guard_i][guard_j] = current_cell
                elif new_cell == '#':

                    guard_i -= di
                    guard_j -= dj
                    map[guard_i][guard_j] = next_direction
        else:
            return distinct_positions
    return 0

result1 = move(guard_i,guard_j,copy.deepcopy(data))

print("Answer for the first half: ", result1)

result2 = 0

for i in range(len(data)):
    for j in range(len(data[0])):
        if data[i][j] == '.':
            new_data = copy.deepcopy(data)
            new_data[i][j] = '#'
            if move(guard_i,guard_j,new_data) == 0:
                result2+=1

print("Answer for the second half: ", result2)
