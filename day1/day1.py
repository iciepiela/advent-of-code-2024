import numpy as np

# load and prepare data
data = np.loadtxt("day1/input.txt", dtype=int)

llist = data[:, 0]
rlist = data[:, 1]

# example data
# llist = np.array([3,4,2,1,3,3])
# rlist = np.array([4,3,5,3,9,3])

# sort in asc order
llist.sort()
rlist.sort()

# add up the absolute value of differences
result1 = sum(abs(llist - rlist))

print("Answer for the first part: ", result1)

last_num = -1
rlist_index = 0
rlist_appearances = 0
result2 = 0

for num in llist:
    if num != last_num:
        rlist_appearances = 0
        while rlist_index < len(rlist) and rlist[rlist_index] < num:
            rlist_index += 1

        while rlist_index < len(rlist) and rlist[rlist_index] == num:
            rlist_appearances += 1
            rlist_index += 1
    result2 += num * rlist_appearances
    last_num = num

print("Answer for the second part: ", result2)
