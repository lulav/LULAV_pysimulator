#from LulavROS1Bag import BagViewer
from PyQt5.QtGui import QCursor
from PyQt5.QtCore import  * 
from PyQt5 import QtWidgets, uic
from PyQt5.QtCore import  QSize
import sys
from tkinter import Tk
from tkinter.filedialog import askopenfilename
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib
matplotlib.use('Qt5Agg')
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg, NavigationToolbar2QT
from matplotlib.figure import Figure

class MplCanvas(FigureCanvasQTAgg): # plot class 
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        self.fig = Figure(figsize=(width, height), dpi=dpi)
        self.fig.set_facecolor((30/255, 30/255, 30/255))
        super(MplCanvas, self).__init__(self.fig)
        self.setStyleSheet("background-color:none;")

class UI(QtWidgets.QMainWindow):
    def __init__(self):
        super(UI, self).__init__()
        uic.loadUi('./monte_carlo_GUI_General.ui', self)
        self.setStyleSheet("background-color: rgb(150, 150, 150);")   
        self.show()

        self.sc = None
        self.axes = None
        self.plotted_topics = []
        self.attrs_flag = False

        ## number of Monte Carlo runs 
        # button for setting a number of runs
        self.number_of_runs_button.clicked.connect(lambda: self.number_of_monte_carlo_runs(self.number_of_monte_carlo_runs_line_edit))
        self.number_of_monte_carlo_runs_line_edit.returnPressed.connect(lambda: self.number_of_monte_carlo_runs(self.number_of_monte_carlo_runs_line_edit))
        # set tool tips for widget
        self.number_of_monte_carlo_runs_line_edit.setToolTip("Set Number Of Runs")
        

        ## desired variables
        # disabling the line edit for the begining
        self.nominal_value_line_edit.setEnabled(False)
        self.variance_line_edit.setEnabled(False)

        # check box for desired variables
        self.checkBox_var.stateChanged.connect(lambda: self.click_box_variance(self.checkBox_var, self.nominal_value_line_edit, self.distribution_combo_box))
        # combo box for desired distribution
        self.distribution_combo_box.currentIndexChanged.connect(lambda: self.combo_box_variance(self.distribution_combo_box, self.variance_line_edit))
        # tool tips for every widget
        self.checkBox_var.setToolTip("Choose Variable to Test")
        self.nominal_value_line_edit.setToolTip("Set a Nominal Value For Chosen Variable")
        self.distribution_combo_box.setToolTip("Set A Type of Distribution")
        self.variance_line_edit.setToolTip("Set A Variance for the Desired Variable")

        ## desired tests

        self.test_checkBox.stateChanged.connect(lambda: self.click_box_test(self.test_checkBox, self.test_label))
        self.checkBox_var.setToolTip("Choose Desired Test")
        self.test_label.setText("")
        # set tool tips for widgets
        self.test_checkBox.setToolTip("Choose Desired Test")

        ## define succesful run
        # set values in the line edit 
        self.define_succesful_run_button.clicked.connect(lambda: self.get_value_from_layout(self.define_succesful_run_layout))
        # set tool tips for widget
        self.succesful_var_line_edit.setToolTip("Enter a Value for the Desired Succes Criteria")

        ## where to save the data
        # get value from line edit
        self.where_to_store_data_value.returnPressed.connect(lambda: self.get_value_from_line_edit(self.where_to_store_data_value))
        self.where_to_store_data_button.clicked.connect(lambda: self.get_value_from_line_edit(self.where_to_store_data_value))
        # set tool tips for widget
        self.where_to_store_data_value.setToolTip("Type Where You Would Like Your Data to be Stored")


    def get_value_from_line_edit(self, line_edit):
        X = line_edit.text()

    def number_of_monte_carlo_runs(self, line_edit):
        X = line_edit.text()
        if X.isnumeric() == True: 
            X = int(X)
        else:
            line_edit.setText("Enter A Number Please")
    
    def click_box_variance(self, check_box, line_edit, combo_box): 
        if check_box.isChecked() == True:
            line_edit.setEnabled(True) 
            combo_box.addItems(["Fixed","Uniform","Normal"])
        else:
            line_edit.setEnabled(False)
            combo_box.clear()
            

    def combo_box_variance(self, combo_box, line_edit): 
        if (combo_box.currentText() == "Uniform") or (combo_box.currentText() == "Normal"):
            line_edit.setEnabled(True)  
        else:
            line_edit.setEnabled(False)
        
        
    def click_box_test(self, check_box, label):
        if check_box.isChecked() == True:
            label.setText("This Test Will Be Commited")
        else:
            label.setText("")

    def get_value_from_layout(self, lay_out):
        X = [[],[]]
        for lay_out.QLine_Edit in lay_out:
            X[[],[]] = [lay_out.QLabel.text(),int(lay_out.QLine_Edit.text())]

           
def main():
    app = QtWidgets.QApplication(sys.argv)
    window = UI()
    app.exec_()

if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(e)
        pass 