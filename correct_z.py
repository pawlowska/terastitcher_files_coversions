# -*- coding: utf-8 -*-
"""
Created on Thu Oct  4 12:35:20 2018

@author: MPawlowska
"""

import os
import readMetadata, listaPozycji, prepFunctions

###### KONFIGURACJA #########
zStepOld=4
zStepNew=10
nazwa_series='imageSeries'
#############################

rawDataDir = prepFunctions.wybierzKatalog()

#find metadata file in it
nazwaPlikuPozycji=prepFunctions.findPositionsFile(rawDataDir)

#read information from metadata file into dic and create lists
dic = readMetadata.zrobListeStringowMM2(rawDataDir, nazwaPlikuPozycji)
lXY = dic['listaStringow']
#choosing unique values from the list of all X positions
used=[]
lX = [x for x in dic['listaXow'] if x not in used and (used.append(x) or True)]

#policz Z slices
dataDir=os.path.abspath(os.path.join(rawDataDir,nazwa_series))
dirX0=os.path.abspath(os.path.join(dataDir,lX[0]))
slices=len(os.listdir(os.path.abspath(os.path.join(dirX0,lXY[0]))))
        
#create Z list
lZOld = listaPozycji.listaPozycji1dim(0, zStepOld, slices)
lZNew = listaPozycji.listaPozycji1dim(0, zStepNew, slices)

if(zStepOld>zStepNew):
    r=range(0,len(lZOld)-1)
else:
    r=range(len(lZOld)-1,0,-1)
    
for subdirX in lX:
    dirX=os.path.abspath(os.path.join(dataDir,subdirX))
    for subdirXY in lXY:
        if(subdirXY.startswith(subdirX)):
            dirXY=os.path.abspath(os.path.join(dirX, subdirXY))
            print(dirXY)
            os.chdir(dirXY)
            for i in r:
                nameOld=subdirXY+'_'+lZOld[i]+'.tif'
                nameNew=subdirXY+'_'+lZNew[i]+'.tif'
                os.rename(nameOld, nameNew)
                