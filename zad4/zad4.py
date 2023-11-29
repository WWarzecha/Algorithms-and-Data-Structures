#Wiktor Warzecha
#Algorytm wyszukuje BFS-em najktórszą ścieżkę. Następnie
#sprawdza podgrafy bez kolejnych krawędzi z tej ścieżki.
#Jeżeli taki podgraf ma dłuższą najkrótszą ściężkę, zwraca
#usuniętą krawędź.
#Złożoność O(V(V+E))

from zad4testy import runtests

def BFS(G,s,t,flag):
    Q = []
    n = len(G)
    d = [-1 for _ in range(n)]
    parent = [None for _ in range(n)]
    visited = [False for _ in range(n)]
    d[s] = 0
    parent[s] = None
    visited[s] = True
    Q.append(s)
    while Q:
        u = Q.pop(0)
        for v in G[u]:
            if not visited[v]:
                parent[v] = u
                d[v] = d[u] + 1
                visited[v] = True
                Q.append(v)
        if visited[t]:
            break
    if visited[t] == False:
        return None
    if not flag:
        return (parent, d[t])
    return d[t]

def longer( G, s, t ):
    tmp = BFS(G, s, t, False)
    shortest = tmp[1]
    p = tmp[0]
    i = t
    while p[i] != None:
        u = i
        v = p[i]
        G[u].remove(v)
        G[v].remove(u)
        tmp = BFS(G,s,t,True)
        if tmp == None or tmp>shortest:
            return (u,v)
        G[u].append(v)
        G[v].append(u)
        i = v
    return None

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(longer, all_tests = True)
