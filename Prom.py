# Zadanie 3. (ładowanie promu)
# Dana jest tablica A[n] z długościami samochodów, które stoją w kolejce,
# żeby wjechać na prom. Prom ma dwa pasy (lewy i prawy), oba długości L. Proszę napisać program, który
# wyznacza, które samochody powinny pojechać na który pas, żeby na promie zmieściło się jak najwięcej aut.
# Auta muszą wjeżdżac w takiej kolejności, w jakiej są podane w tablicy A

def ferry(A,L):
    n = 0
    sum = 0
    while n < len(A) and sum+A[n] <= 2*L:
        n += 1
        sum += A[n]
    A = A[:n]
    F = [[[-1 for _ in range (L+1)] for _ in range (L+1)] for _ in range (n+1)]
    P = [[[None for _ in range (L+1)] for _ in range (L+1)] for _ in range (n+1)]
    F[0][L][L] = 0
    P[0][L][L] = [None]*3
    for i in range (n):
        for j in range (L,-1,-1):
            for k in range (L,-1,-1):
                if F[i][j][k] == i:
                    if -1 < i  < n and -1 < j - A[i]:
                        # print(i+1)
                        if F[i+1][j-A[i]][k] < i + 1:
                            F[i+1][j-A[i]][k] = i + 1
                            P[i+1][j-A[i]][k] = [i,j,k]

                    if -1 < i  < n and -1 < k - A[i]:
                        if F[i+1][j][k-A[i]] < i + 1:
                            F[i+1][j][k-A[i]] = i + 1
                            P[i+1][j][k-A[i]] = [i,j,k]
    ma = -1
    for i in range(n+1):
        for j in range (L):
            for k in range (L):
                if F[i][j][k] > ma:
                    ma = F[i][j][k]
                    P_max = [i,j,k]
    UD = []
    while P[P_max[0]][P_max[1]][P_max[2]][0] != None:
        p_next = P[P_max[0]][P_max[1]][P_max[2]]
        if P_max[1]-p_next[1] < 0:
            UD.append("D")
        else:
            UD.append("U")
        P_max = p_next
    return (ma, UD[::-1])


print(ferry([5,6,6,2,8,3,6,17],18))

#L = 1824

#cars = [1516, 723, 498, 211, 308, 392, 634, 439, 263, 123488]

#L = 1824

#cars = [316, 723, 498, 288, 634, 439, 263, 488]
# L = 1824

# cars = [316, 723, 498, 288, 634, 439, 263, 488]
# print(ferry(cars,L))

