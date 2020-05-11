import numpy as np
import numpy.random as rd
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from math import *

## 0

t = np.linspace(0, 10, 51)
t = np.linspace(0.1, 10, 51)

"""

y' = sin y

dy
-- = sin y
dt

ln !tan (x/2)! = integ(dy/sin y)

"""

def F(y, t):
    return np.sin(y)

y = odeint(F, np.pi / 2, t)

def sol(x):
    return log(abs(tan(x/2)))

sol = np.vectorize(sol)

plt.plot(t, y)
plt.plot(t, sol(t))
plt.show()

## 0 bis

t = np.linspace(0, 10, 1000)

alpha = 1
beta = 0.5

def H(v, t):
    a, b, c = v
    return [-alpha * a, alpha * a - beta * b, beta * b]

v = odeint(H, [1, 0, 0], t)

plt.plot(t, v)

plt.plot(t, v[:,0]) # A
plt.plot(t, v[:,:2]) # A and B
plt.show()

## 0 bis bis

tau = 1
w = 25 / tau # cas limite: 1 / tau, n / tau environ n oscillations

def F(y, t):
    a, b = y
    return -2/tau * a - w ** 2 * b, a

t = np.arange(0, 10, 0.002)

v = odeint(F, [1, 0], t)

plt.plot(t, v[:,1])
plt.show()

## 0 bis bis bis



## tmp

y = [x ** 2 for x in range(10)]
t = range(10)

for i in range(10):
    plt.plot(t, y[i])
    plt.pause(0.5)

plt.show()

#

t = [k for k in range(20)]
y = [[k ** i for k in range(20)] for i in range(10)]

for i in range(10):
    plt.clf()
    plt.plot(t, y[i])
    plt.pause(0.5)
    
plt.show()

## 1

t = np.linspace(0, 10, 100)

def G(v, t):
    return [v[1] - 50, 50 - v[0]]

v = odeint(G, [10, 50], t)
 
plt.plot(min(v[:,0]), min(v[:,1]))
plt.plot(max(v[:,0]), max(v[:,1]))
    
for i in range(len(t)):
    plt.plot(10 / len(t) * i, v[i][1], 'o')
    plt.pause(0.001)
    
#plt.plot(t, v)
plt.show()

## 2

# matplotlib a un module d'animation efficace

plt.clf()

t = np.linspace(0, 10, 100)

def G(v, t):
    return [v[1] - 50, 50 - v[0]]

v = odeint(G, [10, 50], t)

plt.plot(min(v[:,0]), min(v[:,1]))
plt.plot(max(v[:,0]), max(v[:,1]))
    
for i in range(len(t)):
    #plt.clf()  
    #print(v[i][0], v[i][1])
    plt.plot(v[i][0], v[i][1], 'o')
    plt.pause(0.001)
    
#plt.plot(v[:, 0], v[:, 1])
plt.show()

## 3

plt.clf()

def euler2(x0, y0, t0, tn, n):
    X, Y = [x0], [y0]
    dt = (tn - t0) / n
    for i in range(n):
        Y += [Y[-1] + dt * (50 - X[-1])]
        X += [X[-1] + dt * (Y[-2] - 50)]
    return X, Y

v = euler2(10, 50, 0, 10, 100)
t = np.linspace(0, 10, 101)
plt.plot(t, v[0])
plt.plot(t, v[1])

t = np.linspace(0, 10, 101)

def G(v, t):
    return [v[1] - 50, 50 - v[0]]

v = odeint(G, [10, 50], t)
   
plt.plot(t, v)
plt.show()

#

plt.clf()

n = 250
t = np.linspace(0, 10, n)

v = euler2(10, 50, 0, 10, n)

plt.plot(min(v[0]), min(v[1]))
plt.plot(max(v[0]), max(v[1]))
    
for i in range(len(t)):
    plt.plot(v[0][i], v[1][i], 'o')
    plt.pause(0.001)
    
plt.show()

## 4

def fill(f, n, a, v):
    while a > 0:
        x, y = rd.randint(0, n, 2)
        if f[y][x] == 0:
            a -= 1
            f[y][x] = v

def init_foret(n, a, k):
    f = np.zeros((n, n))
    fill(f, n, a, 1)
    fill(f, n, a, 2)
    """
    while a > 0:
        x, y = rd.randint(0, n, 2)
        if f[y][x] == 0:
            a -= 1
            f[y][x] = 1
    while k > 0:
        x, y = rd.randint(0, n, 2)
        if f[y][x] == 0:
            k -= 1
            f[y][x] = 2"""
    return f

# ou tableau de positions et tire au hasard dedans et retire l'élément du tableau
# astuce pour ne pas avoir temps linéaire, met le dernier à l'emplacement en question et retire le dernier (cst)

f = init_foret(200, 5, 5)

# spatiale: n ** 2
# calcul: n ** 2
def evol(f):
    newF = f.copy()
    n = f.shape[0] # it's not a method !
    for y in range(n):
        for x in range(n):
            if newF[y][x] == 2:
                if x < n - 1:
                    f[y][x+1] = 2
                if x > 0:
                    f[y][x-1] = 2
                if y > 0:
                    f[y-1][x] = 2
                if y < n - 1:
                    f[y+1][x] = 2

print(f)
print()
evol(f)
print()
print(f)

# pire cas: (n ** 3) * (n ** 2) sure ?
def anime_foret(f):
    newF = f.copy()
    evol(newF)
    while not np.array_equal(newF, f): # deep ?
        f = newF.copy()
        evol(newF)
        #print(f)
        plt.imshow(f)
        plt.pause(0.001)
        print(densite_feu(f))

anime_foret(f)
plt.show()

def densite_feu(f):
    #print(f)
    n = f.shape[0]
    i = 0
    for y in range(n):
        for x in range(n):
            if f[y][x] == 2:
                i += 1
    return i / (n ** 2)

def densite_feu(f):
    #print(f)
    h, w = f.shape
    i = 0
    for y in range(h):
        for x in range(w):
            if f[y][x] == 2:
                i += 1
    return i / (h * w)

# NON compo connexe signifie que si 2 arbres sont distants d'une case
# n ** 4 * n ** 2
def compo_connexe(f):
    n = f.shape[0]
    h, w = 0, 0
    for y in range(n):
        for x in range(n):
            for sy in range(1, n - y):
                for sx in range(1, n - x):
                    #print(x, y, sx, sy)
                    if densite_feu(f[y:y+sy,x:x+sx]) == 1:
                        if sy * sx > h * w:
                            h = sy
                            w = sx
    return h, w

print(compo_connexe(f))

##

d = 0.05
size = 10

def d(x0, y0, x1, y1):
    return ((x1 - x0) ** 2 + (y1 - y0) ** 2) ** 0.5

def couronne(a, b, n):
    c = np.zeros((n, n))
    cx, cy = n // 2, n // 2
    for y in range(n):
        for x in range(n):
            dis = d(x, y, cx, cy)
            if dis <= b and dis >= a:
                c[y][x] = 1
    return c

c = couronne(4, 6, 15)
print(c)
plt.imshow(c)