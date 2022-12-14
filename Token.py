#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Clase Token
"""
class Token:
   numLinea=0
   def __init__(self,tipotoken, subtipotoken,lexema,numLinea):
      self.tipotoken=tipotoken
      self.subtipotoken=subtipotoken
      self.lexema=lexema
      self.numLinea=numLinea
   def getTipo(self):
      return self.tipotoken
   def getSubTipo(self):
      return self.subtipotoken
   def getlexema(self):
      return self.lexema
   def setnumLinea(self,n):
      self.numLinea=n
   def getnumLinea(self):
      return self.numLinea
   def __str__(self):
           return"[  "+self.tipotoken+" --- "+self.subtipotoken+" --- "+self.lexema+" --- "+str(self.numLinea)+"  ]"
