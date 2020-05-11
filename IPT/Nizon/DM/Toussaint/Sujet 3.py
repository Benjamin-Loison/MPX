import matplotlib.pyplot as plt
import numpy as np
import sys

MAX_INT = sys.maxsize
MIN_INT = -MAX_INT - 1

# there is a fucking missing point in l (according to the working paper): (30, -10)

l = [(10, 10), (50, 30), (20, 10), (40, 25), (50, 40), (64, 12), (25, 35), (30, -10)]
t = [[(10, 10), (50, 30), (20, 10)], [(40, 25), (50, 40), (64, 12)]]

def affiche_triangle(l, t):
    l = np.array(l)
    t = np.array(t)
    for pt in l:
        plt.plot(l[:,0], l[:,1], 'bo') # to learn by heart
    for triangle in t:
        triangle = np.vstack((triangle, triangle[0]))
        plt.plot(triangle[:,0], triangle[:,1])
    plt.show()

#affiche_triangle(l, t)

def d(A, B): # could not use sqrt because x |-> x^2 is growing
    return ((A[0] - B[0]) ** 2 + (A[1] - B[1]) ** 2) ** 0.5

def proche(PI, l): # assume that there is one
    nearestPt = [MIN_INT, MIN_INT]
    bestDistance = MAX_INT
    for pt in l:
        if PI != pt:#not np.array_equal(PI, pt): # wtf with first with not PI != pt: nearestPt is infinity... why not returning distance of PI to PI ? (which is 0)
            currentD = d(PI, pt)
            #print(pt, currentD)
            if currentD < bestDistance:
                bestDistance = currentD
                nearestPt = pt
    return nearestPt

testPt = proche([40, 25], l)
#print(testPt)

def insere(t, a, b, c):
    newTriangle = [a, b, c]
    #print("here", newTriangle, t)
    if not (newTriangle in t):
        t += [newTriangle]

#print(t, end = "\n\n")
#insere(t, (0, 0), (1, 1), (2, 2))
#print(t, end = "\n\n")
#insere(t, (40, 25), (50, 40), (64, 12))
#print(t, end = "\n\n")

def determinantVec(AB, AP): # where does this formula comes from ?
    return AB[0] * AP[1] - AB[1] * AP[0]

def determinant(P, A, B):
    P, A, B, = np.array(P), np.array(A), np.array(B)
    return determinantVec(B - A, P - A)

def isOnLeft(P, A, B): # assume no 3 dots aligned ? (cf the working paper)
    return determinant(P, A, B) > 0

# few tests
A, B = (0, 0), (10, 10)
"""print(isOnLeft((0, 10), A, B)) # True
print(isOnLeft((5, 5), A, B)) # False
print(isOnLeft((0, 0), A, B)) # False
print(isOnLeft((10, 0), A, B)) # False"""

def ang(O, A): # pt
    return abs(np.arctan((A[1] - O[1]) / (A[0] - O[0]))) # abs not to think about trigonometric way

def angle(PI, PJ, l, sens): # "le plus proche" means "le plus proche possible" (angle definition) and not euclidien otherwise need a definition
    nearestPt = [MIN_INT, MIN_INT]
    biggestAngle = MIN_INT
    for pt in l:
        #print(pt, PI, PJ)
        if not np.array_equal(pt, PI) and not np.array_equal(pt, PJ):
            onLeft = isOnLeft(pt, PI, PJ)
            #print(pt, onLeft)
            pt, PI, PJ = np.array(pt), np.array(PI), np.array(PJ)
            if sens == 1:
                if onLeft:
                    currentAngle = ang(pt - PI, PJ - pt)
                    if currentAngle > biggestAngle:
                        biggestAngle = currentAngle
                        nearestPt = pt
            elif sens == -1:
                if not onLeft:
                    currentAngle = ang(pt - PI, PJ - pt)
                    if currentAngle > biggestAngle:
                        biggestAngle = currentAngle
                        nearestPt = pt
    if np.array_equal(nearestPt, [MIN_INT, MIN_INT]):
        return list(PI)
    return list(nearestPt)

"""def delaunay(l, sens = 1):
    if l == []: return []
    toAdd = []
    PJ = proche(l[0], l)
    initialPJ = PJ
    PK = angle(l[0], PJ, l, sens) # why no fucking do while in Python ?
    while (not np.array_equal(PK, initialPJ)) and (not np.array_equal(PK, l[0])):
        toAdd += [(l[0], PJ, PK)]
        PK = angle(l[0], PJ, l, sens)
        #insere(t, l[0], PJ, PK)
        PJ = PK

    if not np.array_equal(PK, initialPJ):
        #insere(t, l[0], PK, initialPJ)
        toAdd += [(l[0], PK, initialPJ)]
    elif not np.array_equal(PK, l[0]):
        toAdd += [delaunay(l, -1)]
    return toAdd + delaunay(l[1:])"""

