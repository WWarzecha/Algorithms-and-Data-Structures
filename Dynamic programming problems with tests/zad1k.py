from zad1ktesty import runtests
import time
def roznica( S ):
    n = len(S)
    F = [-1]*n
    
    for i in range(n):
        counter = 0
        for j in range(i,n):
            if S[j] == "0":
                counter += 1
            else:
                counter -= 1
            F[j] = max(F[j],counter)

    x = -1
    for i in range (n):
        x = max(x, F[i])

    return x

runtests ( roznica )