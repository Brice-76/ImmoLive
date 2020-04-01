from PyQt5 import QtWidgets, uic, QtGui
from PyQt5 import *
import sys
import os
import time

class Dialog(QtWidgets.QDialog) :
    def __init__(self):
        super(Dialog, self).__init__()
        uic.loadUi('Img/Modification identité.ui', self)
        self.setWindowTitle('Modification Identite')


        self.photo=self.findChild(QtWidgets.QLabel,'label_4')
        self.photo.setPixmap(QtGui.QPixmap('Img/276132-real-estate/png/building-3.png'))

        self.__name=self.findChild(QtWidgets.QLineEdit,'lineEdit')
        self.__add1=self.findChild(QtWidgets.QLineEdit,'lineEdit_2')
        self.__add2=self.findChild(QtWidgets.QLineEdit,'lineEdit_3')


        fichier=open('Img/Identite.txt','r')
        liste=fichier.readlines()
        for i in liste :
            if i == '\n' or i ==' \n' :
                del i
        fichier.close()
        self.__name.setText(liste[0])
        self.__add1.setText(liste[1])
        self.__add2.setText(liste[2])

        self.show()


    def accept(self) :
        os.remove('Img/Identite.txt')
        fichier=open('Img/Identite.txt','w')
        if self.__name.text()=='' :
            self.__name.setText(' ')
        if self.__add1.text()=='' :
            self.__add1.setText(' ')
        if self.__add2.text()=='' :
            self.__add2.setText(' ')
        fichier.write(self.__name.text().rstrip('\n')+'\n'+self.__add1.text().rstrip('\n')+'\n'+self.__add2.text().rstrip('\n'))
        fichier.close()
        self.close()



if __name__ == '__main__':
# prog principal
    app = QtWidgets.QApplication(sys.argv)
    window = Dialog()
    app.exec_()
