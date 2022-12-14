#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 17:52:38 2020

@author: jlqf
"""

import AnalizadorLexico

l=AnalizadorLexico.AnalizadorLexico("programa.txt")

l.crearLista()

t=l.obtenerToken()
while t != None:
    print("Token: ",t)
    t=l.obtenerToken()
