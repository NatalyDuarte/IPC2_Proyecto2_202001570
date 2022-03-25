class Robot():
    def __init__(self,tipo,capacidad, nombre):
        self.tipo = tipo
        self.capacidad = capacidad
        self.nombre = nombre
        self.siguiente3=None

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

    def getSiguiente3(self):
        return self.siguiente3

    def setSiguiente3(self,nodis3):
        self.siguiente3=nodis3