from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QTableWidget, 
    QTableWidgetItem, QMessageBox, QFormLayout, QHBoxLayout, QComboBox
)
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import Qt

class TrainingInstituteView(QWidget):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.is_form_expanded = False
        self.updating_table = False  
        self.init_ui()

    def init_ui(self):
        self.layout = QVBoxLayout(self)

        search_layout = QHBoxLayout()
        self.search_input = QLineEdit(self)
        self.search_input.setPlaceholderText("Nhập tên khoa/viện")
        search_layout.addWidget(self.search_input)

        self.search_button = QPushButton(QIcon("search_icon.png"), "Tìm kiếm", self)
        self.search_button.clicked.connect(self.search_institute)
        search_layout.addWidget(self.search_button)
        self.layout.addLayout(search_layout)

        self.toggle_form_button = QPushButton("▼ Thêm khoa/viện", self)
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
        
        self.institute_id_input = QLineEdit(self)
        self.institute_id_input.setPlaceholderText("Mã khoa/viện")
        self.form_layout.addRow("Mã khoa/viện:", self.institute_id_input)

        self.name_input = QLineEdit(self)
        self.name_input.setPlaceholderText("Tên khoa/viện")
        self.form_layout.addRow("Tên khoa/viện:", self.name_input)

        self.short_name_input = QLineEdit(self)
        self.short_name_input.setPlaceholderText("Tên viết tắt")
        self.form_layout.addRow("Tên viết tắt:", self.short_name_input)

        self.address_input = QLineEdit(self)
        self.address_input.setPlaceholderText("Địa chỉ")
        self.form_layout.addRow("Địa chỉ:", self.address_input)

        self.phone_number_input = QLineEdit(self)
        self.phone_number_input.setPlaceholderText("Số điện thoại")
        self.form_layout.addRow("Số điện thoại:", self.phone_number_input)

        self.email_input = QLineEdit(self)
        self.email_input.setPlaceholderText("Email")
        self.form_layout.addRow("Email:", self.email_input)

        self.website_input = QLineEdit(self)
        self.website_input.setPlaceholderText("Website")
        self.form_layout.addRow("Website:", self.website_input)

        self.established_date_input = QLineEdit(self)
        self.established_date_input.setPlaceholderText("Ngày thành lập")
        self.form_layout.addRow("Ngày thành lập:", self.established_date_input)

        self.head_of_institute_input = QLineEdit(self)
        self.head_of_institute_input.setPlaceholderText("Trưởng khoa/viện")
        self.form_layout.addRow("Trưởng khoa/viện:", self.head_of_institute_input)

        self.description_input = QLineEdit(self)
        self.description_input.setPlaceholderText("Mô tả (không bắt buộc)")
        self.form_layout.addRow("Mô tả:", self.description_input)

        self.status_input = QComboBox(self)
        self.status_input.addItems(["Hoạt động", "Tạm ngừng", "Đã đóng"])
        self.status_input.setCurrentText("Hoạt động")
        self.form_layout.addRow("Trạng thái:", self.status_input)

        button_layout = QHBoxLayout()
        self.add_button = QPushButton("Thêm khoa/viện", self)
        self.add_button.clicked.connect(self.add_institute)
        button_layout.addStretch()
        button_layout.addWidget(self.add_button)
        button_layout.addStretch()
        self.form_layout.addRow(button_layout)

        self.form_container.hide()
        self.layout.addWidget(self.form_container)

        self.table = QTableWidget(self)
        self.table.setColumnCount(12)
        self.table.setHorizontalHeaderLabels([
            "ID", "Mã khoa/viện", "Tên khoa/viện", "Tên viết tắt", "Địa chỉ", 
            "Số điện thoại", "Email", "Website", "Ngày thành lập", 
            "Trưởng khoa/viện", "Mô tả", "Trạng thái"
        ])
        self.table.itemChanged.connect(self.cell_changed)
        self.layout.addWidget(self.table)

        delete_layout = QHBoxLayout()
        self.delete_button = QPushButton("Xóa khoa/viện đã chọn", self)
        self.delete_button.clicked.connect(self.delete_institute)
        self.delete_button.setFixedWidth(200)
        delete_layout.addStretch()
        delete_layout.addWidget(self.delete_button)
        delete_layout.addStretch()
        self.layout.addLayout(delete_layout)

        self.setMinimumSize(800, 600)
        self.setWindowTitle("Quản lý khoa/viện")
        self.setLayout(self.layout)
        self.update_table()

    def toggle_registration_form(self):
        self.is_form_expanded = not self.is_form_expanded
        if self.is_form_expanded:
            self.form_container.show()
            self.toggle_form_button.setText("▲ Thêm khoa/viện")
        else:
            self.form_container.hide()
            self.toggle_form_button.setText("▼ Thêm khoa/viện")

    def search_institute(self):
        search_text = self.search_input.text().strip()
        if search_text:
            institutes = self.controller.search_institute_by_name(search_text)
            self.update_table(institutes)
        else:
            institutes = self.controller.get_all_institutes()
            self.update_table(institutes)

    def add_institute(self):
        institute_id = self.institute_id_input.text()
        name = self.name_input.text()
        short_name = self.short_name_input.text()
        address = self.address_input.text()
        phone_number = self.phone_number_input.text() or ""
        email = self.email_input.text() or ""
        website = self.website_input.text() or ""
        established_date = self.established_date_input.text() or ""
        head_of_institute = self.head_of_institute_input.text() or ""
        description = self.description_input.text() or ""
        status = self.status_input.currentText()

        if all([institute_id, name, short_name, address, phone_number]):
            self.controller.add_institute(
                institute_id, name, short_name, address, phone_number,
                email, website, established_date, head_of_institute,
                description, status
            )
            self.update_table()
            self.clear_inputs()
        else:
            QMessageBox.warning(self, "Lỗi nhập liệu", "Vui lòng điền đầy đủ thông tin bắt buộc")

    def delete_institute(self):
        selected_row = self.table.currentRow()
        if selected_row >= 0:
            record_id = self.table.item(selected_row, 0).text()
            self.controller.delete_institute(record_id)
            self.update_table()
        else:
            QMessageBox.warning(self, "Lỗi chọn", "Vui lòng chọn một khoa/viện để xóa")

    def update_table(self, institutes=None):
        self.updating_table = True 
        self.table.setRowCount(0)
        if institutes is None:
            institutes = self.controller.get_all_institutes()
        for row_number, institute in enumerate(institutes):
            self.table.insertRow(row_number)
            for column_number, data in enumerate(institute):
                item = QTableWidgetItem(str(data))
                if column_number == 0:
                    item.setFlags(item.flags() & ~Qt.ItemFlag.ItemIsEditable)
                self.table.setItem(row_number, column_number, item)
        self.table.setColumnHidden(0, True)
        self.updating_table = False

    def cell_changed(self, item):
        if self.updating_table:
            return

        row = item.row()
        record_id = self.table.item(row, 0).text() if self.table.item(row, 0) else ""
        institute_id = self.table.item(row, 1).text() if self.table.item(row, 1) else ""
        name = self.table.item(row, 2).text() if self.table.item(row, 2) else ""
        short_name = self.table.item(row, 3).text() if self.table.item(row, 3) else ""
        address = self.table.item(row, 4).text() if self.table.item(row, 4) else ""
        phone_number = self.table.item(row, 5).text() if self.table.item(row, 5) else ""
        email = self.table.item(row, 6).text() if self.table.item(row, 6) else ""
        website = self.table.item(row, 7).text() if self.table.item(row, 7) else ""
        established_date = self.table.item(row, 8).text() if self.table.item(row, 8) else ""
        head_of_institute = self.table.item(row, 9).text() if self.table.item(row, 9) else ""
        description = self.table.item(row, 10).text() if self.table.item(row, 10) else ""
        status = self.table.item(row, 11).text() if self.table.item(row, 11) else ""
        print("Đã update SQL")
        self.controller.update_institute_info(
            record_id, institute_id, name, short_name, address, phone_number,
            email, website, established_date, head_of_institute,
            description, status
        )

    def clear_inputs(self):
        self.institute_id_input.clear()
        self.name_input.clear()
        self.short_name_input.clear()
        self.address_input.clear()
        self.phone_number_input.clear()
        self.email_input.clear()
        self.website_input.clear()
        self.established_date_input.clear()
        self.head_of_institute_input.clear()
        self.description_input.clear()
        self.status_input.setCurrentText("Hoạt động")
