def find_index(start, len, arr, value):
    offset = 0
    if start > 0:
        offset = arr[start-1]
    for i in range(len-1):
        if (arr[i]-offset) <= value and (arr[i+1]-offset) > value:
            return i
    return -1


def calc_h_n(start, index, H_prefix, H, S_prefix, S, software_left):
    offset_H = 0
    offset_S = 0
    if start > 0:
        offset_H = H_prefix[start-1]
        offset_S = S_prefix[start-1]

    return ((H_prefix[index]-offset_H)+((H[index+1]/S[index+1])*(software_left-(S_prefix[index]-offset_S))))

# WE do a DFS with depth as the current depth, res store the current tasks in the stack and CB is the current best and software_limit is the software limit
# H store the hardware areas and S store the software times


def dfs(depth, res, CB, software_limit, H, S):
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
            print("Cant be allocated Software resources exhausted for :", res)
            return

        print("Can be allocated , and the allocated tasks are :", res)
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
        dfs(depth+1, res1, CB, software_limit, H, S)
        dfs(depth+1, res2, CB, software_limit, H, S)

    return
