from collections import deque

def DFS(G):
    def DFSvisit(G, s):
        nonlocal time
        nonlocal times
        visited[s]=True
        for x in G[s]:
            if not visited[x]:
                DFSvisit(G, x)
        time+=1
        times[s]=(time, s)

    n = len(G)
    times = [0 for i in range(n)]
    visited = [False for i in range(n)]
    time = 0
    for i in range(n):
        if not visited[i]:
            DFSvisit(G, i)

    return times

def DFSnext(G, n, times, pozycje):

    def DFSvisit(G, s):
        nonlocal pozycje
        nonlocal skladowa
        times[pozycje[s]]=None
        skladowa.append(s)

        for x in G[s]:
            if times[pozycje[x]] is not None:
                DFSvisit(G, x)

    skladowa=[]
    DFSvisit(G, n)
    return skladowa




def skladowe(G):
    times = DFS(G)
    n=len(G)
    Graf = [[] for i in range(n)]
    for i in range(n):
        for j in G[i]:
            Graf[j].append(i)

    times=sorted(times, reverse=True)
    print(times)
    pozycje = [0 for i in range(n)]
    for i in range(n):
        pozycje[times[i][1]]=i

    zbior = []

    for x in times:

        if x is not None:
            zbior.append(DFSnext(Graf, x[1], times, pozycje))

    return zbior

G = [[1],
     [2, 4],
     [0, 9],
     [4, 6],
     [5],
     [3],
     [5],
     [9],
     [3, 7],
     [10],
     [5, 8]]
print(skladowe(G))