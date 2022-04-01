from Ciudad import Ciudad
class ListaCiudades():
    def __init__(self):
        self.inicio = None
        self.fin = None
        self.size = 0

    def insertarCiudad(self,fila,columna, nombre):
        resu=self.Buscar(nombre)
        if (resu==True):
            self.eliminar(nombre)
        else:
            pass
        new = Ciudad(fila,columna, nombre)
        self.size += 1
        if self.inicio is None:
            self.inicio = new
        else:
            aux = self.inicio
            while aux.siguiente is not None:
                
                aux = aux.siguiente
            aux.siguiente = new

    def Buscar(self, nombre):
        actual = self.inicio
        while actual!=None:
            if(actual.getNombre() == nombre):
                return True
            else:
                actual=actual.siguiente
            return False

    def getCiudad(self, nombre):
        aux = self.inicio
        while aux is not None:
            if aux.nombre == nombre:
                return aux
            aux = aux.siguiente
        return None

    def imprimirCiuda(self):
        tmp = self.inicio
        print("Imprimiendo ciudades")
        cadena=" "
        while(tmp!=None):
            cadena=cadena+ "\n"+ str(tmp.getNombre())+" --- "+tmp.getFila()+" --- "+tmp.getColumna()
            print(str(tmp.getNombre())+" --- "+tmp.getFila()+" --- "+tmp.getColumna())
            tmp = tmp.siguiente
        return cadena

    def eliminar(self,nombre):
        actual = self.inicio
        anterior = None
        encontrado = None
        while not encontrado:
            if(actual!=None):
                if (actual.getNombre()==nombre):
                    encontrado= True
                else:
                    anterior=actual
                    actual= actual.siguiente
            else:
                break
        if (actual!=None):
            if(anterior==None):
                self.inicio=actual.siguiente
            else:
                anterior.setSiguiente(actual.siguiente)
            

 