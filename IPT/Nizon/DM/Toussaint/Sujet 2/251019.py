import numpy as np
import matplotlib.pyplot as plt
import numpy.random as rd
import os
import time
import sys

os.chdir("C:\\Users\\Benjamin\\Desktop\\BensFolder\\School\\CPGE\\Fenelon\\MPX\\IPT\\Nizon\\DM\\Toussaint\\Sujet 2")

m = 5000 # nb d'images

def cstrY():
    Y = np.zeros((m), dtype=np.int)
    f = open("chiffres.csv")
    for lineIndex in range(m):
        line = f.readline()
        Y[lineIndex] = int(line)
    f.close()
    return Y

Y = cstrY()
#print(Y)

def cstrX():
    X = np.zeros((m, 400), dtype=float)
    f = open("images.csv")
    for lineIndex in range(m):
        line = f.readline()
        components = line.split(",")
        map(float, components)
        X[lineIndex] = np.array(components)
    f.close()
    return X

X = cstrX()
#print(X)

def display(imageIndex):
    im = X[imageIndex].reshape((20, 20))
    plt.imshow(im, 'gray')
    plt.show()

#display(0)
#display(2000) # ! they all look the same and are sorted !

def dispMany(n):
    alreadyTaken = []
    finalImage = np.zeros((n * 20, n * 20), dtype=float)
    for i in range(n):
        for j in range(n):
            imageIndex = np.random.randint(0, m)
            while imageIndex in alreadyTaken:
                imageIndex = np.random.randint(0, m)
            y = i * 20
            x = j * 20
            finalImage[y:y+20,x:x+20] = X[imageIndex].reshape((20, 20)).T
    plt.imshow(finalImage, 'gray')
    plt.show()

# np.sqrt(5000) => 70.7
#dispMany(70)

def prepY(Y, c):
    return [int(Y[i] == c) for i in range(len(Y))]

#Z0 = prepY(Y, 0)
#Z1 = prepY(Y, 1)

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

sigmoid = np.vectorize(sigmoid)

def score(T, theta):
    som = sum([theta[i] * T[i] for i in range(400)])
    return som

def evalue(T, theta):
    return score(T, theta) > 0
    # return sigmoid(sum) > 1 / 2

"""def somme(tab):
    S = 0
    for el in tab:
        S += el
    return S"""

def cout_grad(X, Z, theta):
    beginning = time.time()
    print("begin: " + str(beginning))
    S = [sigmoid(sum([theta[j] * X[i][j] for j in range(400)])) for i in range(m)]
    J = sum([-Z[i] * np.log(S[i]) + (Z[i] - 1) * np.log(1 - S[i]) for i in range(m)]) / m
    grad = sum([((S[i] - Z[i]) * X[i]) / m for i in range(m)])
    print("end: " + str(time.time() - beginning))
    return J, grad # can share computation ?

def cout_grad(X, Z, theta):
    beginning = time.time()
    print("begin: " + str(beginning))
    S = sigmoid(X.dot(theta))
    print(S)
    J = sum([-Z[i] * np.log(S[i]) + (Z[i] - 1) * np.log(1 - S[i]) for i in range(m)]) / m
    grad = sum([((S[i] - Z[i]) * X[i]) / m for i in range(m)])
    print("end: " + str(time.time() - beginning))
    return J, grad

# numpy friendly function
def cout_grad(X, Z, theta):
    beginning = time.time()
    print("begin: " + str(beginning))
    S = sigmoid(X.dot(theta))
    #S = sigmoid(np.array([sum(theta * X[i]) for i in range(m)]))
    J = -sum(Z * np.log(S) + (1 - Z) * np.log(1 - S)) / m # dot ?!
    grad = (S - Z).dot(X) / m
    print("end: " + str(time.time() - beginning))
    return J, grad

Z = np.array(prepY(Y, 9))
theta = np.zeros((400))
J, grad = cout_grad(X, Z, theta)
# 1: 1.09s
# 2: 0.27s
# final: 0.014s

