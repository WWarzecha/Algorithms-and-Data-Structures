'''
Wiktor Warzecha
Istotą tego rozwiązania jest zauważenie,
że przy obliczaniu maksymalnej ilości
śniegu którą można zebrać nie trzeba
uwzględniać kolejności w której śnieg
z konkretnych pól będzie zbierany.
Z tego powodu algorytm sortuje tablicę,
i w pętli while która dodaje kolejne
największe wartości z tablicy,
uwzględniając przy tym ilość śniegu
która stopnieje z danego pola (jest to
ilość zebranych wcześniej pól -1).
Quicksort jest implementacją przedsta-
wioną na ćwiczeniach.
'''
from zad2testy import runtests

def partition(T, left, right):
    if (left >= right):
        return left
    pivot = T[right]
    j = left
    for i in range(left, right, 1):
        if(T[i] < pivot):
            T[i],T[j] = T[j],T[i]
            j += 1
    T[right], T[j] = T[j], T[right]
    return j

def quicksort(T,left,right):
    while(left<right):
        pivot = partition(T, left, right)
        if(right-pivot > pivot-left):
            quicksort(T,left,pivot-1)
            left = pivot+1
        else:
            quicksort(T,pivot+1,right)
            right = pivot-1

def snow( S ):
    n = len(S) - 1
    quicksort(S,0,n)
    sum = S[n]
    n -= 1
    i = 1
    while(sum < sum+S[n]-i and n > -1):
        sum += (S[n]-i)
        i += 1
        n -= 1
    return sum

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( snow, all_tests = True )