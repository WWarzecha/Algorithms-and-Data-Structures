from zad11ktesty import runtests

def kontenerowiec(T):
    inf = float('inf')
    sum_T = 0
    n = len(T)
    
    for i in range(n):
        sum_T += T[i]
    
    capacity = (sum_T+1)//2
    F = [[0 for _ in range (n+1)] for _ in range (capacity + 1)]
    F[0][0] = 0
    
    for i in range (capacity+1):
        for j in range (n):
            F[i][j+1] = max(F[i][j], F[i][j+1])
            if i + T[j] < capacity + 1:
                F[i + T[j]][j+1] = max(F[i + T[j]][j+1], F[i][j] + T[j])
    ma = -inf
    for i in range(capacity+1):
        for j in range (n+1):
            if F[i][j] > ma:
                ma = F[i][j]
    
    return abs(sum_T - 2*ma)

runtests ( kontenerowiec )
    