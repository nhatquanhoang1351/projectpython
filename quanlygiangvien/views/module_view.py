from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QTableWidget, 
    QTableWidgetItem, QMessageBox, QFormLayout, QHBoxLayout, QGroupBox, QComboBox, QSizePolicy
)
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import Qt

class ModuleView(QWidget):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.is_form_expanded = False
        self.init_ui()

    def init_ui(self):
        self.layout = QVBoxLayout(self)

        search_layout = QHBoxLayout()
        self.search_input = QLineEdit(self)
        self.search_input.setPlaceholderText("Nhập tên học phần")
        search_layout.addWidget(self.search_input)

        self.search_button = QPushButton(QIcon("search_icon.png"), "Tìm kiếm", self)
        self.search_button.clicked.connect(self.search_module)
        search_layout.addWidget(self.search_button)

        self.layout.addLayout(search_layout)

        self.toggle_form_button = QPushButton("▼ Thêm học phần", self)
        self.toggle_form_button.clicked.connect(self.toggle_registration_form)
        self.toggle_form_button.setStyleSheet("""
            QPushButton {
                text-align: left;
                padding: 5px;
                background-color: #f0f0f0;
                border: 1px solid #ccc;
                border-radius: 4px;
            }
            QPushButton:hover {
                background-color: #e0e0e0;
            }
        """)
        self.layout.addWidget(self.toggle_form_button)

        self.form_container = QWidget()
        self.form_layout = QFormLayout(self.form_container)
        
        self.module_id_input = QLineEdit(self)
        self.module_id_input.setPlaceholderText("Mã học phần")
        self.form_layout.addRow("Mã học phần:", self.module_id_input)

        self.module_name_input = QLineEdit(self)
        self.module_name_input.setPlaceholderText("Tên học phần")
        self.form_layout.addRow("Tên học phần:", self.module_name_input)

        self.duration_input = QLineEdit(self)
        self.duration_input.setPlaceholderText("Thời lượng (giờ)")
        self.form_layout.addRow("Thời lượng:", self.duration_input)

        self.credit_input = QLineEdit(self)
        self.credit_input.setPlaceholderText("Số tín chỉ")
        self.form_layout.addRow("Số tín chỉ:", self.credit_input)

        self.faculty_input = QComboBox(self)
        self.load_faculties()
        self.form_layout.addRow("Khoa/Viện quản lý:", self.faculty_input)

        self.type_module_input = QComboBox(self)
        self.type_module_input.addItems(["Bắt buộc", "Tự chọn"])
        self.type_module_input.setCurrentText("Bắt buộc")
        self.form_layout.addRow("Loại hình học phần:", self.type_module_input)

        button_layout = QHBoxLayout()
        self.add_button = QPushButton("Thêm học phần", self)
        self.add_button.clicked.connect(self.add_module)
        button_layout.addStretch()
        button_layout.addWidget(self.add_button)
        button_layout.addStretch()
        self.form_layout.addRow(button_layout)

        self.form_container.hide()
        self.layout.addWidget(self.form_container)

        self.table = QTableWidget(self)
        self.table.setColumnCount(6)
        self.table.setHorizontalHeaderLabels([
            "ID", "Mã học phần", "Tên học phần", 
            "Loại học phần", "Số tín chỉ", "Khoa/Viện quản lý"
        ])
        self.table.itemSelectionChanged.connect(self.on_module_selected)
        self.layout.addWidget(self.table)

        self.detail_group = QGroupBox("Thông tin chi tiết")
        self.detail_group.setCheckable(True)
        self.detail_group.setChecked(False)
        self.detail_group.toggled.connect(self.toggle_detail_group)
        self.detail_layout = QFormLayout()
        self.detail_group.setLayout(self.detail_layout)
        self.layout.addWidget(self.detail_group)

        delete_layout = QHBoxLayout()
        self.delete_button = QPushButton("Xóa học phần đã chọn", self)
        self.delete_button.clicked.connect(self.delete_module)
        self.delete_button.setFixedWidth(200)
        delete_layout.addStretch()
        delete_layout.addWidget(self.delete_button)
        delete_layout.addStretch()
        self.layout.addLayout(delete_layout)

        self.setMinimumSize(800, 600)
        self.setWindowTitle("Quản lý học phần")
        self.setLayout(self.layout)
        self.update_table()

    def load_faculties(self):
        faculties = self.controller.fetch_all_training_institute()
        for faculty in faculties:
            self.faculty_input.addItem(faculty[2], faculty[0]) 

    def toggle_registration_form(self):
        self.is_form_expanded = not self.is_form_expanded
        if self.is_form_expanded:
            self.form_container.show()
            self.toggle_form_button.setText("▲ Thêm học phần")
        else:
            self.form_container.hide()
            self.toggle_form_button.setText("▼ Thêm học phần")

    def toggle_detail_group(self, checked):
        if checked:
            self.detail_group.setMaximumHeight(400)
        else:
            self.detail_group.setMaximumHeight(30)

    def search_module(self):
        search_text = self.search_input.text().strip()
        if search_text:
            modules = self.controller.search_module_by_name(search_text)
            self.update_table(modules)
        else:
            modules = self.controller.get_all_modules()
            self.update_table(modules)

    def add_module(self):
        module_id = self.module_id_input.text()
        module_name = self.module_name_input.text()
        duration = self.duration_input.text()
        credit = self.credit_input.text()
        faculty_id = self.faculty_input.currentData()
        type_module = self.type_module_input.currentText()

        if all([module_id, module_name, duration, credit, faculty_id]):
            self.controller.add_module(module_id, module_name, duration, int(credit), faculty_id, type_module)
            self.update_table()
            self.clear_inputs()
        else:
            QMessageBox.warning(self, "Lỗi nhập liệu", "Vui lòng điền đầy đủ thông tin bắt buộc")

    def delete_module(self):
        selected_row = self.table.currentRow()
        if selected_row >= 0:
            module_id = self.table.item(selected_row, 0).text()
            self.controller.delete_module(module_id)
            self.update_table()
        else:
            QMessageBox.warning(self, "Lỗi chọn", "Vui lòng chọn một học phần để xóa")

    def update_table(self, modules=None):
        self.table.setRowCount(0)
        if modules is None:
            modules = self.controller.get_all_modules()
        for row_number, module in enumerate(modules):
            self.table.insertRow(row_number)

            for column_number, data in enumerate(module[:6]):  
                self.table.setItem(row_number, column_number, QTableWidgetItem(str(data)))

    def on_module_selected(self):
        selected_row = self.table.currentRow()
        if selected_row >= 0:
            module_id = self.table.item(selected_row, 1).text()
            self.display_module_info(module_id)

    def display_module_info(self, module_id):
        module_info = self.controller.get_module_by_id(module_id)
        if module_info:
            for i in reversed(range(self.detail_layout.count())):
                self.detail_layout.itemAt(i).widget().setParent(None)

            labels = [
                "Loại hình học phần"
            ]
            for i, label in enumerate(labels):
                self.detail_layout.addRow(QLabel(f"{label}:"), QLabel(str(module_info[i + 5])))

    def clear_inputs(self):
        self.module_id_input.clear()
        self.module_name_input.clear()
        self.duration_input.clear()
        self.credit_input.clear()
        self.faculty_input.setCurrentIndex(0)
        self.type_module_input.setCurrentText("Bắt buộc")