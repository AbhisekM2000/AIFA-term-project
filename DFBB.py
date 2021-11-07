from helper import find_index, calc_h_n
from collections import deque
from queue import LifoQueue
import time

# We initialize the hardware area and software time vectors
len = int(input("Enter the total number of tasks :"))
# H = [10, 10, 12, 18]
# S = [2, 4, 6, 9]
# len = 4
H = list(map(int, input("Enter the hardware area of each task :").split()))
S = list(map(int, input("Enter the software time of each task :").split()))

triplets = []  # In thhe triplet we store the index and the hardware area and software time
for i in range(len):
    triplets.append((i, H[i], S[i]))

# We sort the triplets by the by hardware area/software time ratio
sorted_triplets = sorted(triplets, key=lambda t: t[1]/t[2], reverse=True)

task_order = []  # The new order of tasks after sorting
H_prefix = []  # The prefix sum of hardware areas
S_prefix = []  # The preex sum of software times

for ind, *args in sorted_triplets:
    task_order.append(ind)
    if ind == 0:
        H_prefix.append(H[ind])
        S_prefix.append(S[ind])
    else:
        H_prefix.append(H[ind]+H_prefix[-1])
        S_prefix.append(S[ind]+S_prefix[-1])


D = 15  # Software limit
g_n = 0  # Actual hardware cost of tasks allocated to software
g_dash_n = 0  # Actual software execution time of tasks allocated
CB = 0  # Current best is 0

# We find the index of task to which we can fully allocate to software
index = find_index(0, len, S_prefix, D-g_dash_n)
# We calculate the heuristics (upper bound on estimated hardware cost of the software task of reaching the goal node form given state)
h_n = calc_h_n(0, index, H_prefix, H, S_prefix, S, D-g_dash_n)
f_n = h_n+g_n  # Upper bound function

stack = LifoQueue()
depth = 0  # Current depth in the search tree is 0
START = True

final_solution = []  # Store the final solution
start_time = time.time()
while(1):
    # If we are starting and the stack is empty we simply push the two possibilities for a task, that hardware and software
    if (stack.qsize()) == 0 and START:
        START = False
        stack.put((depth, task_order[depth], 0,
                  g_n, g_dash_n, h_n, f_n, [0]))
        stack.put((depth, task_order[depth], 1,
                  g_n, g_dash_n, h_n, f_n, [1]))

    # If stack becomes empty we simplt break
    elif (stack.qsize()) == 0:
        break

    else:
        # We get the top element from stack
        depth, task_number, state, g_n, g_dash_n, h_n, f_n, res = stack.get()
        if CB >= f_n:  # We simply prune the tree
            continue

        # If its allocated to Software
        if state == 1:
            # We update the parameters
            g_n += H[task_number]
            g_dash_n += S[task_number]
            h_n = calc_h_n(depth+1, find_index(depth, len, S_prefix,
                           D-g_dash_n), H_prefix, H, S_prefix, S, D-g_dash_n)
            f_n = h_n+g_n
            # If h(n) becomes negative we continue as its not possible
            if h_n < 0:
                continue

            # If we reach a leaf node, we update the CB (Current best) and store the solution and we continue
            if depth == len-1:
                CB = g_n
                final_solution = res
                print("Temporary solution found :", res)
                print("Current best=", CB)
                print("-----------------------------------")
                continue

            res1 = res.copy()
            res2 = res.copy()
            res1.append(0)
            res2.append(1)
            # We append the two possibilities to the child node of the current node as we have not reached the leaf node
            stack.put(
                (depth+1, task_order[depth+1], 0, g_n, g_dash_n, h_n, f_n, res1))
            stack.put(
                (depth+1, task_order[depth+1], 1, g_n, g_dash_n, h_n, f_n, res2))

        else:
            h_n = calc_h_n(depth+1, find_index(depth, len, S_prefix,
                           D-g_dash_n), H_prefix, H, S_prefix, S, D-g_dash_n)
            f_n = h_n+g_n
            # If h(n) becomes negative we continue as its not possible
            if h_n < 0:
                continue

            # If we reach a leaf node, we update the CB (Current best) and store the solution and we continue
            if depth == len-1:
                CB = g_n
                final_solution = res
                print("Temporary solution found :", res)
                print("Current best=", CB)
                print("-----------------------------------")
                continue

            res1 = res.copy()
            res2 = res.copy()
            res1.append(0)
            res2.append(1)
            # We append the two possibilities to the child node of the current node as we have not reached the leaf node
            stack.put(
                (depth+1, task_order[depth+1], 0, g_n, g_dash_n, h_n, f_n, res1))
            stack.put(
                (depth+1, task_order[depth+1], 1, g_n, g_dash_n, h_n, f_n, res2))

end_time = time.time()
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
