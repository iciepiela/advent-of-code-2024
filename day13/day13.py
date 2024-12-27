data =[]

with open("day13/input.txt","r") as file:
    for line in file:
        if line[-1] == '\n':
            data.append(line[:-1])
        else:
            data.append(line)

# data = """Button A: X+94, Y+34
# Button B: X+22, Y+67
# Prize: X=8400, Y=5400

# Button A: X+26, Y+66
# Button B: X+67, Y+21
# Prize: X=12748, Y=12176

# Button A: X+17, Y+86
# Button B: X+84, Y+37
# Prize: X=7870, Y=6450

# Button A: X+69, Y+23
# Button B: X+27, Y+71
# Prize: X=18641, Y=10279"""

# data = data.strip().split("\n")


A_buttons = []
B_buttons = []
Prizes = []


for i in range(0, len(data), 4):
    a_coords = data[i].split(", ")
    a_x = int(a_coords[0].split("+")[1])
    a_y = int(a_coords[1].split("+")[1])
    A_buttons.append((a_x, a_y))

    b_coords = data[i + 1].split(", ")
    b_x = int(b_coords[0].split("+")[1])
    b_y = int(b_coords[1].split("+")[1])
    B_buttons.append((b_x, b_y))

    prize_coords = data[i + 2].split(", ")
    p_x = int(prize_coords[0].split("=")[1])
    p_y = int(prize_coords[1].split("=")[1])
    Prizes.append((p_x, p_y))


result1=0

for a_button, b_button, prize in zip(A_buttons, B_buttons, Prizes):
    i = 0
    ax,ay = a_button
    bx,by = b_button
    px,py = prize
    denominator = ay * bx - ax * by
    if denominator != 0: 
        numerator = py * bx - px * by
        if numerator % denominator == 0:
            i = numerator // denominator
        else:
            i = -1  
    else:
        i = -1  
    
    if i >= 0:  
        if (py-ay*i)//by <=100 and i<=100 and  px - ax * i >= 0 and py - ay * i >= 0:
            result1 += 3 * i + (py - ay * i) // by

print("Answer for first part: ",result1)

result2 = 0
for a_button, b_button, prize in zip(A_buttons, B_buttons, Prizes):
    i = 0
    ax,ay = a_button
    bx,by = b_button
    px,py = prize
    px,py = 10000000000000+px,10000000000000+py

    denominator = ay * bx - ax * by
    if denominator != 0: 
        numerator = py * bx - px * by
        if numerator % denominator == 0:
            i = numerator // denominator
        else:
            i = -1  
    else:
        i = -1  
    
    if i >= 0:  
        if i>100 and (py - ay * i) // by > 100 and  px - ax * i >= 0 and py - ay * i >= 0:
            result2 += 3 * i + (py - ay * i) // by

print("Answer for second part: ",result2)
