import sys
from PyQt5 import QtCore, QtWidgets
import main_panel,test_panel,history_panel
from mFont import mFont
from LoadingMask import *
from bean import *
from netUtils import *
from fileUtils import *
import datetime
from mWidget import *
import threading

#下发测试指令
def sendStartTest(self):
    self.curId = int(datetime.datetime.now().strftime("%d%H%M%S"))
    self.test = testUtils(self)
    self.test.start()
    self.modelname = self.ui_test.ComboBox.currentText()
    self.test.mysignal.connect(afterRequest)

def openHistory(self):
    self.ui_test.window = QMainWindow()
    self.ui_history = history_panel.Ui_MainWindow()
    self.ui_test.window.setWindowModality(Qt.ApplicationModal)
    self.ui_history.setupUi(self.ui_test.window)
    self.ui_test.window.show()

def clearText(self):
    self.ui_test.missionState.setText("")
    self.ui_test.model.setText("")
    self.ui_test.CostTime.setText("")
    self.ui_test.Data.setText("")
    self.ui_test.imageNum.setText("")
    self.ui_test.result.setText("")

def CloseWindow(self):
    #client.close()
    print("client close")
    self.win.close()

def selectModel(self):
    if self.ui_test.ComboBox.currentText()=="yolov3":
        self.type = 2
        self.currentModelPath = config[5]
        self.currentImagePath = config[6]
        # self.ui_test.ModelPathEdit.setText(config[5])
        # self.ui_test.ImagePathEdit.setText(config[6])
    else:
        self.type = 1
        if self.ui_test.ComboBox.currentText()=="resnet50":
            self.currentModelPath = config[7]
            # self.ui_test.ModelPathEdit.setText(config[7])
        else:
            self.currentModelPath = config[3]
            # self.ui_test.ModelPathEdit.setText(config[3])
        self.currentImagePath = config[4]
        # self.ui_test.ImagePathEdit.setText(config[4])


def threadFunction():
    if(ui_main.state!=0):
        ui_main.check.start()


    # if (ui_main.state != 0):
    #     t.start()
    # else:
    #     afterRequest(ui_main, Response.STATE)
    #     t.cancel()

