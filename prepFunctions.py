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
    prefixInne='displaySettings'
    nazwaTxt=[i for i in os.listdir(rawDataDir) if i.endswith(suffixTxt)]
    nazwaPlikuPozycjiL = [i for i in nazwaTxt if not i.startswith(prefixInne)]

    if (len(nazwaPlikuPozycjiL)==0):
        nazwaPlikuPozycji=''
        print('Positions file not found')
    else:
        nazwaPlikuPozycji=nazwaPlikuPozycjiL[0]
        print('Found positions file: ', nazwaPlikuPozycji)
        
    return nazwaPlikuPozycji