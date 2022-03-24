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
from ListaCiudades import ListaCiudades

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
        filas = ""
        columnas = ""
        numero = ""
        unidad = ""
        tipo = ""
        capacidad = ""
        nom =""
        global ciudades
        ciudades = ListaCiudades()
        print("===== ¡ARCHIVO LEIDO CORRECTAMENTE! ====")
        for elemento in raiz.iter('listaCiudades'):
            for subelemento in elemento.iter('ciudad'):
                #ciudades
                for subsubelemento in subelemento.iter('nombre'):
                    nombre = subsubelemento.text
                    ciudades.insertarCiudad(subsubelemento.attrib['filas'], subsubelemento.attrib['columnas'], nombre)
                #Fila
                for subsubelemento1 in subelemento.iter('fila'):
                    elem = ciudades.getCiudad(nombre)
                    elem.lista_fila.insertarFila(subsubelemento1.attrib['numero'],subsubelemento1.text)
                #Unidad militar
                for subsubelemento2 in subelemento.iter('nombre'):
                    nombre = subsubelemento.text
                    ciudades.insertarCiudad(subsubelemento.attrib['filas'], subsubelemento.attrib['columnas'], nombre)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    GUI = Ventana()
    GUI.show()
    sys.exit(app.exec_())