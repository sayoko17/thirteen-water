import sys
#从转换的.py文件内调用类
from main import Ui_MainWindow
from denglu1 import Ui_Form
from zhuce import Ui_Dialog
from chupai import Ui_Dialog1
from PyQt5 import QtWidgets
import os
import requests
import http.client
import string
import json
if hasattr(sys, 'frozen'):
    os.environ['PATH'] = sys._MEIPASS + ";" + os.environ['PATH']
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

#下面是登录界面的类！
class myWin(Ui_Form, QtWidgets.QWidget):
    #pushButton = pyqtSignal()

    def __init__(self,parent = None):
        super(myWin, self).__init__()
        self.setupUi(self)
        self.pushButton_2.clicked.connect(self.zhuce)
        #self.pushButton.clicked.connect(self.login)

    def login(self):
        yhid = self.lineEdit.text()
        yhmm = self.lineEdit_2.text()
        if yhid and yhmm:
            data1 = {'username': yhid,'password': yhmm }
            json1_idmm = json.dumps(data1)
            conn = http.client.HTTPSConnection("api.shisanshui.rtxux.xyz")
            payload = json1_idmm
            headers = {'content-type': "application/json"}
            conn.request("POST", "/auth/login", payload, headers)
            res = conn.getresponse()
            data = res.read()
            #user_id = data['user_id']
            print(data.decode("utf-8"))
            global text

            text = json.loads(data.decode("utf-8"))
            #print(text)
            user_id = text['data']['user_id']
            token = text['data']['token']
            print(user_id)
            print(token)


        else:
            print('x')
        mymain.show()
        return text
        #sys.exit(app.exec_())
    def zhuce(self):
        myzc.show()


#注册的类
class myzhuce(Ui_Dialog, QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(myzhuce, self).__init__(parent)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.zc)
        self.pushButton.clicked.connect(self.close)
    def zc(self):
        yhzh = self.lineEdit_3.text()
        yhmmm = self.lineEdit_4.text()
        # 点击注册之后直接传json过去
        data2 = {'username': yhzh, 'password': yhmmm}#json不能重名
        json2_zcidmm = json.dumps(data2)
        headers = {'content-type': "application/json"}
        conn = http.client.HTTPSConnection("api.shisanshui.rtxux.xyz")
        payload = json2_zcidmm
        conn.request("POST", "/auth/register", payload,headers)
        res = conn.getresponse()
        data = res.read()

        print(data.decode("utf-8"))
        print(json2_zcidmm)

