from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog, QMessageBox, QGraphicsPixmapItem, QGraphicsScene
from PyQt5.uic import loadUi
import sys
from PyQt5.QtGui import QPixmap
from tkinter import messagebox
from tkinter import filedialog
import webbrowser
from xml.dom.minidom import ElementInfo
import xml.etree.ElementTree as ET

class Ventana(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("principal.ui", self)
        self.pushButton.clicked.connect(self.lectura)

    def lectura(self):
        global rutarecibida
        archi=filedialog.askopenfilename(filetypes=[("Archivos XML", ".xml .XML")])
        rutarecibida=self.Lectura(archi)

    def Lectura(archivo):
        tree = ET.parse(archivo)
        raiz = tree.getroot()
        global ciudades
        #ciudades = ListaCiudades()
        global nombre, filas, columnas, numero, unidad, tipo, capacidad, nom
        nombre = ""
        r = ""
        c = ""
        f = ""
        s = ""
        codigo = ""
        patron = ""
        print("===== ¡ARCHIVO LEIDO CORRECTAMENTE! ====")
        for elemento in raiz:
            nombre = elemento.attrib['nombre']
            # Pisos
            for belemento in elemento.iter('R'):
                r = belemento.text
            for belemento in elemento.iter('C'):
                c = belemento.text
            for belemento in elemento.iter('F'):
                f = belemento.text
            for belemento in elemento.iter('S'):
                s = belemento.text

            pisos.insertarSimpleEnla(
                    nombre, r, c,f,s)
            # Patrones
            for subelemento in elemento.iter('patron'):
                global elem,elem1
                elem = pisos.getPiso(nombre)
                codigo=subelemento.attrib['codigo']
                patron=subelemento.text
                patron=patron.replace(" ","")
                patron=patron.replace("\n","")   
                elem.lista_patron.insertarSimpleEnlaPa(codigo, patron)
                # Celdas
                elem1= elem.lista_patron.getPatron(codigo)
                longi = list(patron)
                divi=[longi[j:j + int(c)] for j in range(0,len(longi),int(c))]
                for i in range(int(r)):
                    for o in range(int(c)):
                        color=str(divi[i][o])
                        elem1.lista_celda.insertarCelda(str(i),str(o),color) 
    

if __name__ == '__main__':
    app = QApplication(sys.argv)
    GUI = Ventana()
    GUI.show()
    sys.exit(app.exec_())