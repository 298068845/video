# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets
from TextView import TextView
from mFont import mFont
from TitleBar import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        def addshadow(item):
            effect_shadow = QGraphicsDropShadowEffect()
            effect_shadow.setOffset(-1, 2)
            effect_shadow.setBlurRadius(5)
            effect_shadow.setColor(QtCore.Qt.lightGray)
            item.setGraphicsEffect(effect_shadow)

        MainWindow.setObjectName("MainWindow")
        MainWindow.setStyleSheet(str(self.LoadStyleFromQss(WINDOW_QSS)))
        MainWindow.setFixedSize(WINDOW_DEFAULT_WIDTH, WINDOW_DEFAULT_HEIGHT)
        MainWindow.setWindowTitle("AI测试模块")
        MainWindow.setWindowFlags(Qt.FramelessWindowHint)
        MainWindow.setAttribute(Qt.WA_TranslucentBackground)
        MainWindow.setWindowIcon(QIcon("./res/ico2.ico"))

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.titleBar = TitleBar(MainWindow)
        self.titleBar.SetTitle(WINDOW_TITLE);
        self.titleBar.setContentsMargins(PaddingLR, 10, PaddingLR, 0)
        self.MainLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.MainLayout.setContentsMargins(5, 5, 5, 0)
        self.MainLayout.setAlignment(Qt.AlignTop)
        self.QVBoxLayout = QtWidgets.QVBoxLayout()
        self.QVBoxLayout.setAlignment(Qt.AlignTop)
        self.QVBoxLayout.setContentsMargins(PaddingLR, 20, PaddingLR, 0)
        self.ControlLayout = QtWidgets.QHBoxLayout()
        # self.ControlLayout.setContentsMargins(0,10,0,0)
        font = mFont.font1()
        image = QtGui.QPixmap("./res/xp3.png")
        self.Image = QLabel()
        self.Image.setPixmap(image)
        self.Image.setAlignment(Qt.AlignCenter)
        self.Image.setStyleSheet("margin-left:5px")
        self.lineEt = QtWidgets.QLineEdit()
        self.lineEt.setObjectName("lineEt")
        self.lineEt.setStyleSheet("border:none;color:#0490F7;font-weight:bold")
        self.lineEt.setText("摄像头信息xxxxxx")
        self.lineEt.setFocusPolicy(QtCore.Qt.NoFocus)
        self.lineEt.setFont(mFont.font1())
        self.lineEt.setAlignment(Qt.AlignCenter)

        self.lineEt2 = QtWidgets.QLineEdit()
        self.lineEt2.setObjectName("lineEt2")
        self.lineEt2.setStyleSheet("border:none;color:#0490F7;")
        self.lineEt2.setText("摄像头信息xxxxxx")
        self.lineEt2.setFocusPolicy(QtCore.Qt.NoFocus)
        self.lineEt2.setFont(mFont.font1())
        self.lineEt2.setAlignment(Qt.AlignCenter)
        self.ComboBox = QtWidgets.QComboBox()
        self.ComboBox.setObjectName("ComboBox")
        self.ComboBox.addItem("mobilenet_v2")
        self.ComboBox.addItem("resnet50")
        self.ComboBox.addItem("yolov3")
        self.ComboBox.setFont(font)
        self.ComboBox.setFixedHeight(40)
        self.ComboBox.setStyleSheet("QComboBox{color:#FFFFFF;width:130px;background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:1, stop:0 rgba(1,113,204, 255), stop:1 rgba(2,69,168, 255));}\n"
                                    "QComboBox:drop-down{"
                                    "border:none;"
                                    "}\n"
                                    "QComboBox:down-arrow{"
                                    "border:none;"
                                    "margin-right:10px;"
                                    "background:transparent;"
                                    "image:url(\"./res/more.png\");}\n"
                                    "QComboBox QAbstractItemView{"
                                    "background:transparent;"
                                    "color:#ffffff;"
                                    "}\n"
                                    "QCombBox:item:selected{"
                                    "color:#ffffff;"
                                    "}")
        self.QPushButton = QtWidgets.QPushButton()
        self.QPushButton.setObjectName("Start")
        self.QPushButton.setText("开始推断")
        self.QPushButton.setFixedHeight(40)
        self.QPushButton.setStyleSheet("margin-left:10px;margin-right:10px;color:#FFFFFF;width:130px;background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:1, stop:0 rgba(1,113,204, 255), stop:1 rgba(2,69,168, 255));")
        self.QPushButton.setFont(font)

        self.QHistoryButton = QtWidgets.QPushButton()
        self.QHistoryButton.setFixedSize(40, 40)
        self.QHistoryButton.setIcon(QIcon(TITLE_HISTORY_ICON));
        self.QHistoryButton.setIconSize(QtCore.QSize(30, 30))
        self.QHistoryButton.setStyleSheet(
            "border:none;border-radius:5px;background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:1, stop:0 rgba(1,113,204, 255), stop:1 rgba(2,69,168, 255));")
        self.ControlLayout.addWidget(self.Image)
        self.ControlLayout.addWidget(self.lineEt)
        self.ControlLayout.addWidget(self.lineEt2)
        self.ControlLayout.addStretch(20)
        self.ControlLayout.addWidget(self.ComboBox)
        self.ControlLayout.addWidget(self.QPushButton)
        self.ControlLayout.addWidget(self.QHistoryButton)
        self.ControlLayout.setAlignment(Qt.AlignLeft)
        self.ControlWidget = QtWidgets.QWidget()
        self.ControlWidget.setLayout(self.ControlLayout)
        self.ControlWidget.setStyleSheet("background-color:#ffffff;border-radius:5px;border:none;")
        addshadow(self.ControlWidget)
        self.QVBoxLayout.addWidget(self.ControlWidget)
        self.QVBoxLayout2 = QtWidgets.QVBoxLayout()
        self.MQHBoxLayout = QtWidgets.QHBoxLayout()

        # self.ModelPathEdit = TextView.mTextView2("模型路径：",self.QVBoxLayout)
        # self.ModelPathEdit.setText("/mnt/classify_detect/classify_detect/model/mobilenet_v2_magik.pb.bin")
        # self.ImagePathEdit = TextView.mTextView2("图片路径：",self.QVBoxLayout)
        # self.ImagePathEdit.setText("/mnt/classify_detect/classify_detect/classify_images.txt")
        #
        self.QVBoxLayout2.addStretch(5)
        # self.dviceState = TextView.mTextView("终端状态：",self.QVBoxLayout2)
        # self.dviceState.setText("空闲")
        self.QVBoxLayout2.addStretch(1)
        self.model = TextView.mTextView("模型类型：",self.QVBoxLayout2)
        self.QVBoxLayout2.addStretch(1)
        #self.model.setText("分类")
        self.imageNum = TextView.mTextView("图片数量：", self.QVBoxLayout2)
        #self.imageNum.setText("1000")
        self.QVBoxLayout2.addStretch(1)
        self.Data = TextView.mTextView("完成日期：", self.QVBoxLayout2)
        #self.Data.setText("202202170915")
        self.QVBoxLayout2.addStretch(1)
        self.missionState = TextView.mTextView("任务状态：", self.QVBoxLayout2)
        self.QVBoxLayout2.addStretch(1)
        #self.missionState.setText("成功")
        self.CostTime = TextView.mTextView("推断速度：", self.QVBoxLayout2)
        self.QVBoxLayout2.addStretch(1)
        #self.CostTime.setText("3000ms")
        self.result = TextView.mTextView2("推断结果：", self.QVBoxLayout2)
        self.QVBoxLayout2.addStretch(6)
        # self.result.setText("top1:95.5%,\ntop5:98.6%")
        self.movie = QMovie("./res/loading2.gif")
        self.label = QLabel()
        self.label.setMovie(self.movie)
        self.label.setFixedSize(QSize(430, 430))
        self.label.setScaledContents(True)
        self.label.setAttribute(Qt.WA_TranslucentBackground)
        self.label.setAlignment(Qt.AlignLeft)
        self.movie.start()
        self.movie.stop()
        # self.QVBoxLayout2.setAlignment(Qt.AlignHCenter)
        self.MQHBoxLayout.addWidget(self.label)
        self.MQHBoxLayout.addLayout(self.QVBoxLayout2)
        self.MQHBoxLayout.addStretch(1)
        self.QVBoxLayout.addLayout(self.MQHBoxLayout)
        self.MainLayout.addWidget(self.titleBar)
        self.MainLayout.addLayout(self.QVBoxLayout)
        # self.centralwidget.setContentsMargins(0, 0, 0, 0)

        MainWindow.setCentralWidget(self.centralwidget)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def LoadStyleFromQss(self, f):
        file = open(f)
        lines = file.readlines()
        file.close()
        res = ''
        for line in lines:
            res += line

        return res






