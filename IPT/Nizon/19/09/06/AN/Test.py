import numpy as np
import scipy.integrate as integr

import matplotlib.pyplot as plt

def f(x, t) :
    return t*x

T = np.arange(0, 1.01, 0.01)
print(integr.odeint(f, 1, T))

## erreur sujet

def f(x,t) :
    return np.array([x[1], -2*x[1] - 3*x[0] - np.sin(t)]) # here
    
T = np.arange(0, 3*np.pi + 0.01, 0.01)
X = integr.odeint(f, np.array([0,1]), T)
plt.plot(T, X[ :,0])
plt.show()