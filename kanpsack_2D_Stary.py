# Zadanie 5 (dwuwymiarowy problem plecakowy) 
# Proszę zaproponować algorytm dla dwuwymiarowej
# wersji dyskretnego problemu plecakowego. Mamy dany zbiór P = {p1, . . . , pn} przedmiotów i dla każdego
# przedmiotu pi dane sa nastepujace trzy liczby:
# 1. v(pi) – wartość przedmiotu,
# 2. w(pi) – waga przedmiotu, oraz
# 3. h(pi) – wysokość przedmiotu.
# Złodziej chce wybrać przedmioty o maksymalnej wartości, których łączna waga nie przekracza danej liczby
# W oraz których łączna wysokość nie przekracza danej liczby H (przedmioty zapakowane są w kartony, które
# złodziej układa jeden na drugim). Proszę oszacować złozoność czasową swojego algorytmu oraz uzasadnić
# jego poprawność.

def knapsack2D(P, W, H, maxW, maxH):
    n = len(P)
    Pa = [[[[None]*3 for _ in range (maxW + 1)] for _ in range (maxH + 1)] for _ in range (n+1)]
    F = [[[-1 for _ in range (maxW + 1)] for _ in range (maxH + 1)] for _ in range (n+1)]
    F[0][0][0] = 0
    # P[0][0][0] =
    for i in range (n):
        for w in range (maxW+1):
            for h in range (maxH+1):
                if i < n:
                    if F[i+1][h][w] < F[i][h][w]:
                        Pa[i+1][h][w] = [i,h,w]
                    F[i+1][h][w] = max(F[i][h][w],F[i+1][h][w])
                if h+H[i] <= maxH and w+W[i] <= maxW and i < n:
                    if F[i+1][h+H[i]][w+W[i]] < F[i][h][w] + P[i]:
                        Pa[i+1][h+H[i]][w+W[i]] = [i,h,w]
                    F[i+1][h+H[i]][w+W[i]] = max(F[i+1][h+H[i]][w+W[i]],F[i][h][w] + P[i])
    for i in range(n+1):
        j = MaxC
        l = 0
        print(F[i][l][j])
    return
    # for e in F:
    #     print(e)
    # input()
    ma = -1
    for i in range (n+1):
        for j in range (maxW+1):
            for k in range (maxH+1):
                if F[i][k][j] > ma:
                    ma = F[i][k][j]
                    p_max = [i,k,j]
    
    path = []
    while Pa[p_max[0]][p_max[1]][p_max[2]][0] != None:
        p_next = Pa[p_max[0]][p_max[1]][p_max[2]]
        if p_max[1] - p_next[1] != 0 and p_max[2] - p_next[2] != 0:
            path.append(p_max[0]-1)
        p_max = p_next

    return ma, path

# P = [4, 10, 2, 3, 8]
# W = [10, 4, 1, 2, 6]
# H = [3, 9, 12, 4, 2]

# MaxW = 12
# MaxH = 20

# P = [4, 10, 2, 3, 8]
# W = [10, 6, 1, 2, 6]
# H = [3, 9, 12, 4, 9]
C = [10,21,18,15,2,17]
S = [1,0,1,0,1,1]
V = [5,12,28,37,15,21]
MaxS = 3
MaxC = 30

print(knapsack2D(V, C, S, MaxC, MaxS))