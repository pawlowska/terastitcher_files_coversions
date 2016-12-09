# -*- coding: utf-8 -*-
"""
Created on Tue Feb 23 10:44:03 2016

@author: MPawlowska
"""

import os
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

#function for making directories based on a list
def makeDirsX(parent, listaX):
    parent = os.path.abspath(parent)
    os.chdir(parent)
    for d in listaX:
        if not os.path.exists(d):
            os.mkdir(d)
    
#moves directories from listaXY list into corresponding ones in listaX      
def movingVan(parent, listaX, listaXY):
    os.chdir(parent)
    #listaFolderow = os.listdir(parent)
    for dX in listaX:
        for d in listaXY:
            if(d.startswith(dX+'_')):
                os.rename(os.path.abspath(d), os.path.abspath(os.path.join(dX,d)))

#renames and moves data files      
def movingVanPos(parent, listaXY):
    os.chdir(parent)
    lista=os.listdir(parent)
    #listaFolderow = os.listdir(parent)
    i = 0 #moved so far    
    for f in lista:
        if(f.endswith('.ome.tif')):
            os.rename(os.path.abspath(f), os.path.abspath(os.path.join(listaXY[i],listaXY[i]+'.tif')))
            i=i+1

#executes operations one by one 
def doIt(dataDir, lX, lXY):
    #make directories corresponding to X postions
    makeDirsX(dataDir, lX)
    print('x position directories completed')
    #make directories corresponding to X postions
    makeDirsX(dataDir, lXY)
    print('xy position directories completed')
    movingVanPos(dataDir, lXY)
    #move XY files to X directories
    movingVan(dataDir, lX, lXY)
    print('moving completed')
    os.chdir(os.path.abspath('d:/'))



doIt(rawDataDir, lX, lXY)
 