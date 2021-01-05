# -*- coding: utf-8 -*-
"""
Created on Tue Dec 22 20:29:29 2020

@author: mahei
"""
import math as m 
from scipy import optimize
import numpy as np
import random 

def myFunc(x):
    return m.sin(x)

def isTreffer(y, x):
    return y <= myFunc(x)


k = 7
nShots = 0
nHits = 0

lBound = -2
uBound = 8
nStep = 10
tol = 1e-5
minima = []
maxima = []
roots = []

extrema = np.sort(np.concatenate((minima, maxima)))

for isVal in extrema:
    isIndex = np.searchsorted(roots, isVal, side='left') - 1
    print(isVal, roots[isIndex], roots[isIndex + 1], myFunc(isVal))

a = roots[isIndex + 1] - roots[isIndex]
b = extrema 

minima.append(lBound)   
maxima.append(lBound)
roots.append(lBound)
stepSize = (uBound - lBound)/float(nStep)

for i in range(0, nStep + 1):    
    minimum = optimize.fmin_powell(myFunc, i*stepSize + lBound, ftol=tol)
    maximum = optimize.fmin_powell(lambda x: -myFunc(x), i*stepSize + lBound, ftol=tol)
    root = optimize.fsolve(myFunc, i*stepSize + lBound, xtol=tol)
    print(i * stepSize + lBound, minimum, maximum, root)
    if(abs(minimum - minima[-1]) > tol * 10) and (minimum >= lBound) and (minimum <= uBound):
        minima.append(minimum[0])
    if(abs(maximum - maxima[-1]) > tol * 10) and (maximum >= lBound) and (maximum <= uBound):
        maxima.append(maximum[0])
    if(abs(root - roots[-1]) > tol * 10) and ( root >= lBound) and (root <= uBound):
        roots.append(root[0])
    for j in range(3, k):
        n = int(m.pow(10, j))
        for i in range(1, n):
            x = (random.random()) * a + roots[isIndex]
            y = (random.random()) * b
            nShots = nShots + 1
            if isTreffer(y, x):
                nHits = nHits + 1
        myInt = nHits / nShots * a * b

minima.pop(0)
maxima.pop(0)
roots.append(uBound)
    
print(minima, maxima, roots)

extrema = np.sort(np.concatenate((minima, maxima)))

for isVal in extrema:
    isIndex = np.searchsorted(roots, isVal, side='left') - 1
    print(isVal, roots[isIndex], roots[isIndex + 1], myFunc(isVal))

    
    
    
    
    
    