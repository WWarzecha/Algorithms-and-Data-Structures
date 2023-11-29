from queue import Queue

def DFS(G):
    n = len(G)
    time = 0

    visited = [False]*n
    parent = [None]*n

    def DFS_visit(G,u):
        nonlocal time
        nonlocal visited
        nonlocal parent

        time += 1
        visited[u] = True

        for v in G[u]:
            if not visited[v]:
                parent[v] = u
                DFS_visit(G,v)
        
        time += 1

    for u in range(n):
        if not visited[u]:
            DFS_visit(G,u)

#spójność
#dwudzielność
#wykrywanie cykli
#sortowanie topologiczne
#silnie spójne składowe
#cykl Eulera
#mosty/punkty artykularne

G = [
    [1,2],
    [3],
    [0],
    [1]
]
DFS(G)
