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
    