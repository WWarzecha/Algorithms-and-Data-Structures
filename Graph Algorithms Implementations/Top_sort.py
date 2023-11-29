from queue import Queue

def DFS(G):
    n = len(G)
    time = 0
    index = n-1
    result = []#[None]*n
    visited = [False]*n
    parent = [None]*n

    def DFS_visit(G,u):
        nonlocal time
        nonlocal visited
        nonlocal parent
        nonlocal result

        time += 1
        visited[u] = True

        for v in G[u]:
            if not visited[v]:
                parent[v] = u
                DFS_visit(G,v)
        result.append(u)
        time += 1

    for u in range(n):
        if not visited[u]:
            print("dasfasdf",u)
            DFS_visit(G,u)
    return result

G = [[1, 3], [2, 4], [], [1, 2], [2]]
print(DFS(G))
