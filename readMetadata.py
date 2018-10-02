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
    
    
    
def zrobListeStringow(dataDir, nazwaPliku, stageXY):
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