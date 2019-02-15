import sys

import os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from modules import file_set, graph
import pandas as pd
from PyQt5 import uic, QtWidgets
import numpy as np
import matplotlib.pyplot as plt

qtCreatorFile = "../_uiFiles/main.ui"  # Aquí va el nombre de tu archivo

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.csvButton.clicked.connect(self.getCSV)
        self.histogramButton.clicked.connect(self.radioButtonClicked)
        self.scatterButton.clicked.connect(self.radioButtonClicked)
        self.boxButton.clicked.connect(self.radioButtonClicked)
        self.matrixButton.clicked.connect(self.radioButtonClicked)
        self.threedButton.clicked.connect(self.radioButtonClicked)
        self.graphButton.clicked.connect(self.graphButtonClicked)
        self.xListWidget.itemClicked.connect(self.xListWidgetClicked)
        self.yListWidget.itemClicked.connect(self.yListWidgetClicked)
        self.zListWidget.itemClicked.connect(self.zListWidgetClicked)
        self.cListWidget.itemClicked.connect(self.cListWidgetClicked)

        # self.pushButton2.clicked.connect(self.plot)
        # Aquí van los botones

    # Aquí van las nuevas funciones
    # Esta función abre el archivo CSV
    def getCSV(self):
        filePath, _ = QtWidgets.QFileDialog.getOpenFileName(self, 'Open file', '/home')
        if filePath != "":
            # print("Dirección", filePath)  # Opcional imprimir la dirección del archivo
            # self.df = pd.read_csv(str(filePath))
            #데이터 불러오고 셋팅
            self.df_file = file_set.File_set()
            self.data = self.df_file.file_load(filePath)
            self.xListWidget.clear()
            self.yListWidget.clear()
            self.zListWidget.clear()
            self.cListWidget.clear()
            self.df_file.data_columns(self.data)  # 컬럼 리스트 생성
            self.df_file.data_classification(self.data)  # 범주/이산형 데이터 분류
            self.df_file.list_mining(self.data)  # 새로운 컬럼 리스트 생성
            self.df_file.newData_classification(self.data)  # 새로운 범주/이산형 데이터 분류
            self.columns = self.df_file.get_newColumns()
            self.letter = self.df_file.get_newLetter()
            self.number = self.df_file.get_newNumber()
            #self.df_file.set_except(self.letter, self.number)
            self.df_graph = graph.Graph()
            self.xListWidget.addItems(self.number)
            self.yListWidget.addItems(self.number)
            self.zListWidget.addItems(self.number)
            self.cListWidget.addItems(self.number)


    def radioButtonClicked(self):
        self.shape = ''
        if self.histogramButton.isChecked():
            self.shape = 'hist'
        elif self.scatterButton.isChecked():
            self.shape = 'scatter'
        elif self.boxButton.isChecked():
            self.shape = 'box'
        elif self.matrixButton.isChecked():
            self.shape = 'matrix'
        else:
            self.shape = 'threed'

    def xListWidgetClicked(self):
        self.xVar = self.xListWidget.currentItem().text()

    def yListWidgetClicked(self):
        self.yVar = self.yListWidget.currentItem().text()

    def zListWidgetClicked(self):
        self.zVar = self.zListWidget.currentItem().text()

    def cListWidgetClicked(self):
        self.cVar = self.cListWidget.currentItem().text()

    def graphButtonClicked(self):

        # self.xVar = self.xListWidget.currentItem().text()
        # self.yVar = self.yListWidget.currentItem().text()
        try:

            if self.shape == 'hist':
                self.df_graph.histogram(self.data, self.xVar, self.cVar)
            elif self.shape == 'scatter':
                self.df_graph.scatter_plot(self.data, self.xVar, self.yVar, self.cVar)

            elif self.shape == 'box':
                self.df_graph.box_plot(self.data, self.xVar, self.yVar, self.cVar)

            elif self.shape == 'matrix':
                self.df_graph.matrix()
                #self.df_graph.normal_check(self.data, self.xVar)
                # print(self.shape, self.xVar, self.yVar)
                # self.df_graph.seaborn()
            else:
                self.df_graph.Plot3D(self.data, self.xVar, self.yVar, self.zVar, self.cVar)
                #self.df_graph.projection(self.data, self.xVar, self.yVar)
                # print(self.shape, self.xVar, self.yVar)
        except:
            pass






if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    app.exec_()