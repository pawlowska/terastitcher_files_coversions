# -*- coding: utf-8 -*-
"""
Created on Mon Jul  9 12:58:09 2018

@author: MPawlowska
"""

import os
import prepFunctions

d = prepFunctions.wybierzKatalog()

tempX=[]
tempXY=[]
listaPlikow = os.listdir(d)
for f in listaPlikow:
    tX=f[0:6]
    tXY=f[0:13]
    tempX.append(tX)
    tempXY.append(tXY)

lX=[]    
lX = [x for x in tempX if x not in lX and (lX.append(x) or True)]
lXY=[]    
lXY = [x for x in tempXY if x not in lXY and (lXY.append(x) or True)]

prepFunctions.makeDirsX(d, lXY)
prepFunctions.movingVan(d, lXY, listaPlikow)
prepFunctions.makeDirsX(d, lX)
prepFunctions.movingVan(d, lX, lXY)
