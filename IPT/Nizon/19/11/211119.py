"""

a = bq + r
a ^ b = b ^ r

"""

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a%b)

# or

def gcd(a, b):
    if a == b: return a
    else if a > b: return gcd(a-b,b)
    else: return gcd(a, b-a)

# au + bv = d
# bu' + rv' = d
# bu' + (a - bq)v' = d
# av' + b(u' - qv') = d
def bezout(a, b):
    if b == 0:
        return 1, 0
    u, v = bezout(b, a % b)
    return v, u - (a // b) * v

def palindrome(txt):
    if len(txt) < 2:
        return True
    return txt[0] == txt[-1] and palindrome(txt[1:-1]) # extraire une liste se fait en linéaire :( O(n**2)

# best one so (linear)
def palindrome(txt):
    def aux(i, j):
        if i >= j: return True
        return txt[i] == txt[j] and aux(i + 1, j - 1)
    return aux(0, len(txt) - 1)

print(palindrome(""))
print(palindrome("a"))
print(palindrome("ab"))
print(palindrome("aa"))
print(palindrome("kayak"))
print(palindrome("kaybk"))

def sumi(n):
    if n == 0: return 0
    return (n ** 3) + sumi(n - 1)

for i in range(4):
    print(i, sumi(i))

def greatest(l):
    def aux(el, i):
        # missing
        return max(el, i + 1)
    return aux(l[0], 1)

# log
def dich(l, x):
    if l == []: return False
    def aux(i, j):
        if i + 1 >= j:
            return l[i] == x
        k = (i + j) // 2
        if l[k] > x:
            return aux(i, k)
        return aux(k, j)
    return aux(0, len(l) - 1)

def linear(l, x):
    def aux(i):
        if i >= len(l):
            return False
        return l[i] == x or aux(i + 1)
    return aux()

print(dich([], 0))
print(dich([1], 2))
print(dich([2, 4, 7, 5], 3))
print(dich([2, 4, 7, 5], 7))

# complexity ?
def fibo(n):
    a = 0
    b = 1
    res = 
    def aux(i):
        if i < n:
            return aux(i + 1)
        return 
    return aux(0)

# 2 ** n
def fibo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibo(n - 1) + fibo(n - 2)

# bruh
def fibo(n):
    def aux(el):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        return el + aux()
    return aux(0)

# for matrix
def exprap(A, B):
    

import numpy as np

def fibo(n):
    return np.linalg.matrix_power(np.array([[1, 1], [1, 0]]), n).dot(np.array([1, 0]))[0]

# 2x2
# bruh
def prod(A, B):
    return [[sum([A[i][j] * B[j][i] for i in (0, 1)]) for j in (0, 1)] for y in (1, 2)]

A = [[0, 1], [2, 3]]
B = [[4, 5], [6, 7]]
print(prod(A, B))

def fibo(n):
    C = prod(exprap([[1, 1], [1, 0]], n - 1), [1, 0])
    return C[0][0] + C[0][1]

for i in range(100):
    print(i, fibo(i))

fibo(0)
fibo(1)
fibo(2)

"""

(n)
(k) = (n!) / ((n-k)! * k!)

"""

def fact(n):
    if n == 0: return 1
    return n * fact(n - 1)

def pascal(k, n):
    return fact(n) / (fact(n - k) * fact(k))

def fact(begin, i, n):
    if n == i: return begin
    return n * fact(begin, i, n - 1)

def pascal(k, n):
    if n - k > k:
        mini = k
        maxi = n - k
    else:
        mini = n - k
        maxi = k
    a = fact(mini)
    b = fact(a, mini, maxi)
    return fact(b, n - k, n) / (a * b)

# (n)   (n - 1)   (n - 1)
# (k) = (k) + (k - 1)
def pascal(k, n):
    if k == n: return 1
    if k < 0 or n < 0: return 0
    return pascal(k, n - 1) + pascal(k - 1, n - 1)

# bruh
def pascal(k, n):
    P = [[0 for j in range(n)] for i in range(n)]
    for i in range(n):
        P[i][0] = 1
    for i in range(n):
        for j in range(1, i):
            P[i][j] = P[i - 1][j - 1] + P[i - 1][j]
    print(P)
    return P[n - 1][k - 1]

print(pascal(0, 1))
print(pascal(1, 1))
print(pascal(11, 17))
print(pascal(3, 5))

def money(n):
    
    
def money(n, l):
    

