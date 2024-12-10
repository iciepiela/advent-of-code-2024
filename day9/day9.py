data = []

with open("day9/input.txt","r") as file:
    data = file.read()

# data = "2333133121414131402"

left = 0
if len(data)%2==1:
    right = -1
else:
    right = -2

i = 0
result1 = 0
uses_left = int(data[right])
while True:
    if left-right == len(data):
        stop = uses_left
    else:
        stop = int(data[left])
    for _ in range(stop):
        result1+=(left//2)*i
        i+=1

    if left-right>=len(data):
        break

    left+=2
    counter = int(data[left-1])

    while counter>0:
        if uses_left>0:
            result1+=((len(data)+right)//2)*i
            i+=1
            counter-=1
            uses_left-=1

        else:
            if left-right>=len(data):
                break
            right-=2
            uses_left = int(data[right])


print("Answer for part one: ",result1)

left = 0
right = -1 if len(data) % 2 == 1 else -2 
data_len = len(data)  

i = 0
result2 = 0

data_copy = data
while left<=data_len:

    if int(data[left])!=0:
        for _ in range(int(data[left])):
            result2+=(left//2)*i
            i+=1
    else:
        i+=int(data_copy[left])

    left += 2
    if left>data_len:
        break
    counter = int(data[left - 1])
    right = -1

    while counter > 0:
        while left - right <=data_len:
            if int(data[right]) <= counter and int(data[right])!=0:
                for _ in range(int(data[right])):
                    result2 += ((data_len + right) // 2) * i
                    i +=1
                counter -= int(data[right])
                if right==-1:
                    data = data[:right] + "0"
                else:
                    data = data[:right] + "0" + data[right+1:]

            else:
                right -= 2  

        if counter > 0:
            i+=counter
            break



print(result2)
    