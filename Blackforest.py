# Zadanie 1. (Black Forest) 
#Black Forest to las rosnący na osi liczbowej gdzieś w południowej Anglii. Las
# składa się z n drzew rosnących na pozycjach 0, . . . , n−1. Dla każdego i ∈ {0, . . . , n−1} znany jest zysk ci
# , jaki
# można osiągnąć ścinając drzewo z pozycji i. John Lovenoses chce uzyskać maksymalny zysk ze ścinanych
# drzew, ale prawo zabrania ścinania dwóch drzew pod rząd. Proszę zaproponować algorytm, dzięki któremu
# John znajdzie optymalny plan wycinki.

def max_profit(C):
    n = len(C)
    F = [-1]*n
    F[0] = C[0]
    F[1] = C[1]
    for i in range (2,n):
        F[i] = max(F[i-1],C[i]+F[i-2])
    return F[n-1]

T = [8, 12, 3, 4, 7, 1, 2, 10]

print(max_profit(T))
