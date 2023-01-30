from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from mFont import mFont
from default import *
class TextView(object):
    def mTextView(titleContent,QVBoxLayout):
        QHBoxLayout = QtWidgets.QHBoxLayout()
        QHBoxLayout.setAlignment(Qt.AlignLeft)
        font = mFont.font2()
        title = QtWidgets.QTextBrowser()
        title.setStyleSheet("border:none;background:transparent;")
        title.setMaximumHeight(30)
        title.setMaximumWidth(115)
        title.setText(titleContent)
        title.setFocusPolicy(QtCore.Qt.NoFocus)
        title.setFont(font)
        font = mFont.font1()
        content = QtWidgets.QTextBrowser()
        content.setStyleSheet("font-weight:bold;border:none;background:transparent;color:#0490F7;")
        content.setMaximumHeight(30)
        content.setText("")
        content.setFocusPolicy(QtCore.Qt.NoFocus)
        content.setFont(font)
        QHBoxLayout.addWidget(title)
        QHBoxLayout.addWidget(content)
        QVBoxLayout.addLayout(QHBoxLayout)

        return content

    def mTextView2(titleContent,QVBoxLayout):
        QHBoxLayout = QtWidgets.QHBoxLayout()
        QHBoxLayout.setAlignment(Qt.AlignLeft|Qt.AlignTop)
        font = mFont.font2()
        title = QtWidgets.QTextBrowser()
        title.setStyleSheet("border:none;background:transparent;color:#1F2529")
        title.setMaximumHeight(60)
        title.setMaximumWidth(115)
        title.setText(titleContent+"\n")
        title.setFocusPolicy(QtCore.Qt.NoFocus)
        title.setFont(font)
        font = mFont.font1()
        content = QtWidgets.QTextBrowser()
        content.setStyleSheet("font-weight:bold;border:none;background:transparent;color:#0490F7;")
        content.setMaximumHeight(60)
        content.setAlignment(Qt.AlignLeft)
        content.setText("")
        content.setFocusPolicy(QtCore.Qt.NoFocus)
        content.setFont(font)
        QHBoxLayout.addWidget(title)
        QHBoxLayout.addWidget(content)
        QVBoxLayout.addLayout(QHBoxLayout)

        return content


    def mTextView3(titleContent,QVBoxLayout):
        hLayout = QtWidgets.QHBoxLayout()
        font = mFont.font2()
        title = QtWidgets.QLineEdit()
        title.setText(titleContent)
        title.setFont(font)
        title.setMaximumWidth(130)
        title.setMinimumHeight(HISTORY_LABELS_SIZE)
        title.setStyleSheet("border:none;background:transparent;color:#1F2529")
        title.setFocusPolicy(QtCore.Qt.NoFocus)
        content = QtWidgets.QLineEdit()
        content.setText("device" )
        content.setFont(font)
        content.setMinimumHeight(HISTORY_LABELS_SIZE)
        content.setMinimumWidth(300)
        # deviceNameLabel.setMaximumWidth(100)
        content.setStyleSheet("font-weight:bold;border:none;background:transparent;color:#0490F7;")
        content.setFocusPolicy(QtCore.Qt.NoFocus)
        hLayout.addStretch(5)
        hLayout.addWidget(title)
        hLayout.addStretch(2)
        hLayout.addWidget(content)
        hLayout.addStretch(3)
        QVBoxLayout.addLayout(hLayout)

        return content
