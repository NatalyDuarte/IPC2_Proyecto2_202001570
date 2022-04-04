# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'graficar.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import os
import webbrowser
from ListaCiudades import ListaCiudades


class Ui_MainWindow(object):
    global ciudades
    ciudades = ListaCiudades()
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(741, 325)
        MainWindow.setStyleSheet("background-color: rgb(85, 255, 127);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 30, 361, 41))
        self.label.setStyleSheet("font: 26pt \"Britannic Bold\";")
        self.label.setObjectName("label")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(590, 30, 141, 41))
        self.pushButton_5.setStyleSheet("font: 16pt \"Poor Richard\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);")
        self.pushButton_5.setObjectName("pushButton_5")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(100, 130, 261, 16))
        self.label_2.setStyleSheet("font: 16pt \"Arial Narrow\";")
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(110, 160, 311, 41))
        self.lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(380, 230, 91, 41))
        self.pushButton_6.setStyleSheet("font: 16pt \"Poor Richard\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);")
        self.pushButton_6.setObjectName("pushButton_6")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 741, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Chapín Warriors, S. A."))
        self.pushButton_5.setText(_translate("MainWindow", "Regresar"))
        self.label_2.setText(_translate("MainWindow", "Ingrese el nombre de la Ciudad:"))
        self.pushButton_6.setText(_translate("MainWindow", "Graficar"))
        self.pushButton_6.clicked.connect(self.abrir)

    def abrir(self):
        nombre=self.lineEdit.text()
        print(nombre)
        elem = ciudades.getCiudad(nombre)
        self.Grafica4(elem)

    def Grafica4(self,patron):
        count = 0
        grafico = open("graficapatron.dot", 'w+')
        grafico.write('graph G{\n')
        grafico.write('graph[nodesep="0" ranksep="0"]')
        grafico.write('node[shape=box fillcolor="pink:yellow"  style =filled]\n')
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

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())