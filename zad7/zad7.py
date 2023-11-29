#Wiktor Warzecha
#Algorytm przekształca dane wejściowe na tablicę tablic zawierających liczby
#(-2 reprezentuje pokój zamknięty, -1 pokój nieodwiedzony, inne liczby oznaczają
#długość ścieżki która do nich doprowadziła). Korzystając z tego, że Wojownik
#może poruszać się tylko w 3 kierunkach ( nie może w lewo ), algorytm rozwiązuje
#problem "od lewej do prawej". Pierwsza iteracja to przypisanie wartości w pierwszej
#kolumnie, gdyby wojownik poruszał się tylko w dół, tak długo aż natrafi na zamkniętą
#komnatę. Kolejne iteracje do momentu dojścia do ostatniej kolumny to wykonanie ruchu
#w prawo, który jeśli jest możliwy daje zawsze ścieżkę dłuższą niż ta z której wychodzi
#(dzieje się to przez zmianę wartości w tablicy L). Następnie sprawdzenie ścieżek idących 
#tylko w górę i tylko w dół, gdzie ich długości są zapisywane w osobnych tablicach 
# długości n (tablice U i D). Po tym tablica L jest nadpisywana, jeżeli na jakieś pole 
#da się dojść dłuższą ścieżka. Ostatnia iteracja rozpatruje tylko ruchy w prawo i w dół.
#Złożoność O(n^2)

from zad7testy import runtests

def right_move(L,column):
    not_visited = -1
    locked = -2
    n = len(L)
    for row in range(n):
        if L[row][column-1] > not_visited and L[row][column] is not locked:
            L[row][column] = L[row][column - 1] + 1

def up_move(U):
    n = len(U)
    not_visited = -1
    locked = -2
    for row in range(n-2,-1,-1):
        if U[row + 1] > not_visited and U[row] is not locked and U[row + 1] + 1 > U[row]:
            U[row] = U[row + 1] + 1

def down_move(D):
    n = len(D)
    not_visited = -1
    locked = -2
    for row in range(1,n):
        if D[row-1] > not_visited and D[row] is not locked and D[row - 1] + 1 > D[row]:
            D[row] = D[row - 1] + 1

def maze( L ):
    locked = -2
    n = len(L)
    
    for row in range (n):
        tmp = L[row]
        L[row] = []
        for column in range (n):
            if tmp[column] == "#":
                L[row].append(-2)
            else:
                L[row].append(-1)
    
    L[0][0] = 0
    row = 1

    while row < n and L[row][0] is not locked:
        L[row][0] = row
        row += 1

    for column in range (1,n-1):
        right_move(L,column)

        D,U = [], []
        for row in range(n):
            D.append(L[row][column])
            U.append(L[row][column])
        
        down_move(D)
        up_move(U)

        for row in range(n):
            if D[row] > U[row]:
                L[row][column] = D[row]
            else:
                L[row][column] = U[row]
    
    right_move(L,n-1)
    D = []
    for row in range(n):
            D.append(L[row][n-1])
    down_move(D)
    for row in range(n):
        if D[row] > L[row][n-1]:
            L[row][n-1] = D[row]

    return L[n-1][n-1]



# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( maze, all_tests = True )
