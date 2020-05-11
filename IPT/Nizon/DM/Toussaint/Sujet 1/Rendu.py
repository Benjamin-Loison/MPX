import numpy as np
import numpy.random as rd
import matplotlib.pyplot as plt

## 1.

def init(N):
    return np.ones((N, N), dtype=np.int)

## 2.

J = 1

def localEnergie(t, i, j):
    somme = 0
    N = len(t)
    if j > 1:
        somme += t[i][j] * t[i][j - 1]
    if j < N - 2:
        somme += t[i][j] * t[i][j + 1]
    if i > 1:
        somme += t[i][j] * t[i - 1][j]
    if i < N - 2:
        somme += t[i][j] * t[i + 1][j]
    return somme

def energie(t):
    somme = 0
    N = len(t)
    for i in range(0, N):
        for j in range(0, N):
            somme += localEnergie(t, i, j)
    return -J * somme

## 3.

def nearEnergie(t, i, j):
    somme = localEnergie(t, i - 1, j) + localEnergie(t, i + 1, j)
    for k in range(3):
        somme += localEnergie(t, i, j - 1 + k)
    return somme

def modif(t, i, j):
    oldEnGivenLocaly = nearEnergie(t, i, j)
    t[i][j] *= -1
    newEnergie = nearEnergie(t, i, j)
    t[i][j] *= -1
    return oldEnGivenLocaly - newEnergie
    # on devrait retourner: énergie d'arrivée - énergie de départ mais seul la soustraction dans ce sens donne le bon résultat... (énergie de départ - énergie d'arrivée)

## 4.

k = 1

def inversion(delta, T):
    if delta <= 0:
        return True
    return rd.random() < np.exp(-delta / (k * T))

## 5.

def evolution(t, T, k):
    l = []
    E = energie(t)
    N = len(t)
    for i in range(k):
        i, j = rd.randint(1, N - 1), rd.randint(1, N - 1)
        delta = modif(t, i, j)
        if inversion(delta, T):
            t[i][j] *= -1
        else:
            delta = 0
        E += delta
        l += [E]
    return l

## 6.

t = init(100)
iterations = 500000
i = evolution(t, 5, iterations)
j = range(iterations)
plt.plot(j, i)
plt.show()

## 7.

"""

Après 200 000 itérations, statistiquement le système semble rester entre -25 000 et -22 000 donc oui on ne conserve que le régime transitoire intéressant

"""

## 8.

"""

On observe une variation brusque autour de 4.5 K pour l'énergie moyenne et le magnétisme.
On a donc bien montré ce phénomène de transition de phase autour de 4.5 K.

Pour vérifier la valeur théorique, on peut par l'expérimentation chauffer à partir de 2 K (par exemple) et mesurer cette variation brusque.
Ou théoriquement on peut ne pas faire de simplifications comme dans l'énoncé, ou moins.

"""

## 2. Recherche de l'enveloppe convexe d'un ensemble

# approximation avec des coordinnées en valeurs arbitraires de la figure de l'énoncé
x1 = [0, 2]
x2 = [1, 1]
x3 = [2, 3]
x4 = [3, 0.9]
x5 = [4, 2.5]
x6 = [5, 0]
x7 = [6, 4]
x8 = [7, 1.5]

N = [x1, x2, x3, x4, x5, x6, x7, x8]

def angle(O, A):
    return np.arctan((A[1] - O[1]) / (A[0] - O[0]))

# cette fonction a une complexité linéaire en la taille de N
def basEnveloppeConvexe(N):
    l = N[:2]
    lLen = 2
    bool = True
    for k in range(2, len(N)):
        if lLen <= 2 or bool:
            lLen += 1
            l.append(N[k])
        currentAngle = angle(l[-2], l[-1]) - angle(l[-3], l[-2])
        if 0 > currentAngle or currentAngle > np.pi:
            l[-2] = l[-1]
            del l[-1]
            lLen -= 1
            bool = False
        else:
            bool = True
    return l

def enveloppeConvexe(N):
    N = sorted(N)
    NNP = np.array(N)
    plt.plot(NNP[:,0], NNP[:,1], 'bo')

    B = basEnveloppeConvexe(N)
    BNP = np.array(B)
    plt.plot(BNP[:,0], BNP[:,1])

    for i in range(len(N)):
        N[i][1] *= -1
    H = basEnveloppeConvexe(N)
    H.append([BNP[-1][0], -BNP[-1][1]])
    HNP = np.array(H)
    plt.plot(HNP[:,0], -HNP[:,1])

    plt.show()

enveloppeConvexe(N)