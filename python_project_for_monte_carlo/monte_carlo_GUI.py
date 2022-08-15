#from LulavROS1Bag import BagViewer
from ipaddress import v4_int_to_packed
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
        uic.loadUi('./GUI_in_QTpy5/monte_carlo_GUI_General.ui', self)
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
        
       #############################################

        # VB = QtWidgets.QHBoxLayout(())
        # VB.addWidget(QtWidgets.QCheckBox('check_box'))
        # VB.addWidget(QtWidgets.QComboBox('combo_box'))
        # VB.addWidget(QtWidgets.QLineEdit('nominal_line_edit'))
        # VB.addWidget(QtWidgets.QLineEdit('variance_line_edit'))



       ##############################################

        ## desired variables

        line_edit_nom_var = []
        check_box_var = []
        combo_box_distribution = []

        for i in range(self.desired_varibles_layout.count()):
            widgets = self.desired_varibles_layout.itemAt(i)
            if isinstance(widgets, QtWidgets.QVBoxLayout):
                temp_line_edit = []
                for k in range(widgets.count()):
                    widget = widgets.itemAt(k).widget()          
                    if isinstance(widget, QtWidgets.QLineEdit):
                        temp_line_edit.append(widget)
                line_edit_nom_var.append(temp_line_edit)
            if isinstance(widgets, QtWidgets.QGridLayout):
                temp_check_box = []
                temp_combo_box = []
                for k in range(widgets.count()):
                    widget = widgets.itemAt(k).widget()
                    if isinstance(widget, QtWidgets.QCheckBox):
                        temp_check_box.append(widget)
                    if isinstance(widget, QtWidgets.QComboBox):
                        temp_combo_box.append(widget)
                check_box_var.append(temp_check_box)
                combo_box_distribution.append(temp_combo_box)
       
        check_box_var = np.transpose(check_box_var)
        combo_box_distribution = np.transpose(combo_box_distribution)
        line_edit_nom_var = np.transpose(line_edit_nom_var)
                              
        for rows in range(len(check_box_var)):
            line_edit_nom_var[rows][0].setEnabled(False)
            line_edit_nom_var[rows][1].setEnabled(False)

            # tool tips for every widget
            check_box_var[rows][0].setToolTip("Choose Variable to Test")
            combo_box_distribution[rows][0].setToolTip("Set A Type of Distribution")
            line_edit_nom_var[rows][0].setToolTip("Set a Nominal Value For Chosen Variable")            
            line_edit_nom_var[rows][1].setToolTip("Set A Variance for the Desired Variable")
            
        # for rows in range(len(check_box_var)):
            # checkBox_var = check_box_var[rows][0]
            # distribution_combo_box = combo_box_distribution[rows][0]
            # nominal_value_line_edit = line_edit_nom_var[rows][0]
            # variance_line_edit = line_edit_nom_var[rows][1]

            # check box for desired variables            
            # check_box_var[rows][0].stateChanged.connect(lambda r = rows: self.click_box_variance(check_box_var[r][0], 
            # line_edit_nom_var[r][0], combo_box_distribution[r][0])) 
            # # combo box for desired distribution
            # combo_box_distribution[rows][0].currentIndexChanged.connect(lambda r = rows: self.combo_box_variance(combo_box_distribution[r][0], 
            # line_edit_nom_var[r][1]))

        r = 6
        check_box_var[r][0].stateChanged.connect(lambda: self.click_box_variance(check_box_var[r][0], 
            line_edit_nom_var[r][0], combo_box_distribution[r][0]))  
        combo_box_distribution[r][0].currentIndexChanged.connect(lambda: self.combo_box_variance(combo_box_distribution[r][0], 
            line_edit_nom_var[r][1]))

        # self.nominal_value_line_edit.setEnabled(False)
        # self.variance_line_edit.setEnabled(False)

        
        # self.checkBox_var.stateChanged.connect(lambda: self.click_box_variance(self.checkBox_var, self.nominal_value_line_edit, self.distribution_combo_box))
        # self.distribution_combo_box.currentIndexChanged.connect(lambda: self.combo_box_variance(self.distribution_combo_box, self.variance_line_edit))
        
        

        ## desired tests

        check_box_test = []
        label_test = []
        temp_label = []
        temp_check_box = []
        
        for i in range(self.desired_tests_layout.count()):
            widgets = self.desired_tests_layout.itemAt(i)
            
            if isinstance(widgets, QtWidgets.QVBoxLayout):
                
                for k in range(widgets.count()):
                    widget = widgets.itemAt(k).widget() 
                    if isinstance(widget, QtWidgets.QCheckBox):
                        temp_check_box.append(widget) 
                    if isinstance(widget, QtWidgets.QLabel):
                        temp_label.append(widget)    
                label_test.append(temp_label)
                check_box_test.append(temp_check_box)    

        check_box_test = np.transpose(check_box_test)
        label_test = np.transpose(label_test)        

        for rows in range(len(check_box_test)):

            label_test[rows][0].setText("")

            # tool tips for every widget
            check_box_test[rows][0].setToolTip("Mark the Desired Test")
            label_test[rows][0].setToolTip("The Desired Test")

        for rows in range(len(check_box_test)):
            check_box_test[rows][0].stateChanged.connect(lambda r = rows, r1 = rows: self.click_box_test(check_box_test[r][0],
             label_test[r1][0]))    

        self.test_checkBox.stateChanged.connect(lambda: self.click_box_test(self.test_checkBox, self.test_label))
        self.checkBox_var.setToolTip("Choose Desired Test")
        self.test_label.setText("")
        # set tool tips for widgets
        self.test_checkBox.setToolTip("Choose Desired Test")

        ## define succesful run
        # check box for succesful criteria
        self.bigger_than_line_edit.setEnabled(False)
        self.smaller_than_line_edit.setEnabled(False)
        self.succesful_var_check_box.stateChanged.connect(lambda: self.click_box_succesful_var(self.succesful_var_check_box, self.bigger_than_combo_box, 
            self.smaller_than_combo_box, self.bigger_than_line_edit, self.smaller_than_line_edit, self.succesful_value_label, 
            self.bigger_than_label,self.smaller_than_label))

        # combo box for desired succes criteria
        self.bigger_than_combo_box.currentIndexChanged.connect(lambda: self.bigger_than_combo_box_change(self.bigger_than_combo_box, 
            self.bigger_than_line_edit, self.bigger_than_label))

        self.smaller_than_combo_box.currentIndexChanged.connect(lambda: self.smaller_than_combo_box_change(self.smaller_than_combo_box, 
            self.smaller_than_line_edit, self.smaller_than_label))

        # line edit for succes criteria value
        self.bigger_than_line_edit.returnPressed.connect(lambda: self.bigger_than_line_edit_change(self.bigger_than_combo_box, 
            self.bigger_than_line_edit, self.bigger_than_label))

        self.smaller_than_line_edit.returnPressed.connect(lambda: self.smaller_than_line_edit_change(self.smaller_than_combo_box, 
            self.smaller_than_line_edit, self.smaller_than_label))

        # set tool tips for widget
        self.bigger_than_line_edit.setToolTip("Enter a Minimum Value for the Desired Succes Criteria")
        self.smaller_than_line_edit.setToolTip("Enter a Maximum Value for the Desired Succes Criteria")


        ## where to save the data
        # get value from line edit
        self.where_to_store_data_value.returnPressed.connect(lambda: self.get_value_from_line_edit(self.where_to_store_data_value))
        self.where_to_store_data_button.clicked.connect(lambda: self.get_value_from_line_edit(self.where_to_store_data_value))
        # set tool tips for widget
        self.where_to_store_data_value.setToolTip("Type Where You Would Like Your Data to be Stored")

