# Centrale Mines

##

def tri_rapide(l):
    def tri_reel(i, j):
        if i >= len(l):
            return
        avant = i + 1
        apres = j
        while apres >= avant:
            if l[avant] <= l[i]:
                avant += 1
            else:
                l[avant], l[apres] = l[apres], l[avant]
                apres -= 1
        if i < j:
            l[apres], l[i] = l[i], l[apres]
            tri_reel(i, apres - 1)
            #tri_reel(apres + 1, j)
    tri_reel(0, len(l) - 1)

l = [5, 3, 8, 4, 6, 2, 6]
tri_rapide(l)
print(l)

"""print(l)
l[0], l[2] = l[2], l[0]
print(l)"""

##

l = [5, 3, 8, 4, 6, 2, 6]

def keme(l, k):
    """def tri_rapide(l):
        n = len(l)
        if n < 2:
            return l[:]
        p = l[0]
        m, M = [], []
        for i in range(1, n):
            if l[i] <= p:
                m.append(l[i])
            else:
                M.append(l[i])
        return tri_rapide(m) + [p] + tri_rapide(M)
    return tri_rapide(l)[k]"""
    n = len(l)
    if n == 1:
        return l[0]
    p = l[0]
    m, M = [], []
    for i in range(1, n):
        if l[i] <= p:
            m.append(l[i])
        else:
            M.append(l[i])
    if k < len(m):
        return keme(m, k)
    elif k == len(m):
        return p
    else: return keme(M, k - len(m) - 1)

for k in range(len(l)):
    l = [5, 3, 8, 4, 6, 2, 6]
    print(keme(l, k))

##

# toujours existence mais pas unicité

def leMedian(l):
    n = len(l)
    for i in range(n):
        p = l[i]
        mini, maxi = 0, 0
        for j in range(n):
            q = l[j]
            if p != q:
                if p > q:
                    mini += 1
                else:
                    maxi += 1
        if abs(maxi - mini) <= 1:
            return i

def medians(A):
    def median(Ai):
        return keme(Ai, len(Ai) // 2)
    return [median(A[i:i+5]) for i in range(max(1, len(A) // 6))]

print(l)
print(medians(l))

def theMedian(A):
    if len(A) == 1:
        return A[0]
    return theMedian(medians(A))

def tri_rapide(l):
    n = len(l)
    if n < 2:
        return l[:]
    p = theMedian(l)
    m, M = [], []
    for i in range(1, n):
        if l[i] <= p:
            m.append(l[i])
        else:
            M.append(l[i])
    return tri_rapide(m) + [p] + tri_rapide(M)

print(theMedian(l))
print(theMedian([0, 2, 3]))
print(tri_rapide(l))

##

def pancake(l):
    if len(l) > 1:


l = [5, 3, 8, 4, 6, 2, 6]
pancake(l)



