class mychupai(Ui_Dialog1, QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(mychupai, self).__init__(parent)
        self.setupUi(self)



#下面是调用游戏主界面的类！
class MyWindow(QMainWindow, Ui_MainWindow):
     def __init__(self, parent=None):
         super(MyWindow, self).__init__(parent)
         self.setupUi(self)
         #self.pushButton.clicked.connect(self.fapai)
         #self.pushButton_3.clicked.connect(self.showcard)
         #self.pushButton_5.clicked.connect(self.showphb)
         self.pushButton_6.clicked.connect(self.findxq)


# 根据输入框历史战局详情
     def findxq(self):
         print('有在执行我1')
         id =self.lineEdit.text()
         print(id)
         token = text['data']['token']
         headers = {'content-type': "application/json",'x-auth-token': token}
         response = requests.get(url="https://api.shisanshui.rtxux.xyz/history/" +id,
                                  headers=headers)
         text2 = json.loads(response.text)
         print(text2)

# 历史战局列表
     def xxjl(self):
         token = text['data']['token']
         id = text['data']['user_id']
         conn = http.client.HTTPSConnection("api.shisanshui.rtxux.xyz")
         headers = {'x-auth-token': token}
         conn.request("GET", "/history?page=1&limit=5&player_id=%d" %id, headers=headers)
         res = conn.getresponse()
         data = res.read()

         listduizhan = json.loads(data.decode("utf-8"))
         listdui = listduizhan['data']

         strid = []
         strcard = []
         strscore = []

         for i in listdui:

             strid.append(i['id'])
             strcard.append(i['card'])
             strscore.append(i['score'])

         length = len(listdui)
         self.tableWidget_2.setRowCount(length)
         self.tableWidget_2.setColumnCount(3)
         str1 = ('id','card','score')
         self.tableWidget_2.setColumnWidth(0, 110)
         self.tableWidget_2.setColumnWidth(1,445)
         self.tableWidget_2.setHorizontalHeaderLabels(str1)

         for i in range(length):
             newitem1 = QTableWidgetItem("%d" % strid[i])
             newitem2 = QTableWidgetItem("%s" % strcard[i])
             newitem3 = QTableWidgetItem("%d" % strscore[i])

             self.tableWidget_2.setItem(i, 0, newitem1)
             self.tableWidget_2.setItem(i, 1, newitem2)
             self.tableWidget_2.setItem(i, 2, newitem3)
#根据id查询详细历史纪录
     def ffind(self):
         zjid = self.lineEdit.text()
         #把id传出去
         self.xxjl()

     def fapai(self):
         #self.lineEdit_2.setText('#3 #4 #5 #6 &7 &8 &9 &10 &J #7 #8 #9 #10')
         token = text['data']['token']
         conn = http.client.HTTPSConnection("api.shisanshui.rtxux.xyz")

         headers = {'content-type': "application/json",'x-auth-token': token}

         conn.request("POST", "/game/open", headers=headers)

         res = conn.getresponse()
         data = res.read()
         global text1
         text1 = json.loads(data.decode("utf-8"))
         # print(text)
         id = text1['data']['id']
         card = text1['data']['card']
         self.lineEdit_2.setText(card)

         print(data.decode("utf-8"))

     # 出牌
     def showcard(self):
         id = text1['data']['id']
         token = text['data']['token']
         headers = {'content-type': "application/json"}
         jsonstr = json.dumps(text1['data'])


         response = requests.post(url="http://122.51.19.148:8080/Card13SpringBoot-1.0-SNAPSHOT/hello2",data=jsonstr,headers=headers)
         text2 = json.loads(response.text)
         cardresult = text2['card']
         cardliststr = cardresult[0] + ' ' + cardresult[1] + ' ' + cardresult[2]#按空格分开
         cardlist = cardliststr.split(' ')
         print(cardlist)
         for i in range(13):
             print(cardlist)
             print(cardlist[i][0])
             print(cardlist[i][1])
             if cardlist[i][0] == '$':
                 cardlistvalue = cardlist[i][1]
                 lablea = '1'+ '_' + cardlistvalue
             if cardlist[i][0] == '&':
                 cardlistvalue = cardlist[i][1]
                 lablea = '2' + '_' + cardlistvalue
             if cardlist[i][0] == '*':
                 cardlistvalue = cardlist[i][1]
                 lablea = '3' + '_' + cardlistvalue
             if cardlist[i][0] == '#':
                 cardlistvalue = cardlist[i][1]
                 lablea = '#' + cardlistvalue
             img_path = 'border-image: url(:/newPrefix/%s.png);' %lablea
             j = i + 1
             if(j == 1):
                 labelx = mycp.label_1
             elif j == 2:
                 labelx = mycp.label_2
             elif j == 3:
                 labelx = mycp.label_3
             elif j == 4:
                 labelx = mycp.label_4
             elif j == 5:
                 labelx = mycp.label_5
             elif j == 6:
                 labelx = mycp.label_6
             elif j == 7:
                 labelx = mycp.label_7
             elif j == 8:
                 labelx = mycp.label_8
             elif j == 9:
                 labelx = mycp.label_9
             elif j == 10:
                 labelx = mycp.label_10
             elif j == 11:
                 labelx = mycp.label_11
             elif j == 12:
                 labelx = mycp.label_12
             elif j == 13:
                 labelx = mycp.label_13


             labelx.setStyleSheet(img_path)
         mycp.show()

         data1 = {'id': id, 'card': cardresult}
         json1_idmm = json.dumps(data1)
         conn = http.client.HTTPSConnection("api.shisanshui.rtxux.xyz")
         payload = json1_idmm
         headers = {'content-type': "application/json",
                    'x-auth-token': token}
         conn.request("POST", "/game/submit", payload, headers)
         res = conn.getresponse()
         data = res.read()
         print(data)
#排行榜
     def showphb(self):
         #token = text['data']['token']
         conn = http.client.HTTPSConnection("api.shisanshui.rtxux.xyz")
         conn.request("GET", "/rank")

         res = conn.getresponse()
         res2 = requests.get(res.headers['Location'])
         array = json.loads(res2.text)
         strid = []
         strname =[]
         strscore = []
         for i in array:
             strid.append(i['player_id'])
             strname.append(i['name'])
             strscore.append(i['score'])

         length = len(array)
         self.tableWidget.setRowCount(length)
         # if length > 7:
         #     length = 7

         for i in range(length):
             newitem1 = QTableWidgetItem("%d" % strid[i])
             newitem2 = QTableWidgetItem(strname[i])
             newitem3 = QTableWidgetItem("%d" % strscore[i])

             self.tableWidget.setItem(i,0,newitem1)
             self.tableWidget.setItem(i,1, newitem2)
             self.tableWidget.setItem(i,2, newitem3)




if __name__ == '__main__':
     app_1 = QApplication(sys.argv)
     my = myWin()
     my.show()
     mymain = MyWindow()
     myzc = myzhuce()
     mycp = mychupai()
     sys.exit(app_1.exec_())
