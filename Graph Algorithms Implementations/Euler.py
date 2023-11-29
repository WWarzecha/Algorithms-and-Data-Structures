def dfs_rec(e, G, path):
    n = len(G)
    for i in range(n):
        if G[e][i] == 1:
            G[e][i] = G[i][e] = 0
            dfs_rec(i, G, path)
    path.append(e+1)


def Euler(G):
    n = len(G)
    total = 0
    for i in range(n):
        total += sum(G[i])
        if total % 2 == 1:
            return False
    path = []
    dfs_rec(0, G, path)
    if total / 2 + 1 != len(path):
        return False
    return path


G = [[0, 1, 1, 0, 0], 
     [1, 0, 1, 0, 0], 
     [1, 1, 0, 1, 1], 
     [0, 0, 1, 0, 1],
     [0, 0, 1, 1, 0]]

print(Euler(G))