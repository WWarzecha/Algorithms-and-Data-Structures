# Wiktor Warzecha 415660
# Algorytm uruchamia no_robbery_djikstra dla s (zwykład djikstra) i robbery_djikstra (zmodyfikowana do warunków
# po kradzieży) dla t. Następnie za minimalny koszt przyjmuje koszt drogi z s do t bez rabowania zamku. Później
# dla każdego i-tego wierzchołka oblicza koszt drogi, jeśli złycerz obrabuje i-ty zamek. Wykorzystuje do tego
# tablice kosztów z wcześniej wywołanych djikstr.
# Złożoność O(V^2 * logV)

from egz1Atesty import runtests
from queue import PriorityQueue

def gold(G,V,s,t,r):
  n = len(V)

  def dijkstra(M, s):
    inf = float('inf')
    n = len(M)
    d = [inf for _ in range(n)]
    q = PriorityQueue()

    q.put((0, s))

    while not q.empty():
        distance, u = q.get()
        if d[u] == inf:
            d[u] = distance
            for (v, w) in M[u]:
                if d[v] == inf:
                    q.put((d[u] + w, v))
    return d

  def robbery_djikstra(M, s):
    nonlocal r
    inf = float('inf')
    n = len(M)
    d = [inf for _ in range(n)]
    q = PriorityQueue()
    
    q.put((0, s))

    while not q.empty():
        distance, u = q.get()
        if d[u] == inf:
            d[u] = distance
            for (v, w) in M[u]:
                if d[v] == inf:
                    q.put((d[u] + 2*w + r, v))
    return d

  no_robbery_travel = dijkstra(G,s)
  robbery_travel = robbery_djikstra(G,t)
  min_cost = no_robbery_travel[t]

  for i in range(n):
        min_cost = min(min_cost, no_robbery_travel[i] + robbery_travel[i] - V[i])

  return(min_cost)  

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( gold, all_tests = True )
