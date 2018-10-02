# -*- coding: utf-8 -*-
"""
Created on Tue Feb 23 10:44:03 2016

@author: MPawlowska
"""

import os, re
import readMetadata, listaPozycji, prepFunctions


# KONFIGURACJA
zStep=4
slices=1374
nazwa_katalogu=nazwa_pliku='488_medium_1'
nazwa_series='imageSeries_corBasic'
######

rawDataDir = prepFunctions.wybierzKatalog()

#find metadata file in it
nazwaPliku=''
for file in os.listdir(rawDataDir):
    if file.endswith('medium.txt'): 
#    if file.endswith('positions.txt'): 
#    if file.endswith('metadata.txt'): 
        nazwaPliku=file

#read information from metadata file into dic and create lists
dic = readMetadata.zrobListeStringowMM2(rawDataDir, nazwaPliku)
print(dic)
lZ = listaPozycji.listaPozycji1dim(0, zStep, slices)
lXY = dic['listaStringow']
#choosing unique values from the list of all X positions
used=[]
lX = [x for x in dic['listaXow'] if x not in used and (used.append(x) or True)]

def batchRenamingList(parent, prefixWas, listaNazw, prefix = '', suffix = '', verbose = False):
    os.chdir(parent)    
    listaPlikow = os.listdir(parent)
    
    if verbose:
        print(parent)
        print(listaPlikow)
    i = 0
    renamed=False
    for f in listaPlikow:
        if(re.match(prefixWas, f)): #if the file has the right prefix - to reject metadata files etc
            nazwa = prefix+listaNazw[i]+suffix
            #print(f+ ' renaming to '+ nazwa)
            os.rename(f, nazwa)
            renamed=True
            i=i+1
    if not renamed:
        print('Nothing to rename!')
        
def batchRenaming(parent, listaXY, listaZ, folderPrefix, filenamePrefix):
    parent = os.path.abspath(parent)
    os.chdir(parent)
    #rename directories from original name to XY positions
    batchRenamingList(parent, folderPrefix, listaXY, verbose = True)
    print('directories renaming completed')
    i = 0
    #for each renamed directory, rename files in it    
    for s in listaXY:
        dirPath = os.path.abspath(os.path.join(parent, s))
        batchRenamingList(dirPath, filenamePrefix, lZ, s+'_', suffix='.tif')
        i=i+1

dataDir=os.path.abspath(os.path.join(rawDataDir,nazwa_series))

def doIt(dataDir, lX, lXY, lZ):
    #make directories corresponding to X postions
    prepFunctions.makeDirsX(dataDir, lX)
    print('x position directories completed')
    #rename
    batchRenaming(dataDir, lXY, lZ, nazwa_katalogu, nazwa_pliku)
    print('renaming completed')
    #move XY files to X directories
    prepFunctions.movingVan(dataDir, lX, lXY)
    print('moving completed')
    os.chdir(os.path.abspath('d:/'))

doIt(dataDir, lX, lXY, lZ)
 