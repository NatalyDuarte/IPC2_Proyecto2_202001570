class Robot():
    def __init__(self,tipo,capacidad, nombre):
        self.tipo = tipo
        self.capacidad = capacidad
        self.nombre = nombre
        #self.lista_fila = ListaFila()
        #self.lista_unimilitar = ListaUniMilitar()
        self.siguiente1=None

    def getTipo(self):
        return self.tipo
    
    def setTipo(self, tipo):
        self.tipo = tipo

    def getCapacidad(self):
        return self.capacidad
    
    def setCapacidad(self, capacidad):
        self.capacidad = capacidad

    def getNombre(self):
        return self.nombre
    
    def setNombre(self, nombre):
        self.nombre = nombre

    def getSiguiente1(self):
        return self.siguiente1

    def setSiguiente1(self,nodis1):
        self.siguiente1=nodis1