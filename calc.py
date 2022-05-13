# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'calc.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):


    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setEnabled(True)
        Form.resize(512, 501)
        Form.setFocusPolicy(QtCore.Qt.NoFocus)
        Form.setAcceptDrops(False)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("index.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        Form.setWindowOpacity(17.0)
        Form.setLayoutDirection(QtCore.Qt.RightToLeft)
        Form.setStyleSheet("#Form{\n"
"background:#e6e6e6;\n"
"}")
        self.gridWidget = QtWidgets.QWidget(Form)
        self.gridWidget.setGeometry(QtCore.QRect(0, 100, 511, 399))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.gridWidget.setFont(font)
        self.gridWidget.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.gridWidget.setStyleSheet("#gridWidget{\n"
"background:#e6e6e6;\n"
"}")
        self.gridWidget.setObjectName("gridWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(7)
        self.gridLayout.setObjectName("gridLayout")
        self.push_square = QtWidgets.QPushButton(self.gridWidget)
        self.push_square.setMinimumSize(QtCore.QSize(104, 60))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.push_square.setFont(font)
        self.push_square.setStyleSheet("#push_square{\n"
" border:0px;\n"
" background:#f1f1f1;\n"
"}\n"
"#push_square:hover{\n"
"background:#c0c0c0;\n"
" border:2px solid #fff;\n"
"\n"
"}")
        self.push_square.setObjectName("push_square")
        self.gridLayout.addWidget(self.push_square, 1, 4, 1, 1)
        self.push_point = QtWidgets.QPushButton(self.gridWidget)
        self.push_point.setMinimumSize(QtCore.QSize(104, 60))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.push_point.setFont(font)
        self.push_point.setStyleSheet("#push_point{\n"
" border:0px;\n"
" background:#fff;\n"
"}\n"
"#push_point:hover{\n"
"background:#c0c0c0;\n"
" border:2px solid #fff;\n"
"\n"
"}")
        self.push_point.setObjectName("push_point")
        self.gridLayout.addWidget(self.push_point, 5, 1, 1, 1)
        self.push_1 = QtWidgets.QPushButton(self.gridWidget)
        self.push_1.setMinimumSize(QtCore.QSize(104, 60))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.push_1.setFont(font)
        self.push_1.setStyleSheet("#push_1{\n"
" border:0px;\n"
" background:#fff;\n"
"}\n"
"#push_1:hover{\n"
"background:#c0c0c0;\n"
" border:2px solid #fff;\n"
"\n"
"}")
        self.push_1.setObjectName("push_1")
        self.gridLayout.addWidget(self.push_1, 4, 4, 1, 1)
        self.push_cv = QtWidgets.QPushButton(self.gridWidget)
        self.push_cv.setMinimumSize(QtCore.QSize(104, 60))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.push_cv.setFont(font)
        self.push_cv.setStyleSheet("#push_cv{\n"
" border:0px;\n"
" background:#f1f1f1;\n"
"}\n"
"#push_cv:hover{\n"
"background:#c0c0c0;\n"
" border:2px solid #fff;\n"
"\n"
"}")
        self.push_cv.setObjectName("push_cv")
        self.gridLayout.addWidget(self.push_cv, 1, 1, 1, 1)
        self.push_b = QtWidgets.QPushButton(self.gridWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(33)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.push_b.sizePolicy().hasHeightForWidth())
        self.push_b.setSizePolicy(sizePolicy)
        self.push_b.setMinimumSize(QtCore.QSize(104, 60))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.push_b.setFont(font)
        self.push_b.setStyleSheet("#push_b{\n"
" border:0px;\n"
" background:#f1f1f1;\n"
"}\n"
"#push_b:hover{\n"
"background:#c0c0c0;\n"
" border:2px solid #fff;\n"
"\n"
"}")
        self.push_b.setObjectName("push_b")
        self.gridLayout.addWidget(self.push_b, 0, 3, 1, 1)
        self.push_5 = QtWidgets.QPushButton(self.gridWidget)
        self.push_5.setMinimumSize(QtCore.QSize(104, 60))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.push_5.setFont(font)
        self.push_5.setStyleSheet("#push_5{\n"
" border:0px;\n"
" background:#fff;\n"
"}\n"
"#push_5:hover{\n"
"background:#c0c0c0;\n"
" border:2px solid #fff;\n"
"\n"
"}")
        self.push_5.setObjectName("push_5")
        self.gridLayout.addWidget(self.push_5, 3, 3, 1, 1)
        self.push_div = QtWidgets.QPushButton(self.gridWidget)
        self.push_div.setMinimumSize(QtCore.QSize(104, 60))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.push_div.setFont(font)
        self.push_div.setStyleSheet("#push_div{\n"
" border:0px;\n"
" background:#f1f1f1;\n"
"}\n"
"#push_div:hover{\n"
"background:#c0c0c0;\n"
" border:2px solid #fff;\n"
"\n"
"}")
        self.push_div.setObjectName("push_div")
        self.gridLayout.addWidget(self.push_div, 1, 0, 1, 1)
        self.push_3 = QtWidgets.QPushButton(self.gridWidget)
        self.push_3.setMinimumSize(QtCore.QSize(104, 60))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.push_3.setFont(font)
        self.push_3.setStyleSheet("#push_3{\n"
" border:0px;\n"
" background:#fff;\n"
"}\n"
"#push_3:hover{\n"
"background:#c0c0c0;\n"
" border:2px solid #fff;\n"
"\n"
"}")
        self.push_3.setObjectName("push_3")
        self.gridLayout.addWidget(self.push_3, 4, 1, 1, 1)
        self.push_7 = QtWidgets.QPushButton(self.gridWidget)
        self.push_7.setMinimumSize(QtCore.QSize(104, 60))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.push_7.setFont(font)
        self.push_7.setStyleSheet("#push_7{\n"
" border:0px;\n"
" background:#fff;\n"
"}\n"
"#push_7:hover{\n"
"background:#c0c0c0;\n"
" border:2px solid #fff;\n"
"\n"
"}")
        self.push_7.setObjectName("push_7")
        self.gridLayout.addWidget(self.push_7, 2, 4, 1, 1)
        self.push_del = QtWidgets.QPushButton(self.gridWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(33)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.push_del.sizePolicy().hasHeightForWidth())
        self.push_del.setSizePolicy(sizePolicy)
        self.push_del.setMinimumSize(QtCore.QSize(104, 60))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.push_del.setFont(font)
        self.push_del.setStyleSheet("#push_del{\n"
" border:0px;\n"
" background:#f1f1f1;\n"
"}\n"
"#push_del:hover{\n"
"background:#ff0e42;\n"
" color:#fff;\n"
" border:2px solid #fff;\n"
"\n"
"}")
        self.push_del.setObjectName("push_del")
        self.gridLayout.addWidget(self.push_del, 0, 1, 1, 1)
        self.push_add = QtWidgets.QPushButton(self.gridWidget)
        self.push_add.setMinimumSize(QtCore.QSize(104, 60))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.push_add.setFont(font)
        self.push_add.setStyleSheet("#push_add{\n"
" border:0px;\n"
" background:#f1f1f1;\n"
"}\n"
"#push_add:hover{\n"
"background:#c0c0c0;\n"
" border:2px solid #fff;\n"
"\n"
"}")
        self.push_add.setObjectName("push_add")
        self.gridLayout.addWidget(self.push_add, 4, 0, 1, 1)
        self.push_plus_mi = QtWidgets.QPushButton(self.gridWidget)
        self.push_plus_mi.setMinimumSize(QtCore.QSize(104, 60))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.push_plus_mi.setFont(font)
        self.push_plus_mi.setStyleSheet("#push_plus_mi{\n"
" border:0px;\n"
" background:#fff;\n"
"}\n"
"#push_plus_mi:hover{\n"
"background:#c0c0c0;\n"
" border:2px solid #fff;\n"
"\n"
"}")
        self.push_plus_mi.setObjectName("push_plus_mi")
        self.gridLayout.addWidget(self.push_plus_mi, 5, 4, 1, 1)
        self.push_9 = QtWidgets.QPushButton(self.gridWidget)
        self.push_9.setMinimumSize(QtCore.QSize(104, 60))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.push_9.setFont(font)
        self.push_9.setStyleSheet("#push_9{\n"
" border:0px;\n"
" background:#fff;\n"
"}\n"
"#push_9:hover{\n"
"background:#c0c0c0;\n"
" border:2px solid #fff;\n"
"\n"
"}")
        self.push_9.setObjectName("push_9")
        self.gridLayout.addWidget(self.push_9, 2, 1, 1, 1)
        self.push_mul = QtWidgets.QPushButton(self.gridWidget)
        self.push_mul.setMinimumSize(QtCore.QSize(104, 60))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.push_mul.setFont(font)
        self.push_mul.setStyleSheet("#push_mul{\n"
" border:0px;\n"
" background:#f1f1f1;\n"
"}\n"
"#push_mul:hover{\n"
"background:#c0c0c0;\n"
" border:2px solid #fff;\n"
"\n"
"}")
        self.push_mul.setObjectName("push_mul")
        self.gridLayout.addWidget(self.push_mul, 2, 0, 1, 1)
        self.push_sub = QtWidgets.QPushButton(self.gridWidget)
        self.push_sub.setMinimumSize(QtCore.QSize(104, 60))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.push_sub.setFont(font)
        self.push_sub.setStyleSheet("#push_sub{\n"
" border:0px;\n"
" background:#f1f1f1;\n"
"}\n"
"#push_sub:hover{\n"
"background:#c0c0c0;\n"
" border:2px solid #fff;\n"
"\n"
"}")
        self.push_sub.setObjectName("push_sub")
        self.gridLayout.addWidget(self.push_sub, 3, 0, 1, 1)
        self.push_2 = QtWidgets.QPushButton(self.gridWidget)
        self.push_2.setMinimumSize(QtCore.QSize(104, 60))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.push_2.setFont(font)
        self.push_2.setStyleSheet("#push_2{\n"
" border:0px;\n"
" background:#fff;\n"
"}\n"
"#push_2:hover{\n"
"background:#c0c0c0;\n"
" border:2px solid #fff;\n"
"\n"
"}")
        self.push_2.setObjectName("push_2")
        self.gridLayout.addWidget(self.push_2, 4, 3, 1, 1)
        self.push_c = QtWidgets.QPushButton(self.gridWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(33)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.push_c.sizePolicy().hasHeightForWidth())
        self.push_c.setSizePolicy(sizePolicy)
        self.push_c.setMinimumSize(QtCore.QSize(104, 60))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.push_c.setFont(font)
        self.push_c.setStyleSheet("#push_c{\n"
" border:0px;\n"
" background:#f1f1f1;\n"
"}\n"
"#push_c:hover{\n"
"background:#5500ff;\n"
"color:#fff;\n"
" border:2px solid #fff;\n"
"\n"
"}")
        self.push_c.setObjectName("push_c")
        self.gridLayout.addWidget(self.push_c, 0, 0, 1, 1)
        self.push_a = QtWidgets.QPushButton(self.gridWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(33)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.push_a.sizePolicy().hasHeightForWidth())
        self.push_a.setSizePolicy(sizePolicy)
        self.push_a.setMinimumSize(QtCore.QSize(104, 60))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.push_a.setFont(font)
        self.push_a.setStyleSheet("#push_a{\n"
" border:0px;\n"
" background:#f1f1f1;\n"
"}\n"
"#push_a:hover{\n"
"background:#c0c0c0;\n"
" border:2px solid #fff;\n"
"\n"
"}")
        self.push_a.setObjectName("push_a")
        self.gridLayout.addWidget(self.push_a, 0, 4, 1, 1)
        self.push_8 = QtWidgets.QPushButton(self.gridWidget)
        self.push_8.setMinimumSize(QtCore.QSize(104, 60))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.push_8.setFont(font)
        self.push_8.setStyleSheet("#push_8{\n"
" border:0px;\n"
" background:#fff;\n"
"}\n"
"#push_8:hover{\n"
"background:#c0c0c0;\n"
" border:2px solid #fff;\n"
"\n"
"}")
        self.push_8.setObjectName("push_8")
        self.gridLayout.addWidget(self.push_8, 2, 3, 1, 1)
        self.push_0 = QtWidgets.QPushButton(self.gridWidget)
        self.push_0.setMinimumSize(QtCore.QSize(104, 60))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.push_0.setFont(font)
        self.push_0.setStyleSheet("#push_0{\n"
" border:0px;\n"
" background:#fff;\n"
"}\n"
"#push_0:hover{\n"
"background:#c0c0c0;\n"
" border:2px solid #fff;\n"
"\n"
"}")
        self.push_0.setObjectName("push_0")
        self.gridLayout.addWidget(self.push_0, 5, 3, 1, 1)
        self.push_cube = QtWidgets.QPushButton(self.gridWidget)
        self.push_cube.setMinimumSize(QtCore.QSize(104, 60))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.push_cube.setFont(font)
        self.push_cube.setStyleSheet("#push_cube{\n"
" border:0px;\n"
" background:#f1f1f1;\n"
"}\n"
"#push_cube:hover{\n"
"background:#c0c0c0;\n"
" border:2px solid #fff;\n"
"\n"
"}")
        self.push_cube.setObjectName("push_cube")
        self.gridLayout.addWidget(self.push_cube, 1, 3, 1, 1)
        self.push_4 = QtWidgets.QPushButton(self.gridWidget)
        self.push_4.setMinimumSize(QtCore.QSize(104, 60))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.push_4.setFont(font)
        self.push_4.setStyleSheet("#push_4{\n"
" border:0px;\n"
" background:#fff;\n"
"}\n"
"#push_4:hover{\n"
"background:#c0c0c0;\n"
" border:2px solid #fff;\n"
"\n"
"}")
        self.push_4.setObjectName("push_4")
        self.gridLayout.addWidget(self.push_4, 3, 4, 1, 1)
        self.push_equal = QtWidgets.QPushButton(self.gridWidget)
        self.push_equal.setMinimumSize(QtCore.QSize(104, 60))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.push_equal.setFont(font)
        self.push_equal.setStyleSheet("#push_equal{\n"
" border:0px;\n"
" background:#99ff89;\n"
"}\n"
"#push_equal:hover{\n"
"background:#60ff65;\n"
" border:2px solid #fff;\n"
"\n"
"}")
        self.push_equal.setObjectName("push_equal")
        self.gridLayout.addWidget(self.push_equal, 5, 0, 1, 1)
        self.push_6 = QtWidgets.QPushButton(self.gridWidget)
        self.push_6.setMinimumSize(QtCore.QSize(104, 60))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.push_6.setFont(font)
        self.push_6.setStyleSheet("#push_6{\n"
" border:0px;\n"
" background:#fff;\n"
"}\n"
"#push_6:hover{\n"
"background:#c0c0c0;\n"
" border:2px solid #fff;\n"
"\n"
"}")
        self.push_6.setObjectName("push_6")
        self.gridLayout.addWidget(self.push_6, 3, 1, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(0, 30, 511, 61))
        self.lineEdit.setMinimumSize(QtCore.QSize(104, 60))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("#lineEdit{\n"
"background:#e6e6e6;\n"
"border:0px;\n"
"font-size:50px;\n"
"color:black;\n"
"}\n"
"")
        self.lineEdit.setInputMask("")
        self.lineEdit.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing)
        self.lineEdit.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.lineEdit.setObjectName("lineEdit")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.push_0.clicked.connect(self.push0)
        self.push_1.clicked.connect(self.push1)
        self.push_2.clicked.connect(self.push2)
        self.push_3.clicked.connect(self.push3)
        self.push_4.clicked.connect(self.push4)
        self.push_5.clicked.connect(self.push5)
        self.push_6.clicked.connect(self.push6)
        self.push_7.clicked.connect(self.push7)
        self.push_8.clicked.connect(self.push8)
        self.push_9.clicked.connect(self.push9)
        self.push_add.clicked.connect(self.pushadd)
        self.push_sub.clicked.connect(self.pushsub)
        self.push_div.clicked.connect(self.pushdiv)
        self.push_mul.clicked.connect(self.pushmul)
        self.push_point.clicked.connect(self.pushpoint)
        self.push_equal.clicked.connect(self.pushequal)
        self.push_del.clicked.connect(self.pushdel)
        self.push_c.clicked.connect(self.pushc)
        self.push_square.clicked.connect(self.pushsquare)
        self.push_cube.clicked.connect(self.pushcube)
        self.push_plus_mi.clicked.connect(self.pushplus)
        self.push_a.clicked.connect(self.pusha)
        self.push_b.clicked.connect(self.pushb)
        self.push_cv.clicked.connect(self.pushcv)


    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Calculator"))
        self.push_square.setText(_translate("Form", "x²"))
        self.push_point.setText(_translate("Form", "."))
        self.push_1.setText(_translate("Form", "1"))
        self.push_cv.setText(_translate("Form", "^"))
        self.push_b.setText(_translate("Form", "1/x"))
        self.push_5.setText(_translate("Form", "5"))
        self.push_div.setText(_translate("Form", "÷"))
        self.push_3.setText(_translate("Form", "3"))
        self.push_7.setText(_translate("Form", "7"))
        self.push_del.setText(_translate("Form", "Del"))
        self.push_add.setText(_translate("Form", "+"))
        self.push_plus_mi.setText(_translate("Form", "+/-"))
        self.push_9.setText(_translate("Form", "9"))
        self.push_mul.setText(_translate("Form", "x"))
        self.push_sub.setText(_translate("Form", "-"))
        self.push_2.setText(_translate("Form", "2"))
        self.push_c.setText(_translate("Form", "C"))
        self.push_a.setText(_translate("Form", "%"))
        self.push_8.setText(_translate("Form", "8"))
        self.push_0.setText(_translate("Form", "0"))
        self.push_cube.setText(_translate("Form", "x³"))
        self.push_4.setText(_translate("Form", "4"))
        self.push_equal.setText(_translate("Form", "="))
        self.push_6.setText(_translate("Form", "6"))
        self.push_6.setShortcut(_translate("Main", "6"))
        self.push_div.setShortcut(_translate("Main", "/"))
        self.push_5.setShortcut(_translate("Main", "5"))
        self.push_2.setShortcut(_translate("Main", "2"))
        self.push_7.setShortcut(_translate("Main", "7"))
        self.push_c.setShortcut(_translate("Main", "Ctrl+C"))
        self.push_equal.setShortcut(_translate("Main", "Return"))
        self.push_4.setShortcut(_translate("Main", "4"))
        self.push_point.setShortcut(_translate("Main", "."))
        self.push_1.setShortcut(_translate("Main", "1"))
        self.push_add.setShortcut(_translate("Main", "+"))
        self.push_a.setShortcut(_translate("Main", "%"))
        self.push_mul.setShortcut(_translate("Main", "*"))
        self.push_9.setShortcut(_translate("Main", "9"))
        self.push_del.setShortcut(_translate("Main", "Backspace"))
        self.push_0.setShortcut(_translate("Main", "0"))
        self.push_3.setShortcut(_translate("Main", "3"))
        self.push_sub.setShortcut(_translate("Main", "-"))
        self.push_8.setShortcut(_translate("Main", "8"))
        self.lineEdit.setPlaceholderText(_translate("Form", "0"))

    def push0(self):
        entry=self.lineEdit.text()
        self.lineEdit.setText(entry+"0")

    def push1(self):
        entry=self.lineEdit.text()
        self.lineEdit.setText(entry+"1")

    def push2(self):
            entry = self.lineEdit.text()
            self.lineEdit.setText(entry + "2")

    def push3(self):
            entry = self.lineEdit.text()
            self.lineEdit.setText(entry + "3")

    def push4(self):
            entry = self.lineEdit.text()
            self.lineEdit.setText(entry + "4")

    def push5(self):
            entry = self.lineEdit.text()
            self.lineEdit.setText(entry + "5")

    def push6(self):
            entry = self.lineEdit.text()
            self.lineEdit.setText(entry + "6")

    def push7(self):
            entry = self.lineEdit.text()
            self.lineEdit.setText(entry + "7")

    def push8(self):
            entry = self.lineEdit.text()
            self.lineEdit.setText(entry + "8")

    def push9(self):
            entry = self.lineEdit.text()
            self.lineEdit.setText(entry + "9")

    def pushadd(self):
            entry = self.lineEdit.text()
            self.lineEdit.setText(entry + "+")

    def pushsub(self):
            entry = self.lineEdit.text()
            self.lineEdit.setText(entry + "-")

    def pushmul(self):
            entry = self.lineEdit.text()
            self.lineEdit.setText(entry + "*")

    def pushdiv(self):
            entry = self.lineEdit.text()
            self.lineEdit.setText(entry + "/")

    def pushpoint(self):
            entry = self.lineEdit.text()
            self.lineEdit.setText(entry + ".")

    def pushequal(self):
            entry=self.lineEdit.text()
            try:
                    ans=eval(entry)
                    self.lineEdit.setText(str(ans))
            except:
                    self.lineEdit.setText("Error")

    def pushdel(self):
            entry=self.lineEdit.text()
            self.lineEdit.setText(entry[:len(entry)-1])

    def pushc(self):
            entry=self.lineEdit.text()
            self.lineEdit.setText("")

    def pushsquare(self):
            entry=self.lineEdit.text()
            try:
                self.an=int(eval(entry)**2)
                self.lineEdit.setText(str(self.an))
            except:
                self.lineEdit.setText("")

    def pushcube(self):
            entry=self.lineEdit.text()
            try:
                self.an=int(eval(entry)**3)
                self.lineEdit.setText(str(self.an))
            except:
                self.lineEdit.setText("")

    def pushplus(self):

            entry=self.lineEdit.text()
            self.lineEdit.setText("-"+entry)



    def pushb(self):
            entry = self.lineEdit.text()
            try:
                self.an = eval("1/"+entry)
                self.lineEdit.setText(str(self.an))
            except:
                self.lineEdit.setText("")

    def pusha(self):
            entry = self.lineEdit.text()
            try:
                self.an = eval(entry+"/100")
                self.lineEdit.setText(str(self.an))
            except:
                self.lineEdit.setText("")

    def pushcv(self):
            entry = self.lineEdit.text()

            self.lineEdit.setText(entry+"**")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.setFixedWidth(512)
    Form.setFixedHeight(501)
    Form.show()
    sys.exit(app.exec_())
