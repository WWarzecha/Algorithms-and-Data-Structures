from zad12ktesty import runtests 

def autostrada( T, k ):
    n = len(T)
    inf = float('inf')

    F = [[inf for _ in range (n)] for _ in range(k)]

    for i in range (k):
        F[i][i] = max(T[0:i+1])
    for i in range(1,n):
        F[0][i] = F[0][i-1] + T[i]
    
    for i in range(1,k):
        for j in range(i+1,n):
            for l in range(1,j):
                F[i][j] = min(F[i][j],max(F[i-1][j-l],F[0][j]-F[0][j-l]))

    return F[k-1][n-1]

runtests ( autostrada,all_tests=True )