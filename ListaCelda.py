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

    '''
    def getCelda(self):
        suma = 0
        tmp = self.inicio2
        while tmp is not None:
            suma  = suma+int(tmp.color)
            tmp = tmp.siguiente2
        return suma
    '''
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