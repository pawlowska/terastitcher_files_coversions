# -*- coding: utf-8 -*-
"""
Created on Tue Feb 23 10:44:03 2016

@author: MPawlowska
"""

import os, re
import readMetadata, listaPozycji

import tkinter as tk
from tkinter import filedialog

# pick stage
stagePicardXY = 'Picard XY Stage'
stageStandaXY = 'Standa8SMC4XY'


#display dialog for raw data directory
root = tk.Tk()
root.withdraw()
rawDataDir = filedialog.askdirectory()

#find metadata file in it
nazwaPliku=''
for file in os.listdir(rawDataDir):
    if file.endswith('metadata.txt'): 
        nazwaPliku=file

#read information from metadata file into dic and create lists
dic = readMetadata.zrobListeStringow(rawDataDir, nazwaPliku, stageStandaXY)
lZ = listaPozycji.listaPozycji1dim(0, dic['zStep'], dic['slices'])
lXY = dic['listaStringow']
#choosing unique values from the list of all X positions
used=[]
lX = [x for x in dic['listaXow'] if x not in used and (used.append(x) or True)]


def makeDirsX(parent, listaX):
    parent = os.path.abspath(parent)
    os.chdir(parent)
    for d in listaX:
        if not os.path.exists(d):
            os.mkdir(d)
    
def batchRenamingList(parent, prefixWas, listaNazw, prefix = '', suffix = '', verbose = False):
    os.chdir(parent)    
    listaPlikow = os.listdir(parent)
    if verbose:
        print(parent)
        print(listaPlikow)
    i = 0
    for f in listaPlikow:
        if(re.match(prefixWas, f)): #if the file has the right prefix - to reject metadata files etc
            nazwa = prefix+listaNazw[i]+suffix
            #print(f+ ' renaming to '+ nazwa)
            os.rename(f, nazwa)
            i=i+1
        
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

      
def movingVan(parent, listaX, listaXY):
    os.chdir(parent)
    #listaFolderow = os.listdir(parent)
    for dX in listaX:
        for d in listaXY:
            if(d.startswith(dX+'_')):
                os.rename(os.path.abspath(d), os.path.abspath(os.path.join(dX,d)))
    


def doIt(dataDir, lX, lXY, lZ):
    #make directories corresponding to X postions
    makeDirsX(dataDir, lX)
    print('x position directories completed')
    #rename
    batchRenaming(dataDir, lXY, lZ, nazwa_katalogu, nazwa_pliku)
    print('renaming completed')
    #move XY files to X directories
    movingVan(dataDir, lX, lXY)
    print('moving completed')
    os.chdir(os.path.abspath('d:/'))




#doIt(dataDir, lX, lXY, lZ)
 