####################################### FUNCTIONS ##########################################

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
        for i in range(lay_out.count()):
           # X[[],[]] = [lay_out.QLabel.text(),int(lay_out.QLine_Edit.text())]
            print("dfhdhdh")

    def click_box_succesful_var(self, check_box, bigger_than_combo_box, smaller_than_combo_box, bigger_than_line_edit, smaller_than_line_edit, succesful_value_label, bigger_than_label, smaller_than_label):
        if check_box.isChecked() == True:
            bigger_than_line_edit.setEnabled(True) 
            smaller_than_line_edit.setEnabled(True)

            bigger_than_combo_box.addItems(["<","<=","="])
            smaller_than_combo_box.addItems(["<","<=","="])

            succesful_value_label.setText(check_box.text())
        else:
            bigger_than_line_edit.setEnabled(False) 
            smaller_than_line_edit.setEnabled(False)
            bigger_than_combo_box.clear()
            smaller_than_combo_box.clear()    
            succesful_value_label.clear()
            bigger_than_label.clear()
            smaller_than_label.clear()

    def bigger_than_combo_box_change(self, bigger_than_combo_box, bigger_than_line_edit, bigger_than_label):    
        bigger_than_label.setText(f'{bigger_than_line_edit.text() + bigger_than_combo_box.currentText()}')

    def bigger_than_line_edit_change(self, bigger_than_combo_box, bigger_than_line_edit, bigger_than_label):    
        X = bigger_than_line_edit.text()
        if X.isnumeric() == True: 
            bigger_than_label.setText(f'{bigger_than_line_edit.text() + bigger_than_combo_box.currentText()}')
            X = complex(X)
        else:
            bigger_than_line_edit.setText("Enter A Number Please")
            bigger_than_label.clear()
            bigger_than_label.setText(bigger_than_combo_box.currentText())

    def smaller_than_combo_box_change(self, smaller_than_combo_box, smaller_than_line_edit, smaller_than_label):   
        smaller_than_label.setText(f'{smaller_than_combo_box.currentText() + smaller_than_line_edit.text()}')

    def smaller_than_line_edit_change(self, smaller_than_combo_box, smaller_than_line_edit, smaller_than_label):   
        X = smaller_than_line_edit.text()
        if X.isnumeric() == True: 
            smaller_than_label.setText(f'{smaller_than_combo_box.currentText() + smaller_than_line_edit.text()}')
            X = complex(X)
        else:
            smaller_than_line_edit.setText("Enter A Number Please")
            smaller_than_label.clear()
            smaller_than_label.setText(smaller_than_combo_box.currentText())

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