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

        ## define succesful run
        # set values in the line edit 
        self.define_succesful_run_button.clicked.connect(lambda: self.get_value_from_layout(self.define_succesful_run_layout))

    def number_of_monte_carlo_runs(self, line_edit):
        X = line_edit.text()
        if X.isnumeric() == True: 
            X = int(X)
        else:
            line_edit.setText("Enter A Number Please")

    def get_value_from_line_edit(self, line_edit):
        X = line_edit.text()
    
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

#     def _configure_plot_opts(self, y, t, topics_and_attrs):
#         z = None
#         if not self.sc:
#             self.sc = MplCanvas(self, width=2, height=1, dpi=100)
#             self.toolbar = NavigationToolbar2QT(self.sc, self)
#             self.toolbar.setStyleSheet("background-color: rgb(230, 230, 230);")
#             self.lulav_layout = QtWidgets.QVBoxLayout()
#             self.lulav_layout.addWidget(self.toolbar)
#             self.lulav_layout.addWidget(self.sc)
#             self.lulav_plot.setLayout(self.lulav_layout)
#             self.lulav_plot.setGeometry(QRect(350, 5, 445, 455))
#         if topics_and_attrs[2]: # if there is a Z topic read z messages
#             _,_, z = self.bag_reader.get_attrs_from_msgs(topics_and_attrs[2], topics_and_attrs[5])
#         if not self.axes: # if the axes has not been created
#             self.axes = self.sc.fig.add_subplot(111) if not z else self.sc.fig.add_subplot(111, projection='3d')
#             self.axes.set_facecolor((30/255, 30/255, 30/255))
#             self.axes.tick_params(axis='both', colors='white')
#             for spine in self.axes.spines.values():
#                 spine.set_color('white')
        
#         if topics_and_attrs[3] == "t": # if you want to use time axis instead of data
#             x = t
#             self.plotted_topics.append(topics_and_attrs[1]+"/"+topics_and_attrs[4])  # in order to create legend
#         else:
#             _,_,x = self.bag_reader.get_attrs_from_msgs(topics_and_attrs[0], topics_and_attrs[3])
#         if len(self.plotted_topics) > 1:
#             self.plotted_topics = list(set(self.plotted_topics))
#             # self.axes.legend(self.plotted_topics, loc='best')
#         x, y = self._make_x_y_equal(x, y)
#         return x, y, z
    
#     def _get_input_topics_and_attrs(self):
#         topics_and_attrs = []
#         topics_and_attrs_handles = [self.x_axis_topic, self.y_axis_topic, self.z_axis_topic, self.x_axis_data, self.y_axis_data, self.z_axis_data]
#         for handle in topics_and_attrs_handles:
#             topics_and_attrs.append(handle.toPlainText())
#         return topics_and_attrs
    
#     def contextMenuEvent(self, event):
#         self.menu = QtWidgets.QMenu(self)
#         self.menu.setStyleSheet("""
#             QMenu {border: 1px inset grey; background-color: rgb(50, 50, 50); color: rgb(250, 250, 250); padding: 0;}
#             QMenu:selected {background-color: rgb(173, 216, 230); color: rgb(50, 50, 50);}""")
#         pose = QCursor.pos()
#         axis_list = ["x", "y", "z"]
#         actions_list = []
#         for axis in axis_list:
#             actions_list.append(QtWidgets.QAction(f"Set as {axis} axis", self))
#             self.menu.addAction(actions_list[-1])
#         actions_list[0].triggered.connect(lambda: self.display_selection(event, pose, axis_list[0]))
#         actions_list[1].triggered.connect(lambda: self.display_selection(event, pose, axis_list[1]))
#         actions_list[2].triggered.connect(lambda: self.display_selection(event, pose, axis_list[2]))
#         self.menu.popup(QCursor.pos())

