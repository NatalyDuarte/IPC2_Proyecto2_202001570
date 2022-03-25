from Fila import Fila
class ListaFila():
    def __init__(self):
        self.inicio1 = None
        self.fin1 = None
        self.size1 = 0

    def insertarFila(self, numero, secuencia):
        new1 = Fila(numero, secuencia)
        self.size1 += 1
        if self.inicio1 is None:
            self.inicio1 = new1
        else:
            aux1 = self.inicio1
            while aux1.siguiente1 is not None:
                aux1 = aux1.siguiente1
            aux1.siguiente1 = new1

    def imprimirFila(self):
        tmp = self.inicio1
        print("Imprimiendo Fila")
        while(tmp!=None):
            print(str(tmp.getNumero())+" --- "+tmp.getSecuencia())
            tmp = tmp.siguiente1