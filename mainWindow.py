# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

import tools
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_YZK(object):
    def setupUi(self, YZK):
        # 主窗口
        YZK.setObjectName("YZK")
        YZK.resize(1640, 952)
        YZK.setMinimumSize(QtCore.QSize(1640, 0))
        YZK.setMaximumSize(QtCore.QSize(1666, 16777215))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 252))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(128, 158, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 252))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 252))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 252))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(128, 158, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 252))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 252))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 252))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(128, 158, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 252))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 252))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        YZK.setPalette(palette)
        YZK.setMouseTracking(True)
        YZK.setStyleSheet("background-color:rgb(255, 255, 252);")
        self.centralwidget = QtWidgets.QWidget(YZK)
        self.centralwidget.setObjectName("centralwidget")

        # 文件导入
        self.file_path1 = QtWidgets.QComboBox(self.centralwidget)
        self.file_path1.setGeometry(QtCore.QRect(140, 205, 571, 31))
        self.file_path1.setStyleSheet("background-color: rgb(230, 231, 231)")
        self.file_path1.setObjectName("file_path1")
        self.file_path1.setEditable(True)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 205, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.file1 = QtWidgets.QPushButton(self.centralwidget)
        self.file1.setGeometry(QtCore.QRect(730, 210, 35, 22))
        self.file1.setStyleSheet("background-color: rgb(238, 238, 238)")
        self.file1.setObjectName("file1")


        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(830, 205, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.file_path2 = QtWidgets.QComboBox(self.centralwidget)
        self.file_path2.setGeometry(QtCore.QRect(940, 205, 571, 31))
        self.file_path2.setStyleSheet("background-color: rgb(230, 231, 231)")
        self.file_path2.setObjectName("file_path2")
        self.file_path2.setEditable(True)
        self.file2 = QtWidgets.QPushButton(self.centralwidget)
        self.file2.setGeometry(QtCore.QRect(1530, 210, 35, 22))
        self.file2.setStyleSheet("background-color: rgb(238, 238, 238)")
        self.file2.setObjectName("file2")

        # 标题
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(540, 10, 591, 51))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("")
        self.label_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_3.setLineWidth(3)
        self.label_3.setScaledContents(False)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setWordWrap(False)
        self.label_3.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.label_3.setObjectName("label_3")

        # 重复率显示
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(180, 100, 131, 61))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.repetition_rate = QtWidgets.QLabel(self.centralwidget)
        self.repetition_rate.setGeometry(QtCore.QRect(310, 100, 130, 61))
        font = QtGui.QFont()
        font.setPointSize(35)
        self.repetition_rate.setFont(font)
        self.repetition_rate.setStyleSheet("color:rgb(15, 255, 11);")
        self.repetition_rate.setAlignment(QtCore.Qt.AlignCenter)
        self.repetition_rate.setObjectName("repetition_rate")

        # 开始按钮
        self.start = QtWidgets.QPushButton(self.centralwidget)
        self.start.setEnabled(True)
        self.start.setGeometry(QtCore.QRect(760, 100, 111, 61))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.start.setFont(font)
        self.start.setStyleSheet("background-color :rgb(15, 255, 11);")
        self.start.setObjectName("start")

        # 显示框
        self.content1 = QtWidgets.QTextBrowser(self.centralwidget)
        self.content1.setGeometry(QtCore.QRect(30, 270, 771, 641))
        self.content1.setStyleSheet("border:1.5px solid black;background-color: #FFFFF0")
        self.content1.setObjectName("content1")
        self.content2 = QtWidgets.QTextBrowser(self.centralwidget)
        self.content2.setGeometry(QtCore.QRect(840, 270, 771, 641))
        self.content2.setStyleSheet("border:1.5px solid black;background-color:	#FFFFF0")
        self.content2.setObjectName("content2")

        self.file1.raise_()
        self.file_path1.raise_()
        self.label.raise_()
        self.file_path2.raise_()
        self.file2.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.repetition_rate.raise_()
        self.start.raise_()
        self.content1.raise_()
        self.content2.raise_()
        YZK.setCentralWidget(self.centralwidget)
        self.actionsflv = QtWidgets.QAction(YZK)
        self.actionsflv.setCheckable(False)
        self.actionsflv.setChecked(False)
        self.actionsflv.setEnabled(True)
        self.actionsflv.setStatusTip("")
        self.actionsflv.setWhatsThis("")
        self.actionsflv.setShortcut("")
        self.actionsflv.setAutoRepeat(True)
        self.actionsflv.setVisible(True)
        self.actionsflv.setMenuRole(QtWidgets.QAction.TextHeuristicRole)
        self.actionsflv.setIconVisibleInMenu(False)
        self.actionsflv.setShortcutVisibleInContextMenu(False)
        self.actionsflv.setPriority(QtWidgets.QAction.NormalPriority)
        self.actionsflv.setObjectName("actionsflv")

        self.retranslateUi(YZK)
        self.trigger()
        QtCore.QMetaObject.connectSlotsByName(YZK)

    def retranslateUi(self, YZK):
        """设置控件的text"""
        _translate = QtCore.QCoreApplication.translate
        YZK.setWindowTitle(_translate("YZK", "文本查重"))
        self.label.setText(_translate("YZK", " 模板文件"))
        self.file1.setText(_translate("YZK", "..."))
        self.file2.setText(_translate("YZK", "..."))
        self.label_2.setText(_translate("YZK", " 查重文件"))
        self.label_3.setText(_translate("YZK", "文 本 查 重 系 统"))
        self.label_4.setText(_translate("YZK", "重复率："))
        self.repetition_rate.setText(_translate("YZK", "0%"))
        self.start.setText(_translate("YZK", "开始查重"))
        self.actionsflv.setText(_translate("YZK", "重复率"))
        self.actionsflv.setIconText(_translate("YZK", "重复率"))
        self.actionsflv.setToolTip(_translate("YZK", "重复率"))

    def trigger(self):
        """ 添加触发事件 """
        self.file1.clicked.connect(lambda: tools.choose_file(self.file_path1))
        self.file2.clicked.connect(lambda: tools.choose_file(self.file_path2))
        self.start.clicked.connect(lambda: tools.load_file(self.file_path1,
                                                           self.file_path2,
                                                           self.content1,
                                                           self.content2,
                                                           self.repetition_rate))



