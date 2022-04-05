from Robot import Robot
class ListaRobot():
    def __init__(self):
        self.inicio3 = None
        self.fin3 = None
        self.size3 = 0

    def insertarRobot(self,tipo,capacidad, nombre):
        resu=self.Buscar(nombre)
        print(resu)
        if (resu==True):
            print("entro robot")
            self.eliminar(nombre)
        else:
            pass
        new = Robot(tipo,capacidad, nombre)
        self.size3 += 1
        if self.inicio3 is None:
            self.inicio3 = new
        else:
            aux = self.inicio3
            while aux.siguiente3 is not None:
                aux = aux.siguiente3
            aux.siguiente3 = new

    def Buscar(self, nombre):
        actual = self.inicio3
        while actual!=None:
            if(actual.getNombre() == nombre):
                return True
            else:
                actual=actual.siguiente3
            return False

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
        cadena=" "
        while(tmp!=None):
            cadena=cadena+ "\n"+str(tmp.getNombre())+" --- "+tmp.getTipo()+" --- "+tmp.getCapacidad()
            print(str(tmp.getNombre())+" --- "+tmp.getTipo()+" --- "+tmp.getCapacidad())
            tmp = tmp.siguiente3
        return cadena

    def eliminar(self,nombre):
        actual = self.inicio3
        anterior = None
        encontrado = None
        while not encontrado:
            if(actual!=None):
                if (actual.getNombre()==nombre):
                    encontrado= True
                else:
                    anterior=actual
                    actual= actual.siguiente3
            else:
                break
        if (actual!=None):
            if(anterior==None):
                self.inicio3=actual.siguiente3
            else:
                anterior.setSiguiente3(actual.siguiente3)

    def RobotRes(self):
        aux = self.inicio3
        while aux is not None:
            if aux.tipo=="ChapinRescue":
                return aux
            aux = aux.siguiente3
        return None

    def RobotResNom(self):
        aux = self.inicio3
        while aux is not None:
            if aux.tipo=="ChapinRescue":
                return aux.nombre
            aux = aux.siguiente3
        return None

    def RobotResNom1(self):
        aux = self.inicio3
        while aux is not None:
            if aux.tipo=="ChapinFighter":
                return aux.nombre
            aux = aux.siguiente3
        return None

    def RobotResCont(self):
        contador=0
        aux = self.inicio3
        while aux is not None:
            if aux.tipo=="ChapinRescue":
                contador+=1
            aux = aux.siguiente3
        return contador

    def RobotEx(self):
        aux = self.inicio3
        while aux is not None:
            if aux.tipo=="ChapinFighter":
                return aux
            aux = aux.siguiente3
        return None

    def RobotExCont(self):
        contador=0
        aux = self.inicio3
        while aux is not None:
            if aux.tipo=="ChapinFighter":
                contador+=1
            aux = aux.siguiente3
        return contador
        