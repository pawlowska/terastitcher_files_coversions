# -*- coding: utf-8 -*-

#this file is imported in file_prep.py

import json, os

def zrobListeStringowMM2(dataDir, nazwaPliku):
    f = open(os.path.join(dataDir, nazwaPliku))
    t = f.read()
    ind=t.find("[")
    t=t[ind:]
    jObject = json.loads(t)
    
    listaStringow = []
    listaXow = []

    for p in jObject:
        x=p['subpositions'][0]['x']
        y=p['subpositions'][0]['y']
        s = format(10*x, '06')+'_'+format(10*y, '06')
        listaStringow.append(s)
        listaXow.append(format(10*x, '06'))

    d = {'listaStringow':listaStringow, 'listaXow':listaXow}    
    
    return d
    
    
def zrobListeStringow(dataDir, nazwaPliku, stageXY='Standa8SMC4XY'):
    f = open(os.path.join(dataDir, nazwaPliku))
    jObject = json.loads(f.read())

    z = jObject['FrameKey-0-0-0']['ZPositionUm']
    slices = jObject['Summary']['Slices']
    zStep = jObject['Summary']['z-step_um']
    listaPoz = jObject['Summary']['InitialPositionList']

    listaStringow = []
    listaXow = []

    for p in listaPoz:
        l = p['DeviceCoordinatesUm'][stageXY]
        s = format(10*l[0], '06')+'_'+format(10*l[1], '06')
        listaStringow.append(s)
        listaXow.append(format(10*l[0], '06'))
    
    d = {'z':z, 'zStep': zStep, 'slices':slices, 'listaStringow':listaStringow, 'listaXow':listaXow}    
    
    return d

def zrobListeStringowMM2_fromSavedPL(dataDir, nazwaPliku, stageXY='Standa8SMC4XY'):
    f = open(os.path.join(dataDir, nazwaPliku))
    jObject = json.loads(f.read())
    listaPoz = jObject['POSITIONS']

    listaStringow = []
    listaXow = []
    listaLbl=[]

    for p in listaPoz:
        listaLbl.append(p['LABEL'])
        x = p['DEVICES'][0]['X']
        y = p['DEVICES'][0]['Y']
        xs=format(10*x, '06')
        if xs not in listaXow:
            listaXow.append(xs)
        s= format(10*x, '06')+'_'+format(10*y, '06')
        if s not in listaStringow:
            listaStringow.append(s)
        
    d = {'listaStringow':listaStringow, 'listaXow':listaXow, 'labels':listaLbl}    
    
    return d
    
