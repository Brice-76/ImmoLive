from PyQt5 import QtWidgets, uic, QtGui
from PyQt5 import *
import sys
import os
import time
import csv


class Fiche_Locataire(QtWidgets.QDialog) :
    def __init__(self):
        super(Fiche_Locataire, self).__init__()
        uic.loadUi('Locataire/Fiche Locataire.ui', self)
        self.setWindowTitle('Fiche Locataire')
        self.__button_homme=self.findChild(QtWidgets.QRadioButton,'Button_Homme')
        self.__button_homme.toggled.connect(self.onClicked_Homme)
        self.__button_femme=self.findChild(QtWidgets.QRadioButton,'Button_Femme')
        self.__button_femme.toggled.connect(self.onClicked_Femme)

        # self.__button_addpdf=self.findChild(QtWidgets.QPushButton,'pushButton')
        # self.__button_addpdf.clicked.connect(self.onClicked_addPdf)

        self.__image=self.findChild(QtWidgets.QLabel,'label_14')
        self.__image.setPixmap(QtGui.QPixmap('Img/138198-business-collection/png/briefcase-1.png'))

        self.__Col_Naissance=self.findChild(QtWidgets.QLineEdit,'Col_Naissance')
        self.__Col_Nom=self.findChild(QtWidgets.QLineEdit,'Col_Nom')
        self.__Col_Prenom=self.findChild(QtWidgets.QLineEdit,'Col_Prenom')
        self.__Col_Telephone=self.findChild(QtWidgets.QLineEdit,'Col_Telephone')

        self.__Loc_Naissance=self.findChild(QtWidgets.QLineEdit,'Loc_Naissance')
        self.__Loc_Nom=self.findChild(QtWidgets.QLineEdit,'Loc_Nom')
        self.__Loc_Prenom=self.findChild(QtWidgets.QLineEdit,'Loc_Prenom')
        self.__Loc_Telephone=self.findChild(QtWidgets.QLineEdit,'Loc_Telephone')

        self.__date=self.findChild(QtWidgets.QDateEdit,'dateEdit')
        self.__obs=self.findChild(QtWidgets.QTextEdit,'Obsevations')

        self.__bar=self.findChild(QtWidgets.QProgressBar,'progressBar')
        self.__bar.setMaximum(3)
        self.__bar.setValue(3)



        self.show()
    def onClicked_Homme(self):
        self.__image.setPixmap(QtGui.QPixmap("Img/276132-real-estate/png/seller-1.png"))
    def onClicked_Femme(self):
        self.__image.setPixmap(QtGui.QPixmap('Img/276132-real-estate/png/seller-4.png'))
    def onClicked_addPdf(self):


        print('ok')#/Users/brice/PycharmProjects/ImmoLive/Locataire/Liste de Locataire
    def accept(self) :
        ''' SOUS FORMAT CSV
        Code locataire ex : 0
        Loc : nom,prenom,naissance,tel
        Col : nom,prenom,naissance,tel
        type : h = True f=False
        Date arrivé
        Obs : ligne d'observation
        '''
        liste=os.listdir("Locataire/Liste de Locataire") #liste des fichier dans liste locataire
        indice=0
        while 'loc'+str(indice)+'.csv' in liste :
            indice+=1
        fichier=open('Locataire/Liste de Locataire/loc'+str(indice)+'.csv','w')
        writer=csv.writer(fichier)
        writer.writerow((self.__Loc_Nom.text(),self.__Loc_Prenom.text(),self.__Loc_Naissance.text(),self.__Loc_Telephone.text()))
        writer.writerow((self.__Col_Nom.text(),self.__Col_Prenom.text(),self.__Col_Naissance.text(),self.__Loc_Telephone.text()))
        if self.__button_homme.isChecked() == True :
            writer.writerow(('True','0'))
        else :
            writer.writerow(('False','0'))
        a=self.__date.date()
        a=str(a.toPyDate())
        writer.writerow((a,'0'))
        writer.writerow((self.__obs.toPlainText(),indice))

        fichier.close()
        self.close()




if __name__ == '__main__':
# prog principal
    app = QtWidgets.QApplication(sys.argv)
    window = Fiche_Locataire()
    app.exec_()
