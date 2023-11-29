from zad4ktesty import runtests

def falisz ( T ):
    n = len(T)
    for i in range (1,n):
        T[i][0] += T[i-1][0]
        T[0][i] += T[0][i-1]
    
    for row in range (1,n):
        for column in range(1,n):
            T[row][column] += min(T[row][column-1],T[row-1][column])
     
    return T[n-1][n-1]

runtests ( falisz )
