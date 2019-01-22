# -*- coding: utf-8 -*-
"""
Created on Tue Feb 23 10:44:03 2016

@author: MPawlowska
"""

import os, re
import readMetadata, listaPozycji, prepFunctions

dataDir = prepFunctions.wybierzKatalog()

first_file=[i for i in os.listdir(dataDir) if i.endswith('_Pos00.ome.tif')][0]
nazwa_pliku_mm=nazwa_pliku_mm=first_file[:-13]

#read information from metadata file into dic and create lists
dic=readMetadata.makeDic(dataDir)
print(dic)
lXY = dic['listaStringow']
#choosing unique values from the list of all X positions
used=[]
lX = [x for x in dic['listaXow'] if x not in used and (used.append(x) or True)]


def doIt_3D(dataDir, lX, lXY, plik_mm):
    #make directories corresponding to X postions
    prepFunctions.makeDirsX(dataDir, lX)
    print('x position directories completed')    
    
    #rename
    prepFunctions.batchRenamingStack(dataDir, lXY, plik_mm)
    print('renaming completed')
    
    #move XY files to X directories
    prepFunctions.movingVan(dataDir, lX, lXY)
    print('moving completed')
    os.chdir(os.path.abspath('d:/'))

doIt_3D(dataDir, lX, lXY, nazwa_pliku_mm)
 