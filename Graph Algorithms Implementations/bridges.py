def DFS(G): #tu jest czas odwiedzenia

    def DFSvisit(G, s):
        nonlocal times
        nonlocal parent
        nonlocal visited
        nonlocal low
        nonlocal time
        nonlocal mosty
        time+=1
        times[s]=time
        visited[s]=True
        low[s]=time
        for x in G[s]:
            if not visited[x]:
                parent[x]=s
                DFSvisit(G, x)
            else:
                if parent[s]!=x:
                    if low[x]<low[s]:
                        low[s]=low[x]
        for x in G[s]:
            if parent[x]==s:
                low[s]=min(low[s], low[x])

        if low[s]==times[s]:
            if parent[s] is not None:
                mosty.append((s, parent[s]))

    n=len(G)
    visited = [False for i in range(n)]
    parent=[None for i in range(n)]
    times = [2**12 for i in range(n)]
    low = [2**12 for i in range(n)]
    mosty=[]
    time=0
    DFSvisit(G, 0)
    return mosty


G = [[1, 2], [0, 3], [0, 4, 3], [1, 2, 5], [2], [3, 6, 7], [5, 7], [5, 6]]
print(DFS(G))