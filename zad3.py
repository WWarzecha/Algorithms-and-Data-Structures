#Wiktor Warzecha
#Algorytm przy pomocy mergesorta sortuje
#alfabetycznie tablicę, następnie dla 
#każdego elementu zlicza jego ilość, oraz
#jeżeli nie jest palindromem przy pomocy
#przeszukiwania binarnego, szuka czy i gdzie
#znajduje się dane słowo od tyłu. Później
#porównuje to z maksymalną ilością wystąpień
#Złożoność O(N + nlogn)

from zad3testy import runtests

def binary_search(T, s):
    beg = 0
    end = len(T)-1
    while beg <= end:
        range = (end-beg)//2 + beg
        if T[range] == s:
            while range > 0 and T[range-1] == s:
                range -= 1
            return range
        elif T[range] > s:
            end = range - 1
        else:
            beg = range +1
    return -1

def merge(T,L,R):
    t, l, r = 0, 0, 0
    while l < len(L) and r < len(R):
        if L[l] <= R[r]:
            T[t] = L[l]
            l += 1
        else:
            T[t] = R[r]
            r += 1
        t += 1
    while l < len(L):
        T[t] = L[l]
        t += 1
        l += 1
    while r < len(R):
        T[t] = R[r]
        t += 1
        r += 1

def mergesort(T):
    if len(T) == 2:
        if T[0] > T[1]:
            T[0], T[1] = T[1], T[0]
    elif len(T)>1:
        mid = len(T)//2
        L = T[:mid]
        R = T[mid:]
        mergesort(L)
        mergesort(R)
        merge(T,L,R)




def strong_string(T):
    n = len(T)
    counter = 1
    max = 0
    n = len(T)
    mergesort(T)
    i = 0
    while i < n:
        while i+1 < n and T[i+1] == T[i]:
            counter += 1
            i += 1
        s = T[i][::-1]
        j = -1
        if s != T[i]:
            j = binary_search(T, s)
        if j != -1:
            counter += 1
            while j + 1 < n and T[j+1] == s:
                j += 1
                counter += 1
        if counter > max:
            max = counter
        counter = 1
        i += 1
    return max

# # zmien all_tests na True zeby uruchomic wszystkie testy
runtests( strong_string, all_tests=True )
