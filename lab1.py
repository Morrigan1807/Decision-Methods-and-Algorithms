import sys

global col_names
global row_names

def neg_row(s_table, n_var, n_res, t_neg_str):
    while (t_neg_str > 0):
        des_col = 0
        des_row = 0
        temp_min = 0
        des_var = 0
        temp_min = 0
        for i in range (n_var + n_res):
            if(s_table[n_res][i] < 0 and s_table[n_res][i] < temp_min):
                temp_min = s_table[n_res][i]
                des_col = i

        temp_min = 0
        for i in range (n_res):
            if(s_table[i][des_col] != 0 and (s_table[i][n_var + n_res] / s_table[i][des_col]) > 0):
                temp_min = s_table[0][n_var + n_res] / s_table[i][des_col]
                des_row = i
                break
            
        for i in range (n_res):
            if(s_table[i][des_col] != 0 and (s_table[i][n_var + n_res] / s_table[i][des_col]) > 0 and (s_table[i][n_var + n_res] / s_table[i][des_col]) < temp_min):
                temp_min = s_table[i][n_var + n_res] / s_table[i][des_col]
                des_row = i

        des_var = s_table[des_row][des_col]
        if (des_var == 0):
            print ("No solutions.1")
            sys.exit()

        for i in range (n_var + n_res + 1):
            s_table[des_row][i] /= des_var

        for i in range (n_res + 1):
            if (i != des_row):
                des_var = s_table[i][des_col]
                for k in range (n_var + n_res + 1):
                    s_table[i][k] += -(s_table[des_row][k]) * des_var

        t_neg_str = 0
        for i in range (n_var + n_res + 1):
            if (s_table[n_res][i] < 0):
                t_neg_str += 1

        row_names[des_row], col_names[des_col] = col_names[des_col], row_names[des_row]
        
    return s_table

def neg_clmn(s_table, n_var, n_res, t_neg_clmn):
    while (t_neg_clmn > 0):
        des_col = 0
        des_row = 0
        temp_min = 0
        des_var = 0
        temp_min = 0
        for i in range (n_res):
            if (s_table[i][n_var + n_res] < 0 and s_table[i][n_var + n_res] < temp_min):
                temp_min = s_table[i][n_var + n_res]
                des_row = i

        temp_min = 0
        for i in range (n_var + n_res):
            if (s_table[des_row][i] < temp_min):
                temp_min = s_table[des_row][i]
                des_col = i

        if (temp_min == 0):
            print("No solutions.2")
            sys.exit()
        
        des_var = s_table[des_row][des_col]

        if (des_var == 0):
            print("No solutions.3")
            sys.exit()
            
        for i in range (n_var + n_res + 1):
            s_table[des_row][i] /= des_var

        for i in range (n_res + 1):
            if (i != des_row):
                des_var = s_table[i][des_col]
                for k in range (n_var + n_res + 1):
                    s_table[i][k] += -(s_table[des_row][k]) * des_var

        t_neg_clmn = 0
        for i in range (n_res):
            if (s_table[i][n_var + n_res] < 0):
                t_neg_clmn += 1
        row_names[des_row], col_names[des_col] = col_names[des_col], row_names[des_row]

    return s_table


print("Input the number of your variables: ")
n_var = int(input())

print("Input the number of restrictions: ")
n_res = int(input())

print("Input the direction of target function(min/max): ")
temp = input()
direc = True
if (temp == "min"):
    direc = False

s_table = []
arg = 0
col_names = []
row_names = []
for i in range (n_res):
    print("Enter the odds of the ", i+1, " constraint")
    s_table.append([])
    for n in range (n_var):
        print("Enter the odd for the ", n+1," variable")
        if (direc == False):
            s_table[i].append(-float(input()))
        else:
            s_table[i].append(float(input()))
        if(i == 0):
            col_names.append("x" + str(n+1))
        
    row_names.append("s" + str(i+1))
            
    for n in range (n_res):
        if (n == arg):
            s_table[i].append(1)
        else:
            s_table[i].append(0)
        if(i == 0):
            col_names.append("z" + str(n+1))

    print("Enter the result of the ", i+1, " restruction: ")
    if (direc == False):
        s_table[i].append(-float(input()))
    else:
        s_table[i].append(float(input()))
    arg+=1

print ("Enter the odds of the target function:")
s_table.append([])
row_names.append("F")
col_names.append("R")

for i in range (n_var):
    if(direc == True):
        s_table[n_res].append(-float(input()))
    else:
        s_table[n_res].append(float(input()))

for n in range (n_res + 1):
    s_table[n_res].append(0)
print(s_table)  

t_neg_str = 0
t_neg_clmn = 0
for i in range (n_var):
    if (s_table[n_res][i] < 0):
        t_neg_str += 1

for i in range (n_res):
    if (s_table[i][n_var + n_res] < 0):
        t_neg_clmn += 1

while t_neg_clmn > 0 or t_neg_str > 0:
    if (t_neg_clmn > 0):
        s_table = neg_clmn(s_table, n_var, n_res, t_neg_clmn)

        t_neg_str = 0
        t_neg_clmn = 0
        for i in range (n_res):
            if (s_table[i][n_var + n_res] < 0):
                t_neg_clmn += 1
        for i in range (n_var+n_res):
            if (s_table[n_res][i] < 0):
                t_neg_str += 1

        print(s_table)
        for i in range (n_var):
            if (row_names.count("x" + str(i + 1)) != 0):
                print("x" + str(i+1) + " = ", s_table[row_names.index("x" + str(i + 1))][n_var + n_res])
            elif (col_names.count("x" + str(i + 1)) != 0):
                print("x" + str(i+1) + " = ", s_table[n_res][col_names.index("x" + str(i + 1))])

    elif (t_neg_str > 0):
        s_table = neg_row(s_table, n_var, n_res, t_neg_str)

        t_neg_str = 0
        t_neg_clmn = 0
        for i in range (n_res):
            if (s_table[i][n_var + n_res] < 0):
                t_neg_clmn += 1
        for i in range (n_var+n_res):
            if (s_table[n_res][i] < 0):
                t_neg_str += 1

        print(s_table)
        for i in range (n_var):
            if (row_names.count("x" + str(i + 1)) != 0):
                print("x" + str(i+1) + " = ", s_table[row_names.index("x" + str(i + 1))][n_var + n_res])
            elif (col_names.count("x" + str(i + 1)) != 0):
                print("x" + str(i+1) + " = ", s_table[n_res][col_names.index("x" + str(i + 1))])

    else:
        print("No solutions.")
