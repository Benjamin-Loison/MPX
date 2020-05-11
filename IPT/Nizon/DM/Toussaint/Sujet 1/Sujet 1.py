import numpy as np
import numpy.random as rd
import matplotlib.pyplot as plt

##

def init(N):
    return np.ones((N, N), dtype=np.int)

t = init(10)
print(t)

J = 1
k = 1

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
    for i in range(1, N - 1):
        for j in range(1, N - 1):
            somme += localEnergie(t, i, j)
            #somme += t[i][j] * (t[i][j - 1] + t[i][j + 1] + t[i - 1][j] + t[i + 1][j])
    return -somme

E = energie(t)
print(E)

# approche naïve qui sera TROP lourde pour la suite
def modif(t, i, j):
    E = energie(t)
    t[i][j] *= -1
    return energie(t) - E

# should take care of one range more enery
def nearEnergie(t, i, j): # TODO: avoid middle energie for better computation for modif ?
    somme = localEnergie(t, i - 1, j) + localEnergie(t, i + 1, j)
    for k in range(3):
        somme += localEnergie(t, i, j - 1 + k)
    return somme

def modif(t, i, j):
    oldEnGivenLocaly = nearEnergie(t, i, j)
    t[i][j] *= -1
    return oldEnGivenLocaly - nearEnergie(t, i, j)

delta = modif(t, 3, 3)
print(delta)

def inversion(delta, T):
    if delta <= 0:
        return True
    return rd.random() < np.exp(-delta / (k * T)) # 1 a une probabilité nulle d'être retourné par rd.random() (maths and also in implementation)

print(inversion(-16, 5)) # 2nd argument isn't important
print(inversion(16, 5)) # return mainly False and sometimes True

def evolution(t, T, k):
    l = []
    E = energie(t)
    N = len(t)
    for i in range(k):
        #print(i)
        i, j = rd.randint(1, N - 1), rd.randint(1, N - 1)
        # M1: copy t, M2: reinversion if need not to update t (M2 very efficient)
        delta = modif(t, i, j)
        if not inversion(delta, T):
            modif(t, i, j)
            delta = 0
        E += delta
        l += [E]
    return l

print(evolution(t, 5, 10))

#

t = init(100)
iterations = 500000 # not using k for avoiding modification of Boltzmann constant
i = evolution(t, 5, iterations)
j = range(iterations)
plt.plot(j, i)
plt.show()

# Après 200 000 itérations, le système reste entre -25 000 et -22 000 donc oui on ne conserve que le régime transitoire intéressant

"""

On observe une variation brusque autour de 4.5 K pour l'énergie moyenne et le magnétisme
On a donc bien montré ce phénomène de transition de phase autour de 4.5 K

Pour améliorer la valeur théorique:
- la pratique ? (chauffer à partir de 2 K et mesurer cette variation brusque)
- (prefered ?) ne pas faire de simplifications comme dans l'énoncé

"""

# JFF

i = 0
maxi = 0
while maxi != 1:
    test = rd.random()
    if test > maxi:
        maxi = test
        print(maxi, i)
    i += 1

"""

0.16483068774129772 0
0.5757035580698561 1
0.9215643310448847 3
0.9237365874432466 54
0.9546385605410336 95
0.9775277278565543 121
0.983986781152086 155
0.9924772290190808 218
0.9928002935797089 316
0.9960445768917472 424
0.9995572317123959 673
0.9999151555267123 2519
0.9999530766425632 7487
0.999991792972592 12171
0.9999958630569792 14434
0.9999967316646864 99039
0.999999012039235 319756
0.9999992925142451 682110
0.9999993198774524 2167121
0.9999999070248358 2625243
0.999999925515475 6317713
0.9999999268096772 14465735
0.9999999606900934 28183616
0.9999999989171698 54960752

"""

## 2. recherche de l'enveloppe convexe d'un ensemble

x1 = [0, 2]
x2 = [1, 1]
x3 = [2, 3]
x4 = [3, 0.9]
x5 = [4, 2.5]
x6 = [5, 0]
x7 = [6, 4]
x8 = [7, 1.5]

N = [x1, x2, x3, x4, x5, x6, x7, x8]

"""
N = np.array(sorted(N))

plt.plot(N[:,0], N[:,1], 'bo')
plt.show()
"""

