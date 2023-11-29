# Wiktor Warzecha
# Iterujemy po wszystkich elementach wybierając 
# środek palindromu (s[i]). Później tak długo jak kolejne elementy 
# oddalone o curr_length od i-tego elementu są takie same, 
# dodajemy 1 do curr_length gdy spradzany palindrom się skończy,
# porównujemy jego długość z longest (zmienna przechowująca 
# długość najdłuższego palindromu)
# złożoność O(n^2)

from zad1testy import runtests
import time

def ceasar( s ):
    longest = 1
    n = len(s)

    if n == 0:
        return 0

    for i in range (n):
        curr_length = 1
        while i-curr_length > -1 and i+curr_length < n and s[i-curr_length] == s[i+curr_length]:
            curr_length += 1
        tmp = 2*(curr_length-1)+1
        if (tmp > longest):
            longest = tmp

    return longest

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( ceasar , all_tests = True )