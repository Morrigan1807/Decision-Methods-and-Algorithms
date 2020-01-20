def poten(cost_arr, arr):
    i_start=0
    j_start=-1
    for j in range(len(arr[0])):
      if arr[0][j]!=-1:
        j_start=j
        break
    
    u=[-1 for x in arr[0]]
    v=[-1 for x in arr]
    u[j_start]=0
    v[i_start]=cost_arr[i_start][j_start]
    flag=False
    while flag==False:
        for i in range(len(arr)):
            for j in range(len(arr[0])):
                if (arr[i][j]!=-1):
                    if (u[j]!=-1):
                        if (v[i]==-1):
                            v[i]=cost_arr[i][j]-u[j]
                    else:
                        if (v[i]!=-1):
                            u[j]=cost_arr[i][j]-v[i]
        flag=True
        for x in u:
            if x==-1:
                flag=False
        for x in v:
            if x==-1:
                flag=False
    
    return u,v

def checkoptim(cost_arr, arr):
    u = []
    v = []
    u, v = poten(cost_arr, arr)

    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if arr[i][j] == -1:
                if cost_arr[i][j]<u[j]+v[i]:
                    return False,i,j
    return True,-1,-1

def method_optim(cost_arr,arr):
    check_res,i,j = checkoptim(cost_arr,arr)
    if (check_res):
        return arr
    else:
        cycle=[(i,j)]
        for k in range(len(arr[i])):
            if (arr[i][k]!=-1):
                cycle.append((i,k))
                break
        while cycle[-1]!=cycle[0]:
            if cycle[-2][0]==cycle[-1][0]:
                for k in range(len(arr[cycle[-1][0]])):
                    if (arr[cycle[-1][0]][k]!=-1 and (cycle[-1][0],k) not in cycle) or (arr[cycle[-1][0]][k]==-1 and (cycle[-1][0],k) == cycle[0]):
                        cycle.append((cycle[-1][0],k))
                        break
            else:
                for k in range(len(arr)):
                    if (arr[k][cycle[-1][1]]!=-1 and (k,cycle[-1][1]) not in cycle) or (arr[k][cycle[-1][1]]==-1 and (k,cycle[-1][1]) == cycle[0]):
                        cycle.append((k,cycle[-1][1]))
                        break
        minc = cost_arr[cycle[1][0]][cycle[1][1]]
        for k in range(1,len(cycle),2):
            if minc > arr[cycle[k][0]][cycle[k][1]]:
                minc = arr[cycle[k][0]][cycle[k][1]]
        for k in range(len(cycle)):
            if (k%2==0):
                arr[cycle[k][0]][cycle[k][1]]+=minc
            else:
                arr[cycle[k][0]][cycle[k][1]]-=minc
        return method_optim(cost_arr,arr)
def sum_plan(cost_arr,arr):
    res=0
    if (len(cost_arr)!=len(arr)):
        return res
    for i in range(len(cost_arr)):
        for j in range(len(cost_arr[0])):
            if (arr[i][j]!=-1):
                res+=cost_arr[i][j]*arr[i][j]
    return res
c_arr = [[10, 20, 30], [30, 10, 20], [5, 15, 10]]
lc_arr = [[20, 5, 5], [-1, -1, 15], [-1, -1, 25]]
d_arr = [[-1, -1, 30], [-1, 5, 10], [20, -1, 5]]
f_arr = [[20, -1, 10], [-1, 5, 10], [-1, -1, 25]]

print(method_optim(c_arr, lc_arr), sum_plan(c_arr,lc_arr), sep = "\n")
print(method_optim(c_arr, d_arr), sum_plan(c_arr,d_arr), sep = "\n")
print(method_optim(c_arr, f_arr), sum_plan(c_arr,f_arr), sep = "\n")

