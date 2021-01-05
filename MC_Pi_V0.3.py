# MonteCarlo Simulation zur BErechnung der Zahl Pi

import matplotlib as mlp
import matplotlib.pyplot as plt
import math as m 
import random


def isTreffer(x, y, a) : 
    return(m.sqrt(m.pow(x, 2) + m.pow(y, 2)) <= a)


k = 5
nArr = []
rmsArr = []
random.seed(31)
a = 1

nHits = 0
nShots = 0

for j in range(3, k):
    n = int(m.pow(10, j))
    for i in range(1, n):
        x = (random.random()) * a
        y = (random.random()) * a  
        nShots = nShots + 1
        if(isTreffer(x, y, a)):
            print("Treffer")
            nHits = nHits + 1
        else:
            print("Kein Treffer")
    ZahlPi = nHits / nShots * 4.0
    rms = m.sqrt(m.pow(ZahlPi - m.pi, 2))
    print("n=", n)
    print("Pi=", ZahlPi)
    print("Differenz", rms)
    nArr.append(n)
    rmsArr.append(rms)
    
        
print(nArr)
print(rmsArr)
plt.plot(nArr, rmsArr)


