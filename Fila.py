
class Fila():
    def __init__(self, numero, secuencia):
        self.numero = numero
        self.secuencia = secuencia
        #self.lista_celda = ListaCelda()
        self.siguiente1 = None
    
    def getNumero(self):
        return self.numero

    def getSecuencia(self):
        return self.secuencia

    def getSiguiente1(self):
        return self.siguiente1

    def setNumero(self, numero):
        self.numero = numero

    def setSecuencia(self, secuencia):
        self.secuencia = secuencia

    def setSiguiente1(self,nodis1):
        self.siguiente1=nodis1