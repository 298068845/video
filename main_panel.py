# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets
from mFont import mFont
from TitleBar import *
from mWidget import *
class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        def addshadow(item):
            effect_shadow = QGraphicsDropShadowEffect()
            effect_shadow.setOffset(-1, 2)
            effect_shadow.setBlurRadius(5)
            effect_shadow.setColor(QtCore.Qt.lightGray)
            item.setGraphicsEffect(effect_shadow)
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowIcon(QIcon("./res/ico2.ico"))
        MainWindow.setStyleSheet(str(self.LoadStyleFromQss(WINDOW_QSS)))
        MainWindow.setFixedSize(WINDOW_DEFAULT_WIDTH, WINDOW_DEFAULT_HEIGHT)
        MainWindow.setWindowTitle("翼矩摄像头芯片AI测试套件")
        MainWindow.setWindowFlags(Qt.FramelessWindowHint)
        MainWindow.setAttribute(Qt.WA_TranslucentBackground)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        # self.centralwidget.setStyleSheet(
        #     "QWidget#centralwidget{background-image:url('./res/bg.png');border-radius:10px;}"
        # )
        font = mFont.connectBtnFont()
        self.titleBar = TitleBar(MainWindow)
        self.titleBar.SetTitle(WINDOW_TITLE);
        self.titleBar.setContentsMargins(PaddingLR,10,PaddingLR,0)
        self.MainLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.MainLayout.setContentsMargins(5,5,5,0)
        self.MainLayout.setAlignment(Qt.AlignTop)
        self.QVBoxLayout = QtWidgets.QVBoxLayout()
        self.QVBoxLayout.setAlignment(Qt.AlignTop)
        self.QVBoxLayout.setContentsMargins(PaddingLR,0,PaddingLR,0)
        self.QHBoxLayout = QtWidgets.QHBoxLayout()

        # self.ComboBox = QtWidgets.QComboBox()
        # self.ComboBox.setFont(font)
        # self.ComboBox.addItem("厂家a")
        # self.ComboBox.addItem("厂家b")
        # self.ComboBox.addItem("厂家c")
        image = QtGui.QPixmap("./res/xp3.png")
        self.IpImage = QLabel()
        self.IpImage.setPixmap(image)
        self.IpImage.setAlignment(Qt.AlignCenter)
        self.IpImage.setFixedHeight(60)
        self.IpImage.setStyleSheet("margin-top:20px;")
        self.IpEdit = QtWidgets.QLineEdit()
        self.IpEdit.setFont(font)
        self.IpEdit.setText("192.168.2.")
        self.IpEdit.setInputMask('000.000.000.;_')
        self.IpEdit.setStyleSheet("margin-left:6px;margin-right:6px;border-radius:5px;border:none;margin-top:20px;")
        self.IpEdit.setFixedHeight(60)
        self.IpEdit.setAlignment(Qt.AlignCenter)
        self.IpEdit2 = QtWidgets.QLineEdit()
        self.IpEdit2.setFont(font)
        self.IpEdit2.setText("getDetectId")
        self.IpEdit2.setValidator(QIntValidator(0, 255))
        self.IpEdit2.setStyleSheet("border:none;border-radius:5px;margin-top:20px;")
        self.IpEdit2.setFixedWidth(70)
        self.IpEdit2.setFixedHeight(60)
        self.IpEdit2.setAlignment(Qt.AlignCenter)
        self.andEt = QtWidgets.QLineEdit()
        self.andEt.setObjectName("lineEt")
        self.andEt.setStyleSheet("margin-top:20px;border:none;background-color:#EAF0F6;")
        self.andEt.setText("—")
        self.andEt.setFocusPolicy(QtCore.Qt.NoFocus)
        self.andEt.setFont(font)
        self.andEt.setFixedWidth(10)
        self.andEt.setAlignment(Qt.AlignCenter)
        self.IpEdit3 = QtWidgets.QLineEdit()
        self.IpEdit3.setFont(font)
        self.IpEdit3.setText("211")
        self.IpEdit3.setAlignment(Qt.AlignCenter)
        self.IpEdit3.setValidator(QIntValidator(0, 255))
        self.IpEdit3.setStyleSheet("margin-right:5px;border:none;border-radius:5px;margin-top:20px;")
        self.IpEdit3.setFixedWidth(70)
        self.IpEdit3.setFixedHeight(60)
        addshadow(self.IpEdit)
        addshadow(self.IpEdit2)
        addshadow(self.IpEdit3)
        # self.ComboBox.view().setFixedHeight()
        # self.ComboBox.setStyleSheet("QComboBox{padding-left:10px;margin-top:20px;height:"+Control_HEIGHT+"}\n"
        self.QPushButton = QtWidgets.QPushButton()
        self.QPushButton.setFixedSize(40,60)
        self.QPushButton.setIcon(QIcon(TITLE_SEARCH_ICON));
        self.QPushButton.setIconSize(QtCore.QSize(30,30))
        self.QPushButton.setStyleSheet("border:none;border-radius:5px;margin-top:20px;background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:1, stop:0 rgba(1,113,204, 255), stop:1 rgba(2,69,168, 255));")

        self.lineEt = QtWidgets.QLineEdit()
        self.lineEt.setObjectName("lineEt")

        self.lineEt.setStyleSheet("border:none;background-color:#f4f4f4;")
        self.lineEt.setText("检索结果：")
        self.lineEt.setFocusPolicy(QtCore.Qt.NoFocus)
        self.lineEt.setFont(font)
        # self.QHBoxLayout.addWidget(self.ComboBox)
        self.QHBoxLayout.addWidget(self.IpImage)
        self.QHBoxLayout.addWidget(self.IpEdit)
        self.QHBoxLayout.addWidget(self.IpEdit2)
        self.QHBoxLayout.addWidget(self.andEt)
        self.QHBoxLayout.addWidget(self.IpEdit3)
        self.QHBoxLayout.addWidget(self.QPushButton)

        self.listWidget = QtWidgets.QTableWidget()
        self.listWidget.setObjectName("listWidget")
        #self.listWidget.setHidden(True)
        self.listWidget.setStyleSheet("margin-top:3px;margin-bottom:7px;border:none;background-color:#EAF0F6;")
        self.listWidget.setShowGrid(False)
        self.listWidget.setEditTriggers(QTableWidget.NoEditTriggers)
        self.listWidget.setRowCount(2)
        self.listWidget.setColumnCount(3)
        self.listWidget.horizontalHeader().setVisible(False)
        self.listWidget.verticalHeader().setVisible(False)
        self.listWidget.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.listWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.listWidget.setFocusPolicy(QtCore.Qt.NoFocus)
        self.listWidget.setEditTriggers(QAbstractItemView.NoEditTriggers);
        self.listWidget.setSelectionMode(QAbstractItemView.NoSelection);
        # for i in range(2):
        #     for j in range(3):
        #         print(i,j)
        #         widget = mWidget(j)
        #         layout = QVBoxLayout()
        #         layout.setAlignment(Qt.AlignCenter)
        #         widget.setStyleSheet("border:none;background:#F9FBFC;border-radius:10px;")
        #         if(j==0):
        #             widget.setStyleSheet("margin-right:10px;border:none;background:#F9FBFC;border-radius:10px;")
        #         elif(j==1):
        #             widget.setStyleSheet("border:none;background:#F9FBFC;border-radius:10px;")
        #         elif(j==2):
        #             widget.setStyleSheet("margin-left:10px;border:none;background:#F9FBFC;border-radius:10px;")
        #
        #         imageLabel = QLabel()
        #         imageLabel.setAlignment(Qt.AlignHCenter)
        #         image = QtGui.QPixmap("./res/xp1.png")
        #         imageLabel.setPixmap(image)
        #         imageLabel.setStyleSheet("margin-top:20px;background:transparent")
        #         button = QPushButton("连接")
        #         button.setFont(font)
        #         button.setMinimumHeight(46)
        #         # button.setMaximumWidth(100)
        #         button.setStyleSheet("border:none;background:#E1F1FC;color:#0490F7;"
        #                              "border-radius:5px;font-weight:bold;")
        #         button.clicked.connect(lambda:change())
        #         layout.setContentsMargins(30,0,30,0)
        #         label = QtWidgets.QLineEdit(widget)
        #         label.setText("192.168.0.106")
        #         label.setFont(font)
        #         label.setAlignment(Qt.AlignCenter)
        #         label.setStyleSheet("border:none;color:#0490F7;font-weight:bold;background:transparent")
        #         # label.setMaximumWidth(120)
        #         label.setFocusPolicy(QtCore.Qt.NoFocus)
        #         layout.addStretch(1)
        #         layout.addWidget(imageLabel)
        #         layout.addStretch(1)
        #         layout.addWidget(label)
        #         layout.addStretch(1)
        #         layout.addWidget(button)
        #         layout.addStretch(3)
        #         widget.setLayout(layout)
        #         self.listWidget.setCellWidget(i,j,widget)

        # self.loadingLabel = QLabel()
        # self.gif = QMovie("./res/loading.gif")
        # self.loadingLabel.setMovie(self.gif)
        # self.loadingLabel.setStyleSheet("margin-top:160px")
        # self.loadingLabel.setAlignment(Qt.AlignCenter)
        # movie = self.loadingLabel.movie()
        # movie.setScaledSize(QSize(70,74))
        # self.gif.start()
        #self.loadingLabel.setHidden(True)
        self.QVBoxLayout.addLayout(self.QHBoxLayout)
        # self.QVBoxLayout.addWidget(self.loadingLabel)
        self.QVBoxLayout.addWidget(self.listWidget)
        self.MainLayout.addWidget(self.titleBar)
        self.MainLayout.addLayout(self.QVBoxLayout)

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


