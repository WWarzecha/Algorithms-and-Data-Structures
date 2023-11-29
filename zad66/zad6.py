#Wiktor Warzecha
#Algorytm dla każdego pracownika próbuje przypisać maszynę.
#Jeśli maszsyna nie ma nikogo przypisanego wprost zwiększa
#licznik i przypisuje do niej pracownika, w innym wypadku
#rekurencyjnie próbuje przypisać pracę dla pracownika
#dotychczas przypisanego do danej maszyny. W przypadku nie-
#powodzenia pracownik jest pomijany.
#Złożoność O(V(V+E))

from zad6testy import runtests

def binworker(M):

    n = len(M)
    G = [[] for _ in range (n)]
    visited = [False]*n
    is_assigned = [-1]*n
    counter = 0
    def BM(u):
        nonlocal visited
        nonlocal is_assigned
        nonlocal G
        for v in G[u]:
            if not visited[v]:
                visited[v] = True
                if is_assigned[v] < 0 or BM(is_assigned[v]) is True:
                    is_assigned[v] = u
                    return True
        return False
    
    for machine in range (n):
        for worker in M[machine]:
            G[worker].append(machine)

    for v in range (n):
        for i in range (n):
            visited[i] = False
        if BM(v):
            counter += 1
    return counter

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( binworker, all_tests = True )