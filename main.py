from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog, QMessageBox, QGraphicsPixmapItem, QGraphicsScene
from PyQt5.uic import loadUi
import sys
from PyQt5.QtGui import QPixmap
from tkinter import messagebox
from tkinter import filedialog
from xml.dom.minidom import ElementInfo
import xml.etree.ElementTree as ET
from ListaCiudades import ListaCiudades
from ListaUniMilitar import ListaUniMilitar
from ListaRobot import ListaRobot
from Matriz import Matriz
from graficar import Ui_MainWindow
import os
import webbrowser

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
        self.pushButton_2.clicked.connect(self.abrir1)
        self.pushButton_3.clicked.connect(self.impri1)
        self.pushButton_4.clicked.connect(self.impri2)
        self.pushButton_5.clicked.connect(self.salir)
        self.pushButton_7.clicked.connect(self.misi)
        self.pushButton_8.clicked.connect(self.misi1)
        self.label_2.setVisible(False)
        self.label_3.setVisible(False)
        self.label_4.setVisible(False)
        self.label_5.setVisible(False)
        self.label_6.setVisible(False)
        self.label_7.setVisible(False)
        self.label_8.setVisible(False)
        self.label_9.setVisible(False)
        self.label_10.setVisible(False)
        self.lineEdit.setVisible(False)
        self.lineEdit_2.setVisible(False)
        self.lineEdit_3.setVisible(False)
        self.lineEdit_4.setVisible(False)
        self.lineEdit_5.setVisible(False)
        self.lineEdit_6.setVisible(False)
        self.lineEdit_7.setVisible(False)
        self.pushButton_6.setVisible(False)
        self.pushButton_9.setVisible(False)
        self.pushButton_10.setVisible(False)
        self.pushButton_11.setVisible(False)

    def misi1(self):
        el= robot.RobotEx()
        if el!= None:
            self.label_2.setVisible(True)
            self.lineEdit.setVisible(True)
            self.pushButton_11.setVisible(True)
            self.pushButton_11.clicked.connect(self.buscando1)
        else:
            messagebox.showwarning("Alert","No hay robots ChapinFighter por lo tanto no se puede hacer esta misión")

    def buscando1(self):
        nombre=self.lineEdit.text()
        elem = ciudades.getCiudad(nombre)
        ob=elem.lista_celda.Bus("R")
        os=elem.lista_celda.Bus("E")
        global robots1,fila1,columna1
        robots1=" "
        fila1=" "
        columna1=" "
        if os!=None:
            if ob!=None:
                aja= elem.lista_celda.BusUni("R")
                print("Unidadrecurso: ",aja)
                aja1=robot.RobotExCont()
                print("UnidadRobts: ",aja1)
                if aja>1:
                    self.label_6.setVisible(True)
                    self.label_9.setVisible(True)
                    self.label_10.setVisible(True)
                    self.lineEdit_5.setVisible(True)
                    self.lineEdit_7.setVisible(True)
                else:
                    fila1=elem.lista_celda.BusCF1()
                    columna1=elem.lista_celda.BusCC1()
                if aja1>1:
                    self.label_5.setVisible(True)
                    self.lineEdit_4.setVisible(True)
                else:
                    robots1=robot.RobotResNom1()
                self.pushButton_10.setVisible(True)
                self.pushButton_10.clicked.connect(self.Extraccion)
            else:
                messagebox.showwarning("Alert","No hay recursos en esta ciudad por lo tanto no se puede hacer esta misión")
        else:
            messagebox.showwarning("Alert","No hay puntos de entrada en esta ciudad por lo tanto no se puede hacer esta misión")

    def misi(self):
        el= robot.RobotRes()
        if el!= None:
            self.label_2.setVisible(True)
            self.lineEdit.setVisible(True)
            self.pushButton_11.setVisible(True)
            self.pushButton_11.clicked.connect(self.buscando)
        else:
            messagebox.showwarning("Alert","No hay robots ChapinRescue por lo tanto no se puede hacer esta misión")
        
    def buscando(self):
        nombre=self.lineEdit.text()
        elem = ciudades.getCiudad(nombre)
        ob=elem.lista_celda.Bus("C")
        os=elem.lista_celda.Bus("E")
        global robots,fila,columna
        robots=" "
        fila=" "
        columna=" "
        if os!=None:
            if ob!=None:
                aja= elem.lista_celda.BusUni("C")
                print("Unidadcivil: ",aja)
                aja1=robot.RobotResCont()
                print("UnidadRobts: ",aja1)
                if aja>1:
                    self.label_4.setVisible(True)
                    self.label_7.setVisible(True)
                    self.label_8.setVisible(True)
                    self.lineEdit_3.setVisible(True)
                    self.lineEdit_6.setVisible(True)
                else:
                    fila=elem.lista_celda.BusCF()
                    columna=elem.lista_celda.BusCC()
                if aja1>1:
                    self.label_3.setVisible(True)
                    self.lineEdit_2.setVisible(True)
                else:
                    robots=robot.RobotResNom()
                self.pushButton_9.setVisible(True)
                self.pushButton_9.clicked.connect(self.Rescate)
            else:
                messagebox.showwarning("Alert","No hay unidades civiles en esta ciudad por lo tanto no se puede hacer esta misión")
        else:
            messagebox.showwarning("Alert","No hay puntos de entrada en esta ciudad por lo tanto no se puede hacer esta misión")

    def abrir1(self):
        self.label_2.setVisible(True)
        self.lineEdit.setVisible(True)
        self.pushButton_6.setVisible(True)
        self.pushButton_6.clicked.connect(self.grafi)
        

    def grafi(self):
        nombre=self.lineEdit.text()
        print(nombre)
        elem = ciudades.getCiudad(nombre)
        self.Grafica4(elem)
        self.label_2.setVisible(False)
        self.lineEdit.setVisible(False)
        self.pushButton_6.setVisible(False)

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
                #Fila
                for subsubelemento1 in subelemento.iter('fila'):
                    cade= subsubelemento1.text
                    cade= cade.replace("\"","")
                    elem.lista_fila.insertarFila(subsubelemento1.attrib['numero'],cade)
                    contador=1 
                    while contador<=len(cade):
                        for o in range(len(cade)):
                            elem.matriz.InsertarMatriz( int ( subsubelemento1 . attrib [ 'numero' ]), int ( contador ), str ( cade [ o ]))
                            elem.lista_celda.insertarCelda( int( subsubelemento1 . attrib [ 'numero' ]), int ( contador ), str ( cade [ o ]))    
                            contador +=1
                
                #Unidad militar
                for subsubelemento2 in subelemento.iter('unidadMilitar'):
                    elem.lista_unimilitar.insertarUniMili(subsubelemento2.attrib['fila'], subsubelemento2.attrib['columna'],subsubelemento2.text)
                    elem.matriz.Sustitu(int(subsubelemento2.attrib['fila']), int(subsubelemento2.attrib['columna']),str(subsubelemento2.text))
                    elem.lista_celda.Sustitu(int(subsubelemento2.attrib['fila']), int(subsubelemento2.attrib['columna']),str(subsubelemento2.text))
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

    def Grafica4(self,patron):
        count = 0
        grafico = open("graficapatron.dot", 'w+')
        grafico.write('graph G{\n')
        grafico.write('graph[nodesep="0" ranksep="0"]')
        grafico.write('node[shape=box fillcolor="pink:yellow"  style =filled]\n')
        grafico.write(''' subgraph cluster_p{
            label= "REPORTE CIUDAD"
            bgcolor = "pink"''')
        grafico.write('nodo0[label="{}" shape="box"];\n'.format(patron.nombre))

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
            grafico.write('nodoP -- name{}[style ="invis" nodesep="0" ranksep="0"] ;\n'.format(count3))
            count3 += 1
            sum = int(patron.columna)

        for i in range((sum*int(patron.fila))-length):
            grafico.write('name{}   -- name{} [style ="invis" nodesep="0" ranksep="0"];\n'.format(i, (i + sum)))
        grafico.write('}\n}\n')
        grafico.close()
        os.system('dot.exe -Tpng graficapatron.dot -o '+patron.nombre+'_reporte.png')
        os.system('dot.exe -Tpdf graficapatron.dot -o '+patron.nombre+'_reporte.pdf')
        os.startfile(patron.nombre+'_reporte.pdf')            
            
    def Rescate(self):
        nombre=self.lineEdit.text()
        ciudad = ciudades.getCiudad(nombre) 
        UCF=self.lineEdit_3.text()
        UCC=self.lineEdit_6.text()
        RC=self.lineEdit_2.text()
        print(RC)
        if fila!=" ":
            UCF=fila
        if columna!=" ":
            UCC=columna
        if robots!=" ":
            RC=robots
        PE = ciudad.lista_celda.BusPE()
        if PE!=None:
            print(PE)
        else: 
            messagebox.showwarning("Alert","No se encontro el punto de entrada en esta ciudad por lo tanto no se puede hacer esta misión")
        count = 0
        grafico = open("graficapatron.dot", 'w+')
        grafico.write('graph G{\n')
        grafico.write('graph[nodesep="0" ranksep="0"]')
        grafico.write('node[shape=box fillcolor="pink:yellow"  style =filled]\n\n\n\n')
        grafico.write(''' subgraph cluster_p{
            label= "REPORTE RESCATE"
            bgcolor = "pink"''')
        grafico.write('nodoP[label="Ciudad: {}" shape="box"];\n'.format(ciudad.nombre))

        tmp = ciudad.lista_celda.inicio2
        tmp1 = ciudad.lista_unimilitar.inicio2 
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
        
        length = int(ciudad.columna)
        count3 = 0
        for i in range(length):
            grafico.write('nodoP -- name{}[style ="invis" nodesep="0" ranksep="0"] ;\n'.format(count3))
            count3 += 1
            sum = int(ciudad.columna)

        for i in range((sum*int(ciudad.fila))-length):
            grafico.write('name{}   -- name{} [style ="invis" nodesep="0" ranksep="0"];\n'.format(i, (i + sum)))
        grafico.write('nodo1[label="Tipo de misión: rescate"];\n\n\n\n')
        grafico.write('nodo2[label="Unidad civil rescatada fila: {}"];\n\n\n\n'.format(UCF))
        grafico.write('nodo3[label="Unidad civil rescatada columna: {}"];\n\n\n\n'.format(UCC))
        grafico.write('nodo4[label="Robot utilizado: {}"];\n\n\n\n'.format(RC))
        grafico.write('}\n}\n')
        grafico.close()
        os.system('dot.exe -Tpng graficapatron.dot -o '+ciudad.nombre+'_reporteRES.png')
        os.system('dot.exe -Tpdf graficapatron.dot -o '+ciudad.nombre+'_reporteRES.pdf')
        os.startfile(ciudad.nombre+'_reporteRES.pdf') 

    def Extraccion(self):
        nombre=self.lineEdit.text()
        ciudad = ciudades.getCiudad(nombre) 
        UCF=self.lineEdit_5.text()
        UCC=self.lineEdit_7.text()
        RC=self.lineEdit_4.text()
        print(RC)
        if fila1!=" ":
            UCF=fila1
        if columna1!=" ":
            UCC=columna1
        if robots1!=" ":
            RC=robots1
        PE = ciudad.lista_celda.BusPE()
        if PE!=None:
            print(PE)
        else: 
            messagebox.showwarning("Alert","No se encontro el punto de entrada en esta ciudad por lo tanto no se puede hacer esta misión")
        count = 0
        grafico = open("graficapatron.dot", 'w+')
        grafico.write('graph G{\n')
        grafico.write('graph[nodesep="0" ranksep="0"]')
        grafico.write('node[shape=box fillcolor="pink:yellow"  style =filled]\n\n\n\n')
        grafico.write(''' subgraph cluster_p{
            label= "REPORTE EXTRACCIÓN DE RECURSOS"
            bgcolor = "pink"''')
        grafico.write('nodoP[label="Ciudad: {}" shape="box"];\n'.format(ciudad.nombre))

        tmp = ciudad.lista_celda.inicio2
        tmp1 = ciudad.lista_unimilitar.inicio2 
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
        
        length = int(ciudad.columna)
        count3 = 0
        for i in range(length):
            grafico.write('nodoP -- name{}[style ="invis" nodesep="0" ranksep="0"] ;\n'.format(count3))
            count3 += 1
            sum = int(ciudad.columna)

        for i in range((sum*int(ciudad.fila))-length):
            grafico.write('name{}   -- name{} [style ="invis" nodesep="0" ranksep="0"];\n'.format(i, (i + sum)))
        grafico.write('nodo1[label="Tipo de misión: extraccion de recursos"];\n\n\n\n')
        grafico.write('nodo2[label="Fila de recurso extraido: {}"];\n\n\n\n'.format(UCF))
        grafico.write('nodo3[label="Columna de recurso extraido: {}"];\n\n\n\n'.format(UCC))
        grafico.write('nodo4[label="Robot utilizado: {}"];\n\n\n\n'.format(RC))
        grafico.write('}\n}\n')
        grafico.close()
        os.system('dot.exe -Tpng graficapatron.dot -o '+ciudad.nombre+'_reporteRES.png')
        os.system('dot.exe -Tpdf graficapatron.dot -o '+ciudad.nombre+'_reporteRES.pdf')
        os.startfile(ciudad.nombre+'_reporteRES.pdf') 

    
    def impri1(self):
        ciu=ciudades.imprimirCiuda()
        self.plainTextEdit.setPlainText(ciu)

    def impri2(self):
        ro=robot.imprimirRobot()
        self.plainTextEdit.setPlainText(ro)

    def salir(self):
        sys.exit(1)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    GUI = Ventana()
    GUI.show()
    sys.exit(app.exec_())