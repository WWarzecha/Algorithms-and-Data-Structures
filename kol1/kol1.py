'''
Wiktor Warzecha
Algorytm tworzy tmp_arr zawierającą wartości z tablicy T
pod indeksami od beg do end włącznie (0 do p-1 przy pierwszym
stworzeniu). Następnie przy pomocy quickselecta wybiera k-ty
największy element i dodaje go do sumy. Później usuwa wartość
któa znajduje się pod T[beg], przesuwa "wskaźniki" beg i end,
w celu przejścia przez wszystkie przedziały w tablicy i powtarza
ten proces, do momentu w którym end nie wyjdzie za tablicę.
na koniec zwraca sumę.
Złożoność O(np)
'''

from kol1testy import runtests
from random import randint

def partition(T,p,r):
    q = randint(0,r-p) + p
    x = T[q]
    T[q], T[r] = T[r], T[q]
    i = p - 1
    for j in range(p, r):
        if T[j] <= x:
            i += 1
            T[i], T[j] = T[j], T[i]
    T[i+1], T[r] = T[r], T[i+1]
    return i+1

def quickselect(T,k,p,r):
     q = partition(T, p, r)
     if q == k:
          return T[q]
     elif q > k:
          return quickselect(T, k, p, q-1)
     else:
          return quickselect(T, k, q+1, r)

def ksum(T, k, p):
    beg = 0
    end = p-1
    sum = 0
    tmp_arr = [T[g] for g in range (beg,end)]
    while end < len(T):
        tmp_arr.append(T[end])
        kth_elem = quickselect(tmp_arr, p-k, 0 , p-1)
        sum += kth_elem
        tmp_arr.remove(T[beg])
        beg += 1
        end += 1
    return sum

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( ksum, all_tests=True )
