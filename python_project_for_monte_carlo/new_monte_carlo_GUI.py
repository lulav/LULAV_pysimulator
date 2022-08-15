# #from LulavROS1Bag import BagViewer
# from PyQt5.QtGui import QCursor
# from PyQt5.QtCore import  * 
# from PyQt5 import QtWidgets, uic
# from PyQt5.QtCore import  QSize
# import sys
# from tkinter import Tk
# from tkinter.filedialog import askopenfilename
# from mpl_toolkits.mplot3d import Axes3D
# import numpy as np
# import matplotlib
# matplotlib.use('Qt5Agg')
# from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg, NavigationToolbar2QT
# from matplotlib.figure import Figure

# import PyQt5.QtWidgets as qtw
# import PyQt5.QtGui as qtg


# class MainWindow(qtw.QWidget):
#     def __init__(self):
#         super().__init__()
        
#         # add a title
#         self.setWindowTitle("Monte Carlo Model")
#         self.setLayout(qtw.QVBoxLayout())

#         # create a label

        

# ####################################### FUNCTIONS ##########################################

#     def get_value_from_line_edit(self, line_edit):
#         X = line_edit.text()

#     def number_of_monte_carlo_runs(self, line_edit):
#         X = line_edit.text()
#         if X.isnumeric() == True: 
#             X = int(X)
#         else:
#             line_edit.setText("Enter A Number Please")
    
#     def click_box_variance(self, check_box, line_edit, combo_box): 
#         if check_box.isChecked() == True:
#             line_edit.setEnabled(True) 
#             combo_box.addItems(["Fixed","Uniform","Normal"])
#         else:
#             line_edit.setEnabled(False)
#             combo_box.clear()
            

#     def combo_box_variance(self, combo_box, line_edit): 
#         if (combo_box.currentText() == "Uniform") or (combo_box.currentText() == "Normal"):
#             line_edit.setEnabled(True)  
#         else:
#             line_edit.setEnabled(False)
        
        
#     def click_box_test(self, check_box, label):
#         if check_box.isChecked() == True:
#             label.setText("This Test Will Be Commited")
#         else:
#             label.setText("")

#     def get_value_from_layout(self, lay_out):
#         X = [[],[]]
#         for i in range(lay_out.count()):
#            # X[[],[]] = [lay_out.QLabel.text(),int(lay_out.QLine_Edit.text())]
#             print("dfhdhdh")

#     def click_box_succesful_var(self, check_box, bigger_than_combo_box, smaller_than_combo_box, bigger_than_line_edit, smaller_than_line_edit, succesful_value_label, bigger_than_label, smaller_than_label):
#         if check_box.isChecked() == True:
#             bigger_than_line_edit.setEnabled(True) 
#             smaller_than_line_edit.setEnabled(True)

#             bigger_than_combo_box.addItems(["<","<=","="])
#             smaller_than_combo_box.addItems(["<","<=","="])

#             succesful_value_label.setText(check_box.text())
#         else:
#             bigger_than_line_edit.setEnabled(False) 
#             smaller_than_line_edit.setEnabled(False)
#             bigger_than_combo_box.clear()
#             smaller_than_combo_box.clear()    
#             succesful_value_label.clear()
#             bigger_than_label.clear()
#             smaller_than_label.clear()

#     def bigger_than_combo_box_change(self, bigger_than_combo_box, bigger_than_line_edit, bigger_than_label):    
#         bigger_than_label.setText(f'{bigger_than_line_edit.text() + bigger_than_combo_box.currentText()}')

#     def bigger_than_line_edit_change(self, bigger_than_combo_box, bigger_than_line_edit, bigger_than_label):    
#         X = bigger_than_line_edit.text()
#         if X.isnumeric() == True: 
#             bigger_than_label.setText(f'{bigger_than_line_edit.text() + bigger_than_combo_box.currentText()}')
#             X = complex(X)
#         else:
#             bigger_than_line_edit.setText("Enter A Number Please")
#             bigger_than_label.clear()
#             bigger_than_label.setText(bigger_than_combo_box.currentText())

#     def smaller_than_combo_box_change(self, smaller_than_combo_box, smaller_than_line_edit, smaller_than_label):   
#         smaller_than_label.setText(f'{smaller_than_combo_box.currentText() + smaller_than_line_edit.text()}')

#     def smaller_than_line_edit_change(self, smaller_than_combo_box, smaller_than_line_edit, smaller_than_label):   
#         X = smaller_than_line_edit.text()
#         if X.isnumeric() == True: 
#             smaller_than_label.setText(f'{smaller_than_combo_box.currentText() + smaller_than_line_edit.text()}')
#             X = complex(X)
#         else:
#             smaller_than_line_edit.setText("Enter A Number Please")
#             smaller_than_label.clear()
#             smaller_than_label.setText(smaller_than_combo_box.currentText())
# app = qtw.QApplication([])
# mw = MainWindow()

# # run the app
# app.exec_()


# if __name__ == '__main__':
#     try:
#         main()
#     except Exception as e:
#         print(e)
#         pass 
import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg

def get_value_from_text(value_from_text_box):
    global MC_Rapper

    MC_Rapper = int(value_from_text_box)
    return

class MainWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()
        
        # add a title
        self.setWindowTitle("Monte Carlo Model")
        VB = self.setLayout(qtw.QVBoxLayout())

        # create a label
        number_of_runs_label = qtw.QLabel("Enter The Number Of Runs In The Monte Carlo Model")
        VB.addWidget(number_of_runs_label)

        # create a text box
        enter_number_of_runs = qtw.QLineEdit()
        enter_number_of_runs.setObjectName("runs_field")
        
        VB.addWidget(enter_number_of_runs)

        #create a button 
        monte_carlo_button = qtw.QPushButton("O.K.", clicked = lambda: pressed_monte_carlo_button())
        VB.addWidget(monte_carlo_button)

        self.show()

        def pressed_monte_carlo_button():
            get_value_from_text(enter_number_of_runs.text()) 
app = qtw.QApplication([])
mw = MainWindow()

# run the app
app.exec_()