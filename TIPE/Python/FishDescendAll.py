import numpy as np
import matplotlib.pyplot as plt
import numpy.random as rd
import os
import time
import sys
from PIL import Image

folderSpeciesPath = "C:\\Users\\Benjamin\\Desktop\\BensFolder\\School\\CPGE\\Fenelon\\MPSI\\TIPE\\mainComputer\\fish\\QUT_fish_data\\images\\images\\training\\trainingDataset\\species\\bySpecies"

os.chdir(folderSpeciesPath)

"""
model:
- black and white (forme) 1st (easy because like digits)
- colored (forme et coloration) 2nd
"""

m = sum([len(files) for r, d, files in os.walk(folderSpeciesPath)])
speciesNumber = 0 # really need initialization ?

for r, d, files in os.walk(folderSpeciesPath):
    if len(files) == 0:
        speciesNumber = len(d)
        continue
    im = Image.open(r + "\\" + files[0])
    width, height = im.size
    pixelNumber = width * height
    break

# ~ execution time: (10 seconds for 5 000 digits of 400 pixels): (m / 5000) * (pixelNumber / 400) = 62 so about 620 seconds

"""for r, d, files in os.walk(folderSpeciesPath):
    r += "\\"
    for file in files:
        file = r + file
        im = Image.open(file)
        width, height = im.size
        print(file, width, height)""" # already set at same size

# pictures should initially be in png because we can find "pure" white on fishes

# WARNING LOOPING LIKE: 0, 1, 10, 100, 101, 102... not 0, 1, 2...

def cstrY():
    Y = np.zeros((m), dtype=np.int)
    index = 0
    walk = os.walk(folderSpeciesPath)
    for r, d, files in walk:
        if r == folderSpeciesPath: continue
        filesLen = len(files)
        Y[index : index + filesLen + 1] = int(r.split("\\")[-1])
        index += filesLen
    return Y

Y = cstrY()

def cstrX():
    X = np.zeros((m, pixelNumber), dtype=float) # used to be float, may need to regle de trois
    j = 0
    for r, d, files in os.walk(folderSpeciesPath):
        r += "\\"
        for file in files:
            file = r + file
            L = np.zeros(pixelNumber, dtype=float)
            im = Image.open(file)
            data = im.getdata()
            for i in range(pixelNumber):
                L[i] = sum(data[i]) / 3
            X[j] = L
            j += 1
        print(j)
    return X

X = cstrX()

def display(imageIndex):
    im = X[imageIndex].reshape((height, width))
    print(X[imageIndex])
    plt.imshow(im, 'gray')
    plt.show()

display(57)

def dispMany(n):
    alreadyTaken = []
    finalImage = np.zeros((n * height, n * width), dtype=float)
    for i in range(n):
        for j in range(n):
            imageIndex = np.random.randint(0, m)
            while imageIndex in alreadyTaken:
                imageIndex = np.random.randint(0, m)
            y = i * height
            x = j * width
            finalImage[y:y+height,x:x+width] = X[imageIndex].reshape((height, width))
    plt.imshow(finalImage, 'gray')
    plt.show()

dispMany(25)

def prepY(Y, c):
    return [int(Y[i] == c) for i in range(len(Y))]

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

sigmoid = np.vectorize(sigmoid)

def score(T, theta):
    som = sum([theta[i] * T[i] for i in range(pixelNumber)])
    return som

def evalue(T, theta):
    return score(T, theta) > 0

def cout_grad(X, Z, theta):
    S = sigmoid(X.dot(theta))
    return (S - Z).dot(X) / m

Z = np.array(prepY(Y, 0))
theta = np.zeros((pixelNumber))
grad = cout_grad(X, Z, theta)

def grad(X, Z, theta):
    S = sigmoid(X.dot(theta))
    return (S - Z).dot(X) / m

def descente(X, Z, alpha = 0.6, iter = 150):
    theta = np.zeros((pixelNumber))
    for i in range(iter):
        theta -= alpha * grad(X, Z, theta)
    return theta

theta = descente(X, Z)

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
    thetatotal = [descente(X, prepY(Y, d), alpha, iter) for d in range(speciesNumber)] # descente tant que efficacite tout augmente ou de l'espère donné ? et quelle valeur pour alpha ?
    return thetatotal

thetatotal = descente_tout(X, Y)

def evalue_tout(T, thetatotal):
    best = -sys.maxsize - 1
    predictedD = -1
    for d in range(speciesNumber):
        scoreD = score(T, thetatotal[d])
        if scoreD > best:
            best = scoreD
            predictedD = d
    return predictedD

def efficacite_tout(X, Y, thetatotal):
    goods = 0
    for i in range(m):
        if Y[i] == evalue_tout(X[i], thetatotal):
            goods += 1
    return goods / m

eTotal = efficacite_tout(X, Y, thetatotal)
print(eTotal)

# todo: other method (or improve) AND WORK ON DESCENTE PROCESS (ARBITRARY VALUES) !

def example(n):
    biggest = max([max(X[i]) for i in range(m)])
    lowest = min([min(X[i]) for i in range(m)])
    middle = (biggest + lowest) / 2
    print(middle)
    alreadyTaken = []
    finalImage = np.zeros((n * height, n * width), dtype=float)
    for i in range(n):
        for j in range(n):
            imageIndex = np.random.randint(0, m)
            while imageIndex in alreadyTaken:
                imageIndex = np.random.randint(0, m)
            tmpImage = X[imageIndex]
            prediction = evalue_tout(X[imageIndex], thetatotal)
            real = Y[imageIndex]
            if prediction != real:
                print("prediction:", prediction, "real:", real)
                tmpImage = biggest - tmpImage
            y = i * height
            x = j * width
            finalImage[y:y+height,x:x+width] = tmpImage.reshape((height, width))
    plt.imshow(finalImage, 'gray')
    plt.show()

example(5)

