def floyd_warshall(G,distance,parents):
    n = len(G)
    for k in range(n):
        for i in range(n):
            for j in range(n):
               if distance[i][j] > distance[i][k] + distance[k][j]:
                   distance[i][j] = distance[i][k] + distance[k][j]
                   parents[i][j] = parents[k][j]


def Floyd_Warshall(graph):
    V = len(graph)
    Distances = [[float('inf') for _ in range(V)] for _ in range(V)]
    Parents = [[None for _ in range(V)] for _ in range(V)]

    for start in range(V):
        for end in range(V):
            if start == end:
                Distances[start][end] = 0
            elif graph[start][end] != 0:
                Distances[start][end] = graph[start][end]
                Parents[start][end] = start

    for fir in range(V):
        for mid in range(V):
            for end in range(V):
                if Distances[fir][end] > Distances[fir][mid] + Distances[mid][end]:
                    Distances[fir][end] = Distances[fir][mid] + Distances[mid][end]
                    Parents[fir][end] = Parents[mid][end]

    return Distances, Parents