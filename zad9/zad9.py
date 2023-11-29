#Wiktor Warzecha
#Algorytm działa dynamicznie obliczjąc minimalny koszt z postojem
#na danym ( i-tym ) parkingu, bez użycia wyjątku i z dopuszczeniem 
#jego użycia. Robi to obliczając początkowe edgecase'y, a później
#porównująć poprzednie koszty w zasięgu i-tego parkingu.
#Złożoność O(n^2)

from zad9testy import runtests
import time

O = [5,11,12,17,20]
C = [9,7,3,7,7]
T = 7
L = 25

def min_cost( O, C, T, L ):
    inf = float('inf')
    n = len(O)
    distance, price, without_2T, with_2T = 0, 1, 0, 1

    def stay_without_2T(i):
        nonlocal F
        nonlocal O
        nonlocal T
        nonlocal n
        distance, price, without_2T, with_2T = 0, 1, 0, 1
        j = i - 1
        while j > -1 and O[i][distance] - O[j][distance] < T + 1:
            #print("BEZ: ",F[j][without_2T], F[i][without_2T])
            if F[j][without_2T] < F[i][without_2T]:
                F[i][without_2T] = F[j][without_2T]
            j -= 1
        F[i][without_2T] += O[i][price]

    def stay_with_2T(i):
        nonlocal F
        nonlocal O
        nonlocal T
        nonlocal n
        distance, price, without_2T, with_2T = 0, 1, 0, 1
        j = i - 1
        while j > -1 and O[i][distance] - O[j][distance] <= T + 1:
            print(F[j][with_2T], F[i][with_2T])
            if F[j][with_2T] < F[i][with_2T]:
                F[i][with_2T] = F[j][with_2T]
            j -= 1
        while j > -1 and O[i][distance] - O[j][distance] <= 2*T + 1:
            if F[j][without_2T] < F[i][with_2T]:
                F[i][with_2T] = F[j][without_2T]
            j -= 1
        F[i][with_2T] += O[i][price]
        if F[i][without_2T] < F[i][with_2T]:
            F[i][with_2T] = F[i][without_2T]

    F = [[inf,inf] for _ in range (n)]

    for i in range (n):
        O[i] = [O[i],C[i]]
    O = sorted(O)

    i = -1
    
    while i + 1 < n and O[i + 1][distance] <= T:
        i += 1
        F[i][without_2T] = O[i][price]

    without_2T_edgecase = i
    
    while i + 1 < n and O[i + 1][distance] <= 2*T:
        i += 1
        F[i][with_2T] = O[i][price]
    with_2T_edgecase = i

    for i in range (without_2T_edgecase+1,with_2T_edgecase+1):
        print(F)
        stay_without_2T(i)
    
    for i in range (with_2T_edgecase+1,n):
        print(F)
        stay_without_2T(i)
        stay_with_2T(i)
    
    i = n-1
    min = inf

    while i > -1 and O[i][distance] + T + 1 >= L:
        if F[i][1] < min:
            min = F[i][1]
        if F[i][0] < min:
            min = F[i][0]
        i -= 1
    print(n,T,F)
    time.sleep(100)
    return min

min_cost(O,C,T,L)

# zmien all_tests na True zeby uruchomic wszystkie testy
#runtests( min_cost, all_tests = True )