#S = sigmoid(X.dot(theta))

def grad(X, Z, theta):
    #S = sigmoid(np.array([sum(theta * X[i]) for i in range(m)]))
    S = sigmoid(X.dot(theta))
    return (S - Z).dot(X) / m

def descente(X, Z, alpha = 0.6, iter = 150):
    beginning = time.time()
    print("begin: " + str(beginning))
    theta = np.zeros((400))
    for i in range(iter):
        J, grad = cout_grad(X, Z, theta)
        theta -= alpha * grad
    print("end: " + str(time.time() - beginning))
    return theta

def descente(X, Z, alpha = 0.6, iter = 150):
    """beginning = time.time()
    print("begin: " + str(beginning))"""
    theta = np.zeros((400))
    for i in range(iter):
        theta -= alpha * grad(X, Z, theta) # why compute J so ?
    #print("end: " + str(time.time() - beginning))
    return theta

theta = descente(X, Z)
# 1: 129.6s
# 2: 51.19s
# without computing J: ~ 51.26...
# fnl: 1.3s

def efficacite(X, Z, theta):
    goodsSame = 0
    same = 0
    goodsDifferent = 0
    different = 0
    for i in range(m):
        isD = evalue(X[i], theta)
        if Z[i] == 1:
            same += 1
            if isD:
                goodsSame += 1
        else:
            different += 1
            if not isD:
                goodsDifferent += 1
    return goodsSame / same, goodsDifferent / different, (goodsSame + goodsDifferent) / m

e = efficacite(X, Z, theta)
print(e)

def descente_tout(X, Y, alpha = 0.6, iter = 150):
    beginning = time.time()
    print("begin: " + str(beginning))
    thetatotal = [descente(X, prepY(Y, d), alpha, iter) for d in range(10)]
    print("end: " + str(time.time() - beginning))
    return thetatotal

# before: ~ 20 minutes
# now: 13.76 s

thetatotal = descente_tout(X, Y)

def evalue_tout(T, thetatotal):
    best = -sys.maxsize - 1
    predictedD = -1
    for d in range(10):
        scoreD = score(T, thetatotal[d])
        if scoreD > best:
            best = scoreD
            predictedD = d
    return predictedD

def efficacite_tout(X, Y, thetatotal):
    som = 0
    for d in range(10):
        som += efficacite(X, prepY(Y, d), thetatotal[d])[2]
    return som / 10

def efficacite_tout(X, Y, thetatotal):
    goods = 0
    for i in range(m):
        if Y[i] == evalue_tout(X[i], thetatotal):
            goods += 1
    return goods / m

eTotal = efficacite_tout(X, Y, thetatotal) # 89.36 why not exactly the same ?
print(eTotal)

def example(n):
    biggest = max([max(X[i]) for i in range(m)])
    lowest = min([min(X[i]) for i in range(m)])
    middle = (biggest + lowest) / 2
    print(middle)
    alreadyTaken = []
    finalImage = np.zeros((n * 20, n * 20), dtype=float)
    for i in range(n):
        for j in range(n):
            imageIndex = np.random.randint(0, m)
            while imageIndex in alreadyTaken:
                imageIndex = np.random.randint(0, m)
            tmpImage = X[imageIndex]
            prediction = evalue_tout(X[imageIndex], thetatotal)
            real = Y[imageIndex]
            if prediction != real:
                print("prediction:", prediction, "real:", real) # what does "indiquer" mean ?
                tmpImage = biggest - tmpImage # en gros ça ? not sure car tmpImage peut être négatif parfois et donc on élargie l'échelle des couleurs...
                #tmpImage *= -1 # comment faire des couleurs inversées ?! le format de la couleur des pixels est tellement weird
            y = i * 20
            x = j * 20
            finalImage[y:y+20,x:x+20] = tmpImage.reshape((20, 20)).T
    plt.imshow(finalImage, 'gray')
    plt.show()

example(10)

