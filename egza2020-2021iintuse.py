
def intuse(T,x,y):
    n = len(T)
    T.sort()
    P = [[] for _ in range (n)]
    
    for i in range(n):
        if T[i][0] == x and T[i][1] <= y:
            P[i].append(i) 
    
    for i in range(n):
        if T[i][0] > x and T[i][1] <= y:
            for j in range (0,n):
                if T[j][0] >= x and T[j][1] == T[i][0]:
                    P[i].append(j)
    
    print(P)


T = [(1,3),(1,4),(2,5),(3,4),(4,6)]
intuse(T,1,6)

