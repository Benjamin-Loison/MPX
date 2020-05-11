import numpy as np
import numpy.random as rd
import matplotlib.pyplot as plt

##

n = 10 ** 7
a = np.zeros((6))

for x in range(n):
    r = rd.randint(0, 6)
    a[r] += 1
print(a / n)

print(1 / 6)

##

def march(n):
    u = 0
    t = [u]
    for i in range(n):
        if rd.randint(0, 2) == 1:
            u += 1
        else:
            u -= 1
        t += [u]
    return t

n = 10 ** 6
X = range(n + 1)
Y = march(n)

plt.plot(X, Y)
plt.show()

# TODO: https://fr.wikipedia.org/wiki/Esp%C3%A9rance_math%C3%A9matique