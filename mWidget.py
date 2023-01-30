from PyQt5.QtWidgets import QLabel,QWidget,QStyleOption,QStyle,QPushButton,QLineEdit
from PyQt5.QtGui import  QPainter
from PyQt5 import  QtGui
class mWidget(QWidget):
    def __init__(self,index):
        super(mWidget,self).__init__()
        self.index = index

    def enterEvent(self, QEvent):
        # here the code for mouse hover
        #print("enter")
        button = self.findChildren(QPushButton)[0]
        #button.setText("选中")
        button.setMinimumHeight(60)
        button.setStyleSheet("border:none;background:#FFFFFF;color:#0490F7;"
                             "border-radius:5px;font-weight:bold;")
        label = self.findChildren(QLineEdit)[0]
        label.setStyleSheet("margin-top:10px;border:none;color:#FFFFFF;font-weight:bold;background:transparent")
        imageLabel = self.findChildren(QLabel)[0]
        image = QtGui.QPixmap("./res/xp2.png")
        imageLabel.setPixmap(image)
        if (self.index  == 0):
            self.setStyleSheet("margin-right:10px;border:none;background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:1, stop:0 rgba(1,113,204, 255), stop:1 rgba(2,69,168, 255));border-radius:10px;")
        elif (self.index  == 1):
            self.setStyleSheet("border:none;background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:1, stop:0 rgba(1,113,204, 255), stop:1 rgba(2,69,168, 255));border-radius:10px;")
        elif (self.index  == 2):
            self.setStyleSheet("margin-left:10px;border:none;background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:1, stop:0 rgba(1,113,204, 255), stop:1 rgba(2,69,168, 255));border-radius:10px;")

        pass

    def leaveEvent(self, QEvent):
        # here the code for mouse leave
        #print("leave")
        button = self.findChildren(QPushButton)[0]
        #button.setText("未选中")
        button.setMinimumHeight(46)
        button.setStyleSheet("border:none;background:#E1F1FC;color:#0490F7;"
                             "border-radius:5px;font-weight:bold;")
        label = self.findChildren(QLineEdit)[0]
        label.setStyleSheet("border:none;color:#0490F7;font-weight:bold;background:transparent")
        imageLabel = self.findChildren(QLabel)[0]
        image = QtGui.QPixmap("./res/xp1.png")
        imageLabel.setPixmap(image)
        if (self.index == 0):
            self.setStyleSheet("margin-right:10px;border:none;background:#F9FBFC;border-radius:10px;")
        elif (self.index == 1):
            self.setStyleSheet("border:none;background:#F9FBFC;border-radius:10px;")
        elif (self.index == 2):
            self.setStyleSheet("margin-left:10px;border:none;background:#F9FBFC;border-radius:10px;")
        pass

    def mousePressEvent(self, QEvent) :
        print("")

    def paintEvent(self,Qevent):
        opt = QStyleOption()
        opt.initFrom(self)
        p = QPainter(self)
        self.style().drawPrimitive(QStyle.PE_Widget,opt,p,self)