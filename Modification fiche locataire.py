from PyQt5 import QtWidgets, uic, QtGui,QtCore
from PyQt5 import *

import sys
import os
import time
import csv

class Fiche_Locataire(QtWidgets.QDialog) :
    def __init__(self,fichier_csv):
        super(Fiche_Locataire, self).__init__()
        uic.loadUi('Locataire/Fiche Locataire.ui', self)
        self.setWindowTitle('Fiche Locataire')
        self.__fichier_csv=fichier_csv
        self.__button_homme=self.findChild(QtWidgets.QRadioButton,'Button_Homme')
        self.__button_homme.toggled.connect(self.onClicked_Homme)
        self.__button_femme=self.findChild(QtWidgets.QRadioButton,'Button_Femme')
        self.__button_femme.toggled.connect(self.onClicked_Femme)

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

        fichier=open(fichier_csv,'r')
        reader=csv.reader(fichier)
        liste=[]
        for row in reader :
            liste+=row
        fichier.close()
        print(liste)
        self.__Loc_Nom.setText(liste[0])
        self.__Loc_Prenom.setText(liste[1])
        self.__Loc_Naissance.setText(liste[2])
        self.__Loc_Telephone.setText(liste[3])
        self.__Col_Nom.setText(liste[4])
        self.__Col_Prenom.setText(liste[5])
        self.__Col_Naissance.setText(liste[6])
        self.__Col_Telephone.setText(liste[7])
        if liste[8]=='True' :
            self.__button_homme.setChecked(True)
        else :
            self.__button_femme.setChecked(True)
        self.__obs.setText(liste[12])
        ok=liste[10].split('-')# date
        self.__date.setDate(QtCore.QDate(int(ok[0]),int(ok[1]),int(ok[2])))
        self.__indice=liste[13]






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
        os.remove(self.__fichier_csv)
        fichier=open('Locataire/Liste de Locataire/loc'+self.__indice+'.csv','w')
        writer=csv.writer(fichier)
        writer.writerow((self.__Loc_Nom.text(),self.__Loc_Prenom.text(),self.__Loc_Naissance.text(),self.__Loc_Telephone.text()))
        writer.writerow((self.__Col_Nom.text(),self.__Col_Prenom.text(),self.__Col_Naissance.text(),self.__Loc_Telephone.text()))
        if self.__button_homme == True :
            writer.writerow(('True'))
        else :
            writer.writerow(('False','0'))
        a=self.__date.date()
        a=str(a.toPyDate())
        writer.writerow((a,'0'))
        writer.writerow((self.__obs.toPlainText(),self.__indice))

        fichier.close()
        self.close()




if __name__ == '__main__':
# prog principal
    app = QtWidgets.QApplication(sys.argv)
    window = Fiche_Locataire('Locataire/Liste de Locataire/loc1.csv')
    app.exec_()
