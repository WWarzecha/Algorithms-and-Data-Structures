def dfs_rec(v, vis, G, posortowane):
    vis[v] = True
    for u in G[v]:
        if not vis[u]:
            dfs_rec(u, vis, G, posortowane)
    posortowane.append(v)


def sortowanie(G):
    n = len(G)
    vis = [False for _ in range(n)]
    posortowowane = []
    for v in range(n):
        if not vis[v]:
            dfs_rec(v, vis, G, posortowowane)
    for i in range(n - 1, 0, -1):
        if posortowowane[i - 1] not in G[posortowowane[i]]:
            return False
    return True


G = [[1, 3], [2, 4], [], [1, 2], [2]]
print(sortowanie(G))
