from PyQt5 import QtWidgets, uic, QtGui
from PyQt5 import *
import sys
import os
from ModificationIdentité import *

class Ecran_Accueil(QtWidgets.QMainWindow):
    def __init__(self):

        super(Ecran_Accueil, self).__init__()

        uic.loadUi('Img/Ecran Accueil.ui', self)
        self.setWindowTitle('Accueil')
        self.setFixedSize(1280,720)

        # INSTALLATION DES IMAGES
        self.logo_patrimoine=self.findChild(QtWidgets.QLabel, 'label')
        self.logo_patrimoine.setPixmap(QtGui.QPixmap('Img/276132-real-estate/png/building-1.png'))

        self.logo_locataire=self.findChild(QtWidgets.QLabel, 'label_2')
        self.logo_locataire.setPixmap(QtGui.QPixmap('Img/276132-real-estate/png/seller.png'))

        self.logo_loyers=self.findChild(QtWidgets.QLabel, 'label_3')
        self.logo_loyers.setPixmap(QtGui.QPixmap('Img/276132-real-estate/png/money-flow.png'))

        self.logo_marque=self.findChild(QtWidgets.QLabel,'label_4')
        self.logo_marque.setPixmap(QtGui.QPixmap('Img/CHB inc-3.png'))

        # BOUTON
        self.bouton_option=self.findChild(QtWidgets.QToolButton,'toolButton')
        self.bouton_option.setIcon(QtGui.QIcon('Img/138198-business-collection/png/stamp-1.png'))
        self.bouton_option.clicked.connect(self.ButtonPressed_Option)

        self.button_locataire= self.findChild(QtWidgets.QPushButton, 'pushButton')
        self.button_locataire.clicked.connect(self.ButtonPressed_Locataire)
        self.button_patrimoine= self.findChild(QtWidgets.QPushButton, 'pushButton_2')
        self.button_patrimoine.clicked.connect(self.ButtonPressed_Patrimoine)
        self.button_loyers= self.findChild(QtWidgets.QPushButton, 'pushButton_3')
        self.button_loyers.clicked.connect(self.ButtonPressed_Loyers)

        self.identite=self.findChild(QtWidgets.QTextBrowser, 'textBrowser')
        fichier=open('Img/Identite.txt','r')
        liste=fichier.readlines()
        str='\n'
        for i in range(0,len(liste)) :
            if liste[i] != '\n' :
                str+=liste[i]
        self.identite.setText(str)
        fichier.close()





        self.show()

    def ButtonPressed_Locataire(self):
        print('push Locataire')
    def ButtonPressed_Patrimoine(self):
        print('push Patrimoine')
    def ButtonPressed_Loyers(self):
        print('push Loyers')
    def ButtonPressed_Option(self):
        print('push Option')
        window=Dialog()
        window.exec()
        #apres execution maj
        fichier=open('Img/Identite.txt','r')
        liste=fichier.readlines()
        print(liste)
        str='\n'
        for i in range(0,len(liste)) :
            if liste[i] != '\n' :
                print('ok')
                str+=liste[i]


        self.identite.setText(str)
        fichier.close()



if __name__ == '__main__':
# prog principal
    app = QtWidgets.QApplication(sys.argv)
    window = Ecran_Accueil()
    app.exec_()
