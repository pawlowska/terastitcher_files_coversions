# -*- coding: utf-8 -*-
"""
Created on Tue Feb 23 10:44:03 2016

@author: MPawlowska
"""

import os, re
import readMetadata, listaPozycji, prepFunctions

# KONFIGURACJA
zStep=4
nazwa_series='imageSeries'
suffixPlikuPozycji='low.txt'
######

rawDataDir = prepFunctions.wybierzKatalog()

#find metadata file in it
nazwaPlikuPozycji=''
l=os.listdir(rawDataDir)
nazwaPlikuPozycji = [i for i in l if i.endswith(suffixPlikuPozycji)][0]

#if (nazwaPlikuPozycji==''):
#    print('Positions file not found')
#for file in os.listdir(rawDataDir):
#    if file.endswith('metadata.txt'): 
#        nazwaPlikuPozycji=file

#znajdz nazwy katalogow z danymi
dataDir=os.path.abspath(os.path.join(rawDataDir,nazwa_series))
l=os.listdir(dataDir)
first_dir=[i for i in l if i.endswith('_Pos00')][0]
nazwa_katalogu=nazwa_pliku=first_dir[:-6]

#policz pliki
l=os.listdir(os.path.abspath(os.path.join(dataDir,first_dir)))
slices=len(l)
        
#create Z list
lZ = listaPozycji.listaPozycji1dim(0, zStep, slices)
#read information from metadata file into dic and create lists
dic = readMetadata.zrobListeStringowMM2(rawDataDir, nazwaPlikuPozycji)
print(dic)
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
 