from PySide6.QtWidgets import QMainWindow, QMenu
from PySide6.QtGui import QAction
from ui_index import Ui_MainWindow

class MySideBar(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("SideBar Menu")
        self.icon_only_widget.setHidden(True)

        self.students_dropdown.setHidden(True)
        self.teachers_dropdown.setHidden(True)
        self.finacnes_dropdown.setHidden(True)

        self.dashboard_1.clicked.connect(self.switch_to_dashboard_page) 
        self.dashboard_2.clicked.connect(self.switch_to_dashboard_page)

        self.institution_1.clicked.connect(self.switch_to_institution_page)
        self.institution_2.clicked.connect(self.switch_to_institution_page)

        self.student_info.clicked.connect(self.switch_to_student_info_page)
        self.student_payments.clicked.connect(self.switch_to_student_payments_page)
        self.student_transactions.clicked.connect(self.switch_to_student_transactions_page)

        self.teacher_info.clicked.connect(self.switch_to_teacher_info_page)
        self.teacher_salaries.clicked.connect(self.switch_to_teacher_salaries_page)
        self.teacher_transactions.clicked.connect(self.switch_to_teacher_transactions_page)

        self.budgets.clicked.connect(self.switch_to_budgets_page)
        self.expenses.clicked.connect(self.switch_to_expenses_page)
        self.business_overview.clicked.connect(self.switch_to_business_overview_page)
        
        self.settings_1.clicked.connect(self.switch_to_settings_page)
        self.settings_2.clicked.connect(self.switch_to_settings_page)

        self.students_1.clicked.connect(self.students_context_menu)
        self.teachers_1.clicked.connect(self.teachers_context_menu)
        self.finances_1.clicked.connect(self.finances_context_menu)
        self.file_menu.clicked.connect(self.file_context_menu)
        self.view_menu.clicked.connect(self.view_context_menu)
    def switch_to_dashboard_page(self):
        self.stackedWidget.setCurrentIndex(0)
    
    def switch_to_institution_page(self):
        self.stackedWidget.setCurrentIndex(1)
    
    def switch_to_student_info_page(self):
        self.stackedWidget.setCurrentIndex(2)
    def switch_to_student_payments_page(self):
        self.stackedWidget.setCurrentIndex(3)
    def switch_to_student_transactions_page(self):
        self.stackedWidget.setCurrentIndex(4)
    def switch_to_teacher_info_page(self):
        self.stackedWidget.setCurrentIndex(5)
    def switch_to_teacher_salaries_page(self):
        self.stackedWidget.setCurrentIndex(6)
    def switch_to_teacher_transactions_page(self):
        self.stackedWidget.setCurrentIndex(7)
    def switch_to_budgets_page(self):
        self.stackedWidget.setCurrentIndex(8)
    def switch_to_expenses_page(self):
        self.stackedWidget.setCurrentIndex(9)
    def switch_to_business_overview_page(self):
        self.stackedWidget.setCurrentIndex(10)
    def switch_to_settings_page(self):
        self.stackedWidget.setCurrentIndex(11)

    def students_context_menu(self):
        self.show_custom_context_menu(self.students_1,["Student Information", "Student Payments", "Student Transactions"])
    
    def teachers_context_menu(self):
        self.show_custom_context_menu(self.teachers_1,["Teacher Information", "Teacher Salaries", "Teacher Transactions"])

    def finances_context_menu(self):
        self.show_custom_context_menu(self.finances_1,["Budgets", "Expenses", "Business Overview"])

    def file_context_menu(self):
        self.show_custom_context_menu(self.file_menu,["Load Ini", "Save", "Exit"])

    def view_context_menu(self):
        self.show_custom_context_menu(self.view_menu,["option 1", "option 2"])
    def show_custom_context_menu(self, button, menu_items):
        menu = QMenu(self)
        menu.setStyleSheet("""QMenu{background-color: #333333; color: white;} 
                           QMenu::item:selected{background-color: #666666;}""")
        
        for item_text in menu_items:
            action = QAction(item_text, self)
            action.triggered.connect(self.handle_menu_item_click)
            menu.addAction(action)
        # if the button is the file button, show the menu below the button
        if button.text() == "File" or button.text() == "View":
            menu.move(button.mapToGlobal(button.rect().bottomLeft()))
        else:
            menu.move(button.mapToGlobal(button.rect().topRight()))
        menu.exec()
    
    def handle_menu_item_click(self):
        text = self.sender().text()

        if text=="Student Information":
            self.switch_to_student_info_page()
        elif text=="Student Payments":
            self.switch_to_student_payments_page()
        elif text=="Student Transactions":
            self.switch_to_student_transactions_page()
        elif text=="Teacher Information":
            self.switch_to_teacher_info_page()
        elif text=="Teacher Salaries":
            self.switch_to_teacher_salaries_page()
        elif text=="Teacher Transactions":
            self.switch_to_teacher_transactions_page()
        elif text=="Budgets":
            self.switch_to_budgets_page()
        elif text=="Expenses":
            self.switch_to_expenses_page()
        elif text=="Business Overview":
            self.switch_to_business_overview_page()
        
        