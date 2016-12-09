# -*- coding: utf-8 -*-
"""
Created on Mon Apr 25 15:39:43 2016

@author: MPawlowska
"""

def listaPozycji1dim(x0, dx, ile, razy = 10, dlugosc = '06'):
    lista=[]    
    x=x0
    for i in range(0,ile):
        lista.append(format(razy*x, dlugosc))
        x=x+dx
    return lista

def listaPozycjiXY(lX, lY):
    lista=[]    
    for x in lX:
        for y in lY:
            s = x+'_'+y
            lista.append(s)
    return lista