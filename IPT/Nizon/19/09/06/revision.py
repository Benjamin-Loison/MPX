import matplotlib.pyplot as plt
import math
import numpy as np
import numpy.linalg as alg
import scipy.integrate as integr

### Intoduction
### Q1

print((2+1j)**(1/3))

### Q2

t=np.linspace(0,2*np.pi,100)
x=np.cos(3*t)
y=3*np.sin(t)
plt.plot(x,y)
plt.axis([-4,4,-4,4])
plt.show()

### Q3

N=500    # nombre de points en abscisses pour la résolution

def f(y,t):    #classiquement Y est le vecteur (x'(t),x(t))
    return np.sin(t)-(t**2-2)*y[1],y[0]
    
x=np.linspace(0,10,N)
res=integr.odeint(f,[10,0],x)
plt.plot(x,res[:,1])
plt.show()

### Q4

def u(n,x):
    def f(t):
        return 1/(x**(1/n)+t**2)
    return integr.quad(f,0,np.inf)[0]
    
print(integr.quad(lambda x:u(2,x),0,1)[0])

### Q5

A=[[1,3,0],[3,-2,-1],[0,-1,1]]

def  diagonalise(mat):
    tmp=alg.eig(mat)   # pour éviter de l'appeler 2 fois après
    D=np.diag(tmp[0])
    P=tmp[1]
    return (P,D)
    
P,D=diagonalise(A)
prod=np.dot(np.dot(P,D),alg.inv(P))
print(np.around(prod,2))

### Q6

A=1/math.sqrt(10)*np.array([[1,3],[3,-1]])

def est_ortho(mat):
    test=np.dot(m,m.T)
    return np.array_equal(np.around(test,5),np.eye(len(mat)))
    
print(est_ortho(A))

### Q7
#
# Ici on calcule en limitant le nombre de calculs, c'est important si on veut
# le tester avec un nombre suffisant d'itérations. Tout peut rester en 
# complexité linéaire si on s'y prend bien!

N=500     # nombre de termes calculés
T=1000    # nombre de termes pour le calcul du reste d'ordre N

def a(n):
    return 1/(n*n)
    
R=[sum([a(k) for k in range(N+1,N+T)])]
for i in range(N-1,0,-1):
    R.append(R[-1]+a(i))
R.reverse()

s0=[0]
s1=[0]
s2=[0]
for k in range(N):
    s1.append(s1[-1]+a(k+1)/R[k])
    s2.append(s2[-1]+a(k+1)/(R[k]**(1/2)))
    s0.append(s0[-1]+1/(2*(k+1)))

plt.plot(s0,color='blue')
plt.plot(s1,color='red')
plt.plot(s2,color='green')
plt.plot([math.log(k+1) for k in range(N)],color='black')
plt.show()

### Exponentielle

def B(t,n):
    A=np.array([[0,-t],[t,0]])
    res=np.eye(2)
    puis=np.eye(2)
    fac=1
    for k in range(1,n+1):
        puis=np.dot(puis,A)
        fac=fac*k
        res=res+puis/fac
    return res
    
N=100
n=50
Ti=0; Tf=20    
X,a,b,c,d=[],[],[],[],[]
for i in range(N):
    t=Ti+i*(Tf-Ti)/(N-1)
    X.append(t)
    res=B(t,n)
    a.append(res[0,0])
    b.append(res[0,1])
    c.append(res[1,0])
    d.append(res[1,1])
    
plt.plot(X,a)
plt.plot(X,b)
plt.plot(X,c)
plt.plot(X,d)
plt.show()  # explication de la fin du graphe?

###

def expA(t):
    return np.array([[0,-t],[t,0]])*np.sin(t)/t+np.cos(t)*np.eye(2)
    
n=10 # puis n=100
X=np.arange(0,10,0.2)
Y=[alg.norm(expA(t)-B(t,n)) for t in X]
plt.plot(X,Y)
plt.show()

###  Polynomes

resol=300  # nombre de points en abscisses/ordonnées

def P(z):
    return z**4+z

def f(z,N):
    v=z
    i=0
    while i<N+1 and abs(v)<1.5:
        i+=1
        v=P(v)
    return i

x=np.linspace(-1.8,1.8,resol)
y=np.linspace(-1.8,1.8,resol)
z=np.zeros((resol,resol))
for i in range(resol):
    for j in range(resol):
        z[i,j]=f(x[j]+y[resol-1-i]*1j,20)
        
plt.imshow(z)
plt.show()
    
### Matrices nilpotentes

def test_nil(A):
    p=1
    n=len(A)
    res=np.eye(n)
    z=np.zeros((n,n))
    while p<=n:
        res=np.dot(res,A)
        if np.array_equal(res,z):
           return p
        p+=1
    return -1
    
    
A=np.array([[0,1,1],[0,0,1],[0,0,0]])
B=np.eye(6)
C=np.array([[2,1,0,0],[-4,-2,0,0],[7,1,1,1],[-17,-6,-1,-1]])
print(test_nil(A))
print(test_nil(B))
print(test_nil(C))

