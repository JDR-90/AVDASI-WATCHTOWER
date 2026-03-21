# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'UIGate3.ui'
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
        Form.resize(900, 586)
        Form.setMaximumSize(QSize(900, 16777215))
        Form.setStyleSheet(u"")
        self.layoutWidget = QWidget(Form)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(4, 16, 891, 562))
        self.verticalLayout_3 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_6 = QSpacerItem(230, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_6)

        self.ControlsLabel = QLabel(self.layoutWidget)
        self.ControlsLabel.setObjectName(u"ControlsLabel")
        font = QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setItalic(True)
        font.setUnderline(True)
        self.ControlsLabel.setFont(font)
        self.ControlsLabel.setMouseTracking(False)

        self.horizontalLayout.addWidget(self.ControlsLabel)

        self.horizontalSpacer_2 = QSpacerItem(123, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.OutputLabel = QLabel(self.layoutWidget)
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
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalSpacer_8 = QSpacerItem(163, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_8)

        self.PortLabel = QLabel(self.layoutWidget)
        self.PortLabel.setObjectName(u"PortLabel")
        font1 = QFont()
        font1.setPointSize(11)
        font1.setBold(False)
        font1.setItalic(True)
        font1.setUnderline(True)
        self.PortLabel.setFont(font1)

        self.horizontalLayout_5.addWidget(self.PortLabel)

        self.StarLabel = QLabel(self.layoutWidget)
        self.StarLabel.setObjectName(u"StarLabel")
        font2 = QFont()
        font2.setPointSize(11)
        font2.setUnderline(True)
        self.StarLabel.setFont(font2)

        self.horizontalLayout_5.addWidget(self.StarLabel)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.Flap = QHBoxLayout()
        self.Flap.setObjectName(u"Flap")
        self.FlapLabel = QLabel(self.layoutWidget)
        self.FlapLabel.setObjectName(u"FlapLabel")
        font3 = QFont()
        font3.setPointSize(11)
        self.FlapLabel.setFont(font3)

        self.Flap.addWidget(self.FlapLabel)

        self.horizontalSpacer = QSpacerItem(14, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.Flap.addItem(self.horizontalSpacer)

        self.FlapEntryPort = QLineEdit(self.layoutWidget)
        self.FlapEntryPort.setObjectName(u"FlapEntryPort")

        self.Flap.addWidget(self.FlapEntryPort)

        self.FlapButtonPort = QPushButton(self.layoutWidget)
        self.FlapButtonPort.setObjectName(u"FlapButtonPort")
        self.FlapButtonPort.setStyleSheet(u"QPushButton {\n"
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

        self.Flap.addWidget(self.FlapButtonPort)

        self.FlapEntryStar = QLineEdit(self.layoutWidget)
        self.FlapEntryStar.setObjectName(u"FlapEntryStar")
        self.FlapEntryStar.setStyleSheet(u"")

        self.Flap.addWidget(self.FlapEntryStar)

        self.FlapButtonStar = QPushButton(self.layoutWidget)
        self.FlapButtonStar.setObjectName(u"FlapButtonStar")
        self.FlapButtonStar.setStyleSheet(u"QPushButton {\n"
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

        self.Flap.addWidget(self.FlapButtonStar)


        self.verticalLayout.addLayout(self.Flap)

        self.Aileron = QHBoxLayout()
        self.Aileron.setObjectName(u"Aileron")
        self.AileronLabel = QLabel(self.layoutWidget)
        self.AileronLabel.setObjectName(u"AileronLabel")
        self.AileronLabel.setFont(font3)

        self.Aileron.addWidget(self.AileronLabel)

        self.AileronEntryPort = QLineEdit(self.layoutWidget)
        self.AileronEntryPort.setObjectName(u"AileronEntryPort")

        self.Aileron.addWidget(self.AileronEntryPort)

        self.AileronButtonPort = QPushButton(self.layoutWidget)
        self.AileronButtonPort.setObjectName(u"AileronButtonPort")
        self.AileronButtonPort.setStyleSheet(u"QPushButton {\n"
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

        self.Aileron.addWidget(self.AileronButtonPort)

        self.AileronEntryStar = QLineEdit(self.layoutWidget)
        self.AileronEntryStar.setObjectName(u"AileronEntryStar")

        self.Aileron.addWidget(self.AileronEntryStar)

        self.AileronButtonStar = QPushButton(self.layoutWidget)
        self.AileronButtonStar.setObjectName(u"AileronButtonStar")
        self.AileronButtonStar.setStyleSheet(u"QPushButton {\n"
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

        self.Aileron.addWidget(self.AileronButtonStar)


        self.verticalLayout.addLayout(self.Aileron)

        self.Rudder = QHBoxLayout()
        self.Rudder.setObjectName(u"Rudder")
        self.RudderLabel = QLabel(self.layoutWidget)
        self.RudderLabel.setObjectName(u"RudderLabel")
        self.RudderLabel.setFont(font3)

        self.Rudder.addWidget(self.RudderLabel)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.Rudder.addItem(self.horizontalSpacer_4)

        self.RudderEntry = QLineEdit(self.layoutWidget)
        self.RudderEntry.setObjectName(u"RudderEntry")

        self.Rudder.addWidget(self.RudderEntry)

        self.RudderButton = QPushButton(self.layoutWidget)
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
        self.ElevatorLabel = QLabel(self.layoutWidget)
        self.ElevatorLabel.setObjectName(u"ElevatorLabel")
        self.ElevatorLabel.setFont(font3)

        self.Elevator.addWidget(self.ElevatorLabel)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.Elevator.addItem(self.horizontalSpacer_5)

        self.ElevatorEntry = QLineEdit(self.layoutWidget)
        self.ElevatorEntry.setObjectName(u"ElevatorEntry")

        self.Elevator.addWidget(self.ElevatorEntry)

        self.ElevatorButton = QPushButton(self.layoutWidget)
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

        self.verticalSpacer_2 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.AutoPortLabel = QLabel(self.layoutWidget)
        self.AutoPortLabel.setObjectName(u"AutoPortLabel")
        self.AutoPortLabel.setFont(font3)

        self.horizontalLayout_4.addWidget(self.AutoPortLabel)

        self.PortTakeOff = QCommandLinkButton(self.layoutWidget)
        self.PortTakeOff.setObjectName(u"PortTakeOff")
        self.PortTakeOff.setMaximumSize(QSize(100, 16777215))
        self.PortTakeOff.setStyleSheet(u"QCommandLinkButton {\n"
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
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.GoUp))
        self.PortTakeOff.setIcon(icon)

        self.horizontalLayout_4.addWidget(self.PortTakeOff)

        self.PortCruise = QCommandLinkButton(self.layoutWidget)
        self.PortCruise.setObjectName(u"PortCruise")
        self.PortCruise.setMaximumSize(QSize(100, 16777215))
        self.PortCruise.setStyleSheet(u"QCommandLinkButton {\n"
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
        icon1 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.GoNext))
        self.PortCruise.setIcon(icon1)

        self.horizontalLayout_4.addWidget(self.PortCruise)

        self.PortLanding = QCommandLinkButton(self.layoutWidget)
        self.PortLanding.setObjectName(u"PortLanding")
        self.PortLanding.setMaximumSize(QSize(100, 16777215))
        self.PortLanding.setStyleSheet(u"QCommandLinkButton {\n"
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
        icon2 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.GoDown))
        self.PortLanding.setIcon(icon2)

        self.horizontalLayout_4.addWidget(self.PortLanding)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.AutoStarboardLabel = QLabel(self.layoutWidget)
        self.AutoStarboardLabel.setObjectName(u"AutoStarboardLabel")
        self.AutoStarboardLabel.setFont(font3)

        self.horizontalLayout_6.addWidget(self.AutoStarboardLabel)

        self.StarTakeOff = QCommandLinkButton(self.layoutWidget)
        self.StarTakeOff.setObjectName(u"StarTakeOff")
        self.StarTakeOff.setMaximumSize(QSize(100, 16777215))
        self.StarTakeOff.setStyleSheet(u"QCommandLinkButton {\n"
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
        self.StarTakeOff.setIcon(icon)

        self.horizontalLayout_6.addWidget(self.StarTakeOff)

        self.StarCruise = QCommandLinkButton(self.layoutWidget)
        self.StarCruise.setObjectName(u"StarCruise")
        self.StarCruise.setMaximumSize(QSize(100, 16777215))
        self.StarCruise.setStyleSheet(u"QCommandLinkButton {\n"
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
        self.StarCruise.setIcon(icon1)

        self.horizontalLayout_6.addWidget(self.StarCruise)

        self.StarLanding = QCommandLinkButton(self.layoutWidget)
        self.StarLanding.setObjectName(u"StarLanding")
        self.StarLanding.setMaximumSize(QSize(100, 16777215))
        self.StarLanding.setStyleSheet(u"QCommandLinkButton {\n"
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
        self.StarLanding.setIcon(icon2)

        self.horizontalLayout_6.addWidget(self.StarLanding)


        self.verticalLayout.addLayout(self.horizontalLayout_6)

        self.verticalSpacer = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalSpacer_9 = QSpacerItem(240, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_9)

        self.UAVLabel = QLabel(self.layoutWidget)
        self.UAVLabel.setObjectName(u"UAVLabel")
        self.UAVLabel.setFont(font)

        self.horizontalLayout_13.addWidget(self.UAVLabel)


        self.verticalLayout_4.addLayout(self.horizontalLayout_13)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.ModesLabel = QLabel(self.layoutWidget)
        self.ModesLabel.setObjectName(u"ModesLabel")
        self.ModesLabel.setFont(font3)

        self.horizontalLayout_14.addWidget(self.ModesLabel)

        self.FBWBButton = QCommandLinkButton(self.layoutWidget)
        self.FBWBButton.setObjectName(u"FBWBButton")
        self.FBWBButton.setMaximumSize(QSize(183, 16777215))
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

        self.horizontalLayout_14.addWidget(self.FBWBButton)

        self.ManualButton = QCommandLinkButton(self.layoutWidget)
        self.ManualButton.setObjectName(u"ManualButton")
        self.ManualButton.setMaximumSize(QSize(182, 16777215))
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

        self.horizontalLayout_14.addWidget(self.ManualButton)


        self.verticalLayout_5.addLayout(self.horizontalLayout_14)


        self.horizontalLayout_10.addLayout(self.verticalLayout_5)


        self.verticalLayout_4.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.RCLabel = QLabel(self.layoutWidget)
        self.RCLabel.setObjectName(u"RCLabel")
        self.RCLabel.setFont(font3)

        self.horizontalLayout_7.addWidget(self.RCLabel)

        self.OverrideStartButton = QCommandLinkButton(self.layoutWidget)
        self.OverrideStartButton.setObjectName(u"OverrideStartButton")
        self.OverrideStartButton.setMaximumSize(QSize(184, 16777215))
        self.OverrideStartButton.setStyleSheet(u"QCommandLinkButton {\n"
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

        self.horizontalLayout_7.addWidget(self.OverrideStartButton)

        self.OverrideStopButton = QCommandLinkButton(self.layoutWidget)
        self.OverrideStopButton.setObjectName(u"OverrideStopButton")
        self.OverrideStopButton.setMaximumSize(QSize(184, 16777215))
        self.OverrideStopButton.setStyleSheet(u"QCommandLinkButton {\n"
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

        self.horizontalLayout_7.addWidget(self.OverrideStopButton)


        self.verticalLayout_4.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.KitsLabel = QLabel(self.layoutWidget)
        self.KitsLabel.setObjectName(u"KitsLabel")
        self.KitsLabel.setFont(font3)

        self.horizontalLayout_9.addWidget(self.KitsLabel)

        self.Kit7Connect = QCommandLinkButton(self.layoutWidget)
        self.Kit7Connect.setObjectName(u"Kit7Connect")
        self.Kit7Connect.setMaximumSize(QSize(121, 16777215))
        self.Kit7Connect.setStyleSheet(u"QCommandLinkButton {\n"
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
        icon3 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.NetworkWireless))
        self.Kit7Connect.setIcon(icon3)

        self.horizontalLayout_9.addWidget(self.Kit7Connect)

        self.Kit8Connect = QCommandLinkButton(self.layoutWidget)
        self.Kit8Connect.setObjectName(u"Kit8Connect")
        self.Kit8Connect.setMaximumSize(QSize(121, 16777215))
        self.Kit8Connect.setStyleSheet(u"QCommandLinkButton {\n"
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
        self.Kit8Connect.setIcon(icon3)

        self.horizontalLayout_9.addWidget(self.Kit8Connect)

        self.Kit9Connect = QCommandLinkButton(self.layoutWidget)
        self.Kit9Connect.setObjectName(u"Kit9Connect")
        self.Kit9Connect.setMaximumSize(QSize(121, 16777215))
        self.Kit9Connect.setStyleSheet(u"QCommandLinkButton {\n"
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
        self.Kit9Connect.setIcon(icon3)

        self.horizontalLayout_9.addWidget(self.Kit9Connect)


        self.verticalLayout_4.addLayout(self.horizontalLayout_9)


        self.horizontalLayout_8.addLayout(self.verticalLayout_4)


        self.verticalLayout.addLayout(self.horizontalLayout_8)


        self.horizontalLayout_3.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.OutputBox = QTextEdit(self.layoutWidget)
        self.OutputBox.setObjectName(u"OutputBox")
        self.OutputBox.setMaximumSize(QSize(400, 16777215))
        self.OutputBox.setStyleSheet(u"QTextEdit {\n"
"    background-color: #ececec;\n"
"    border: 2px solid #4b4b4b;\n"
"    border-radius: 6px;\n"
"    padding: 6px;\n"
"    color: #2c2c2c;\n"
"}")

        self.horizontalLayout_2.addWidget(self.OutputBox)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)


        self.horizontalLayout_3.addLayout(self.verticalLayout_2)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.ControlsLabel.setText(QCoreApplication.translate("Form", u"Control Surfaces", None))
        self.OutputLabel.setText(QCoreApplication.translate("Form", u"Output & Command Log", None))
        self.PortLabel.setText(QCoreApplication.translate("Form", u"Port Wing", None))
        self.StarLabel.setText(QCoreApplication.translate("Form", u"Starboard Wing", None))
        self.FlapLabel.setText(QCoreApplication.translate("Form", u"Flap angle(s):", None))
        self.FlapButtonPort.setText(QCoreApplication.translate("Form", u"Send CMD", None))
        self.FlapButtonStar.setText(QCoreApplication.translate("Form", u"Send CMD", None))
        self.AileronLabel.setText(QCoreApplication.translate("Form", u"Aileron angle(s):", None))
        self.AileronButtonPort.setText(QCoreApplication.translate("Form", u"Send CMD", None))
        self.AileronButtonStar.setText(QCoreApplication.translate("Form", u"Send CMD", None))
        self.RudderLabel.setText(QCoreApplication.translate("Form", u"Rudder angle:", None))
        self.RudderButton.setText(QCoreApplication.translate("Form", u"Send CMD", None))
        self.ElevatorLabel.setText(QCoreApplication.translate("Form", u"Elevator angle:", None))
        self.ElevatorButton.setText(QCoreApplication.translate("Form", u"Send CMD", None))
        self.AutoPortLabel.setText(QCoreApplication.translate("Form", u"Port:", None))
        self.PortTakeOff.setText(QCoreApplication.translate("Form", u"Take off", None))
        self.PortCruise.setText(QCoreApplication.translate("Form", u"Cruise", None))
        self.PortLanding.setText(QCoreApplication.translate("Form", u"Landing", None))
        self.AutoStarboardLabel.setText(QCoreApplication.translate("Form", u"Starboard:", None))
        self.StarTakeOff.setText(QCoreApplication.translate("Form", u"Take off", None))
        self.StarCruise.setText(QCoreApplication.translate("Form", u"Cruise", None))
        self.StarLanding.setText(QCoreApplication.translate("Form", u"Landing", None))
        self.UAVLabel.setText(QCoreApplication.translate("Form", u"UAV Controls", None))
        self.ModesLabel.setText(QCoreApplication.translate("Form", u"Mode Switch:", None))
        self.FBWBButton.setText(QCoreApplication.translate("Form", u"FBW Mode", None))
        self.ManualButton.setText(QCoreApplication.translate("Form", u"Manual Mode", None))
        self.RCLabel.setText(QCoreApplication.translate("Form", u"RC Override:", None))
        self.OverrideStartButton.setText(QCoreApplication.translate("Form", u"RC Override Start", None))
        self.OverrideStopButton.setText(QCoreApplication.translate("Form", u"RC Override Stop", None))
        self.KitsLabel.setText(QCoreApplication.translate("Form", u"Kit Connection:", None))
        self.Kit7Connect.setText(QCoreApplication.translate("Form", u"Kit 7 ", None))
        self.Kit8Connect.setText(QCoreApplication.translate("Form", u"Kit 8", None))
        self.Kit9Connect.setText(QCoreApplication.translate("Form", u"Kit 9", None))
    # retranslateUi

