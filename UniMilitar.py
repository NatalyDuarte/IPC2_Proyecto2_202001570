
class UniMilitar():
    def __init__(self, fila, columna, numero):
        self.fila = fila
        self.columna = columna
        self.numero = numero
        self.siguiente2 = None

    def getFila(self):
        return self.fila

    def getColumna(self):
        return self.columna
    
    def getNumero(self):
        return self.numero

    def getSiguiente2(self):
        return self.siguiente2

    def setFila(self, fila):
        self.fila = fila

    def setColumna(self, columna):
        self.columna = columna

    def setNumero(self, numero):
        self.numero = numero

    def setSiguiente2(self,nodis2):
        self.siguiente2=nodis2