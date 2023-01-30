# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets
from mFont import mFont
from TitleBar import *
from mWidget import *
from TextView import TextView
from fileUtils import *

class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        def additem(data):
            def roundStr(d):
                newstr = str(round(float(d),2))+"ms"
                return newstr
            font = mFont.font1()
            item = QListWidgetItem()  # 创建QListWidgetItem对象
            item.setSizeHint(QSize(720, 450))  # 设置QListWidgetItem大小
            widget = QWidget()
            widget.setStyleSheet("margin-bottom:20px;background:rgba(255,255,255, 70);border-radius:10px")
            vLayout=  QVBoxLayout()
            hLayout = QHBoxLayout()
            modelNameLabel = QtWidgets.QLineEdit(widget)
            modelNameLabel.setFont(font)
            modelNameLabel.setMaximumWidth(130)
            modelNameLabel.setMinimumHeight(HISTORY_LABELS_SIZE)
            modelNameLabel.setStyleSheet("background:transparent;font-weight:bold;border:none;color:#002C75")
            modelNameLabel.setFocusPolicy(QtCore.Qt.NoFocus)
            deviceNameLabel = QtWidgets.QLineEdit(widget)
            deviceNameLabel.setFont(font)
            deviceNameLabel.setMinimumWidth(300)
            deviceNameLabel.setMinimumHeight(HISTORY_LABELS_SIZE)
            deviceNameLabel.setStyleSheet("background:transparent;font-weight:bold;border:none;color:#002C75")
            deviceNameLabel.setFocusPolicy(QtCore.Qt.NoFocus)
            hLayout.addStretch(5)
            hLayout.addWidget(modelNameLabel)
            hLayout.addStretch(2)
            hLayout.addWidget(deviceNameLabel)
            hLayout.addStretch(3)
            vLayout.addStretch(1)
            vLayout.addLayout(hLayout)
            date = TextView.mTextView3("推断日期：", vLayout)
            signName = TextView.mTextView3("厂家名称：", vLayout)
            imageNum = TextView.mTextView3("图片数目：", vLayout)
            modelTime = TextView.mTextView3("模型加载时间：", vLayout)
            imageTime = TextView.mTextView3("图片加载时间：", vLayout)
            inferenceTime = TextView.mTextView3("推断耗时：", vLayout)
            fps = TextView.mTextView3("推断速度：", vLayout)
            totalTime = TextView.mTextView3("总耗时：", vLayout)
            result = TextView.mTextView3("精度：", vLayout)
            signName.setText(data[0])
            deviceNameLabel.setText(data[1])
            modelNameLabel.setText(data[2])
            date.setText(data[3])
            imageNum.setText(data[4])
            modelTime.setText(roundStr(data[5]))
            imageTime.setText(roundStr(data[6]))
            inferenceTime.setText(roundStr(data[7]))
            fps.setText(data[8])
            totalTime.setText(roundStr(data[9]))
            result.setText(data[10])
            widget.setLayout(vLayout)
            self.listWidget.addItem(item)  # 添加item
            self.listWidget.setItemWidget(item, widget)
        MainWindow.setObjectName("MainWindow")
        MainWindow.setStyleSheet(str(self.LoadStyleFromQss(WINDOW_QSS)))
        MainWindow.setFixedSize(WINDOW_DEFAULT_WIDTH, WINDOW_DEFAULT_HEIGHT)
        MainWindow.setWindowIcon(QIcon("./res/ico2.ico"))
        MainWindow.setWindowTitle("测试记录")
        MainWindow.setWindowFlags(Qt.FramelessWindowHint)
        MainWindow.setAttribute(Qt.WA_TranslucentBackground)
        list = readHistory()
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        font = mFont.connectBtnFont()
        self.titleBar = TitleBar(MainWindow)
        self.titleBar.SetTitle(WINDOW_TITLE);
        self.titleBar.setContentsMargins(PaddingLR,10,PaddingLR,0)
        self.MainLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.MainLayout.setContentsMargins(5,10,5,10)
        self.MainLayout.setAlignment(Qt.AlignTop)
        self.QVBoxLayout = QtWidgets.QVBoxLayout()
        self.QVBoxLayout.setAlignment(Qt.AlignTop)
        self.QVBoxLayout.setContentsMargins(PaddingLR,0,PaddingLR,0)
        self.QHBoxLayout = QtWidgets.QHBoxLayout()
        image = QtGui.QPixmap("./res/xp3.png")
        self.IpImage = QLabel()
        self.IpImage.setPixmap(image)
        self.IpImage.setAlignment(Qt.AlignCenter)
        self.IpImage.setFixedHeight(60)
        self.IpImage.setStyleSheet("margin-top:20px;")
        self.andEt = QtWidgets.QLineEdit()
        self.andEt.setObjectName("lineEt")
        self.andEt.setStyleSheet("margin-left:5px;margin-top:20px;border:none;background-color:#EAF0F6;color:#1F2529")
        self.andEt.setText("测试记录")
        self.andEt.setFocusPolicy(QtCore.Qt.NoFocus)
        font.setLetterSpacing(QtGui.QFont.AbsoluteSpacing,1)
        self.andEt.setFont(font)
        self.andEt.setAlignment(Qt.AlignLeft)
        self.QHBoxLayout.addWidget(self.IpImage)
        self.QHBoxLayout.addWidget(self.andEt)
        self.QHBoxLayout.addStretch(1)
        self.listWidget = QtWidgets.QListWidget()
        # self.listWidget.setSpacing(8)
        self.listWidget.setObjectName("listWidget")
        # self.listWidget.setStyleSheet("border-radius:5px;margin-top:3px;margin-bottom:7px;border:none;background-color:#FFFFFF;")
        self.listWidget.setStyleSheet("""
                QListWidget{
                    border-radius:5px;
                    margin-top:3px;
                    margin-bottom:7px;
                    border:none;
                    background:#EAF0F6;
              }
              QScrollBar:vertical {              
                  border: none;
                  border-radius:3px;
                  background:#EAF0F6;
                  width:18px;
                  margin-left:8px;
              }
              QScrollBar::handle:vertical {
                  background: rgba(3,53,156, 15);
                  min-height: 160px;
                  border-radius:3px;
                  border:none;
              }
              QScrollBar::add-line:vertical {
                  height: 0px;
              }
              QScrollBar::sub-line:vertical {
                  height: 0 px;
              }
                QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical,
                QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal {
                    background: none;
                }
          """)
        self.listWidget.setEditTriggers(QTableWidget.NoEditTriggers)
        self.listWidget.setFocusPolicy(QtCore.Qt.NoFocus)
        self.listWidget.setEditTriggers(QAbstractItemView.NoEditTriggers);
        self.listWidget.setSelectionMode(QAbstractItemView.NoSelection);
        self.QVBoxLayout.addLayout(self.QHBoxLayout)
        # self.QVBoxLayout.addWidget(self.loadingLabel)
        self.QVBoxLayout.addWidget(self.listWidget)
        self.MainLayout.addWidget(self.titleBar)
        self.MainLayout.addLayout(self.QVBoxLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        for i in range(len(list)):
            additem(list[i])

    def LoadStyleFromQss(self, f):
        file = open(f)
        lines = file.readlines()
        file.close()
        res = ''
        for line in lines:
            res += line

        return res


