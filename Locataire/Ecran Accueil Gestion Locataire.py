from PyQt5 import QtWidgets, uic, QtGui,QtCore
from PyQt5 import *

import sys
import os
import time
import csv

class Gestion_Des_Locataires(QtWidgets.QMainWindow) :
    def __init__(self):
        super(Gestion_Des_Locataires, self).__init__()

        uic.loadUi('Locataire/Gestion_Des_Locataires.ui', self)
        self.setWindowTitle('Accueil')
        self.setFixedSize(1280,720)


if __name__ == '__main__':
# prog principal
    app = QtWidgets.QApplication(sys.argv)
    window = Gestion_Des_Locataires()
    app.exec_()
