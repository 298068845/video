from PyQt5 import QtGui
class mFont:
    @staticmethod
    def font1():
        font = QtGui.QFont()
        font.setPixelSize(16)
        font.setLetterSpacing(QtGui.QFont.AbsoluteSpacing,1)
        font.setFamily("Microsoft YaHei")
        return font

    @staticmethod
    def connectBtnFont():
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPixelSize(16)
        return font

    @staticmethod
    def font2():
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPixelSize(15)
        return font