def do_str(matrix):
    min_matr = []
    max_str = 1000000
    min_max_str_i = []
    min_max_str_j = []

    tempi = -1
    tempj = -1

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if max_str > matrix[i][j]:
                max_str = matrix[i][j]
                tempi = i + 1
                tempj = j + 1
        min_matr.append(max_str)
        min_max_str_i.append(tempi)
        min_max_str_j.append(tempj)
        max_str = 10000005

    res = min_matr[0]
    tempi = 0
    for i in range(1, len(min_matr)):
        if min_matr[i] > res:
            res = min_matr[i]
            tempi = i
    return res, min_max_str_i[tempi], min_max_str_j[tempi]

def do_col(matrix):
    max_matr = []
    min_str = -1
    max_min_str_i = []
    max_min_str_j = []

    tempi = -1
    tempj = -1

    for j in range(len(matrix[0])):
        for i in range(len(matrix)):
            if min_str < matrix[i][j]:
                min_str = matrix[i][j]
                tempi = i + 1
                tempj = j + 1
        max_matr.append(min_str)
        max_min_str_i.append(tempi)
        max_min_str_j.append(tempj)
        min_str = -1

    res = max_matr[0]
    tempi = 0
    for i in range(1, len(max_matr)):
        if max_matr[i] < res:
            res = max_matr[i]
            tempi = i
    return res, max_min_str_i[tempi], max_min_str_j[tempi]


    
matrix = [[3, 8],
          [10, 4]]
print("Matrix: ", matrix)
res1, i1, j1 = do_str(matrix)
res2, i2, j2 = do_col(matrix)
if (res1, i1, j1) == (res2, i2, j2):
    print("Result = ", res1)
    print("i = ", i1)
    print("j = ", j1)
else:
    print("1.Result = ", res1)
    print("1.i = ", i1)
    print("1.j = ", j1)
    print("\n2.Result = ", res2)
    print("2.i = ", i2)
    print("2.j = ", j2)

