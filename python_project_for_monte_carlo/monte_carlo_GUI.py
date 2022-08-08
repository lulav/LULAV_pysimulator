# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'monte_carlo_GUI.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(750, 1184)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.number_of_runs_label = QtWidgets.QLabel(self.centralwidget)
        self.number_of_runs_label.setGeometry(QtCore.QRect(30, 20, 451, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.number_of_runs_label.setFont(font)
        self.number_of_runs_label.setFrameShape(QtWidgets.QFrame.Panel)
        self.number_of_runs_label.setFrameShadow(QtWidgets.QFrame.Raised)
        self.number_of_runs_label.setObjectName("number_of_runs_label")
        self.number_of_monte_carlo_runs_input = QtWidgets.QLineEdit(self.centralwidget)
        self.number_of_monte_carlo_runs_input.setGeometry(QtCore.QRect(30, 80, 91, 31))
        self.number_of_monte_carlo_runs_input.setObjectName("number_of_monte_carlo_runs_input")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 750, 20))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Preformance Analysis"))
        self.number_of_runs_label.setText(_translate("MainWindow", "Enter Number of Runs (Integer)"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
