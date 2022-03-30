from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog, QMessageBox, QGraphicsPixmapItem, QGraphicsScene
from PyQt5.uic import loadUi
import sys
from PyQt5.QtGui import QPixmap
from tkinter import messagebox
from tkinter import filedialog
import os
import webbrowser
from xml.dom.minidom import ElementInfo
import xml.etree.ElementTree as ET
from ListaCiudades import ListaCiudades
from ListaUniMilitar import ListaUniMilitar
from ListaRobot import ListaRobot
from Matriz import Matriz

class Ventana(QMainWindow):
    global ciudades
    ciudades = ListaCiudades()
    global robot
    robot = ListaRobot()
    global matriz 
    matriz = Matriz()
    def __init__(self):
        super().__init__()
        loadUi("principal.ui", self)
        self.pushButton.clicked.connect(self.lectura)
        self.pushButton_3.clicked.connect(self.impri1)
        self.pushButton_4.clicked.connect(self.impri2)
        self.pushButton_5.clicked.connect(self.salir)

    def lectura(self):
        global rutarecibida
        archi=filedialog.askopenfilename(filetypes=[("Archivos XML", ".xml .XML")])
        if archi!="":
            self.Lectura(archi)
        else:
            messagebox.showwarning("Alert","No se pudo abrir el archivo")
                   

    def Lectura(self,archivo):
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
        print("===== ¡ARCHIVO LEIDO CORRECTAMENTE! ====")
        #Lista Ciudades
        for elemento in raiz.iter('listaCiudades'):
            for subelemento in elemento.iter('ciudad'):
                #ciudades
                for subsubelemento in subelemento.iter('nombre'):
                    nombre = subsubelemento.text
                    filas = subsubelemento.attrib['filas']
                    colum = subsubelemento.attrib['columnas']
                    ciudades.insertarCiudad(filas, colum, nombre)
                elem = ciudades.getCiudad(nombre)
                #Unidad militar
                for subsubelemento2 in subelemento.iter('unidadMilitar'):
                    elem.lista_unimilitar.insertarUniMili(subsubelemento2.attrib['fila'], subsubelemento2.attrib['columna'],subsubelemento2.text)
                #Fila
                for subsubelemento1 in subelemento.iter('fila'):
                    cade= subsubelemento1.text
                    cade= cade.replace("\"","")
                    elem.lista_fila.insertarFila(subsubelemento1.attrib['numero'],cade)
                    contador=1 
                    while contador<=len(cade):
                        for o in range(len(cade)):
                            if(str(subsubelemento2.attrib['fila'])==str(subsubelemento1.attrib['numero']) and str(subsubelemento2.attrib['columna'])==str(contador)):
                                elem.matriz.InsertarMatriz(int(subsubelemento1.attrib['numero']),int(contador),subsubelemento2.text) 
                                elem.lista_celda.insertarCelda(int(subsubelemento1.attrib['numero']),int(contador),subsubelemento2.text)                            
                            else:
                                elem.matriz.InsertarMatriz( int ( subsubelemento1 . attrib [ 'numero' ]), int ( contador ), str ( cade [ o ]))
                                elem.lista_celda.insertarCelda( int( subsubelemento1 . attrib [ 'numero' ]), int ( contador ), str ( cade [ o ]))    
                            contador +=1
                elem.lista_celda.imprimirDobleEnlaPa()
                
                    
        #Lista Robots
        for elemento1 in raiz.iter('robots'):
            for subele in elemento1.iter('robot'):
                #robots
                for subsubele in subele.iter('nombre'):
                    tipo=subsubele.attrib['tipo']
                    capacidad =" "
                    if tipo!="ChapinFighter":
                        robot.insertarRobot(subsubele.attrib['tipo'], capacidad,subsubele.text)
                    else:
                        robot.insertarRobot(subsubele.attrib['tipo'], subsubele.attrib['capacidad'],subsubele.text)
        #self.VerificarUni(elem)
        self.Grafica4(elem)
        
    def VerificarUni(self, elem):
        cont=0
        cont1=0
        tmp = elem.lista_celda.inicio2
        tmp1 = elem.lista_unimilitar.inicio2 
        while (tmp!= None):
            while( tmp1 != None):
                print(str(tmp.coordefila) )
                if(str(tmp1.fila) == str(tmp.coordefila) and str(tmp1.columna) == str(tmp.coordecolumna)): 
                    tmp.caracter = "U"
                cont1 +=1
                tmp = tmp.siguien
                tmp1 = tmp1.siguiente2 
            cont +=1  
            tmp = tmp.siguien
            
            

    def impri1(self):
        ciu=ciudades.imprimirCiuda()
        self.plainTextEdit.setPlainText(ciu)

    def impri2(self):
        ro=robot.imprimirRobot()
        self.plainTextEdit.setPlainText(ro)

    def salir(self):
        sys.exit(1)

    def Grafica4(self,patron):
        count = 0
        grafico = open("graficapatron.dot", 'w+')
        grafico.write('graph G {\n')
        grafico.write('node[shape=box fillcolor="pink:yellow" style =filled]\n')
        grafico.write(''' subgraph cluster_p{
            label= "REPORTE CIUDAD"
            bgcolor = "pink"''')
        grafico.write('nodoP[label="{}" shape="box"];\n'.format(patron.nombre))

        tmp = patron.lista_celda.inicio2
        tmp1 = patron.lista_unimilitar.inicio2 
        while tmp is not None:
            if(tmp.caracter=="*"):
                grafico.write('name{}[label="{}" fillcolor="black" shape="box"];\n'.format(count,  tmp.caracter))
            elif(tmp.caracter=="E"):
                grafico.write('name{}[label="{}" fillcolor="green" shape="box"];\n'.format(count,  tmp.caracter))
            elif(tmp.caracter=="C"):
                grafico.write('name{}[label="{}" fillcolor="blue" shape="box"];\n'.format(count,  tmp.caracter))
            elif(tmp.caracter=="R"):
                grafico.write('name{}[label="{}" fillcolor="gray" shape="box"];\n'.format(count,  tmp.caracter))
            elif(tmp.caracter==" "):
                grafico.write('name{}[label="{}" fillcolor="white" shape="box"];\n'.format(count,  tmp.caracter))
            else:
                grafico.write('name{}[label="{}" fillcolor="red" shape="box"];\n'.format(count,  tmp.caracter))
            count += 1
            tmp = tmp.siguien
        
        length = int(patron.columna)
        count3 = 0
        for i in range(length):
            grafico.write('nodoP -- name{}[style ="invis" rank="min"] ;\n'.format(count3))
            count3 += 1
            sum = int(patron.columna)

        for i in range((sum*int(patron.fila))-length):
            grafico.write('name{}   -- name{} [style ="invis" rank="min"];\n'.format(i, (i + sum)))
        grafico.write('}\n}\n')
        grafico.close()
        os.system('dot.exe -Tpng graficapatron.dot -o '+patron.nombre+'_reporte.png')
        os.system('dot.exe -Tpdf graficapatron.dot -o '+patron.nombre+'_reporte.pdf')
        os.startfile(patron.nombre+'_reporte.pdf')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    GUI = Ventana()
    GUI.show()
    sys.exit(app.exec_())