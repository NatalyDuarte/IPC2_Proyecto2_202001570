from Cabecera import Cabecera
class ListaCabecera():
    def __init__(self, tipo):
        self.primero4 = None
        self.ultimo4 = None
        self.tipo = tipo
        self.size4 = 0
   
    def insertarCabe(self, nuevo):
        self.size4 += 1
        if self.primero4 == None:
            self.primero4 = nuevo
            self.ultimo4 = nuevo
        else:
            if nuevo.correlativo < self.primero4.correlativo:
                nuevo.siguiente4 = self.primero4
                self.primero4.anterior4 = nuevo
                self.primero4 = nuevo
            elif nuevo.correlativo > self.ultimo4.correlativo:
                self.ultimo4.siguiente4 = nuevo
                nuevo.anterior4 = self.ultimo4
                self.ultimo4 = nuevo
            else:
                tmp = self.primero4 
                while tmp != None:
                    if nuevo.correlativo < tmp.correlativo:
                        nuevo.siguiente4 = tmp
                        nuevo.anterior4 = tmp.anterior4
                        tmp.anterior4.siguiente4 = nuevo
                        tmp.anterior4 = nuevo
                        break
                    elif nuevo.correlativo > tmp.correlativo:
                        tmp = tmp.siguiente4
                    else:
                        break
  
    def imprimirCabecera(self):
        tmp = self.primero4
        while tmp != None:
            print('Cabecera', self.tipo, tmp.correlativo)
            tmp = tmp.siguiente4
            
    def getCabecera(self, id): 
        tmp = self.primero4
        while tmp != None:
            if id == tmp.correlativo:
                return tmp
            tmp = tmp.siguiente4
        return None
