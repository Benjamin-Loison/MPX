from math import pi
import os

##

def somme():
    l = [0]
    while l[-1] * (l[-1] + 1) <= 1000:
        l += [l[-1] + 1]
    return sum(l)

print(somme())

##

# linéaire
def inin():
    n = int(input())
    """s = ""
    for i in range(n):
        s += str(i) + '_'
    return s + str(n)"""
    return '_'.join(str(k) for k in range(n + 1))

def inin(n):
    return '_'.join(str(k) for k in range(n + 1))

for n in (0, 1, 2, 5):
    print(inin(n))

##

# quadratique
def greatest(n):
    i = 1
    while sum(range(1, i + 1, 2)) <= n:
        i += 1
    return i - 1

# linéaire
def greatest(n):
    i = 0
    mySum = 0
    while mySum <= n:
        print(i, mySum)
        if i % 2 != 0:
            print("here")
            mySum += i
        i += 1
    return i - 1

def greatest(n):
    i = 0
    s = 0
    while s <= n:
        if i % 2 != 0:
            s += i
        i += 1
    return i - 2

for n in (0, 1, 2, 3, 5):
    print(greatest(n))

# or comme Gustave, direct increment 2 par 2 ?

# cmd + enter: execute block
         
##

# len(texte) * len(mot)
# quadratique
def sous_mot(mot, texte):
    #return mot in texte
    texteLen = len(texte)
    motLen = len(mot)
    for texteIndex in range(texteLen - motLen + 1):
        good = True
        for index in range(motLen):
            if mot[index] != texte[texteIndex + index]:
                good = False
                break
        if good: return True
    return False

for mot, texte in (("a", "abc"), ("", "abc"), ("!", "Test !"), ("!", "Test ")):
    print(sous_mot(mot, texte))

##

def f(x):
    return x - pi 

# assume given a and b as f(a) != 0 and f(b) != 0
def zero_dichotomie(f, a, b, eps):
    if b - a <= eps: return a
    m = (a + b) / 2
    y = f(a) * f(m)
    if y < 0:
        return zero_dichotomie(f, a, m, eps)
    else:
        return zero_dichotomie(f, m, b, eps)

def zero_dichotomie(f, a, b, eps):
    d = b - a
    while d > eps:
        m = (a + b) / 2
        #print(a, b, m)
        if f(a) * f(m) < 0:
            b = m
        else:
            a = m
        d = b - a
    return m
    
print(zero_dichotomie(f, 2, 4, 10 ** (-8)), pi)

##

def f(x):
    return x

def int_rect(f, a, b, n):
    s = 0
    e = (b - a) / n
    for i in range(n): # can't float step ?
        s += f(a + i * e) * e
    return s

for b, n in ((0, 1), (0, 2), (1, 1), (1, 2), (1, 3), (1, 10 ** 2)):
    print(int_rect(f, 0, b, n))

##

# backslash with alt + shift + /

print(os.getcwd())
f = open("test.txt", 'w')
f.write("Hello\nWorld\n!")
f.close()

def readFile(fileName):
    f = open(fileName)
    for line in f.readlines():
        if line[-1] == '\n':
            print(line[:-1])
        else:
            print(line)
    f.close()

def readFile(fileName):
    f = open(fileName)
    line = f.readline()
    while line != "":
        print(line, end='')
        line = f.readline()
    f.close()
    print()

readFile("test.txt")

def readFileStar(fileName):
    f = open(fileName)
    line = f.readline()
    while line != "":
        print('*' + line, end='')
        line = f.readline()
    f.close()

readFileStar("test.txt")

##

# assume l != []
def minmax(l):
    min, max = l[0], l[0]
    for el in l[1:]:
        if min > el: min = el
        if max < el: max = el
    return min, max

for l in ([42], [69, 42], [72, 45, 74, 89, 52, 12]):
    print(minmax(l))

##

# deuxième max peut être confondu ? let say no and assume length >= 2
def max2(l):
    maxi, deuxiemeMax = max(l[0], l[1]), min(l[0], l[1])
    for el in l[1:]:
        #print(deuxiemeMax, el, maxi)
        if deuxiemeMax < el and deuxiemeMax < maxi: deuxiemeMax = el
        if maxi < el: maxi = el
    return maxi, deuxiemeMax
# if return max and deuxiemeMax as same, then we conclude that there isn't any second maximum different from the maximum

# too many to test
for l in ([69, 42], [72, 45, 74, 89, 52, 12]):
    print(max2(l))

##

def occurence(l):
    res = [0] * 100
    for el in l:
        res[el] += 1
    return res

for l in ([], [1], range(10)):
    print(occurence(l))

# dépend des éléments de la liste
# O(sum(l))
def premier_tri(l):
    res = occurence(l)
    newRes = []
    for i in range(len(res)):
        newRes += [i] * res[i]
    return newRes
    
for l in ([], [1], range(10), [4] * 10):
    print(premier_tri(l))

# décalage négatifs vers positifs
def occurence(l):
    mini, maxi = minmax(l)
    tmpMini = mini
    if mini < 0:
        maxi -= mini
        mini = 0
    res = [0] * (maxi - mini +1)
    offset = -tmpMini
    #print(l, res)
    for el in l:
        #print(el + offset)
        res[el + offset] += 1
    return res

for l in ([1], range(10), [-2, -3, 4, -5, 4, 7]):
    print(occurence(l))

# toujours linéaire les deux
def premier_tri(l):
    res = occurence(l)
    newRes = []
    mini, maxi = minmax(l)
    for i in range(len(res)):
        newRes += [i + mini] * res[i]
    return newRes

for l in ([1], range(10), [-2, -3, 4, -5, 4, 7]):
    print(premier_tri(l))

##

# l liste d'entiers positifs a priori non triée
# assume l != []
def doublon(l):
    ctns = []
    for el in l:
        if el in ctns: return el
        else: ctns += [el] # could sort ctns list
    return -1

lists = [], [42], [41, 42], [42, 41, 43], [24, 25, 41, 52, 25]
for l in (lists):
    print(doublon(l))

def sans_doublon(l):
    ctns = []
    for el in l:
        if not (el in ctns): ctns += [el]
    return ctns

for l in (lists):
    print(sans_doublon(l))

##

def count(l):
    d = dict()
    for el in l:
        if el in d:
            d[el] += 1
        else:
            d[el] = 1
    ll = []
    for el in d:
        ll += [[el, d[el]]]
    return ll

# to do with lists ?
"""def count(l):
    ll = []
    for el in l:
        if el in ll:"""

for l in lists:
    print(count(l))

def incremente(new_l, x):
    for i in range(len(new_l)):
        if x == new_l[i][0]:
            new_l[i][1] += 1
            return
    new_l.append([[x, 1]])

for l in lists:
    l = count(l)
    incremente(l, 25)
    print(l)

##

def liste_couple(l):
    return count(l)

##

def max_couple(new_l):
    xBest, nBest = new_l[0]
    for x, n in new_l:
        if n > nBest:
            nBest = n
            xBest = x
    return xBest, nBest

def majoritaire():
    

# tri linéaire