def afterRequest(self,code):
    # print("after",code)
    if code == Response.HELLO:
        self.window = QMainWindow()
        self.ui_test = test_panel.Ui_MainWindow()
        self.window.setWindowModality(Qt.ApplicationModal)
        self.ui_test.setupUi(self.window)
        self.ui_test.lineEt.setText(self.deviceName+"")
        self.ui_test.lineEt2.setText("| "+self.signName)
        len1 = len(self.ui_test.lineEt.text())
        len2 = len(self.ui_test.lineEt2.text())
        # print(self.ui_test.lineEt.width(),self.ui_test.lineEt2.width())
        self.ui_test.lineEt.setFixedWidth(len1*11+5)
        self.ui_test.lineEt2.setFixedWidth(len2*11)
        # print(self.ui_test.lineEt.width(),self.ui_test.lineEt2.width())
        self.currentModelPath = config[3]
        self.currentImagePath = config[4]
        # self.ui_test.ModelPathEdit.setText(config[3])
        # self.ui_test.ImagePathEdit.setText(config[4])
        self.type = 1
        self.ui_test.ComboBox.currentIndexChanged[str].connect(lambda:selectModel(self))
        self.ui_test.titleBar.closeButton.clicked.connect(lambda: CloseWindow(self.ui_test.titleBar))
        self.ui_test.QPushButton.clicked.connect(lambda: sendStartTest(self))
        self.ui_test.QHistoryButton.clicked.connect(lambda: openHistory(self))
        #self.ui.lastResult.clicked.connect(lambda: sendGetDetectResult(self.ui))
        self.window.show()
    elif code == Response.TEST:
        clearText(self)
        # self.ui_test.dviceState.setText(u"忙碌")
        self.startTime = datetime.datetime.now()
        print("starttime:",datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        self.ui_test.movie.start()
        self.ui_test.loading_mask = LoadingMask(self.window,None,"开始推断任务",500)
        self.ui_test.loading_mask.show()
        self.ui_test.loading_mask.close()
        self.ui_test.QPushButton.setText("正在推断……")
        self.ui_test.QPushButton.setStyleSheet("margin-left:10px;margin-right:10px;font-weight:bold;color:#B0C4DE;width:130px;background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:1, stop:0 rgba(1,113,204, 255), stop:1 rgba(2,69,168, 255));")
        self.ui_test.QPushButton.setDisabled(True)
        # self.check = CheckUtils(self)
        # self.check.start()
        # self.check.mysignal.connect(afterRequest)
        self.check = CheckUtils(ui_main)
        self.check.mysignal.connect(afterRequest)
        self.state = 1
        t = threading.Timer(2, threadFunction)
        t.start()
    elif code ==Ruquest.STATE:
        print("设备忙碌")
        t = threading.Timer(2, threadFunction)
        t.start()
        # self.ui_test.loading_mask = LoadingMask(self.window,None,"推断中",1100)
        # self.ui_test.loading_mask.show()
        # self.ui_test.loading_mask.close()
        # t = threading.Thread(target = threadFunction,args=(datetime.datetime.now(),),name = 'function')
        # t.start()
    elif code ==Response.STATE:
        print("设备空闲")
        self.ui_test.movie.stop()
        self.ui_test.QPushButton.setText("开始推断")
        self.ui_test.QPushButton.setDisabled(False)
        self.ui_test.QPushButton.setStyleSheet("margin-left:10px;margin-right:10px;font-weight:bold;color:#FFFFFF;width:130px;background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:1, stop:0 rgba(1,113,204, 255), stop:1 rgba(2,69,168, 255));")
        endTime = datetime.datetime.now()
        self.trueTime = (endTime - self.startTime).seconds*1000
        print("endtime:",datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        print("trueTime:",self.trueTime)
        # self.ui_test.dviceState.setText(u"空闲")
        self.ui_test.loading_mask = LoadingMask(self.window,None,"推断完毕，正在获取结果……")
        self.ui_test.loading_mask.show()
        if self.type==2:
            self.idlist = getDetectId()
            self.convert = getConvert()
            self.getDetect = getDetectUtils(self)
            self.getDetect.start()
            self.getDetect.mysignal.connect(afterRequest)    
            self.ui_test.model.setText(u"检测")
        elif self.type==1:
            self.getClassfy = getClassfyUtils(self)
            self.getClassfy.start()
            self.getClassfy.mysignal.connect(afterRequest)
            self.ui_test.model.setText(u"分类")
    elif code ==Response.RESULT:
        self.ui_test.loading_mask.close()
        self.ui_test.missionState.setText(u"成功")
        self.ui_test.Data.setText(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        self.data = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.ui_test.CostTime.setText(self.fps)
        self.ui_test.imageNum.setText(self.imagesize)
        if self.type==1:
            self.result = "top1:"+str(self.top1)+"% top5:"+str(self.top5)+"%"
            self.ui_test.result.setText("top1:"+str(self.top1)+"%\ntop5:"+str(self.top5)+"%")
        if self.type==2:
            self.result = "Map(0.5-0.95):"+str(round(self.map[0],3))+" Map(0.5):"+str(round(self.map[1],3))
            self.ui_test.result.setText("Map(0.5-0.95):"+str(round(self.map[0],3))+"\nMap(0.5):"+str(round(self.map[1],3)))
        try:
            writeHistory(self)
        except Exception as e:
            self.ui_test.loading_mask = LoadingMask(self.window, None, "history.csv被占用，无法写入新数据，请关闭history.csv后再推断",1000)
            self.ui_test.loading_mask.show()
            self.ui_test.loading_mask.close()
    elif code == Response.CLOSE:
        loading_mask = LoadingMask(MainWindow,None,"连接中断！",500)
        loading_mask.show()  
        loading_mask.close()
        self.ui_test.movie.stop()
    elif code == Response.REJECT:
        loading_mask = LoadingMask(MainWindow,None,"连接被拒绝",500)
        loading_mask.show()  
        loading_mask.close()
        if(hasattr(self,"ui_test")):
            self.ui_test.movie.stop()
    elif code == Response.TIMEOUT:
        loading_mask = LoadingMask(MainWindow,None,"连接超时",500)
        loading_mask.show()  
        loading_mask.close()
        if (hasattr(self, "ui_test")):
            self.ui_test.movie.stop()

    

def add_item(self,ip):
    def handleButtonClicked(deviceIp):
        print(deviceIp[2:])
        self.selectIp = deviceIp[2:]
        self.loading_mask = LoadingMask(MainWindow,"./res/loading.gif","正在连接设备",500)
        self.loading_mask.show()
        self.loading_mask.close()
        self.hello = helloUtils(self)
        self.hello.start()
        self.hello.mysignal.connect(afterRequest)

    i = self.itemNum//3
    j = self.itemNum%3-1
    print(self.itemNum,i,j)
    font = mFont.connectBtnFont()
    widget = mWidget(j)
    layout = QVBoxLayout()
    layout.setAlignment(Qt.AlignCenter)
    widget.setStyleSheet("border:none;background:#F9FBFC;border-radius:10px;")
    if (j == 0):
        widget.setStyleSheet("margin-right:10px;border:none;background:#F9FBFC;border-radius:10px;")
    elif (j == 1):
        widget.setStyleSheet("border:none;background:#F9FBFC;border-radius:10px;")
    elif (j == 2):
        widget.setStyleSheet("margin-left:10px;border:none;background:#F9FBFC;border-radius:10px;")

    imageLabel = QLabel()
    imageLabel.setAlignment(Qt.AlignHCenter)
    image = QtGui.QPixmap("./res/xp1.png")
    imageLabel.setPixmap(image)
    imageLabel.setStyleSheet("margin-top:20px;background:transparent")
    button = QPushButton("连接")
    button.setFont(font)
    button.setMinimumHeight(46)
    # button.setMaximumWidth(100)
    button.setStyleSheet("border:none;background:#E1F1FC;color:#0490F7;"
                         "border-radius:5px;font-weight:bold;")
    button.clicked.connect(lambda: handleButtonClicked(ip))
    layout.setContentsMargins(30, 0, 30, 0)
    label = QtWidgets.QLineEdit(widget)
    label.setText(ip)
    label.setFont(font)
    label.setAlignment(Qt.AlignCenter)
    label.setStyleSheet("border:none;color:#0490F7;font-weight:bold;background:transparent")
    # label.setMaximumWidth(120)
    label.setFocusPolicy(QtCore.Qt.NoFocus)
    layout.addStretch(1)
    layout.addWidget(imageLabel)
    layout.addStretch(1)
    layout.addWidget(label)
    layout.addStretch(1)
    layout.addWidget(button)
    layout.addStretch(3)
    widget.setLayout(layout)
    self.listWidget.setCellWidget(i, j, widget)

def afterPing(ret,ui_main,index):
    #if(ui.ip[len(ui.ip)-1])
    ui_main.loading_mask.close()
    if index+1<len(ui_main.ip):
        ui_main.loading_mask = LoadingMask(MainWindow,"./res/loading.gif","正在检索%s……"%ui_main.ip[index+1],500)
        ui_main.loading_mask.show()
    if(ret==0):
        ui_main.itemNum = ui_main.itemNum+1
        add_item(ui_main,"设备%s"%ui_main.ip[index])


        

def Find(self):
    self.itemNum = 0;
    self.listWidget.clear()
    iplist = []
    if ui_main.IpEdit2.text() =="" and ui_main.IpEdit3.text()=="":
        self.loading_mask = LoadingMask(MainWindow, None, "地址不能为空", 500)
        self.loading_mask.show()
        self.loading_mask.close()
    elif ui_main.IpEdit2.text() !="" and ui_main.IpEdit3.text()!="":
        for x in range(int(ui_main.IpEdit2.text()),int(ui_main.IpEdit3.text())+1):
            iplist.append(ui_main.IpEdit.text() + str(x))
    elif ui_main.IpEdit2.text() !="":
        iplist.append(ui_main.IpEdit.text() + ui_main.IpEdit2.text())
    elif ui_main.IpEdit3.text() !="":
        iplist.append(ui_main.IpEdit.text() + ui_main.IpEdit3.text())

    if len(iplist)>0:
        self.ip = iplist
        self.loading_mask = LoadingMask(MainWindow,"./res/loading.gif","正在检索%s……"%self.ip[0],500)
        self.loading_mask.show()
        # print("loading2")
        self.p = pingUtils(ui_main)
        self.p.start()
        self.p.mysignal.connect(afterPing)
    #loading_mask.close()
    
def configChange(self,index):
    global config
    if index ==0:
        config[index] = self.IpEdit.text()
    if index ==1:
        config[index] = self.IpEdit2.text()
    if index ==2:
        config[index] = self.IpEdit3.text()


def btn_close_clicked(self):
    self.parent.close()


config = ["192.168.2","211","","modelpath","imagepath","modelpath2","imagepath2"]
if __name__ == '__main__':
    # if not QApplication.instance():
    #     app = QApplication(sys.argv)
    # else:
    #     app = QApplication.instance()
    app = QApplication(sys.argv)
    c = getConfig()
    if len(c)!=0:
        config = c
    MainWindow = QMainWindow()
    ui_main = main_panel.Ui_MainWindow()
    ui_main.truelabel = getClassifyLabel()
    ui_main.setupUi(MainWindow)
    ui_main.IpEdit.setText(config[0])
    ui_main.IpEdit2.setText(config[1])
    ui_main.IpEdit3.setText(config[2])
    ui_main.IpEdit.textChanged.connect(lambda:configChange(ui_main,0))
    ui_main.IpEdit2.textChanged.connect(lambda:configChange(ui_main,1))
    ui_main.IpEdit3.textChanged.connect(lambda:configChange(ui_main,2))
    #ui.ComboBox.currentIndexChanged[str].connect(print_value)  # 条目发生改变，发射信号，传递条目内容
    ui_main.QPushButton.clicked.connect(lambda:Find(ui_main))
    # ui_main.itemNum = 1
    # add_item(ui_main, "设备192.168.0.6")
    MainWindow.show()

    sys.exit(app.exec_())