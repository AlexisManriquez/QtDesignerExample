# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'index.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QSpacerItem, QStackedWidget, QVBoxLayout,
    QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1146, 781)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(0, 20, 1221, 761))
        self.gridLayout = QGridLayout(self.layoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.icon_only_widget = QWidget(self.layoutWidget)
        self.icon_only_widget.setObjectName(u"icon_only_widget")
        self.icon_only_widget.setMinimumSize(QSize(71, 0))
        self.icon_only_widget.setMaximumSize(QSize(71, 16777215))
        self.icon_only_widget.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(0, 0, 0);\n"
"}\n"
"QPushButton:checked{\n"
"	background-color:white;\n"
"	border-radius:3px;\n"
"}")
        self.verticalLayout_12 = QVBoxLayout(self.icon_only_widget)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(-1, 30, -1, -1)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_2 = QSpacerItem(17, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.label_4 = QLabel(self.icon_only_widget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(40, 40))
        self.label_4.setPixmap(QPixmap(u":/icons/logo.png"))
        self.label_4.setScaledContents(True)

        self.horizontalLayout_2.addWidget(self.label_4)

        self.horizontalSpacer = QSpacerItem(17, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)


        self.verticalLayout_12.addLayout(self.horizontalLayout_2)

        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setSpacing(20)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(-1, 35, -1, -1)
        self.dashboard_1 = QPushButton(self.icon_only_widget)
        self.dashboard_1.setObjectName(u"dashboard_1")
        icon = QIcon()
        icon.addFile(u":/icons/dashboardsmall1.png", QSize(), QIcon.Normal, QIcon.Off)
        icon.addFile(u":/icons/dashboardsmall2.png", QSize(), QIcon.Normal, QIcon.On)
        self.dashboard_1.setIcon(icon)
        self.dashboard_1.setCheckable(True)
        self.dashboard_1.setAutoExclusive(True)

        self.verticalLayout_9.addWidget(self.dashboard_1)

        self.institution_1 = QPushButton(self.icon_only_widget)
        self.institution_1.setObjectName(u"institution_1")
        icon1 = QIcon()
        icon1.addFile(u":/icons/institutionsmall1.png", QSize(), QIcon.Normal, QIcon.Off)
        icon1.addFile(u":/icons/institutionsmall2.png", QSize(), QIcon.Normal, QIcon.On)
        self.institution_1.setIcon(icon1)
        self.institution_1.setCheckable(True)
        self.institution_1.setAutoExclusive(True)

        self.verticalLayout_9.addWidget(self.institution_1)

        self.students_1 = QPushButton(self.icon_only_widget)
        self.students_1.setObjectName(u"students_1")
        icon2 = QIcon()
        icon2.addFile(u":/icons/studentssmall1.png", QSize(), QIcon.Normal, QIcon.Off)
        icon2.addFile(u":/icons/studentssmall2.png", QSize(), QIcon.Normal, QIcon.On)
        self.students_1.setIcon(icon2)
        self.students_1.setCheckable(True)
        self.students_1.setAutoExclusive(True)

        self.verticalLayout_9.addWidget(self.students_1)

        self.teachers_1 = QPushButton(self.icon_only_widget)
        self.teachers_1.setObjectName(u"teachers_1")
        icon3 = QIcon()
        icon3.addFile(u":/icons/teacherssmall1.png", QSize(), QIcon.Normal, QIcon.Off)
        icon3.addFile(u":/icons/teacherssmall2.png", QSize(), QIcon.Normal, QIcon.On)
        self.teachers_1.setIcon(icon3)
        self.teachers_1.setCheckable(True)
        self.teachers_1.setAutoExclusive(True)

        self.verticalLayout_9.addWidget(self.teachers_1)

        self.finances_1 = QPushButton(self.icon_only_widget)
        self.finances_1.setObjectName(u"finances_1")
        icon4 = QIcon()
        icon4.addFile(u":/icons/financessmall1.png", QSize(), QIcon.Normal, QIcon.Off)
        icon4.addFile(u":/icons/financessmall2.png", QSize(), QIcon.Normal, QIcon.On)
        self.finances_1.setIcon(icon4)
        self.finances_1.setCheckable(True)
        self.finances_1.setAutoExclusive(True)

        self.verticalLayout_9.addWidget(self.finances_1)


        self.verticalLayout_12.addLayout(self.verticalLayout_9)

        self.verticalSpacer_2 = QSpacerItem(20, 456, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_12.addItem(self.verticalSpacer_2)

        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setSpacing(20)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.settings_1 = QPushButton(self.icon_only_widget)
        self.settings_1.setObjectName(u"settings_1")
        icon5 = QIcon()
        icon5.addFile(u":/icons/settingssmall1.png", QSize(), QIcon.Normal, QIcon.Off)
        icon5.addFile(u":/icons/settingssmall2.png", QSize(), QIcon.Normal, QIcon.On)
        self.settings_1.setIcon(icon5)
        self.settings_1.setCheckable(True)
        self.settings_1.setAutoExclusive(True)

        self.verticalLayout_10.addWidget(self.settings_1)

        self.signout_1 = QPushButton(self.icon_only_widget)
        self.signout_1.setObjectName(u"signout_1")
        icon6 = QIcon()
        icon6.addFile(u":/icons/signoutsmall1.png", QSize(), QIcon.Normal, QIcon.Off)
        icon6.addFile(u":/icons/signoutsmall2.png", QSize(), QIcon.Normal, QIcon.On)
        self.signout_1.setIcon(icon6)
        self.signout_1.setCheckable(True)
        self.signout_1.setAutoExclusive(True)

        self.verticalLayout_10.addWidget(self.signout_1)


        self.verticalLayout_12.addLayout(self.verticalLayout_10)


        self.gridLayout.addWidget(self.icon_only_widget, 0, 0, 1, 1)

        self.icon_text_widget = QWidget(self.layoutWidget)
        self.icon_text_widget.setObjectName(u"icon_text_widget")
        self.icon_text_widget.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(0, 0, 0);\n"
"	color:white;\n"
"}\n"
"QPushButton{\n"
"	height:30px;\n"
"	border:none;\n"
"}")
        self.verticalLayout_11 = QVBoxLayout(self.icon_text_widget)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(-1, 30, -1, -1)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(20)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(20, -1, -1, -1)
        self.label_2 = QLabel(self.icon_text_widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(40, 40))
        self.label_2.setPixmap(QPixmap(u":/icons/logo.png"))
        self.label_2.setScaledContents(True)

        self.horizontalLayout.addWidget(self.label_2)

        self.label_3 = QLabel(self.icon_text_widget)
        self.label_3.setObjectName(u"label_3")
        font = QFont()
        font.setPointSize(20)
        self.label_3.setFont(font)

        self.horizontalLayout.addWidget(self.label_3)


        self.verticalLayout_11.addLayout(self.horizontalLayout)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setSpacing(15)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(-1, 35, -1, -1)
        self.dashboard_2 = QPushButton(self.icon_text_widget)
        self.dashboard_2.setObjectName(u"dashboard_2")
        self.dashboard_2.setStyleSheet(u"QPushButton{\n"
"	padding-left:-60px\n"
"}\n"
"QPushButton:checked{\n"
"	background-color:white;\n"
"	border-radius:3px;\n"
"}")
        icon7 = QIcon()
        icon7.addFile(u":/icons/dashboard2.png", QSize(), QIcon.Normal, QIcon.Off)
        icon7.addFile(u":/icons/dashboard1.png", QSize(), QIcon.Normal, QIcon.On)
        self.dashboard_2.setIcon(icon7)
        self.dashboard_2.setIconSize(QSize(100, 60))
        self.dashboard_2.setCheckable(True)

        self.verticalLayout_7.addWidget(self.dashboard_2)

        self.institution_2 = QPushButton(self.icon_text_widget)
        self.institution_2.setObjectName(u"institution_2")
        self.institution_2.setStyleSheet(u"QPushButton{\n"
"	padding-left:-65px\n"
"}\n"
"QPushButton:checked{\n"
"	background-color:white;\n"
"	border-radius:3px;\n"
"}")
        icon8 = QIcon()
        icon8.addFile(u":/icons/institution2.png", QSize(), QIcon.Normal, QIcon.Off)
        icon8.addFile(u":/icons/institution1.png", QSize(), QIcon.Normal, QIcon.On)
        self.institution_2.setIcon(icon8)
        self.institution_2.setIconSize(QSize(100, 60))
        self.institution_2.setCheckable(True)

        self.verticalLayout_7.addWidget(self.institution_2)

        self.students = QFrame(self.icon_text_widget)
        self.students.setObjectName(u"students")
        self.students.setFrameShape(QFrame.StyledPanel)
        self.students.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.students)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.students_2 = QPushButton(self.students)
        self.students_2.setObjectName(u"students_2")
        self.students_2.setStyleSheet(u"QPushButton{\n"
"	padding-left:-20px\n"
"}\n"
"QPushButton:hover{\n"
"	color:#12b298;\n"
"}")
        icon9 = QIcon()
        icon9.addFile(u":/icons/students3.png", QSize(), QIcon.Normal, QIcon.Off)
        icon9.addFile(u":/icons/students4.png", QSize(), QIcon.Normal, QIcon.On)
        self.students_2.setIcon(icon9)
        self.students_2.setIconSize(QSize(100, 60))
        self.students_2.setCheckable(True)

        self.verticalLayout_4.addWidget(self.students_2)

        self.students_dropdown = QFrame(self.students)
        self.students_dropdown.setObjectName(u"students_dropdown")
        self.students_dropdown.setFrameShape(QFrame.StyledPanel)
        self.students_dropdown.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.students_dropdown)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.student_info = QPushButton(self.students_dropdown)
        self.student_info.setObjectName(u"student_info")
        self.student_info.setStyleSheet(u"QPushButton{\n"
"	padding-left:-11px\n"
"}\n"
"QPushButton:hover{\n"
"	color:#12b298;\n"
"}")
        self.student_info.setCheckable(True)

        self.verticalLayout.addWidget(self.student_info)

        self.student_payments = QPushButton(self.students_dropdown)
        self.student_payments.setObjectName(u"student_payments")
        self.student_payments.setStyleSheet(u"QPushButton{\n"
"	padding-left:-16px\n"
"}\n"
"QPushButton:hover{\n"
"	color:#12b298;\n"
"}")
        self.student_payments.setCheckable(True)

        self.verticalLayout.addWidget(self.student_payments)

        self.student_transactions = QPushButton(self.students_dropdown)
        self.student_transactions.setObjectName(u"student_transactions")
        self.student_transactions.setStyleSheet(u"QPushButton{\n"
"	padding-left:-11px\n"
"}\n"
"QPushButton:hover{\n"
"	color:#12b298;\n"
"}")
        self.student_transactions.setCheckable(True)

        self.verticalLayout.addWidget(self.student_transactions)


        self.verticalLayout_4.addWidget(self.students_dropdown)


        self.verticalLayout_7.addWidget(self.students)

        self.teachers = QFrame(self.icon_text_widget)
        self.teachers.setObjectName(u"teachers")
        self.teachers.setFrameShape(QFrame.StyledPanel)
        self.teachers.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.teachers)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.teachers_2 = QPushButton(self.teachers)
        self.teachers_2.setObjectName(u"teachers_2")
        icon10 = QIcon()
        icon10.addFile(u":/icons/teachers3.png", QSize(), QIcon.Normal, QIcon.Off)
        icon10.addFile(u":/icons/teachers4.png", QSize(), QIcon.Normal, QIcon.On)
        self.teachers_2.setIcon(icon10)
        self.teachers_2.setIconSize(QSize(100, 60))
        self.teachers_2.setCheckable(True)

        self.verticalLayout_5.addWidget(self.teachers_2)

        self.teachers_dropdown = QFrame(self.teachers)
        self.teachers_dropdown.setObjectName(u"teachers_dropdown")
        self.teachers_dropdown.setFrameShape(QFrame.StyledPanel)
        self.teachers_dropdown.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.teachers_dropdown)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.teacher_info = QPushButton(self.teachers_dropdown)
        self.teacher_info.setObjectName(u"teacher_info")
        self.teacher_info.setStyleSheet(u"QPushButton{\n"
"	padding-left:-10px\n"
"}\n"
"QPushButton:hover{\n"
"	color:#12b298;\n"
"}")
        self.teacher_info.setCheckable(True)

        self.verticalLayout_2.addWidget(self.teacher_info)

        self.teacher_salaries = QPushButton(self.teachers_dropdown)
        self.teacher_salaries.setObjectName(u"teacher_salaries")
        self.teacher_salaries.setStyleSheet(u"QPushButton{\n"
"	padding-left:-10px\n"
"}\n"
"QPushButton:hover{\n"
"	color:#12b298;\n"
"}")
        self.teacher_salaries.setCheckable(True)

        self.verticalLayout_2.addWidget(self.teacher_salaries)

        self.teacher_transactions = QPushButton(self.teachers_dropdown)
        self.teacher_transactions.setObjectName(u"teacher_transactions")
        self.teacher_transactions.setStyleSheet(u"QPushButton{\n"
"	padding-left:-10px\n"
"}\n"
"QPushButton:hover{\n"
"	color:#12b298;\n"
"}")
        self.teacher_transactions.setCheckable(True)

        self.verticalLayout_2.addWidget(self.teacher_transactions)


        self.verticalLayout_5.addWidget(self.teachers_dropdown)


        self.verticalLayout_7.addWidget(self.teachers)

        self.finances = QFrame(self.icon_text_widget)
        self.finances.setObjectName(u"finances")
        self.finances.setFrameShape(QFrame.StyledPanel)
        self.finances.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.finances)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.finances_2 = QPushButton(self.finances)
        self.finances_2.setObjectName(u"finances_2")
        icon11 = QIcon()
        icon11.addFile(u":/icons/finances3.png", QSize(), QIcon.Normal, QIcon.Off)
        icon11.addFile(u":/icons/finances4.png", QSize(), QIcon.Normal, QIcon.On)
        self.finances_2.setIcon(icon11)
        self.finances_2.setIconSize(QSize(100, 60))
        self.finances_2.setCheckable(True)

        self.verticalLayout_6.addWidget(self.finances_2)

        self.finacnes_dropdown = QFrame(self.finances)
        self.finacnes_dropdown.setObjectName(u"finacnes_dropdown")
        self.finacnes_dropdown.setFrameShape(QFrame.StyledPanel)
        self.finacnes_dropdown.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.finacnes_dropdown)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.budgets = QPushButton(self.finacnes_dropdown)
        self.budgets.setObjectName(u"budgets")
        self.budgets.setStyleSheet(u"QPushButton{\n"
"	padding-left:-10px\n"
"}\n"
"QPushButton:hover{\n"
"	color:#12b298;\n"
"}")
        self.budgets.setCheckable(True)

        self.verticalLayout_3.addWidget(self.budgets)

        self.expenses = QPushButton(self.finacnes_dropdown)
        self.expenses.setObjectName(u"expenses")
        self.expenses.setStyleSheet(u"QPushButton{\n"
"	padding-left:-10px\n"
"}\n"
"QPushButton:hover{\n"
"	color:#12b298;\n"
"}")
        self.expenses.setCheckable(True)

        self.verticalLayout_3.addWidget(self.expenses)

        self.business_overview = QPushButton(self.finacnes_dropdown)
        self.business_overview.setObjectName(u"business_overview")
        self.business_overview.setStyleSheet(u"QPushButton{\n"
"	padding-left:-10px\n"
"}\n"
"QPushButton:hover{\n"
"	color:#12b298;\n"
"}")
        self.business_overview.setCheckable(True)

        self.verticalLayout_3.addWidget(self.business_overview)


        self.verticalLayout_6.addWidget(self.finacnes_dropdown)


        self.verticalLayout_7.addWidget(self.finances)


        self.verticalLayout_11.addLayout(self.verticalLayout_7)

        self.verticalSpacer = QSpacerItem(20, 62, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_11.addItem(self.verticalSpacer)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setSpacing(20)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.settings_2 = QPushButton(self.icon_text_widget)
        self.settings_2.setObjectName(u"settings_2")
        self.settings_2.setStyleSheet(u"QPushButton{\n"
"	padding-left:-65px\n"
"}\n"
"QPushButton:checked{\n"
"	background-color:white;\n"
"	border-radius:3px;\n"
"}")
        icon12 = QIcon()
        icon12.addFile(u":/icons/settings2.png", QSize(), QIcon.Normal, QIcon.Off)
        icon12.addFile(u":/icons/settings1.png", QSize(), QIcon.Normal, QIcon.On)
        self.settings_2.setIcon(icon12)
        self.settings_2.setIconSize(QSize(100, 60))
        self.settings_2.setCheckable(True)

        self.verticalLayout_8.addWidget(self.settings_2)

        self.signout_2 = QPushButton(self.icon_text_widget)
        self.signout_2.setObjectName(u"signout_2")
        self.signout_2.setStyleSheet(u"QPushButton{\n"
"	padding-left:-65px\n"
"}\n"
"QPushButton:checked{\n"
"	background-color:white;\n"
"	border-radius:3px;\n"
"}")
        icon13 = QIcon()
        icon13.addFile(u":/icons/signout2.png", QSize(), QIcon.Normal, QIcon.Off)
        icon13.addFile(u":/icons/signout1.png", QSize(), QIcon.Normal, QIcon.On)
        self.signout_2.setIcon(icon13)
        self.signout_2.setIconSize(QSize(100, 60))
        self.signout_2.setCheckable(True)

        self.verticalLayout_8.addWidget(self.signout_2)


        self.verticalLayout_11.addLayout(self.verticalLayout_8)


        self.gridLayout.addWidget(self.icon_text_widget, 0, 1, 1, 1)

        self.verticalLayout_14 = QVBoxLayout()
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.header_widget = QWidget(self.layoutWidget)
        self.header_widget.setObjectName(u"header_widget")
        self.horizontalLayout_5 = QHBoxLayout(self.header_widget)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.pushButton = QPushButton(self.header_widget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setStyleSheet(u"border:none;")
        icon14 = QIcon()
        icon14.addFile(u":/icons/menu.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon14)
        self.pushButton.setIconSize(QSize(29, 35))
        self.pushButton.setCheckable(True)

        self.horizontalLayout_4.addWidget(self.pushButton)

        self.verticalLayout_13 = QVBoxLayout()
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(-1, 25, -1, 25)
        self.label = QLabel(self.header_widget)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setPointSize(15)
        font1.setBold(True)
        self.label.setFont(font1)

        self.verticalLayout_13.addWidget(self.label)

        self.label_5 = QLabel(self.header_widget)
        self.label_5.setObjectName(u"label_5")
        font2 = QFont()
        font2.setPointSize(10)
        self.label_5.setFont(font2)
        self.label_5.setStyleSheet(u"color: rgb(93, 93, 93);")

        self.verticalLayout_13.addWidget(self.label_5)


        self.horizontalLayout_4.addLayout(self.verticalLayout_13)


        self.horizontalLayout_5.addLayout(self.horizontalLayout_4)

        self.horizontalSpacer_3 = QSpacerItem(367, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_3)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, -1, 25, -1)
        self.lineEdit = QLineEdit(self.header_widget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMaximumSize(QSize(16777215, 31))
        self.lineEdit.setStyleSheet(u"QLineEdit{\n"
"pad-left:20px;\n"
"border:1px solid gray;\n"
"border-radius:10px;\n"
"}")

        self.horizontalLayout_3.addWidget(self.lineEdit)

        self.label_6 = QLabel(self.header_widget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMaximumSize(QSize(40, 40))
        self.label_6.setPixmap(QPixmap(u":/icons/profile.png"))
        self.label_6.setScaledContents(True)

        self.horizontalLayout_3.addWidget(self.label_6)


        self.horizontalLayout_5.addLayout(self.horizontalLayout_3)


        self.verticalLayout_14.addWidget(self.header_widget)

        self.main_screen_widget = QWidget(self.layoutWidget)
        self.main_screen_widget.setObjectName(u"main_screen_widget")
        self.main_screen_widget.setMinimumSize(QSize(920, 741))
        self.main_screen_widget.setMaximumSize(QSize(920, 741))
        self.main_screen_widget.setStyleSheet(u"")
        self.stackedWidget = QStackedWidget(self.main_screen_widget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(9, 10, 901, 711))
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.label_7 = QLabel(self.page)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(270, 170, 171, 221))
        font3 = QFont()
        font3.setPointSize(25)
        self.label_7.setFont(font3)
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.label_8 = QLabel(self.page_2)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(178, 125, 141, 161))
        self.label_8.setFont(font3)
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.label_9 = QLabel(self.page_3)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(100, 260, 141, 161))
        self.label_9.setFont(font3)
        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.label_10 = QLabel(self.page_4)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(200, 210, 141, 161))
        self.label_10.setFont(font3)
        self.stackedWidget.addWidget(self.page_4)
        self.page_5 = QWidget()
        self.page_5.setObjectName(u"page_5")
        self.label_11 = QLabel(self.page_5)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(240, 220, 141, 161))
        self.label_11.setFont(font3)
        self.stackedWidget.addWidget(self.page_5)
        self.page_6 = QWidget()
        self.page_6.setObjectName(u"page_6")
        self.label_12 = QLabel(self.page_6)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(50, 260, 141, 161))
        self.label_12.setFont(font3)
        self.stackedWidget.addWidget(self.page_6)
        self.page_7 = QWidget()
        self.page_7.setObjectName(u"page_7")
        self.label_13 = QLabel(self.page_7)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(100, 300, 141, 161))
        self.label_13.setFont(font3)
        self.stackedWidget.addWidget(self.page_7)
        self.page_8 = QWidget()
        self.page_8.setObjectName(u"page_8")
        self.label_14 = QLabel(self.page_8)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(60, 220, 141, 161))
        self.label_14.setFont(font3)
        self.stackedWidget.addWidget(self.page_8)
        self.page_9 = QWidget()
        self.page_9.setObjectName(u"page_9")
        self.label_15 = QLabel(self.page_9)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(100, 270, 141, 161))
        self.label_15.setFont(font3)
        self.stackedWidget.addWidget(self.page_9)
        self.page_10 = QWidget()
        self.page_10.setObjectName(u"page_10")
        self.label_16 = QLabel(self.page_10)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(100, 260, 141, 161))
        self.label_16.setFont(font3)
        self.stackedWidget.addWidget(self.page_10)
        self.page_11 = QWidget()
        self.page_11.setObjectName(u"page_11")
        self.label_17 = QLabel(self.page_11)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(90, 250, 331, 161))
        self.label_17.setFont(font3)
        self.stackedWidget.addWidget(self.page_11)
        self.page_12 = QWidget()
        self.page_12.setObjectName(u"page_12")
        self.label_18 = QLabel(self.page_12)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(90, 230, 141, 161))
        self.label_18.setFont(font3)
        self.stackedWidget.addWidget(self.page_12)

        self.verticalLayout_14.addWidget(self.main_screen_widget)


        self.gridLayout.addLayout(self.verticalLayout_14, 0, 2, 1, 1)

        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(0, 0, 1241, 21))
        self.widget.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.widget1 = QWidget(self.widget)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setGeometry(QRect(10, 0, 101, 21))
        self.horizontalLayout_6 = QHBoxLayout(self.widget1)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.file_menu = QPushButton(self.widget1)
        self.file_menu.setObjectName(u"file_menu")
        self.file_menu.setStyleSheet(u"QPushButton{\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:checked{\n"
"	background-color:white;\n"
"	color: black;\n"
"	border-radius:3px;\n"
"}")
        self.file_menu.setCheckable(False)

        self.horizontalLayout_6.addWidget(self.file_menu)

        self.view_menu = QPushButton(self.widget1)
        self.view_menu.setObjectName(u"view_menu")
        self.view_menu.setStyleSheet(u"QPushButton{\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:checked{\n"
"	background-color:white;\n"
"	color: black;\n"
"	border-radius:3px;\n"
"}")
        self.view_menu.setCheckable(False)

        self.horizontalLayout_6.addWidget(self.view_menu)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.students_2.toggled.connect(self.students_dropdown.setHidden)
        self.teachers_2.toggled.connect(self.teachers_dropdown.setHidden)
        self.finances_2.toggled.connect(self.finacnes_dropdown.setHidden)
        self.dashboard_2.toggled.connect(self.dashboard_1.setChecked)
        self.institution_2.toggled.connect(self.institution_1.setChecked)
        self.students_2.toggled.connect(self.students_1.setChecked)
        self.teachers_2.toggled.connect(self.teachers_1.setChecked)
        self.finances_2.toggled.connect(self.finances_1.setChecked)
        self.settings_2.toggled.connect(self.settings_1.setChecked)
        self.signout_2.toggled.connect(self.signout_1.setChecked)
        self.signout_1.toggled.connect(self.signout_1.close)
        self.signout_2.toggled.connect(self.signout_2.close)
        self.pushButton.toggled.connect(self.icon_text_widget.setHidden)
        self.pushButton.toggled.connect(self.icon_only_widget.setVisible)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_4.setText("")
        self.dashboard_1.setText("")
        self.institution_1.setText("")
        self.students_1.setText("")
        self.teachers_1.setText("")
        self.finances_1.setText("")
        self.settings_1.setText("")
        self.signout_1.setText("")
        self.label_2.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"TPSDD", None))
        self.dashboard_2.setText("")
        self.institution_2.setText("")
        self.students_2.setText("")
        self.student_info.setText(QCoreApplication.translate("MainWindow", u"Student Information", None))
        self.student_payments.setText(QCoreApplication.translate("MainWindow", u"Student Payments", None))
        self.student_transactions.setText(QCoreApplication.translate("MainWindow", u"Student Transactions", None))
        self.teachers_2.setText("")
        self.teacher_info.setText(QCoreApplication.translate("MainWindow", u"Teacher Information", None))
        self.teacher_salaries.setText(QCoreApplication.translate("MainWindow", u"Teacher Salaries", None))
        self.teacher_transactions.setText(QCoreApplication.translate("MainWindow", u"Teacher Transactions", None))
        self.finances_2.setText("")
        self.budgets.setText(QCoreApplication.translate("MainWindow", u"Budgets", None))
        self.expenses.setText(QCoreApplication.translate("MainWindow", u"Expenses", None))
        self.business_overview.setText(QCoreApplication.translate("MainWindow", u"Business Overview", None))
        self.settings_2.setText("")
        self.signout_2.setText("")
        self.pushButton.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"Hello, Mark", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Welcome to your page", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search Here...", None))
        self.label_6.setText("")
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Dashboard", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Institution", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Student Info", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Student Payments", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Student Transactions", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Teacher Info", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Teacher Salaries", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Teacher Transactions", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Budgets", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Expenses", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Business Overview", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.file_menu.setText(QCoreApplication.translate("MainWindow", u"File", None))
        self.view_menu.setText(QCoreApplication.translate("MainWindow", u"View", None))
    # retranslateUi

