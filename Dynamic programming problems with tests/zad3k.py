from zad3ktesty import runtests

def min_elem(T):
    n = len(T) # == k
    minimal = float('inf')
    for i in range (n):
        if T[i] < minimal:
            minimal = T[i]
    return minimal

def ksuma( T, k ):
    min = float('inf')
    F = []
    n = len(T)

    for i in range (k):
        F.append(T[i])
    
    for i in range (k,n):
        p = min_elem(F)
        T[i] += p
        F.pop(0)
        F.append(T[i])
    
    for i in range(n-k,n):
        if T[i] < min:
            min = T[i]

    return min
    
runtests ( ksuma )