class Ciudad():
    def __init__(self,fila,columna, nombre):
        self.fila = fila
        self.columna = columna
        self.nombre = nombre
        #self.lista_fila = ListaFila()
        #self.lista_unimilitar = ListaUniMilitar()
        self.siguiente=None

    def getFila(self):
        return self.fila
    
    def setFila(self, fila):
        self.fila = fila

    def getColumna(self):
        return self.columna
    
    def setColumna(self, columna):
        self.columna = columna

    def getNombre(self):
        return self.nombre
    
    def setNombre(self, nombre):
        self.nombre = nombre

    def getSiguiente(self):
        return self.siguiente

    def setSiguiente(self,nodis):
        self.siguiente=nodis