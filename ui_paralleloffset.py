# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_paralleloffset.ui'
#
# Created: Tue Jul 23 12:41:12 2013
#      by: PyQt4 UI code generator 4.10
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_ParallelOffset(object):
    def setupUi(self, ParallelOffset):
        ParallelOffset.setObjectName(_fromUtf8("ParallelOffset"))
        ParallelOffset.resize(344, 310)
        self.buttonBox = QtGui.QDialogButtonBox(ParallelOffset)
        self.buttonBox.setGeometry(QtCore.QRect(-20, 260, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.txtDistance = QtGui.QLineEdit(ParallelOffset)
        self.txtDistance.setGeometry(QtCore.QRect(230, 20, 81, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.txtDistance.setFont(font)
        self.txtDistance.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.txtDistance.setObjectName(_fromUtf8("txtDistance"))
        self.label = QtGui.QLabel(ParallelOffset)
        self.label.setGeometry(QtCore.QRect(20, 20, 201, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(ParallelOffset)
        self.label_2.setGeometry(QtCore.QRect(20, 70, 141, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gbDirection = QtGui.QGroupBox(ParallelOffset)
        self.gbDirection.setGeometry(QtCore.QRect(230, 70, 81, 61))
        self.gbDirection.setTitle(_fromUtf8(""))
        self.gbDirection.setObjectName(_fromUtf8("gbDirection"))
        self.radLeft = QtGui.QRadioButton(self.gbDirection)
        self.radLeft.setGeometry(QtCore.QRect(10, 10, 82, 18))
        self.radLeft.setChecked(True)
        self.radLeft.setObjectName(_fromUtf8("radLeft"))
        self.radRight = QtGui.QRadioButton(self.gbDirection)
        self.radRight.setGeometry(QtCore.QRect(10, 30, 82, 18))
        self.radRight.setObjectName(_fromUtf8("radRight"))
        self.label_3 = QtGui.QLabel(ParallelOffset)
        self.label_3.setGeometry(QtCore.QRect(20, 150, 171, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gbMethod = QtGui.QGroupBox(ParallelOffset)
        self.gbMethod.setGeometry(QtCore.QRect(230, 150, 81, 81))
        self.gbMethod.setTitle(_fromUtf8(""))
        self.gbMethod.setObjectName(_fromUtf8("gbMethod"))
        self.radRound = QtGui.QRadioButton(self.gbMethod)
        self.radRound.setGeometry(QtCore.QRect(10, 10, 82, 18))
        self.radRound.setChecked(True)
        self.radRound.setObjectName(_fromUtf8("radRound"))
        self.radMitre = QtGui.QRadioButton(self.gbMethod)
        self.radMitre.setGeometry(QtCore.QRect(10, 30, 82, 18))
        self.radMitre.setObjectName(_fromUtf8("radMitre"))
        self.radBevel = QtGui.QRadioButton(self.gbMethod)
        self.radBevel.setGeometry(QtCore.QRect(10, 50, 82, 18))
        self.radBevel.setObjectName(_fromUtf8("radBevel"))

        self.retranslateUi(ParallelOffset)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), ParallelOffset.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), ParallelOffset.reject)
        QtCore.QMetaObject.connectSlotsByName(ParallelOffset)

    def retranslateUi(self, ParallelOffset):
        ParallelOffset.setWindowTitle(_translate("ParallelOffset", "ParallelOffset", None))
        self.txtDistance.setText(_translate("ParallelOffset", "0", None))
        self.label.setText(_translate("ParallelOffset", "Enter the offset distance (meters)", None))
        self.label_2.setText(_translate("ParallelOffset", "Enter the offset side", None))
        self.radLeft.setText(_translate("ParallelOffset", "Left", None))
        self.radRight.setText(_translate("ParallelOffset", "Right", None))
        self.label_3.setText(_translate("ParallelOffset", "Enter the offset line method", None))
        self.radRound.setText(_translate("ParallelOffset", "Round", None))
        self.radMitre.setText(_translate("ParallelOffset", "Mitre", None))
        self.radBevel.setText(_translate("ParallelOffset", "Bevel", None))

