data = []

with open("day11/input.txt","r") as file:
    data = [int(num) for num in file.read().split(" ")]

# data = [125, 17]
mem = {}

def blink(stone,blink_no,max_blinks):
    if (stone,blink_no) in mem.keys():
        return mem[(stone,blink_no)]
    
    if blink_no > max_blinks:
        mem[(stone,blink_no)] = 1
        return 1
    
    if stone == 0:
        mem[(stone,blink_no)] = blink(1,blink_no+1,max_blinks)
        return mem[(stone,blink_no)]
    num_digits = len(str(stone))

    if num_digits%2 == 0:
        mem[(stone,blink_no)] = blink(int(str(stone)[:num_digits//2]),blink_no+1,max_blinks) + blink(int(str(stone)[num_digits//2:]),blink_no+1,max_blinks)
        return mem[(stone,blink_no)]
    
    else:
        mem[(stone,blink_no)] = blink(stone*2024,blink_no+1,max_blinks)
        return mem[(stone,blink_no)]
    
result1 = 0
result2 = 0

for num in data:
    result1+=blink(num,1,25)


print("Answer for first part: ",result1)

mem = {}


for num in data:
    result2+=blink(num,1,75)

print("Answer for second part: ",result2)
