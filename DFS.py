from collections import deque
from queue import LifoQueue
import time
import random

# We initialize the hardware area and software time vectors
print_intermediate=False

# len = int(input("Enter the total number of tasks :"))
# H = list(map(int, input("Enter the hardware area of each task :").split()))
# S = list(map(int, input("Enter the software time of each task :").split()))
# D=int(input("Enter the software time limit (constraint) :"))

H = []
S = []
D = 200  # Software limit
len = 20
for i in range(len):
    H.append(random.randint(1, 30))
for i in range(len):
    S.append(random.randint(1, 30))

triplets = []  # In thhe triplet we store the index and the hardware area and software time
for i in range(len):
    triplets.append((i, H[i], S[i]))

# We sort the triplets by the by hardware area/software time ratio
sorted_triplets = sorted(triplets, key=lambda t: t[1]/t[2], reverse=True)

task_order = []  # The new order of tasks after sorting
H_prefix = []  # The prefix sum of hardware areas
S_prefix = []  # The preex sum of software times

cnt = 0
for ind, *args in sorted_triplets:
    task_order.append(ind)
    if cnt == 0:
        H_prefix.append(H[ind])
        S_prefix.append(S[ind])
    else:
        H_prefix.append(H[ind]+H_prefix[-1])
        S_prefix.append(S[ind]+S_prefix[-1])
    cnt += 1

CB = 1000000  # Current best hardware area, we take a large value since we need to minimize it
final_solution = []  # Store the final solution
depth = 0  # Current depth
res = []  # Current tasks in the recursion stack


def dfs(depth, res, software_limit, H, S):
    global CB
    global final_solution
    if depth == len:  # If we hit a leaf node we check for all conditions
        hardware_area = 0
        software_time = 0
        index = 0
        for val in res:
            if val == 0:
                hardware_area += H[index]
            if val == 1:
                software_time += S[index]
            index += 1
        if software_time > software_limit:
            if print_intermediate==True:
                print("Allocation impossible, software resources exhausted for :", res)
            return

        if print_intermediate==True:
            print("Allocated tasks are :", res)
        if software_time <= software_limit and hardware_area < CB:
            final_solution = res
            CB = hardware_area
        return

    else:
        res1 = res.copy()
        res2 = res.copy()
        res1.append(0)
        res2.append(1)
        # We do the same for its chicld nodes
        dfs(depth+1, res1, software_limit, H, S)
        dfs(depth+1, res2, software_limit, H, S)

    return


start_time = time.time()
dfs(depth, res, D, H, S)
end_time = time.time()
print("-"*40)

# Finally we print the costs and the final solution (allocated tasks)
hardware_area = 0
software_time = 0
index = 0
for val in final_solution:
    if val == 0:
        hardware_area += H[index]
    if val == 1:
        software_time += S[index]
    index += 1

index = 0
print("Tasks allocated to Software :", end="")
for val in final_solution:
    if val == 1:
        print(" Task {}".format(index+1), end="")
    index += 1

index = 0
print("\nTasks allocated to Hardware :", end="")
for val in final_solution:
    if val == 0:
        print(" Task {}".format(index+1), end="")
    index += 1

print("\nTotal hardware area = ", hardware_area)
print("Total software execution time = ", software_time)
print("TIME TAKEN = ", end_time-start_time)
