"""
Creating a PyQt Application:

1- Create a UI file using the QtDesigner.

2- Convert the UI file to a Python file using the conversion tool:
    /package/eda/anaconda3/bin/pyuic5 <fileName.ui> -o <fileName.py>
   The generated file must NOT be modified, as indicated in the header warning!
   
3- Use the given file <blank.py> to create a consumer Python file, and write the code that drives the UI.

"""

# Import PyQt5 classes
import sys
from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QMainWindow, QApplication

# from <Module Name> import *
#
# class <Consumer Class Name>(QMainWindow, <UI Class Name>):
#
#     def __init__(self, parent=None):
#         super(<Consumer Class Name>, self).__init__(parent)
#         self.setupUi(self)
#
# if __name__ == "__main__":
#     currentApp = QApplication(sys.argv)
#     currentForm = <Consumer Class Name>()
#
#     currentForm.show()
#     currentApp.exec_()

