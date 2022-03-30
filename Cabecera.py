class Cabecera():
    
    def __init__(self, correlativo):
        self.correlativo = correlativo
        self.siguiente4 = None
        self.anterior4 = None
        self.acceso = None

    def getCorrelativo(self):
        return self.correlativo

    def setCorrelativo(self, correlativo):
        self.correlativo = correlativo

    def getAcceso(self):
        return self.acceso

    def setAcceso(self, acceso):
        self.acceso = acceso
    '''
    def __init__(self, valor, x =None, y = None):
        self.x = x
        self.y = y
        self.valor = valor
        self.derecho = None
        self.izquierdo = None
        self.arriba = None
        self.abajo = None
        self.siguiente = self.anterior = None
    '''