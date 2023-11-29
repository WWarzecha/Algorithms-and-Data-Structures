from kol1btesty import runtests

def merge(T,L,R):
    t, l, r = 0, 0, 0
    while l < len(L) and r < len(R):
        if L[l] <= R[r]:
            T[t] = L[l]
            l += 1
        else:
            T[t] = R[r]
            r += 1
        t += 1
    while l < len(L):
        T[t] = L[l]
        l += 1
        t += 1
    while r < len(R):
        T[t] = R[r]
        r += 1
        t += 1

def mergesort(T):
    if len(T) == 2:
        if T[0] > T[1]:
            T[0], T[1] = T[1], T[0]
    elif len(T) > 2:
        mid = len(T)//2
        L = T[mid:]
        R = T[:mid]
        mergesort(L)
        mergesort(R)
        merge(T,L,R)

def string_to_arr(s):
    T = [0 for i in range (26)]
    n = len(s)
    for i in range (n):
        T[ord(s[i])-97] += 1
    T = tuple(T)
    return T

def f(T):
    for i in range (len(T)):
        T[i] = string_to_arr(T[i])
    mergesort(T)
    i = 0
    counter = 1
    max = 0
    n = len(T)
    while i < n:
        while i+1 < len(T) and T[i] == T[i+1]:
            i += 1
            counter += 1
        if counter > max:
            max = counter
        counter = 1
        i += 1
    return max

# Zamien all_tests=False na all_tests=True zeby uruchomic wszystkie testy
runtests( f, all_tests=True )
