from Celda import Celda
import os
import webbrowser
class ListaCelda():
    def __init__(self):
        self.inicio2 = None
        self.size2 = 0

    def insertarCelda(self, Ro, Co, caracter):
        nuevo = Celda(Ro, Co,caracter)
        self.size2 += 1
        if self.inicio2 is None:
            self.inicio2 = nuevo
        else:
            tmp = self.inicio2
            while tmp.siguien is not None:
                tmp = tmp.siguien
            tmp.siguien = nuevo
            nuevo.anteri = tmp

    def imprimirDobleEnlaPa(self):
        tmp = self.inicio2
        while(tmp!=None):
            print(str(tmp.getFila())+" --- "+str(tmp.getColum())+" --- "+tmp.getCaracter())
            tmp = tmp.siguien
            
    def Sustitu(self, fila, columna, cade):
        try:
            tmp = self.inicio2
            while tmp != None:
                if tmp.coordefila == fila and tmp.coordecolumna == columna:
                    print("Llego")
                    tmp.caracter = cade
                tmp = tmp.siguien
            return None
        except: 
            print('Coordenada no encontrada')
            return None

    def Bus(self,cade):
        try:
            tmp = self.inicio2
            while tmp != None:
                if tmp.caracter == cade:
                    return tmp
                tmp = tmp.siguien
            return None
        except: 
            print('Coordenada no encontrada')
            return None

    def BusUni(self, cade):
        contador=0
        try:
            tmp = self.inicio2
            while tmp != None:
                if tmp.caracter == cade:
                    contador+=1
                tmp = tmp.siguien
            return contador
        except: 
            print('Coordenada no encontrada')
            return None
        
    def BusPE(self):
        contador=0
        try:
            tmp = self.inicio2
            while tmp != None:
                if tmp.caracter == "E" :
                    return tmp.coordefila,tmp.coordecolumna
                tmp = tmp.siguien
            return None
        except: 
            print('Coordenada no encontrada')
            return None

    def BusCF(self):
        contador=0
        try:
            tmp = self.inicio2
            while tmp != None:
                if tmp.caracter == "C" :
                    return tmp.coordefila
                tmp = tmp.siguien
            return None
        except: 
            print('Coordenada no encontrada')
            return None

    def BusCC(self):
        contador=0
        try:
            tmp = self.inicio2
            while tmp != None:
                if tmp.caracter == "C" :
                    return tmp.coordecolumna
                tmp = tmp.siguien
            return None
        except: 
            print('Coordenada no encontrada')
            return None

    def BusCF1(self):
        contador=0
        try:
            tmp = self.inicio2
            while tmp != None:
                if tmp.caracter == "R" :
                    return tmp.coordefila
                tmp = tmp.siguien
            return None
        except: 
            print('Coordenada no encontrada')
            return None

    def BusCC1(self):
        contador=0
        try:
            tmp = self.inicio2
            while tmp != None:
                if tmp.caracter == "R" :
                    return tmp.coordecolumna
                tmp = tmp.siguien
            return None
        except: 
            print('Coordenada no encontrada')
            return None

    
        
    