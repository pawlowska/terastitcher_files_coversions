# -*- coding: utf-8 -*-
"""
Created on Mon Jul  9 12:51:06 2018

@author: MPawlowska
"""

import os, tkinter, re
from tkinter import filedialog

def wybierzKatalog():
    print('Pick directory!')
    #display dialog for raw data directory
    root = tkinter.Tk()
    root.withdraw()
    dataDir = filedialog.askdirectory()
    return dataDir

def makeDirsX(parent, listaX):
    parent = os.path.abspath(parent)
    os.chdir(parent)
    for d in listaX:
        if not os.path.exists(d):
            os.mkdir(d)
            
                  
def movingVan(parent, listaX, listaXY):
    os.chdir(parent)
    #listaFolderow = os.listdir(parent)
    for dX in listaX:
        for d in listaXY:
            if(d.startswith(dX+'_')):
                os.rename(os.path.abspath(d), os.path.abspath(os.path.join(dX,d)))

                
def correctNames(basedir, old, new) : #podmien substring old na new w basedir
    for fname in os.listdir(basedir):
        curpath = os.path.join(basedir, fname)
        if os.path.isdir(curpath):
            print(fname)
            os.chdir(basedir)
            dNew = re.sub(old, new, fname)
            os.rename(fname, dNew)
            os.chdir(os.path.join(basedir,dNew))
            listaPlikow = os.listdir()
            for p in listaPlikow:
                pNew = p.replace(old, new)
                os.rename(p, pNew)
                
def findPositionsFile(rawDataDir):
    suffixTxt='.txt'
    prefixMeta='METADATA_xy'
    prefixInne='displaySettings'
    nazwaTxt=[i for i in os.listdir(rawDataDir) if i.endswith(suffixTxt)]
    nazwaPlikuPozycjiL = [i for i in nazwaTxt if not i.startswith(prefixInne)]
    nazwaPlikuMetadanych=[i for i in nazwaPlikuPozycjiL if i.startswith(prefixMeta)]

    if (len(nazwaPlikuPozycjiL)==0):
        nazwaPlikuPozycji=''
        print('Positions file not found')
    elif (len(nazwaPlikuMetadanych)>0):
        nazwaPlikuPozycji=nazwaPlikuMetadanych[0]
        print('Found positions file: ', nazwaPlikuPozycji)
    else:    
        nazwaPlikuPozycji=nazwaPlikuPozycjiL[0]
        print('Found positions file: ', nazwaPlikuPozycji)
        
    return nazwaPlikuPozycji


    
def findImageSeries(rawDataDir):
    prefix='imageSeries'
    nazwaL = [i for i in  os.listdir(rawDataDir) if i.startswith(prefix)]

    for nazwa in nazwaL:
        if (nazwa=='imageSeries' or nazwa=='imageSeries_corBasic'):
            print('Found directory: ', nazwa)
            return nazwa

    print('Image series not found')

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
    batchRenamingList(parent, folderPrefix, listaXY)
    print('directories renaming completed')
    i = 0
    #for each renamed directory, rename files in it    
    for s in listaXY:
        dirPath = os.path.abspath(os.path.join(parent, s))
        batchRenamingList(dirPath, filenamePrefix, lZ, s+'_', suffix='.tif')
        i=i+1
        
def batchRenamingStack(parent, listaNazw, filenamePrefix):
    os.chdir(os.path.abspath(parent))
    listaPlikow = os.listdir(parent)
    i = 0
    renamed=False
    for f in listaPlikow:
        if(re.match(filenamePrefix, f)): #if the file has the right prefix - to reject metadata files etc
            nazwa = listaNazw[i]+'.tif'
            #print(f+ ' renaming to '+ nazwa)
            os.mkdir(listaNazw[i])
            os.rename(f, os.path.abspath(os.path.join(listaNazw[i],nazwa)))
            renamed=True
            i=i+1
    if not renamed:
        print('Nothing to rename!')
