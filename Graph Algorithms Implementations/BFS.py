from queue import Queue

def BFS(G,s):
    n = len(G)
    q = Queue()
    
    visited = [False]*n
    distance = [-1]*n
    parent = [None]*n

    distance[s] = 0
    visited[s] = True
    parent[s] = None
    q.put(s)

    while not q.empty():
        u = q.get()
        for v in G[u]:
            if not visited[v]:
                distance[v] = distance[u] + 1
                parent[v] = u
                visited[v] = True
                q.put(v)
    
    return distance, parent, visited


G = [
    [1,2],
    [3],
    [0],
    [1]
]
print(BFS(G,0))