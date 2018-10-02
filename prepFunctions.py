# -*- coding: utf-8 -*-
"""
Created on Mon Jul  9 12:51:06 2018

@author: MPawlowska
"""

import os, tkinter
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