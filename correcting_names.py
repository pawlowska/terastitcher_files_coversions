# -*- coding: utf-8 -*-
"""
Created on Fri Mar  4 14:53:44 2016

@author: MPawlowska
"""

import os, re
import listaPozycji

dataDir = r'E:\Dane\2016\2016_11\2016_11_21\02_cfos35_powtorka\mysz_cfos35_1\imageSeries\050000'

def correctNames(basedir, old, new) :
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


correctNames(dataDir, '050000_', '054000_')

def shiftNames(dir):
    os.chdir(dir)    
    listaPlikow = os.listdir(dir)
    print(listaPlikow[0:5])
    listaNazw = listaPozycji.listaPozycji1dim(0, 1, len(listaPlikow), 1, '04')
    indx=listaPlikow[0].rfind('_')
    for i in range(0, len(listaPlikow)):
        plik = listaPlikow[i]
        os.rename(listaPlikow[i], listaPlikow[i].replace(plik[indx+1:indx+5], listaNazw[i]))
    listaPlikowNowa = os.listdir(dir)    
    print(listaPlikowNowa[0:5])
        
def repeatSubdirs(dir):
    listaFolderow = os.listdir(dir)
    print(listaFolderow)
    for d in listaFolderow:
        shiftNames(os.path.join(dir,d))
            
        
dirT = r'E:\Dane\2016\2016_04\2016_04_20\01_szczurTDP\mapa_1\imageSeries\083000'



#repeatSubdirs(dirT)
