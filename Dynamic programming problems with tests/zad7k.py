from zad7ktesty import runtests 
from queue import Queue


def ogrodnik (T, D, Z, l):
    n = len(D)
    depth = len(T)
    width = len(T[0])
    visited = [[False for _ in range (width)] for _ in range (depth)]

    def root_DFS(j,i):
        nonlocal depth, width, sum
        sum += T[j][i]
        if -1 < j < depth and -1 < i-1 < width and T[j][i-1] != 0 and visited[j][i-1] == False:
            visited[j][i-1] = True
            root_DFS(j,i-1)
        if -1 < j < depth and -1 < i+1 < width and T[j][i+1] != 0 and visited[j][i+1] == False:
            visited[j][i+1] = True
            root_DFS(j,i+1)
        if -1 < j+1 < depth and -1 < i < width and T[j+1][i] != 0 and visited[j+1][i] == False:
            visited[j+1][i] = True
            root_DFS(j+1,i)
    
    for j in range(n):
        i = D[j]
        if T[0][i] != 0:
            sum = 0
            root_DFS(0,i)
            D[j] = sum
            sum = 0

    F = [[-1 for _ in range (n+1)] for _ in range (l+1)]
    F[0][0] = 0
    
    for i in range (l):
        for j in range (n):
            if F[i][j] != -1:
                F[i][j+1] = max(F[i][j+1], F[i][j])
                if i + D[j] < l + 1:
                    F[i+D[j]][j+1] = max(F[i+D[j]][j+1], F[i][j] + Z[j])

    ma = 0
    for i in range(l+1):
        for j in range(n+1):
            if F[i][j] > ma:
                ma = F[i][j]

    return ma

runtests( ogrodnik, all_tests=True )
