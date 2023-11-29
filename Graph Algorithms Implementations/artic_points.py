def DFS(G):
    def DFSvisit(G, s):
        nonlocal time
        time+=1
        visited[s]=True
        times[s]=time
        low[s]=times[s]
        for x in G[s]:
            if not visited[x]:
                parent[x]=s
                DFSvisit(G, x)
            # else:
            #     if low[x]<low[s] and x != parent[s]:
            #         low[s]=low[x]
        for x in G[s]:
            if low[x] < low[s] and x != parent[s]:
                low[s] = low[x]
        for x in G[s]:
            if s == parent[x]:
                low[s]=min(low[s], low[x])





    n=len(G)
    time = 0
    low = [0 for i in range(n)]
    times = [0 for i in range(n)]
    parent = [0 for i in range(n)]
    visited = [False for i in range(n)]
    parent[0]=None
    licznik = 0
    punkty = []
    DFSvisit(G, 0)
    for x in G[0]:
        if parent[x] == 0:

            licznik+=1
    if licznik>1:
        punkty.append(0)
    for i in range(1, n):
        for x in G[i]:
            if parent[x] == i and low[x]>=times[i]:
                punkty.append(i)
                break
    return punkty



#G = [[1, 2], [0, 3], [0, 4, 3], [1, 2, 5], [2], [3, 6, 7], [5, 7], [5, 6]]

G=[
    [3,5,6],
    [2,4,7],
    [1,7],
    [0,5,6],
    [1,6],
    [0,3],
    [0,3,4],
    [1,2,8],
    [8]

]
print(DFS(G))