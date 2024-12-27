from time import sleep


positions = []
velocities = []


with open("day14/input.txt", "r") as f:
    for line in f:
        position_part, velocity_part = line.split('v=')
        
        position_str = position_part.replace('p=', '').strip()
        velocity_str = velocity_part.strip()
        
        position = tuple(map(int, position_str.split(',')))
        velocity = tuple(map(int, velocity_str.split(',')))
        
        positions.append(position)
        velocities.append(velocity)

n = 103
m = 101

position_map = [[0 for _ in range(m)] for _ in range(n)]

quadrants = [0 for _ in range(4)]

for position,velocity in zip(positions,velocities):
    new_x = (position[0] + velocity[0]*100)%m
    new_y = (position[1] + velocity[1]*100)%n

    if new_x < m//2 and new_y<n//2:
        quadrants[0]+=1
    elif new_x > m//2 and new_y<n//2:
        quadrants[1]+=1
    elif new_x<m//2 and new_y>n//2:
        quadrants[2]+=1
    elif new_x>m//2 and new_y>n//2:
        quadrants[3]+=1
    
    position_map[new_y][new_x] +=1

result1 =1

for quadrant in quadrants:
    print(quadrant)
    result1*=quadrant


def print_map(map):
    for i in range(n):
        row = ""
        for j in range(m):
            if map[i][j]==0:  
                row += "." 
            else:
                row += "#"  
        print(row)

print(result1)
position_map = [[0 for _ in range(m)] for _ in range(n)]


for position in positions:
    position_map[position[1]][position[0]] +=1


for i in range(10000):
    new_positions = []
    quadrants = [0 for _ in range(4)]


    for position, velocity in zip(positions, velocities):
        # Usuwamy starą pozycję z mapy
        position_map[position[1]][position[0]] -= 1

        # Obliczamy nową pozycję
        new_x = (position[0] + velocity[0]) % m
        new_y = (position[1] + velocity[1]) % n

        # Dodajemy nową pozycję na mapę
        position_map[new_y][new_x] += 1
        new_positions.append((new_x, new_y))


    # Aktualizujemy pozycje na nowe
    positions = new_positions

    if (i-97)%m==0 and (i-48)%n==0:
        print("timestamp: ", i)
        print_map(position_map)
        sleep(0.5)