"""def d(x, y): # pts
    return (x ** 2 + y ** 2) ** 0.5

def dVec(vec):
    return d(vec[0], vec[1])

def angle(AB, BC): # vecs
    return np.arccos((AB[0] * BC[0] + AB[1] * BC[1]) / (dVec(AB) * dVec(BC)))

def vec(A, B):
    return [B[0] - A[0], B[1] - A[1]]

def anglePt(A, B, C):
    return angle(vec(A, B), vec(B, C))"""

l = N[:2]

def angle(O, A): # pt
    return np.arctan((A[1] - O[1]) / (A[0] - O[0]))

lLen = 2
bool = True
# quadratique
for k in range(2, len(N)):
    if lLen < 2:
        print("test") # really usefull ? (ex ?) see next function (I think)
        break
    if bool:
        lLen += 1
        l.append(N[k])
    print(l)
    currentAngle = angle(l[-2], l[-1]) - angle(l[-3], l[-2])
    print(currentAngle)
    if 0 > currentAngle or currentAngle > np.pi:
        l[-2] = l[-1]
        del l[-1]
        print("hey")
        lLen -= 1
        bool = False
    else:
        bool = True

def basEnveloppeConvexe(N):
    l = N[:2]
    lLen = 2
    bool = True
    # quadratique
    for k in range(2, len(N)):
        if lLen <= 2 or bool:
            lLen += 1
            l.append(N[k])
        print(l)
        currentAngle = angle(l[-2], l[-1]) - angle(l[-3], l[-2])
        print(currentAngle)
        if 0 > currentAngle or currentAngle > np.pi:
            l[-2] = l[-1]
            del l[-1]
            print("hey")
            lLen -= 1
            bool = False
        else:
            bool = True
    return l

x1 = [0, 2]
x2 = [1, 1]
x3 = [2, 3]
x4 = [3, 0.9]
x5 = [4, 2.5]
x6 = [5, 0]
x7 = [6, 4]
x8 = [7, 1.5]

N = [x1, x2, x3, x4, x5, x6, x7, x8]

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

"""

 A0  A1   A2  A3  A4

[x1, x2]
[[0, 2], [1, 1]]

[x1, x2, x3]
[[0, 2], [1, 1], [2, 3]]

[x1, x2, x3, x4]
[[0, 2], [1, 1], [2, 3], [3, 0.9]]

[x1, x2, x4]
[[0, 2], [1, 1], [3, 0.9]]

[x1, x2, x4, x5]
[[0, 2], [1, 1], [3, 0.9], [4, 2.5]]

[x1, x2, x4, x5, x6]
[[0, 2], [1, 1], [3, 0.9], [4, 2.5], [5, 0]]

[x1, x2, x4, x6]
[[0, 2], [1, 1], [3, 0.9], [5, 0]]

[x1, x2, x6]
[[0, 2], [1, 1], [5, 0]]

[x1, x2, x6, x8]
[[0, 2], [1, 1], [5, 0], [7, 1.5]]


#Ajm2 = l[0] # A_{j-2}
#Ajm1 = l[1] # A_{j-1}
    #Aj = N[k] # A_j (to check (algo))
    #currentAngle = anglePt(l[-3], l[-2], l[-1])
    #currentAngle = angle(Ajm2, Ajm1, Aj)

"""

## BELOW NOT ME

def point_segment(P1,P2,P):
    return (P2[0]-P1[0])*(P[1]-P1[1])-(P2[1]-P1[1])*(P[0]-P1[0])>0

def enveloppe_direct(points):
    enveloppe = []
    N = len(points)
    for i in range(N):
        for j in range(N):
            if i!=j:
                bord = True
                for k in range(N):
                    if k!=i and k!=j:
                        if point_segment(points[i],points[j],points[k]):
                            bord = False
                            break
                if bord:
                    enveloppe.append([points[i],points[j]])
    return enveloppe

print(enveloppe_direct(N))

plt.figure()
plt.axis([0,10,0,10])
plt.axes().set_aspect('equal')
for i in range(len(N)):
    P = N[i]
    plt.plot([P[0]],[P[1]],"ko")
env = enveloppe_direct(N)
for i in range(len(env)):
    segment = env[i]
    P1 = segment[0]
    P2 = segment[1]
    plt.plot([P1[0],P2[0]],[P1[1],P2[1]],"k-")

plt.show()