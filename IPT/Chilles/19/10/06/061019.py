print(i for i in range(10)) # doesn't work
print([i for i in range(10)])

import numpy as np

l = [1, 2, 3]
print(l)
print(type(l))
a = np.array(l)
print(a)
print(type(a))

b = [1 2 3] # doesn't work

print(np.diag([1., 2, 3]))

print(np.gcd(10, 5))
print(np.gcd(0, 0)) # really 0 ?

n = 10
A = np.array([np.gcd(i + 1, j + 1) for i in range(n) for j in range(n)]).reshape(n, n)
print(A)

print(A[3:6:2, 0:7:3])
print(A[3:6:2, 0:6:3])

t = np.array([3, 5]).reshape(2, 1),[0, 3, 6]
print(t)
print(A[t])

tp = np.array(np.array([3, 5]), np.array([0, 3, 6])) # ... don't work
print(tp)
print(A[tp])

tpp = np.ix_([-3, -2, -1], [-4, -3, -1])
print(tpp) # why print like this ? Humm... for extracting... ix give indexes for extracting may be
print(A[tpp]) # nice

l = np.linspace(-5, 5, 11)
print(l)

