import re

# load and prepare data
with open("day3/input.txt","r") as file:
    data = file.read()


# first half

#example data
# data = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"

mul_list = re.findall("mul\([0-9][0-9]?[0-9]?,[0-9][0-9]?[0-9]?\)",data)

result1 = 0

for mul in mul_list:
    digits = mul[4:-1].split(",")
    result1 += int(digits[0]) * int(digits[1])
    

print("All of the multiplications result: ",result1)

# second half

# example data
# data = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"

enabled = True
result2 = 0

instruction_list = re.findall("mul\([0-9][0-9]?[0-9]?,[0-9][0-9]?[0-9]?\)|do\(\)|don't\(\)",data)

for instruction in instruction_list:
    if instruction == "do()":
        enabled = True

    elif instruction == "don't()":
        enabled = False

    elif enabled:
        digits = instruction[4:-1].split(",")
        result2 += int(digits[0]) * int(digits[1])
    


print("All of the enabled multiplications result: ",result2)

