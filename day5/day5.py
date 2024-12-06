data =[]

rules = {}
updates = []


with open("day5/input.txt","r") as file:
    for line in file:
        if len(line)>2 and line[2] == '|':
            before , after = line[:-1].split('|')
            before,after = int(before),int(after)
            if before in rules.keys():
                rules[before].add(after)
            else:
                rules.update({before:{after}})
        
        elif len(line)>1:
            if line[-1] == '\n':
                line = (line[:-1])
            updates.append([ int(num) for num in line.split(',')])

result1 = 0
incorrectly_ordered_updates = []

for update in updates:
    correct_num = {update[0]}
    for i in range(1, len(update)):
        correctly_ordered = True

        if len(rules[update[i]] & correct_num) != 0:
            incorrectly_ordered_updates.append(update)
            correctly_ordered = False
            break
        else:
            correct_num.add(update[i])
    if correctly_ordered:
        result1 += update[len(update)//2]

print("Answer for the first half: ",result1)


result2 = 0

for update in incorrectly_ordered_updates:
    correct_num = set()
    correct_num.update(update)
    for i in range(len(update)-1,-1,-1):
        if len(rules[update[i]] & correct_num) != 0:
            j = i-1
            while len(rules[update[j]] & correct_num) != 0:
                j-=1
            update[i],update[j] = update[j], update[i]
        correct_num.remove(update[i])

    result2 += update[len(update)//2]

print("Answer for the second half: ",result2)