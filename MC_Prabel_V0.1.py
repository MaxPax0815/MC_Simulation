# MonteCarlo Simulation zur BErechnung der Zahl Pi

import matplotlib as mlp
import matplotlib.pyplot as plt
import math as m 
import random
from sympy import *

def Nullstellen(): 
   x = symbols("x")
   solve(x**2, x)
   if 


def myFunc(x):
    return m.pow(x, 2)

def isTreffer(y, x):
    return y <= myFunc(x)
 

k = 7
nArr = []
rmsArr = []
random.seed(13)
upperBound = 4
lowerBound = 2
a = upperBound - lowerBound  
b = myFunc(upperBound)



nHits = 0
nShots = 0

for j in range(3, k):
    n = int(m.pow(10, j))
    for i in range(1, n):
        x = (random.random()) * (upperBound - lowerBound) + lowerBound
        y = (random.random()) * b
        nShots = nShots + 1
        if isTreffer(y, x):
            nHits = nHits + 1
    myInt = nHits / nShots * a * b
    print("n=", n)
    print("Integral =", myInt)
    nArr.append(n)
    rmsArr.append(myInt)
    
print(nArr)
print(rmsArr)
plt.plot(nArr, rmsArr)


