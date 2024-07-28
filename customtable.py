from PySide6.QtWidgets import QApplication, QMainWindow, QMenu, QTableWidget, QTableWidgetItem, QInputDialog, QMessageBox, QListWidget, QVBoxLayout, QWidget
import sys
from ui_table import Ui_MainWindow
from PySide6.QtCore import Qt, QPoint

class CustomTableWidget(QTableWidget):
    def __init__(self, parent=None, main_window=None):
        super().__init__(parent)
        self.setContextMenuPolicy(Qt.CustomContextMenu)
        self.customContextMenuRequested.connect(self.show_context_menu)
        self.groups = {}
        self.main_window = main_window  # Reference to the main window


    def show_context_menu(self, pos: QPoint):
        selected_items = self.selectedItems()
        if selected_items:
            context_menu = QMenu(self)
            delete_action = context_menu.addAction("Delete")
            copy_action = context_menu.addAction("Copy")
            create_group_action = context_menu.addAction("Create Group")
            # Connect actions to slots
            delete_action.triggered.connect(self.delete_selected_rows)
            copy_action.triggered.connect(self.copy_selected_rows)
            create_group_action.triggered.connect(self.create_group)
            context_menu.exec(self.mapToGlobal(pos))

    def create_group(self):
        selected_rows = set(item.row() for item in self.selectedItems())
        group = []
        for row in sorted(selected_rows):
            item = self.item(row, 0)  # Get the item in the first column
            if item:
                group.append(item.text())
        
        if group:
            group_name, ok = QInputDialog.getText(self, "Group Name", "Enter the name for the group:")
            if ok and group_name:
                if group_name in self.groups:
                    QMessageBox.warning(self, "Duplicate Group", "A group with this name already exists.")
                else:
                    self.groups[group_name] = group
                    self.main_window.group_list_widget.addItem(group_name)
                    print(f"Created group '{group_name}':", group)
            else:
                QMessageBox.warning(self, "Invalid Input", "Group name cannot be empty.")
        else:
            QMessageBox.warning(self, "No Selection", "No items selected to create a group.")

    def delete_selected_rows(self):
        selected_rows = set(item.row() for item in self.selectedItems())
        for row in sorted(selected_rows, reverse=True):
            self.removeRow(row)

    def copy_selected_rows(self):
        selected_rows = set(item.row() for item in self.selectedItems())
        copied_data = []
        for row in sorted(selected_rows):
            row_data = []
            for column in range(self.columnCount()):
                item = self.item(row, column)
                if item:
                    row_data.append(item.text())
            copied_data.append(row_data)
        # Here you can handle the copied data as needed
        print("Copied data:", copied_data)

class Table(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.central_widget = QWidget()
        self.layout = QVBoxLayout(self.central_widget)
        
        self.tableWidget = CustomTableWidget(self, main_window=self)
        self.group_list_widget = QListWidget(self)
        
        self.layout.addWidget(self.tableWidget)
        self.layout.addWidget(self.group_list_widget)
        self.setCentralWidget(self.central_widget)
        
        self.tableWidget.setRowCount(10)
        self.tableWidget.setColumnCount(5)
        for row in range(10):
            for column in range(5):
                self.tableWidget.setItem(row, column, QTableWidgetItem(f"Item {row},{column}"))
        
        self.group_list_widget.itemClicked.connect(self.display_group_items)

    def display_group_items(self, item):
        group_name = item.text()
        group_items = self.tableWidget.groups.get(group_name, [])
        QMessageBox.information(self, f"Group: {group_name}", f"Items: {', '.join(group_items)}")

app = QApplication(sys.argv)
window = Table()
window.show()
app.exec()