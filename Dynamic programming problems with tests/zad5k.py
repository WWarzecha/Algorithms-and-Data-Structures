from zad5ktesty import runtests
import time
def garek ( A ):
    n = len(A)
    F = [[None for _ in range(n)] for _ in range(n)]

    for i in range(n):
        F[i][i] = (A[i],0)

    for i in range(n-1):
        F[i][i+1] = (max(A[i],A[i+1]),min(A[i],A[i+1]))

    for l in range(2,n):
        for j in range(l,n):
            i = j-l
            if A[i] + F[i+1][j][1] > A[j] + F[i][j-1][1]:
                F[i][j] = (A[i] + F[i+1][j][1], F[i+1][j][0])
            else:
                F[i][j] = (A[j] + F[i][j-1][1], F[i][j-1][0])
            # F[i][j] = (max(A[i] + F[i+1][j][1], A[j] + F[i][j-1][1]),)

    return max(F[0][n-1])
    return 0

#A = [3, 9, 1, 2]
#garek(A)
runtests ( garek )