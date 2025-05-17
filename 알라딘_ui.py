# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file '알라딘.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFormLayout, QHBoxLayout, QLabel,
    QLayout, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QTextBrowser, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.setEnabled(True)
        Form.resize(968, 669)
        Form.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.verticalLayoutWidget = QWidget(Form)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(170, 20, 431, 501))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.verticalLayoutWidget)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setAcceptDrops(False)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_2 = QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName(u"label_2")
        font1 = QFont()
        font1.setBold(True)
        self.label_2.setFont(font1)

        self.horizontalLayout.addWidget(self.label_2)

        self.file_name = QLineEdit(self.verticalLayoutWidget)
        self.file_name.setObjectName(u"file_name")

        self.horizontalLayout.addWidget(self.file_name)

        self.file = QPushButton(self.verticalLayoutWidget)
        self.file.setObjectName(u"file")

        self.horizontalLayout.addWidget(self.file)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.label_3 = QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font1)

        self.verticalLayout.addWidget(self.label_3)

        self.verticalSpacer = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.label_4 = QLabel(self.verticalLayoutWidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font1)

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label_4)

        self.id = QLineEdit(self.verticalLayoutWidget)
        self.id.setObjectName(u"id")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.id)

        self.label_5 = QLabel(self.verticalLayoutWidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font1)

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.label_5)

        self.pw = QLineEdit(self.verticalLayoutWidget)
        self.pw.setObjectName(u"pw")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.pw)


        self.verticalLayout.addLayout(self.formLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer = QSpacerItem(80, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.login_btn = QPushButton(self.verticalLayoutWidget)
        self.login_btn.setObjectName(u"login_btn")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(70)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.login_btn.sizePolicy().hasHeightForWidth())
        self.login_btn.setSizePolicy(sizePolicy)
        self.login_btn.setMaximumSize(QSize(295, 50))
        self.login_btn.setFont(font1)

        self.horizontalLayout_2.addWidget(self.login_btn)

        self.horizontalSpacer_2 = QSpacerItem(80, 50, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.formLayout_2 = QFormLayout()
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.label_6 = QLabel(self.verticalLayoutWidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font1)

        self.formLayout_2.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label_6)

        self.total_books = QLabel(self.verticalLayoutWidget)
        self.total_books.setObjectName(u"total_books")

        self.formLayout_2.setWidget(0, QFormLayout.ItemRole.FieldRole, self.total_books)

        self.label_8 = QLabel(self.verticalLayoutWidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font1)

        self.formLayout_2.setWidget(1, QFormLayout.ItemRole.LabelRole, self.label_8)

        self.account = QLabel(self.verticalLayoutWidget)
        self.account.setObjectName(u"account")

        self.formLayout_2.setWidget(1, QFormLayout.ItemRole.FieldRole, self.account)


        self.verticalLayout.addLayout(self.formLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)

        self.start_btn = QPushButton(self.verticalLayoutWidget)
        self.start_btn.setObjectName(u"start_btn")
        self.start_btn.setMaximumSize(QSize(295, 50))
        self.start_btn.setFont(font1)

        self.horizontalLayout_3.addWidget(self.start_btn)

        self.horizontalSpacer_4 = QSpacerItem(40, 50, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_4)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.formLayout_3 = QFormLayout()
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.label_10 = QLabel(self.verticalLayoutWidget)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font1)

        self.formLayout_3.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label_10)

        self.ing = QLabel(self.verticalLayoutWidget)
        self.ing.setObjectName(u"ing")

        self.formLayout_3.setWidget(0, QFormLayout.ItemRole.FieldRole, self.ing)


        self.verticalLayout.addLayout(self.formLayout_3)

        self.textBrowser = QTextBrowser(self.verticalLayoutWidget)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setMaximumSize(QSize(1000, 500))

        self.verticalLayout.addWidget(self.textBrowser)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_5)

        self.save_btn = QPushButton(self.verticalLayoutWidget)
        self.save_btn.setObjectName(u"save_btn")
        self.save_btn.setMaximumSize(QSize(200, 50))
        self.save_btn.setFont(font1)

        self.horizontalLayout_4.addWidget(self.save_btn)

        self.horizontalSpacer_6 = QSpacerItem(40, 50, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_6)


        self.verticalLayout.addLayout(self.horizontalLayout_4)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"\uc54c\ub77c\ub518 \uc911\uace0\ucc45 \ucd5c\uc800\uac00 \ucc3e\uae30 \ud504\ub85c\uadf8\ub7a8", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\uc120\ud0dd\ud55c \ud30c\uc77c :", None))
        self.file.setText(QCoreApplication.translate("Form", u"\ud30c\uc77c \uc120\ud0dd", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"\ud30c\uc77c\uc5d0 '\uc0c1\ud488\uba85', '\ubc14\ucf54\ub4dc', '\ud488\uc9c8 \ub4f1\uae09' \uc774 \uaf2d \uc788\uc5b4\uc57c \ud569\ub2c8\ub2e4.", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"\uc544\uc774\ub514 :", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"\ube44\ubc00\ubc88\ud638 :", None))
        self.login_btn.setText(QCoreApplication.translate("Form", u"\ub85c\uadf8\uc778", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"\uc804\uccb4 \ucc45 \uc218 :", None))
        self.total_books.setText(QCoreApplication.translate("Form", u"[]", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"\ud604\uc7ac \uacc4\uc815 :", None))
        self.account.setText(QCoreApplication.translate("Form", u"[]", None))
        self.start_btn.setText(QCoreApplication.translate("Form", u"\ud06c\ub864\ub9c1 \uc2dc\uc791", None))
        self.label_10.setText(QCoreApplication.translate("Form", u"\uc9c4\ud589 \ud604\ud669 :", None))
        self.ing.setText(QCoreApplication.translate("Form", u"[]", None))
        self.save_btn.setText(QCoreApplication.translate("Form", u"\uc5d1\uc140\ub85c \uc800\uc7a5", None))
    # retranslateUi

