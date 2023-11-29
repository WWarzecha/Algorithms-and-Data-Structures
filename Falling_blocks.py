# Zadanie 2. (spadające klocki) 
# Każdy klocek to przedział postaci [a, b]. Dany jest ciąg klocków [a1, b1],
# [a2, b2], . . ., [an, bn]. Klocki spadają na oś liczbową w kolejności podanej w ciągu. Proszę zaproponować
# algorytm, który oblicza ile klocków należy usunąć z listy tak, zeby każdy kolejny spadajacy klocek mieścił
# się w całości w tam, który spadł tuż przed nim.

def count_removed_bricks(T):
    n = len(T)
    F = [1] * n
    for i in range (1,n):
        for j in range(0,i):
            print(T[i],T[j])
            if T[j][0] <= T[i][0] and T[j][1] >= T[i][1]:
                F[i] = max(F[i],F[j]+1)
    return n - max(F)

ranges = [(0, 10), (1, 10), (2, 6), (6, 7), (11, 20), (11, 19), (12, 18), (13, 19), (14, 20)]

print(count_removed_bricks(ranges))