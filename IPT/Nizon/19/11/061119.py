import numpy as np

"""

append(l, element) # first one can be generic
l.append(element)

l = append(l, 5)
l.append(5) # ne fait pas une copie de la liste

"""

class Cercle():
    "test"
    # like this !
    # works also with """ test """
    # if spaces are given, __doc__ will return with spaces
    
    nCercle = 0 # is required !
    
    def __init__(self, a = 100, b = 100, c = 10): # required self
        self.centrex = a # if don't use "self." create local (functon) variable
        self.centrey = b
        self.rayon = c
        self.epaisseur = 2
        Cercle.nCercle += 1 # REQUIRED Cercle. ! (can't use self.nCercle otherwise "masquage" et devient une variable locale)
    
    def appartient(self, x, y): # self is required ! (even required if writing: Cercle.appartient(testCircle, 0, 0))
        "             appartient doc         !" # first spaces aren't taken in account
        # also works with triple '"'
        return (x - self.centrex) ** 2 + (y - self.centrey) ** 2 <= self.rayon ** 2

    def affiche(self):
        return

"""

Cercle.__doc__ works too
testCircle.nCercle works of course

as in paper: testCircle.__doc__ works too

"""

testCircle = Cercle()
print(dir(Cercle))
print(dir(testCircle)) # works too

print(help(Cercle.appartient)) # TODO: why None at the end ?
print(help(testCircle.appartient)) # add "method of __main__.Cercle instance"

print(dir(int)) # denumerator ?!
print(help(int.denominator)) # works

"""

assert comme raise arrête le programme, assert plus pour les erreurs qui ne sont censés jamais arrivés
raison plus pour les erreurs que l'on gère

"""

# TODO: test assert and raise
# np.zeros((nb)) same as np.zeros(nb)

# could not initialize array
# TODO: find these functions

"""

3 + 4 # infixe
+(3, 4) # prefix (exemple: functions)
(3, 4)+ # postfix (exemple: factorial)

"""

class Pile1():
    def __init__(self):
        self.data = []
    
    def empile(self, a):
        self.data.append(a)
    
    def depile(self):
        assert len(self.data) > 0, "Pile vide"
        return self.data.pop()
    
    def est_vide(self):
        return self.data == []

class Pile2():
    def __init__(self, max):
        self.data = np.zeros((max))
        self.taille = 0
        self.max = max
    
    def empile(self, a):
        if self.taille == self.max:
            raise Exception("pile pleine")
        self.data[self.taille] = a
        self.taille += 1
    
    def depile(self):
        if self.taille == 0:
            raise Exception("pile vide")
        self.taille -= 1
        return self.data[self.taille]

# TODO: polonais + laby

pol = ["23", "5", "+", "2", "*"]

def polo(l): # warning let say: don't modify l
    polPil = Pile1()
    def aux(l):
        if len(l) == 1:
            if type(l[0]) == int:
                return 
            else:
                raise Exception("not well formatted !")
    aux(l)
    return polPil.depile()

print(polo(pol))

"""

TODO: ensemble des expressions postfix "clotûre"
Peut prouver par induction structurelle l'algorithme

"""

def decomp(n):
    # bas de la pile = l[-1]
    # return list(map(int, list(str(n))))
    # pop return last element
    p = []
    while n != 0:
        r = n % 10
        n //= 10
        p.append(r)
    return p

a = decomp(123)
b = decomp(456)

def depile(p, r):
    while not (p == []):
        r.append(p.pop())

depile(a, b)
print(b)

##

def wellParenthesis(txt):
    separators = "{([])}"
    endSeparators = "})]"
    p = []
    for chr in txt:
        if chr in separators:
            #print(chr, p)
            if chr in endSeparators:
                openChar = endSeparators[separators.find(p.pop())]
                #print(openChar)
                """if openChar == '(': openChar = ')'
                elif openChar == '[': openChar = ']'
                elif openChar == '{': openChar = '}'"""
                if chr != openChar:
                    return False
            else:
                p.append(chr)
    return p == []

"""

ord:

( 40
[ 91
{ 123

"""

print(wellParenthesis("test(test]"))
print(wellParenthesis("test(test{test})"))

# TODO: link between pile and file ?

def creer_file():
    return []

def enfile(f, x):
    r = []
    depile(f, r)
    r.append(x)
    depile(f, [])
    depile(r, f)
   
f = creer_file()
print(f)
enfile(f, 2)
print(f)
enfile(f, 3)
print(f)

def defile(f):
    r = []
    depile(f, r)
    el = r.pop()
    depile(f, [])
    depile(r, f)
    return el

print(f)
print(defile(f))
print(f)

def est_vide(f):
    return f == []

# better version

def creer_file():
    return [], []

def enfile(f, x):
    depile([x], f[0])

def defile(f):
    if est_vide(f): raise Exception("empty file")
    depile(f[0], f[1])
    return f[1].pop()

def est_vide(f):
    return f[0] == [] and f[1] == []

""" PROUT PROUT PROUT
def polopolo(l):
    print(l)
    b = l.pop()
    if type(b) == int:
        return b
    a = l.pop()
    if chr == '-':
        a -= b
    elif chr == '*':
        a *= b
    elif chr == '+':
        a += b
    l.append(a)
    return polopolo(l)"""
    
def polopolo(l):
    operateurs = "+-*"
    p = []
    for el in l:
        if str(el) in operateurs:
            y = p.pop()
            x = p.pop()
            if el == '+': x += y
            elif el == '-': x -= y
            else: x *= y
            p.append(x)
        else:
            p.append(el)
    return p.pop()

l = [3, 4, "-", 6, 5, "-", "*", 4, "-"]
print(polopolo(l))

def creer_listedouble(taillemax):
    t = np.zeros(taillemax + 2) # last: i, f
    t[-2] = taillemax // 2 - 1
    t[-1] = taillemax // 2
    return t

# if i = j => full, if i = j - 1 => empty
def checkPlein(f):
    if f[-1] == f[-2]: raise Exception("plein !")

def checkVide(f):
    if f[-1] == f[-2] - 1: raise Exception("vide !")

def empile_haut(f, x):
    checkPlein(f)
    f[f[-1]] = x
    if f[-1] == len(f) - 3:
        f[-1] = 0 
    else:
        f[-1] += 1

def empile_bas(f, x):
    checkPlein(f)
    f[f[-2]] = x
    if f[-2] == 0:
        f[-2] = len(f) - 3
    else:
        f[-2] -= 1

def depile_haut(f):
    checkVide(f)
    f[-1] -= 1
    return f[f[-1] + 1]

def depile_bas(f):
    checkVide(f)
    f[-2] += 1
    return f[f[-2] - 1]

ld = creer_listedouble(25)
print(ld)
empile_haut(ld, 42)
print(ld)
empile_haut(ld, 43)
empile_bas(ld, 41) # TODO: can't add last element solve IT
print(ld)

"""

minimum local descente de gradient
exemple: selle de cheval
dimension 400: minimum locale il faut que les 400 soient dans la même direction

dim: 2 : une chance sur 2
donc 400 balek

"""

