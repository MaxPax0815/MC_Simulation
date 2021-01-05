# MonteCarlo Simulation zur BErechnung der Zahl Pi

import matplotlib as mlp
import matplotlib.pyplot as plt
import math as m 
import random

k = 8
nArr = []
rmsArr = []
random.seed(31)

nHits = 0
nShots = 0

for j in range(2, k):
    n = int(m.pow(10, j))
    for i in range(1, n):
        x = (random.random())
        y = (random.random())
        r = m.sqrt(m.pow(x,2) + m.pow(y,2))
        nShots = nShots + 1
        if r <= 1:
            nHits = nHits + 1
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


