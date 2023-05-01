# Form implementation generated from reading ui file 'frontQt6.ui'
#
# Created by: PyQt6 UI code generator 6.5.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(640, 320)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        self.verticalLayoutWidget = QtWidgets.QWidget(parent=Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(90, 70, 451, 131))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.GenerateKey = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        self.GenerateKey.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.GenerateKey.sizePolicy().hasHeightForWidth())
        self.GenerateKey.setSizePolicy(sizePolicy)
        self.GenerateKey.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.GenerateKey.setObjectName("GenerateKey")
        self.verticalLayout.addWidget(self.GenerateKey)
        self.Cript = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        self.Cript.setObjectName("Cript")
        self.verticalLayout.addWidget(self.Cript)
        self.Desencript = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        self.Desencript.setObjectName("Desencript")
        self.verticalLayout.addWidget(self.Desencript)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "CriptoRSA"))
        self.GenerateKey.setText(_translate("Dialog", "Gerar chave pública"))
        self.Cript.setText(_translate("Dialog", "Encriptar"))
        self.Desencript.setText(_translate("Dialog", "Desencriptar"))

    def setCommand(self, button: QtWidgets.QPushButton, func):
        button.clicked.connect(func)

    def unsetCommand(self, button: QtWidgets.QPushButton, func):
        button.clicked.disconnect(func)

