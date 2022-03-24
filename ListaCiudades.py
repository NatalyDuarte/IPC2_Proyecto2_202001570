from Ciudad import Ciudad
class ListaCiudades():
    def __init__(self):
        self.inicio = None
        self.fin = None
        self.size = 0

    def insertarCiudad(self,fila,columna, nombre):
        new = Ciudad(fila,columna, nombre)
        self.size += 1
        if self.inicio is None:
            self.inicio = new
        else:
            aux = self.inicio
            while aux.siguiente is not None:
                aux = aux.siguiente
            aux.siguiente = new

    def getCiudad(self, nombre):
        aux = self.inicio
        while aux is not None:
            if aux.nombre == nombre:
                return aux
            aux = aux.siguiente
        return None