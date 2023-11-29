from zad8ktesty import runtests 
import time

def napraw ( s, t ):
    print(s,t)
    F = [[-1 for _ in range (len(s))] for _ in range (len(t))]

    if s[0] == t[0]:
        F[0][0] = 0
    else:
        F[0][0] = 1
    for e in F:
        print(e)
    for i in range (1,len(t)):
        if s[0] == t[i]:
            F[i][0] = F[i-1][0]
        else:
            F[i][0] = F[i-1][0] + 1
    print("\n")
    for e in F:
        print(e)
    for i in range (1,len(s)):
        if t[0] == s[i]:
            F[0][i] = F[0][i-1]
        else:
            F[0][i] = F[0][i-1] + 1
    print("\n")
    for e in F:
            print(e)
    for i in range (1,len(s)):
        for j in range (1,len(t)):
            if s[i] == t[j]:
                F[j][i] = F[j-1][i-1]
            else:
                F[j][i] = min(F[j-1][i-1],F[j][i-1],F[j-1][i])
                F[j][i] += 1
    print("\n")
    for e in F:
        print(e)
    input()
    return(F[len(t)-1][len(s)-1])

runtests (napraw)

