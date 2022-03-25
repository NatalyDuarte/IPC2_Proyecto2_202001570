from Robot import Robot
class ListaRobot():
    def __init__(self):
        self.inicio3 = None
        self.fin3 = None
        self.size3 = 0

    def insertarRobot(self,tipo,capacidad, nombre):
        new = Robot(tipo,capacidad, nombre)
        self.size3 += 1
        if self.inicio3 is None:
            self.inicio3 = new
        else:
            aux = self.inicio3
            while aux.siguiente3 is not None:
                aux = aux.siguiente3
            aux.siguiente3 = new

    def getRobot(self, nombre):
        aux = self.inicio3
        while aux is not None:
            if aux.nombre == nombre:
                return aux
            aux = aux.siguiente3
        return None

    def imprimirRobot(self):
        tmp = self.inicio3
        print("Imprimiendo Robots")
        while(tmp!=None):
            print(str(tmp.getNombre())+" --- "+tmp.getTipo()+" --- "+tmp.getCapacidad())
            tmp = tmp.siguiente3