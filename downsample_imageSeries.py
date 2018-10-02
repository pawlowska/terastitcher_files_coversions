# -*- coding: utf-8 -*-
"""
Created on Thu Jul  5 10:06:59 2018

@author: MPawlowska
"""

substring='000.tif'

import os
import readMetadata, listaPozycji, prepFunctions
import shutil


rawDataDir = prepFunctions.wybierzKatalog()
imageSeriesDir = os.path.abspath(os.path.join(rawDataDir, 'imageSeries'))

os.chdir(rawDataDir)
nazwa='seriesSubset'
if not os.path.exists(nazwa):
            os.mkdir(nazwa)

if not 'lXY' in locals():
    print('robie listy')
    zStep=5
    slices=1036
    #find metadata file in it
    nazwaPliku=''
    for file in os.listdir(rawDataDir):
        if file.endswith('ositions.txt'): 
            nazwaPliku=file

    #read information from metadata file into dic and create lists
    dic = readMetadata.zrobListeStringowMM2(rawDataDir, nazwaPliku)
    print(dic)
    lZ = listaPozycji.listaPozycji1dim(0, zStep, slices)
    lXY = dic['listaStringow']
    #choosing unique values from the list of all X positions
    used=[]
    lX = [x for x in dic['listaXow'] if x not in used and (used.append(x) or True)]

for dX in lX:
    for dXY in lXY:
        if(dXY.startswith(dX+'_')):
            dirPath = os.path.abspath(os.path.join(os.path.join(imageSeriesDir, dX), dXY))
            print(dirPath)
            for file in os.listdir(dirPath):
                if file.endswith(substring): 
                    print(file)
                    shutil.copy2(os.path.join(dirPath, file), os.path.join(rawDataDir, nazwa))


