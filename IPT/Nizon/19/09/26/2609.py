# corrigé en ligne

l = [2, 4, 4, 7, 1, 1, 1]

# O(n^2)
def doublons(l):
    res = []
    for i in range(1, len(l)):
        for j in range(i):
            if l[i] == l[j]:
                res.append(l[i])
    return res

print(doublons(l))

## Table de hachage

# liste Py: tableau dynamique (liste), liste triée, ABR, table de hachage

# insert   1   n   log n 1
# suppr    n   n   log n 1
# recherch n log n log n 1

# lien entre h et log n
# forcer arbre équilibré pour forcer le log n
# arbre AVL ?

# chercher un livre dans une bibliothèque

import numpy as np

def creation(M):
    return np.zeros(M, dtype=str)

def insere(h, key, value):
    if h[key] == '':
        h[key] = value

def recherche(h, key):
    if h[key] != '':
        return h[key]
    return ''
    
def supprime(h, key):
    h[key] = ''

h = creation(10)
print(h)
insere(h, 2, "hey") # why one char ?
print(h)
print(recherche(h, 2))
print(recherche(h, 3))
supprime(h, 2)
print(h)

##

BITS_NB = 8
M = BITS_NB * 3

# bit de poids faible ... bit de poids fort
# 8 bits unsigned: 0 -> 255
# 8 bits signed: -128 -> 127

# keys: 0 -> M - 1

def creation(M):
    return np.zeros(M // BITS_NB, dtype=np.uint8)

def payload(key):
    return 2 ** (key % BITS_NB)

def index(key):
    return key // BITS_NB

def insere(h, key):
    if not(recherche(h, key)):
        h[index(key)] += payload(key)

def recherche(h, key):
    return (h[index(key)] & payload(key)) != 0

def supprime(h, key):
    if recherche(h, key):
        h[index(key)] -= payload(key)

h = creation(M)
print(h)
insere(h, 7)

insere(h, 8)
insere(h, 10)

print(h)
for i in range(M):
    if recherche(h, i):
        print(i)
supprime(h, 8)
print(h)

##

def hach_div(m):
    def h(k):
        return k % m
    return h

print((hach_div(10))(15))

##

def horner(P, x):
    S = P[0]
    for i in range(1, len(P)):
        S = S * x + P[i]
    return S
    
P = [2, 1]
print(horner(P, 0))
print(horner(P, 1))
print(horner(P, 2))

##

def newOrd(chr):
    return ord(chr) - 1

def hach_div(string):
    return sum(newOrd(char) * (256 ** i) for i, char in enumerate(reversed(string)))

# TODO: SHOULD BE DONE WITH key, value multiple times in each slot of the array

# teacher
def hach_div(string):
    return horner(list(ord(c) for c in string), 256) % M
    
print(hach_div("AER"))

def creation(M):
    return [[] for i in range(M)], hach_div

def insere(s, key, value):
    s[h(key)] += [value]

def recherche(s, key):
    if len(s[h(key)]) != 0:
        return s[h(key)][0]
    return None

def suppression(s, key):
    s[h(key)] = s[h(key)][1:]

# N / 3 ?

M = 256
s, h = creation(M)
print(s)
insere(s, "he", "hey")
print(s)
print(recherche(s, "he"))
print(recherche(s, "test"))
suppression(s, "he")
print(recherche(s, "he"))
print(s)

##

s = set()
s.add("a")
print(s)
s.add("a")
print(s)

def doublon(l):
    a = set()
    res = []
    for x in l:
        if x in a: # temps constant et ajout aussi 
            res.append(x)
        else:
            a.add(x)
    return res # donc linéaire
