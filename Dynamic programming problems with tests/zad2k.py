from zad2ktesty import runtests



def palindrom( S ):
    #print(S)
    #print(type(S),type(str(S)))
    #print(len(S))
    #t = str(S)
    n = len(S)
    max = 1
    pali = ""
    for i in range(n):

        #palindromy nieparzyste
        counter = 1
        j = i - 1
        k = i + 1
        
        while j > -1 and k < n and S[j] == S[k]:
            counter += 2
            j -= 1
            k += 1
        if counter > max:
            max = counter
            pali = S[j+1:k]
        
        #palindromy parzyste

        counter = 0
        l = i
        m = i + 1

        while l > -1 and m < n and S[l] == S[m]:
            counter += 2
            l -= 1
            m += 1
        if counter > max:
            max = counter
            pali = S[l+1:m]
    return pali


runtests ( palindrom )