import sys
#从转换的.py文件内调用类
from main import Ui_MainWindow
from denglu1 import Ui_Form
from PyQt5 import QtWidgets
import os
if hasattr(sys, 'frozen'):
    os.environ['PATH'] = sys._MEIPASS + ";" + os.environ['PATH']
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class myWin(Ui_Form, QtWidgets.QWidget):
    #pushButton = pyqtSignal()

    def __init__(self,parent = None):
        super(myWin, self).__init__()
        self.setupUi(self)
        self.pushButton_2.clicked.connect(self.zhuce)
        #self.pushButton.clicked.connect(self.login)

    def login(self):
        print('yes登进主界面啦')
        #app = QtWidgets.QApplication(sys.argv)
        #mymain = MyWindow()
        mymain.show()
        #sys.exit(app.exec_())
    def zhuce(self):
        print('hhh我还没搞')




class MyWindow(QMainWindow, Ui_MainWindow):
     def __init__(self, parent=None):
         super(MyWindow, self).__init__(parent)
         self.setupUi(self)
     def ffind(self):
         print('hh这也还没搞')


if __name__ == '__main__':
     app_1 = QApplication(sys.argv)
     my = myWin()
     my.show()
     mymain = MyWindow()
     sys.exit(app_1.exec_())
