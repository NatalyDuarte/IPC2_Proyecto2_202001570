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
'''
    def __init__(self):
        self.raiz = self.ultimo = None

    def insertar(self, valor):
        nuevo = Cabecera(valor)
        if self.raiz == None:
            self.raiz = self.ultimo = nuevo
        else:
            self.ordenar(nuevo)
    
    def ordenar(self, nodo):
        aux = self.raiz
        while(aux!=None):
            if aux.valor < nodo.valor:
                aux = aux.siguiente
            else:
                if aux == self.raiz:
                    nodo.siguiente = aux
                    aux.anterior = nodo
                    self.raiz = nodo
                    return
                else:
                    nodo.anterior = aux.anterior
                    aux.anterior.siguiente = nodo
                    nodo.siguiente = aux
                    aux.anterior = nodo
                    return
            self.ultimo.siguiente = nodo
            nodo.anterior = self.ultimo
            self.ultimo = nodo
    
    def search(self, valor):
        temp = self.raiz
        while(temp != None):
            if temp.valor == valor:
                return temp
            temp = temp.siguiente
        return None

    def print(self):
        temp = self.raiz
        while(temp!=None):
            print("Cabecera:", temp.valor)
            temp = temp.siguiente
    '''