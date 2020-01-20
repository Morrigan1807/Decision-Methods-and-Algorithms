import copy

const_inf = 1000000
def Sum_for_zero(arr, n, i, j):
    min_i = const_inf
    min_j = const_inf
    for k in range(n):
        if k != i and min_j > arr[k][j]:
            min_j = arr[k][j]
        if k != j and min_i > arr[i][k]:
            min_i = arr[i][k]
    return min_j + min_i
def find_sum_const(arr, n):
    min_el = 0 #minimum of elements row/column
    sum_const = 0 #sum of constants
    for i in range(n):
        min_el = min(arr[i])

        sum_const +=min_el

        for j in range(n):
            if arr[i][j] != const_inf:
                arr[i][j] -= min_el
                
    for i in range(n):
        min_el = arr[0][i]

        for j in range(n):
            if arr[j][i] < min_el:
                min_el = arr[j][i]

        sum_const +=min_el

        for j in range(n):
            if arr[j][i] != const_inf:
                arr[j][i] -= min_el
    return sum_const
                
def Sol_Kom(arr, n, name_arr, res_sum = 0):
    sum_const = 0
    max_sum = -1 #minimum sum of minimum elements
    temp_i = -1
    temp_j = -1
    
    sum_const = find_sum_const(arr, n)
    if res_sum == 0:
        res_sum = sum_const
    
    if n == 2:
        if arr[0][0] == 0 and arr[1][1] == 0:
            temp_i=0
            temp_j=0
        else:
            temp_i=0
            temp_j=1
            
        print ("Sum of result way:", res_sum)
        return [(name_arr[0][temp_i] + 1, name_arr[1][temp_j] + 1), (name_arr[0][1 - temp_i] + 1, name_arr[1][1 - temp_j] + 1)]
    
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 0 and Sum_for_zero(arr, n, i, j) > max_sum:
                max_sum = Sum_for_zero(arr, n, i, j)
                temp_i = i
                temp_j = j

    temp_arr_exc = copy.deepcopy(arr)
    temp_arr_exc[temp_i][temp_j] = const_inf
    sum_const_exc = find_sum_const(temp_arr_exc, n)

    temp_arr_inc = copy.deepcopy(arr)
    try:
        temp_temp_i = name_arr[0].index(name_arr[1][temp_j])
        temp_temp_j = name_arr[1].index(name_arr[0][temp_i])
        if temp_temp_i < n and temp_temp_j < n:
            temp_arr_inc[temp_temp_i][temp_temp_j]=const_inf
    except:
        True
    temp_arr_inc.pop(temp_i)
    for i in range(n - 1):
        temp_arr_inc[i].pop(temp_j)

    sum_const_inc = find_sum_const(temp_arr_inc, n-1)

    if sum_const_inc < sum_const_exc:
        return [(name_arr[0].pop(temp_i) + 1, name_arr[1].pop(temp_j) + 1)] + Sol_Kom(temp_arr_inc, n-1, name_arr, res_sum + sum_const_inc)
    else:
        return Sol_Kom(temp_arr_exc, n, name_arr, res_sum)
    
print("Enter N:")
n = int(input())
print("Enter array(1000000 = inf): ")
arr = []
for i in range(n):
    arr.append([])
    for j in range(n):
        arr[i].append(int(input()))
name_arr = [[i for i in range(n)],[i for i in range(n)]]
print("Input array: ", arr, sep = "\n")
print("Result: ", Sol_Kom(arr, n, name_arr))