NULL = [MIN_INT, MIN_INT]

"""
d'après l'énoncé on commence par exemple par le 2ème point (50, 30) puis on a donc PJ = (50, 40) et le point le plus à gauche (en terme d'angle) est alors (30, -10) et on l'ajoute (sauf que non il n'est pas affiché dans le corrigé)
"""
def delaunay(l, sens = 1, PI = NULL, PJ = NULL):
    if l == []: return []
    if PI == NULL:
        PI = l[0]
    if PJ == NULL:
        PJ = proche(PI, l)
    initialPJ = PJ
    tmpPJ = PJ
    PK = angle(PI, PJ, l, sens) # why no fucking do while in Python ?
    while (not np.array_equal(PK, initialPJ)) and (not np.array_equal(PK, PI)):
        insere(t, PI, PJ, PK)
        tmpPJ = PJ
        PJ = PK
        PK = angle(PI, PJ, l, sens)

    if np.array_equal(PK, initialPJ):
        insere(t, PI, PK, initialPJ)
        delaunay(l[1:])
    elif np.array_equal(PK, PI):
        if sens == 1:
            delaunay(l, -1, PI, initialPJ)
        else:
            delaunay(l[1:])

t = []
delaunay(l)
affiche_triangle(l, t[:-1])

t = [[(10, 10), (20, 10), (30, -10)], [(10, 10), (20, 10), (25, 35)], [(20, 10), (40, 25), (30, -10)], [(20, 10), (40, 25), (25, 35)], [(30, -10), (40, 25), (64, 12)], [(25, 35), (50, 40), (40, 25)], [(50, 40), (64, 12), (50, 30)], [(40, 25), (50, 30), (64, 12)]]

affiche_triangle(l, t)

## 2

"""
def normal(AB):
    return (AB[1], -AB[0])

"""

"""
y = ax + b

n[1] = a * n[0] + b
"""

"""

def intersection(AB, AC):


def circonscrit(a, b, c):
    a, b, c = np.array(a), np.array(b), np.array(c)
    AB = b - a
    AC = c - a
    n = normal(AB)
    nP = normal(AC)
    I = (a + b) / 2
    IP = (a + c) / 2
    return intersection(I, n, IP, nP)
"""

def pt(z):
    return (z.real, z.imag)

def cplx(a):
    return complex(a[0], a[1])

# justification précise ? http://www.les-mathematiques.net/phorum/read.php?8,1238751,1239181
def circonscrit(a, b, c):
    a, b, c = cplx(a), cplx(b), cplx(c)
    aBar = a.conjugate()
    bBar = b.conjugate()
    cBar = c.conjugate()
    modCarA = a * aBar
    modCarB = b * bBar
    modCarC = c * cBar
    """num = a * (modCarB - modCarC) + b * (modCarC - modCarA)
    denum = a * bBar - a * cBar + b * cBar - aBar * b # doesn't work for c = (10, 10)
    print(denum)"""
    num = (b - c) * modCarA + (c - a) * modCarB + (a - b) * modCarC
    denum = (b - c) * aBar + (c - a) * bBar + (a - b) * cBar
    return pt(num / denum)

a = (0, 10)
b = (10, 0)
c = (10, 10)
ctr = circonscrit(a, b, c)
#print(ctr)

def demid(a, b, c):
    return (a, b)

def cotes(triangle):
    print(triangle)
    return ((triangle[0], triangle[1]), (triangle[1], triangle[2]), (triangle[2], triangle[0]))

def coteEqual(cote0, cote1):
    return (cote0 == cote1) or (cote0[0] == cote1[1] and cote0[1] == cote1[0])

def isDuplicates(cote0, l):
    for triangle in l:
        for cote1 in cotes(triangle):
            if coteEqual(cote0, cote1):
                return True, (NULL, NULL, NULL)
    return False, triangle

def middle(cote):
    return ((cote[0][0] + cote[1][0]) / 2, (cote[0][1] + cote[1][1]) / 2)

def voronoi(l):
    s, t = [], []
    for triangle in l:
        for cote in cotes(triangle):
            b, tri = isDuplicates(cote, l[1:])
            if b:
                s += [(circonscrit(tri[0], tri[1], tri[2]), circonscrit(triangle[0], triangle[1], triangle[2]))]
            else:
                # "le côté est dans l'enveloppe convexe" ?
                s += [demid(circonscrit(triangle[0], triangle[1], triangle[2]), middle(cote))]
    return s, t

l = t
s, t = voronoi(l)
s = np.array(s)
plt.plot()
plt.show()