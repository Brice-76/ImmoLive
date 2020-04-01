from PyQt5 import QtWidgets, uic, QtGui
from PyQt5 import *
import sys
import os

class Ui(QtWidgets.QMainWindow):
    def __init__(self,Fiche_Loc='Liste Locataire/Locataire_Vide.txt'):

        super(Ui, self).__init__()
        uic.loadUi('Locataire_1.ui', self)
        self.show()
    #WIDGET ASSOCIATION
        self.Fichier_dentre=Fiche_Loc

        self.button = self.findChild(QtWidgets.QPushButton, 'pushButton') # Bonton Valider
        self.button.clicked.connect(self.ButtonPressed_Valider)

        self.button = self.findChild(QtWidgets.QPushButton, 'pushButton_2') # Bouton Imprimer

        self.button.clicked.connect(self.ButtonPressed_Imprimer)
        self.__line1=self.findChild(QtWidgets.QLineEdit, 'lineEdit')
        self.__line2=self.findChild(QtWidgets.QLineEdit, 'lineEdit_2')
        self.__line3=self.findChild(QtWidgets.QLineEdit, 'lineEdit_3')
        self.__line4=self.findChild(QtWidgets.QLineEdit, 'lineEdit_4')
        self.__line5=self.findChild(QtWidgets.QLineEdit, 'lineEdit_5')
        self.__note=self.findChild(QtWidgets.QTextEdit, 'textEdit')
        self.__adresse=self.findChild(QtWidgets.QTextEdit, 'textEdit_2')
        self.__datenaissance=self.findChild(QtWidgets.QDateEdit,'DateEdit')




        fichier=open(Fiche_Loc,'r')
        self.__line1.setText(fichier.readline())
        self.__line2.setText(fichier.readline())
        self.__line3.setText(fichier.readline())
        self.__line4.setText(fichier.readline())
        self.__line5.setText(fichier.readline())
        # strg=''
        # reader=fichier.readline()
        # while reader != 'End' :
        #     strg+=reader
        #     print(reader)
        #     reader=fichier.readline()
        # self.__adresse.setText(strg)
        # while fichier.readline() != 'End' :
        #     strg+=fichier.readline()
        self.__note.setText(fichier.readline())
        ''' Lecture fichier text : 
        ligne 1 : nom
        ligne 2 : prenom
        ligne 3 : telephone
        ligne 4 : portable
        ligne 5 : mail
        ligne 6 : date
        ligne 6-'end' : Adresse
        ligne 'end' - 'end' : Notes
        
        '''


    def ButtonPressed_Valider(self): # Quand on appui sur Valider
        print('valider')
        liste=os.listdir("/Users/brice/PycharmProjects/Real Immo/Liste Locataire") #liste des fichier dans liste locataire

        fichier=open('/Users/brice/PycharmProjects/Real Immo/Liste Locataire/locataire'+str(len(liste)+1)+'.txt','w')
        fichier.write(self.__line1.text()+'\n'+self.__line2.text()+'\n'+self.__line3.text()+'\n'+self.__line4.text()+'\n'+self.__line5.text())
        fichier.write(self.__adresse.toPlainText()+'\nEnd\n')
        fichier.write(self.__note.toPlainText()+'\nEnd\n')
        a=self.__datenaissance.date()


        fichier.close()
        if self.Fichier_dentre != 'Liste Locataire/Locataire_Vide.txt' :#suppression du locataire, car creation avant
            os.remove(self.Fichier_dentre)



    def ButtonPressed_Imprimer(self): # Quand on appui sur Imprimer
        print('impression')

        print(self.__line1.text()+'\n'+self.__line2.text()+'\n'+self.__line3.text()+'\n'+self.__line4.text()+'\n'+self.__line5.text()+'\n')




if __name__ == '__main__':
# prog principal
    app = QtWidgets.QApplication(sys.argv)
    window = Ui()
    app.exec_()
