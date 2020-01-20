def Check_n_answer(arr, size, ex_row, ex_col):
    for i in range(size):
        for j in range(size):
             if i not in ex_row and j not in ex_col and arr[i][j]==0:
                next_ex_row = ex_row.copy()
                next_ex_row.append(i)
                next_ex_col = ex_col.copy()
                next_ex_col.append(j)
                if len(next_ex_row)==size:
                    return [(i,j)]
                else:
                    try_next = Check_n_answer(arr,size,next_ex_row,next_ex_col)
                    if try_next!=[]:
                        answer = [(i,j)]
                        answer.extend(try_next)
                        return answer
    return []

def Find_min(arr, size_n, size_m):
    marked_rows=[]
    marked_cols=[]
    flag_ch = True
    while True:
        temp = 0
        zero_row = [0 for i in range (size_n)]
        zero_col = [0 for i in range (size_m)]

        for i in range(size_n):
            for j in range(size_m):
                if i not in marked_rows and j not in marked_cols and arr[i][j] == 0:
                    temp += 1
                    zero_row[i] += 1
                    zero_col[j] += 1
                    
        if temp == 0:
            break
            
        if max(zero_row) > max(zero_col) or (max(zero_row) == max(zero_col) and flag_ch):
            marked_rows.append(zero_row.index(max(zero_row)))
            flag_ch = False
        else:       
            marked_cols.append(zero_col.index(max(zero_col)))
            flag_ch = True
    min_non_marked=-1
    for i in range(size_n):
        for j in range(size_m):
            if i not in marked_rows and j not in marked_cols:
                if min_non_marked==-1 or arr[i][j]<min_non_marked:
                    min_non_marked=arr[i][j]
    for i in range (size_n):
        for j in range(size_m):
            if i not in marked_rows and j not in marked_cols:
                arr[i][j]-=min_non_marked
            if i in marked_rows and j in marked_cols:
                arr[i][j]+=min_non_marked
    return arr

def Check(arr, size, ex_row, ex_col):
    for i in range(size):
        for j in range(size):
             if i not in ex_row and j not in ex_col and arr[i][j]==0:
                next_ex_row = ex_row.copy()
                next_ex_row.append(i)
                next_ex_col = ex_col.copy()
                next_ex_col.append(j)
                if len(next_ex_row)==size:
                    return True
                else:
                    try_next = Check(arr,size,next_ex_row,next_ex_col)
                    if try_next==True:
                        return True
    return False
        
def Veng(matrix, n):
    min_matr = [matrix[i][0] for i in range(n)]
    temp = 3
    for i in range(n):
        for j in range (n):
            if(min_matr[i] > matrix[i][j]):
                min_matr[i] = matrix[i][j]

    for i in range(n):
        for j in range(n):
            matrix[i][j] -= min_matr[i]

    print("1. ", matrix)

    min_matr = [matrix[0][i] for i in range(n)]
    for i in range(n):
        for j in range(n):
            if(min_matr[i] > matrix[j][i]):
                min_matr[i] = matrix[j][i]

    for i in range(n):
        for j in range(n):
            matrix[j][i] -= min_matr[i]

    print("2. ", matrix)

    while(not Check(matrix, n, [], [])):
        matrix = Find_min(matrix, n, n)
        print(temp, ".", matrix)
        temp += 1      

print("Input size of matrix:")
n = int(input())
in_matrix = []
print("Input elements of matrix: ")
for i in range (n):
    in_matrix.append([])
    for j in range(n):
        in_matrix[i].append(int(input()))

matrix = []
for i in range(n):
    matrix.append(in_matrix[i].copy())
print("0. ", matrix)

Veng(matrix, n)

i_j_zero = Check_n_answer(matrix, n, [], [])

print("Solution:")
sol = 0
for i in range(n):
    for j in range(n):
        if (i,j) in i_j_zero:
            print("*", matrix[i][j], "*", end = " ")
            sol += matrix[i][j]
        else:
            print(matrix[i][j], end = " ")
    print()

for i in range(n):
    for j in range(n):
        if (i,j) in i_j_zero:
            sol += in_matrix[i][j]

print("Distance =", sol)
