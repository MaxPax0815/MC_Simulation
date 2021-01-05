# MonteCarlo Simulation zur BErechnung der Zahl Pi


import math as m 
import random

n = 1000000
random.seed(13)

nHits = 0
nShots = 0

for i in range(1, n):
    x = (random.random())
    y = (random.random())
    r = m.sqrt(m.pow(x,2) + m.pow(y,2))
    nShots = nShots + 1
    if r <= 1:
        nHits = nHits + 1

ZahlPi = nHits / nShots * 4.0
print("Pi=", ZahlPi)
print("Differenz", m.sqrt(m.pow(ZahlPi - m.pi, 2)))



