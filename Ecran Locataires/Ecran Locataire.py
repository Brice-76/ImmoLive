from PyQt5 import QtWidgets, uic, QtGui, QtCore
from PyQt5 import *
import sys
import os
from os import walk
import csv
from Service_Mail import *
class Gestion_Des_Locataires(QtWidgets.QMainWindow) :
    def __init__(self):
        super(Gestion_Des_Locataires, self).__init__()


        uic.loadUi('../Ecran Locataires/Ecran Locataires.ui', self)
        self.setFixedSize(1280,720)
        self.__ecran=self.findChild(QtWidgets.QLabel,'label')
        self.__ecran.setPixmap(QtGui.QPixmap('../Ecran Locataires/Copie de Logic Immo.png'))

        self.__liste=self.findChild(QtWidgets.QListWidget,'listWidget')
        self.__liste.itemClicked.connect(self.Clicked_Item)
        self.__liste.itemDoubleClicked.connect(self.Double_Clicked_Item)
        self.__locataire_ordre=[]

        # for  i in range (0,10) :
        #     item=QtWidgets.QListWidgetItem(self.__liste)
        #
        #     itemwidget=Ui_Form('brice'+str(i),'chauvat','_','_')
        #     item.setSizeHint(itemwidget.sizeHint())
        #     self.__locataire_ordre.append(itemwidget)
        #     self.__liste.addItem(item)
        #     self.__liste.setItemWidget(item,itemwidget)
        #     itemwidget.image.setPixmap(QtGui.QPixmap('/Users/brice/PycharmProjects/ImmoLive/Img/276132-real-estate/png/house-12.png'))
        #     itemwidget.button.setIcon(QtGui.QIcon('/Users/brice/PycharmProjects/ImmoLive/Img/276132-real-estate/png/phone-call.png'))

        self.show()
        print(self.__locataire_ordre)
        a=os.listdir('../Locataire/Liste de Locataire')
        for i in a :
            with open('../Locataire/Liste de Locataire/'+i, newline='') as f :
                reader = csv.reader(f)
                for row in reader:
                    item=QtWidgets.QListWidgetItem(self.__liste)

                    itemwidget=Ui_Form('brice'+str(i),'chauvat','adresse1','adresse2')
                    item.setSizeHint(itemwidget.sizeHint())
                    self.__locataire_ordre.append(itemwidget)
                    self.__liste.addItem(item)
                    self.__liste.setItemWidget(item,itemwidget)
                    itemwidget.image.setPixmap(QtGui.QPixmap('/Users/brice/PycharmProjects/ImmoLive/Img/276132-real-estate/png/house-12.png'))
                    itemwidget.button.setIcon(QtGui.QIcon('/Users/brice/PycharmProjects/ImmoLive/Img/276132-real-estate/png/phone-call.png'))





    def Clicked_Item(self) :
        print('clicked')
        a=self.__liste.currentRow()
        print(self.__locataire_ordre[a].get_prenom())
    def Double_Clicked_Item(self):
        print('double clicked')



class Ui_Form(QtWidgets.QWidget):
    def __init__(self,nom,prenom,adresse1,adresse2, parent=None):
        super(QtWidgets.QWidget,self).__init__(parent)
        self.__nom=nom
        self.__prenom=prenom
        self.__adresse1=adresse1
        self.__adresse2=adresse2
        self.widget = QtWidgets.QWidget()
        self.widget.setGeometry(QtCore.QRect(10, 10, 581, 91))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(18)
        font.setItalic(True)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 3, 1)
        self.line = QtWidgets.QFrame(self.widget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 1, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(18)
        font.setItalic(True)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 2, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 2, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 2, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.widget)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/phone-call.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QtCore.QSize(32, 32))
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 0, 3, 4, 1)
        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setMaximumSize(QtCore.QSize(61, 61))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap(":/newPrefix/house-10.png"))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 0, 1, 4, 1)

        QtCore.QMetaObject.connectSlotsByName(self)
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", str(self.__nom)+' '+str(self.__prenom)))
        self.label_2.setText(_translate("Form", "Adresse"))
        self.label_4.setText(_translate("Form", str(self.__adresse1)))
        self.label_3.setText(_translate("Form", str(self.__adresse2)))
        self.pushButton.setText(_translate("Form", "Contacter"))
        self.setLayout(self.gridLayout)
        self.image=self.findChild(QtWidgets.QLabel,'label_5')
        self.button=self.findChild(QtWidgets.QPushButton,'pushButton')
        self.button.clicked.connect(self.Push_Envoi_Mail)

    def Push_Envoi_Mail(self):
        print('ok')
        window = Service_mail()
        window.exec()
    def get_prenom(self):
        return self.__nom





if __name__ == '__main__':


    app = QtWidgets.QApplication(sys.argv)
    window = Gestion_Des_Locataires()
    app.exec_()
