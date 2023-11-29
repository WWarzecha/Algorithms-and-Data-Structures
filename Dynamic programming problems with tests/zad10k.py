from zad10ktesty import runtests
import math

def dywany ( N ):
    inf = float('inf')
    F = [inf] * (N+1)
    P = [None] * (N+1)
    F[0] = 0
    for i in range (1,N+1):
        tmp = 1
        while i - tmp*tmp > -1:
            if F[i - tmp*tmp] + 1 < F[i]:
                F[i] = F[i - tmp*tmp] + 1
                P[i] = i - tmp*tmp
            tmp += 1
    path = []
    par = N
    while P[par] != None:
        path.append(int(math.sqrt(par-P[par])))
        par = P[par]
    return path


runtests( dywany )

