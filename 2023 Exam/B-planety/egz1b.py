# Wiktor Warzecha 415660
# Algorytm tworzy tablicę F do zapamiętywania wartości. F[i][b] to minimalny koszt dotarcia na i-tą
# planetę posiadając b ton paliwa. Mamy kilka możliwości dotarcia na dane pole. Przylecieć z poprzedniej
# planety bezpośredio na "F[i][b]", przeteleportować się na F[i][0] i dotankować, lub dotankować z pól
# niżej. Algorytm rozważa wszystkie te opcje, wybierając najkorzystniejszą. Jest on iteracyjną wersją
# problemu rekurencyjnego, a edgecase'y są obliczane w osobnej pętli, przed "pętlą główną".
# Złożoność O(nE)

from egz1btesty import runtests

def planets( D, C, T, E ):
    inf = float('inf')
    n = len(D)
    F = [[inf for _ in range (E+1)] for _ in range (n)]

    for j in range(E+1):    #   Edgecase
        F[0][j] = j*C[0]
    
    edge_teleport = T[0]    #   Teleport edgecase
    F[edge_teleport[0]][0] = edge_teleport[1]

    for i in range(1,n):

        if D[i]-D[i-1] < E+1:   #   Teleport
            F[i][0] = min(F[i][0], F[i-1][D[i]-D[i-1]])
        tp_destination, tp_prize = T[i]
        if i != tp_destination:
            F[tp_destination][0] = min(F[tp_destination][0],F[i][0] + tp_prize)
        

        for j in range(1,E+1):
            F[i][j] = min(F[i][j],F[i][j-1] + C[i])
            if D[i]-D[i-1] <= E and j + D[i] - D[i-1] < E+1:
                F[i][j] = min(F[i][j],F[i-1][j+D[i]-D[i-1]])

    return F[n-1][0]

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( planets, all_tests = True )

