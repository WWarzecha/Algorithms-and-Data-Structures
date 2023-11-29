from zad6ktesty import runtests 

def haslo ( S ):
    n = len(S)
    F = [0]*(n)

    if F[0] != "0":
        F[0] = 1
    if F[0:2] != "00":
        F[1] = 1
    if S[0:2] < "27":
        F[1] += 1

    for i in range (2,n):
        if S[i:i+1] != "0":
            F[i] += F[i-1]
        if 9 < int(S[i-1:i+1]) < 27 and S[i-1:i+1] != "00":
            F[i] += F[i-2]
    return F[n-1]

runtests ( haslo )

# from zad6ktesty import runtests 

# def haslo ( S ):
#     print(S)
#     n = len(S)
#     F = [0]*(n)
#     F[0] = 1
#     F[1] = 1
#     if F[0] != "0":
#         F[0] == 1
#     if F[0:2] != "00":
#         F[1] = 1
#     if S[0:2] < "27":
#         F[1] += 1

#     for i in range (2,n):
#         flag = False
#         if 9 < int(S[i-1:i+1]) < 27:
#             flag = True
#         if not flag:
#             if S[i:i+1] != "0":
#                 F[i] += F[i-1]
#         elif flag:
#             if S[i-1:i+1] != "00":
#                 if S[i:i+1] != "0":
#                     F[i] += F[i-1]
#                 F[i] += F[i-2]
#     return F[n-1]

# runtests ( haslo )