#     def display_selection(self, event, pose, axis):
#         m_pose = self.mapFromGlobal(QCursor.pos()).x()
#         table = self.table_topics if m_pose < 450 else self.table_attrs
#         vp_pos = table.viewport().mapFromGlobal(pose)
#         row = table.rowAt(vp_pos.y())
#         col = table.columnAt(1)
#         cell = table.item(row, col)
#         text = cell.text()
#         if axis == 'x':
#             self.x_axis_topic.setText(text) if m_pose < 450 else self.x_axis_data.setText(text)
#         elif axis == 'y':
#             self.y_axis_topic.setText(text) if m_pose < 450 else self.y_axis_data.setText(text)
#         else:
#             self.z_axis_topic.setText(text) if m_pose < 450 else self.z_axis_data.setText(text)
#         if not self.attrs_flag:
#             self._change_table("attrs", topic=text)
#             self.attrs_flag = True

#     def _return_attrs_from_topic(self, topic):
#         info = self.bag_reader.bag.get_type_and_topic_info(topic_filters=topic)
#         values = list(info[1].values())
#         msg_type = values[0][0]
#         ATTRS = {"geometry_msgs/PoseStamped": ["t", "pose.position.x", "pose.position.y", "pose.position.z"],
#                  "nav_msgs/Odometry": ["t", "pose.pose.position.x", "pose.pose.position.y", "pose.pose.position.z"],
#                  "sensor_msgs/Imu": ["t", "linear_acceleration.x", "linear_acceleration.y", "linear_acceleration.z"], 
#                  "geometry_msgs/TwistStamped": ["t", "twist.linear.x", "twist.linear.y", "twist.linear.z"],
#                  "geometry_msgs/Point": ["t", ".x", ".y", ".z"],
#                  "std_msgs/Float64": ["t", ".data"]}
#         return ATTRS[msg_type] if msg_type in ATTRS else ["No Availiable Attributes","Select Another Topic", "Or Insert Manually"]

#     def _change_table(self, dtypes, topic=None):
#         if dtypes in "attrs":
#             table = self.table_attrs
#             data_list = self._return_attrs_from_topic(topic)
#         elif dtypes in "topics":
#             table = self.table_topics
#             data_list = self.bag_reader.get_topics()

#         for data in sorted(data_list) if dtypes in "topics" else data_list:
#             table.setColumnCount(1)
#             table.setHorizontalHeaderLabels(["Topics"]) if dtypes in "topics" else table.setHorizontalHeaderLabels(["Available Attributes"])
#             rowPosition = table.rowCount()
#             table.insertRow(rowPosition)
#             table.setItem(rowPosition , 0, QtWidgets.QTableWidgetItem(data))
#             table.horizontalHeader().setStretchLastSection(True)
#             table.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
#             table.resizeColumnsToContents()
        
#     def plot_cb(self):
#         topics_and_attrs = self._get_input_topics_and_attrs()
#         t, _, y = self.bag_reader.get_attrs_from_msgs(topics_and_attrs[1], topics_and_attrs[4])
#         x, y, z = self._configure_plot_opts(y, t, topics_and_attrs)
#         if topics_and_attrs[2]:
#             self.axes.plot(x, y, z)
#             self.axes.set_zlim3d(np.amin([np.amin(x)/2, np.amin(z)/2]), np.amax([np.amax(x)*2, np.amax(z)*1.5]))
#         else:
#             self.axes.plot(x, y, marker='.') 
#         self.sc.draw()

#     def close_cb(self):
#         self.close()

#     def load_bag_and_fill_topics_table_cb(self):
#         Tk().withdraw()
#         bagfile = askopenfilename(initialdir="/home/lulav/bagfiles/gazebo")
#         bag_name = bagfile.split("/")[-1]
#         self.bag_reader = BagViewer(bagfile)
#         self.lbl_ready.setText(f"Loaded: {bag_name}")
#         self._change_table("topics")

#     def clear_plot_and_table_cb(self):
#         text_labels = [self.x_axis_topic, self.y_axis_topic, self.z_axis_topic, self.x_axis_data, self.y_axis_data, self.z_axis_data]
#         for text_label in text_labels:
#             text_label.setText('')
#         self.table_attrs.setRowCount(0)
#         self.table_attrs.setColumnCount(0)
#         self.attrs_flag = False
#         if self.axes:
#             self.axes.cla()
#             self.plotted_topics = []
#             self.sc.draw()
#             self.axes = None
           
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