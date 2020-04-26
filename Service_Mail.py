from PyQt5 import QtWidgets, uic, QtGui, QtCore
from PyQt5 import *
import sys
import os
import smtplib



class Service_mail(QtWidgets.QDialog) :
    def __init__(self):
        super(Service_mail, self).__init__()

        uic.loadUi('/Users/brice/PycharmProjects/ImmoLive/Service Mail/fenetre_mail.ui', self)
        self.show()
        self.__image=self.findChild(QtWidgets.QLabel,'label_3')
        self.__image.setPixmap(QtGui.QPixmap('/Users/brice/PycharmProjects/ImmoLive/Img/786392-user-interface/png/072-arroba.png'))
        self.__destinataire=self.findChild(QtWidgets.QLineEdit,'lineEdit')
        self.__obj=self.findChild(QtWidgets.QLineEdit,'lineEdit_2')
        self.__txt=self.findChild(QtWidgets.QTextEdit,'textEdit')



    def accept(self):
        obj=self.__obj.text()
        destinataire=self.__destinataire.text()
        txt=self.__txt.toPlainText()
        txt=str(txt)
        obj=str(obj)
        expediteur='brice.chauvat@msn.com'
        mailtext='Subject:'+obj+'\n\n'+txt
        #login
        username='brice.chauvat@msn.com'
        password='porschegt3'
        server=smtplib.SMTP('SMTP.office365.com:587')
        server.ehlo()
        server.starttls()
        server.login(username,password)

        try:
            server.sendmail(expediteur, destinataire, mailtext)
        except smtplib.SMTPException as e:
            print(e)
        server.quit()
        self.close()


if __name__ == '__main__':


# prog principal
    app = QtWidgets.QApplication(sys.argv)
    window = Service_mail()
    app.exec_()
