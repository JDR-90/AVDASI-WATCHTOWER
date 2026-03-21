# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'UI_Updated.ui'
##
## Created by: Qt User Interface Compiler version 6.10.1
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
from PySide6.QtWidgets import (QApplication, QCommandLinkButton, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QTextEdit, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(804, 384)
        Form.setStyleSheet(u"")
        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(14, 16, 782, 363))
        self.verticalLayout_3 = QVBoxLayout(self.widget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_6 = QSpacerItem(100, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_6)

        self.ControlsLabel = QLabel(self.widget)
        self.ControlsLabel.setObjectName(u"ControlsLabel")
        font = QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setItalic(True)
        font.setUnderline(True)
        self.ControlsLabel.setFont(font)
        self.ControlsLabel.setMouseTracking(False)

        self.horizontalLayout.addWidget(self.ControlsLabel)

        self.horizontalSpacer_7 = QSpacerItem(107, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_7)

        self.OutputLabel = QLabel(self.widget)
        self.OutputLabel.setObjectName(u"OutputLabel")
        self.OutputLabel.setFont(font)

        self.horizontalLayout.addWidget(self.OutputLabel)

        self.horizontalLayout.setStretch(1, 1)
        self.horizontalLayout.setStretch(3, 1)

        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.Flap = QHBoxLayout()
        self.Flap.setObjectName(u"Flap")
        self.FlapLabel = QLabel(self.widget)
        self.FlapLabel.setObjectName(u"FlapLabel")
        font1 = QFont()
        font1.setPointSize(11)
        self.FlapLabel.setFont(font1)

        self.Flap.addWidget(self.FlapLabel)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Minimum)

        self.Flap.addItem(self.horizontalSpacer_2)

        self.FlapEntry = QLineEdit(self.widget)
        self.FlapEntry.setObjectName(u"FlapEntry")
        self.FlapEntry.setStyleSheet(u"")

        self.Flap.addWidget(self.FlapEntry)

        self.FlapButton = QPushButton(self.widget)
        self.FlapButton.setObjectName(u"FlapButton")
        self.FlapButton.setStyleSheet(u"QPushButton {\n"
"    background-color: #4b4b4b;\n"
"    color: white;\n"
"    border: 1px solid #2e2e2e;\n"
"    border-radius: 6px;\n"
"    padding: 6px 12px;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #5e5e5e;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #3b3b3b;\n"
"}")

        self.Flap.addWidget(self.FlapButton)


        self.verticalLayout.addLayout(self.Flap)

        self.Aileron = QHBoxLayout()
        self.Aileron.setObjectName(u"Aileron")
        self.AileronLabel = QLabel(self.widget)
        self.AileronLabel.setObjectName(u"AileronLabel")
        self.AileronLabel.setFont(font1)

        self.Aileron.addWidget(self.AileronLabel)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.Aileron.addItem(self.horizontalSpacer_3)

        self.AileronEntry = QLineEdit(self.widget)
        self.AileronEntry.setObjectName(u"AileronEntry")

        self.Aileron.addWidget(self.AileronEntry)

        self.AileronButton = QPushButton(self.widget)
        self.AileronButton.setObjectName(u"AileronButton")
        self.AileronButton.setStyleSheet(u"QPushButton {\n"
"    background-color: #4b4b4b;\n"
"    color: white;\n"
"    border: 1px solid #2e2e2e;\n"
"    border-radius: 6px;\n"
"    padding: 6px 12px;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #5e5e5e;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #3b3b3b;\n"
"}")

        self.Aileron.addWidget(self.AileronButton)


        self.verticalLayout.addLayout(self.Aileron)

        self.Rudder = QHBoxLayout()
        self.Rudder.setObjectName(u"Rudder")
        self.RudderLabel = QLabel(self.widget)
        self.RudderLabel.setObjectName(u"RudderLabel")
        self.RudderLabel.setFont(font1)

        self.Rudder.addWidget(self.RudderLabel)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.Rudder.addItem(self.horizontalSpacer_4)

        self.RudderEntry = QLineEdit(self.widget)
        self.RudderEntry.setObjectName(u"RudderEntry")

        self.Rudder.addWidget(self.RudderEntry)

        self.RudderButton = QPushButton(self.widget)
        self.RudderButton.setObjectName(u"RudderButton")
        self.RudderButton.setStyleSheet(u"QPushButton {\n"
"    background-color: #4b4b4b;\n"
"    color: white;\n"
"    border: 1px solid #2e2e2e;\n"
"    border-radius: 6px;\n"
"    padding: 6px 12px;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #5e5e5e;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #3b3b3b;\n"
"}")

        self.Rudder.addWidget(self.RudderButton)


        self.verticalLayout.addLayout(self.Rudder)

        self.Elevator = QHBoxLayout()
        self.Elevator.setObjectName(u"Elevator")
        self.ElevatorLabel = QLabel(self.widget)
        self.ElevatorLabel.setObjectName(u"ElevatorLabel")
        self.ElevatorLabel.setFont(font1)

        self.Elevator.addWidget(self.ElevatorLabel)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.Elevator.addItem(self.horizontalSpacer_5)

        self.ElevatorEntry = QLineEdit(self.widget)
        self.ElevatorEntry.setObjectName(u"ElevatorEntry")

        self.Elevator.addWidget(self.ElevatorEntry)

        self.ElevatorButton = QPushButton(self.widget)
        self.ElevatorButton.setObjectName(u"ElevatorButton")
        self.ElevatorButton.setStyleSheet(u"QPushButton {\n"
"    background-color: #4b4b4b;\n"
"    color: white;\n"
"    border: 1px solid #2e2e2e;\n"
"    border-radius: 6px;\n"
"    padding: 6px 12px;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #5e5e5e;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #3b3b3b;\n"
"}")

        self.Elevator.addWidget(self.ElevatorButton)


        self.verticalLayout.addLayout(self.Elevator)


        self.horizontalLayout_3.addLayout(self.verticalLayout)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.OutputBox = QTextEdit(self.widget)
        self.OutputBox.setObjectName(u"OutputBox")
        self.OutputBox.setStyleSheet(u"QTextEdit {\n"
"    background-color: #ececec;\n"
"    border: 2px solid #4b4b4b;\n"
"    border-radius: 6px;\n"
"    padding: 6px;\n"
"    color: #2c2c2c;\n"
"}")

        self.verticalLayout_2.addWidget(self.OutputBox)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.FBWBButton = QCommandLinkButton(self.widget)
        self.FBWBButton.setObjectName(u"FBWBButton")
        self.FBWBButton.setStyleSheet(u"QCommandLinkButton {\n"
"    background-color: #4b4b4b;\n"
"    color: white;\n"
"    border: 1px solid #2e2e2e;\n"
"    border-radius: 10px;\n"
"    padding: 12px;\n"
"    font-size: 15px;\n"
"}\n"
"\n"
"QCommandLinkButton:hover {\n"
"    background-color: #5e5e5e;\n"
"}\n"
"\n"
"QCommandLinkButton:pressed {\n"
"    background-color: #3b3b3b;\n"
"}")

        self.horizontalLayout_2.addWidget(self.FBWBButton)

        self.ManualButton = QCommandLinkButton(self.widget)
        self.ManualButton.setObjectName(u"ManualButton")
        self.ManualButton.setStyleSheet(u"QCommandLinkButton {\n"
"    background-color: #4b4b4b;\n"
"    color: white;\n"
"    border: 1px solid #2e2e2e;\n"
"    border-radius: 10px;\n"
"    padding: 12px;\n"
"    font-size: 15px;\n"
"}\n"
"\n"
"QCommandLinkButton:hover {\n"
"    background-color: #5e5e5e;\n"
"}\n"
"\n"
"QCommandLinkButton:pressed {\n"
"    background-color: #3b3b3b;\n"
"}")

        self.horizontalLayout_2.addWidget(self.ManualButton)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.ConnectionStartButton = QCommandLinkButton(self.widget)
        self.ConnectionStartButton.setObjectName(u"ConnectionStartButton")
        self.ConnectionStartButton.setStyleSheet(u"QCommandLinkButton {\n"
"    background-color: #4b4b4b;\n"
"    color: white;\n"
"    border: 1px solid #2e2e2e;\n"
"    border-radius: 10px;\n"
"    padding: 12px;\n"
"    font-size: 15px;\n"
"}\n"
"\n"
"QCommandLinkButton:hover {\n"
"    background-color: #5e5e5e;\n"
"}\n"
"\n"
"QCommandLinkButton:pressed {\n"
"    background-color: #3b3b3b;\n"
"}")

        self.verticalLayout_2.addWidget(self.ConnectionStartButton)


        self.horizontalLayout_3.addLayout(self.verticalLayout_2)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.ControlsLabel.setText(QCoreApplication.translate("Form", u"Control Surfaces:", None))
        self.OutputLabel.setText(QCoreApplication.translate("Form", u"Output & Command Log:", None))
        self.FlapLabel.setText(QCoreApplication.translate("Form", u"Flap angle: ", None))
        self.FlapButton.setText(QCoreApplication.translate("Form", u"Send CMD", None))
        self.AileronLabel.setText(QCoreApplication.translate("Form", u"Aileron angle", None))
        self.AileronButton.setText(QCoreApplication.translate("Form", u"Send CMD", None))
        self.RudderLabel.setText(QCoreApplication.translate("Form", u"Rudder angle", None))
        self.RudderButton.setText(QCoreApplication.translate("Form", u"Send CMD", None))
        self.ElevatorLabel.setText(QCoreApplication.translate("Form", u"Elevator angle", None))
        self.ElevatorButton.setText(QCoreApplication.translate("Form", u"Send CMD", None))
        self.FBWBButton.setText(QCoreApplication.translate("Form", u"FBW Mode", None))
        self.ManualButton.setText(QCoreApplication.translate("Form", u"Manual Mode", None))
        self.ManualButton.setDescription("")
        self.ConnectionStartButton.setText(QCoreApplication.translate("Form", u"Start Connection", None))
        self.ConnectionStartButton.setDescription(QCoreApplication.translate("Form", u"Inititialise connection with the cube and wait for heartbeat", None))
    # retranslateUi

