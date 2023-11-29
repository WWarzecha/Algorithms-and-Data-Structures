from zad2testy import runtests
from copy import deepcopy
from time import sleep

def mergesort_with_pos(T, pos):
    if len(T) == 2:
        if T[0][pos] > T[1][pos]:
            T[0], T[1] = T[1], T[0]
    if len(T) > 2:
        mid = len(T)//2
        L = T[mid:]
        R = T[:mid]
        mergesort_with_pos(L, pos)
        mergesort_with_pos(R, pos)
        l = r = t = 0
        while l < len(L) and r < len(R):
            if L[l][pos] <= R[r][pos]:
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
    if len(T) > 2:
        mid = len(T)//2
        L = T[mid:]
        R = T[:mid]
        mergesort(L)
        mergesort(R)
        l = r = t = 0
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

def counting_sort(A, T, pos):
    n = len(A)
    C = [0 for _ in range (n)]
    B = [0 for _ in range (len(T))]
    for e in A:
        B[e[pos]] += 1
    for i in range (1, len(B)):
        B[i] += B[i-1]
    for i in range (len(B)):
        T[i] = B[i]
    for i in range (-1,-n-1,-1):
        C[B[A[i][pos]]-1] = A[i]
        B[A[i][pos]] -= 1
    for i in range(n):
        A[i] = C[i]
    
def quick_sort(A, p, r):
	while p < r:
		q = partition(A, p, r)
		quick_sort(A, p, q-1)
		p = q + 1

def partition(A, p, r):
	a = A[r][0]
	b = A[r][1]
	i = p - 1
	
	for j in range(p, r):
		if A[j][0] < a or ( A[j][0] == a and A[j][1] >= b ):
			i += 1
			A[i],A[j] = A[j],A[i]
		
	A[i+1],A[r] = A[r],A[i+1]

	return i+1

def binary_search(T,n,pos):
    left = 0
    right = len(T)
    while left<right:
        range = (right-left)//2 + left
        if T[range][pos] == n:
            return range
        elif T[range][pos] > n:
            right = range - 1
        else:
            left = range + 1
    return -1

def depth(L):
    quick_sort(L, 0, len(L)-1)
    n = len(L)
    i = 0
    while i < n:
        counter = 0
        while i + 1 < n and L[i+1] == L[i]:
            L[i][0] = 0
            counter += 1
            i += 1
        L[i][0] = counter
        counter = 0
        i += 1
    for i in range (n):
        L[i][0] -= i
    
    mergesort_with_pos(L,1)
    for i in range (n):
        L[i] = L[i][0] + i
    return max(L)

def qucikselect(T,k,p,r):
     #if p == r:
     #     return T[p]
     q = partition(T, p, r)
     if q == k:
          return T[q]
     elif q > k:
          return qucikselect(T, k, p, q-1)
     else:
          return qucikselect(T, k, q+1, r)

#from zad2testy import runtests


'''
def depth(L):
	n = len(L)
	quick_sort(L, 0, n-1)
	max_zawieranie = 0
	start = 0
	flaga = True
	
	while flaga:
		zawieranie = 0
		flaga = False
	
		for y in range(start+1, n):
			if L[start][1] < L[y][1]:
				if not flaga:
					new_start = y
					flaga = True
				
				if L[start][1] < L[y][0]:
					break
			else:
				zawieranie += 1
		
		if flaga:
			start = new_start
		
		if zawieranie > max_zawieranie:
			max_zawieranie = zawieranie
	
		if max_zawieranie >= n-start-1:
			break
	
	return max_zawieranie
'''

runtests( depth )