from UniMilitar import UniMilitar
class ListaUniMilitar():
    def __init__(self):
        self.inicio2 = None
        self.fin2 = None
        self.size2 = 0

    def insertarUniMili(self, fila, columna, numero):
        new1 = UniMilitar(fila, columna, numero)
        self.size2 += 1
        if self.inicio2 is None:
            self.inicio2 = new1
        else:
            aux1 = self.inicio2
            while aux1.siguiente2 is not None:
                aux1 = aux1.siguiente2
            aux1.siguiente2 = new1