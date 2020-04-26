from PyQt5 import QtWidgets, uic, QtGui
from PyQt5 import *
import sys
import os


class Gestion_Des_Locataires(QtWidgets.QMainWindow) :
    def __init__(self):

        super(Gestion_Des_Locataires, self).__init__()
        uic.loadUi('Locataire/Gestion Des Locataires.ui', self)
        self.setWindowTitle('Accueil')
        self.setFixedSize(1280,720)

        self.show()
        self.__tableWidget=self.findChild(QtWidgets.QTableWidget,'tableWidget')
        cont=0
        for i in os.listdir("Locataire/Liste de Locataire") :

            print('ok')
            self.__tableWidget.insertRow(cont)
            cont+=1



            self.__tableWidget.setItem(cont,1,QtWidgets.QTableWidgetItem())

class Widget_Locataire(QtWidgets) :
    def __init__(self):

        super(Widget_Locataire, self).__init__()
        uic.loadUi('Widget_Locataire', self)


if __name__ == '__main__':
# prog principal
    app = QtWidgets.QApplication(sys.argv)
    window = Gestion_Des_Locataires()
    app.exec_()
