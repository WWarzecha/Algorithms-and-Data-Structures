
def max_length_merge(A, k):
    inf = float('inf')
    a, b, length = 0, 1, 2
    n = len(A)
    A.sort()
    for i in range (n):
        A[i] = [A[i][a],A[i][b],A[i][b]-A[i][a]]
    F = [[-inf for _ in range (n)] for _ in range (k)]
    for i in range (n):
        segment = A[i]
        F[0][i] = segment[length]

    for i in range(1,k):
        for j in range(i-1,n):
            for l in range(i-1,j):
                if A[l][b] == A[j][a]:
                    F[i][j] = max(F[i][j], F[i-1][l] + A[j][length])

    ma = -inf
    for i in range (k):
        for j in range (n):
            if F[i][j] > ma:
                ma = F[i][j]
    
    for e in A:
        print(e)
    for e in F:
        print(e)
    
    return ma


# A = [[4.1, 5.2], [2.15, 4.4], [1.5, 3.2], [3.2, 6.83], [5.2, 7.1], [1.2, 5.2], [-5.75, 2.15]]
# #                     ^                                                               ^

# print(max_length_merge(A,4))

E = [(0,2),(1,2), (2,4), (3,6), (4,5), (5,10), (5,9)]
k = 3

print(max_length_merge(E,k))