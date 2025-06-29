from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QTableWidget, 
    QTableWidgetItem, QMessageBox, QFormLayout, QHBoxLayout, QComboBox, QSizePolicy
)
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import Qt

class ClassView(QWidget):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.is_form_expanded = False
        self.init_ui()
    
    def init_ui(self):
        self.layout = QVBoxLayout(self)
        
        search_layout = QHBoxLayout()
        self.search_input = QLineEdit(self)
        self.search_input.setPlaceholderText("Nhập mã lớp")
        search_layout.addWidget(self.search_input)
        self.search_button = QPushButton(QIcon("search_icon.png"), "Tìm kiếm", self)
        self.search_button.clicked.connect(self.search_class)
        search_layout.addWidget(self.search_button)
        self.layout.addLayout(search_layout)
        
        self.toggle_form_button = QPushButton("▼ Thêm lớp", self)
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
        
        self.teacher_combo = QComboBox(self)
        self.teacher_combo.currentIndexChanged.connect(self.fill_teacher_full_name)
        self.form_layout.addRow("Mã giảng viên:", self.teacher_combo)
        
        self.full_name_input = QLineEdit(self)
        self.full_name_input.setReadOnly(True)
        self.form_layout.addRow("Họ và tên:", self.full_name_input)
        
        self.semester_input = QLineEdit(self)
        self.semester_input.setPlaceholderText("Nhập học kỳ")
        self.form_layout.addRow("Học kỳ:", self.semester_input)
        
        self.class_faculty_input = QLineEdit(self)
        self.class_faculty_input.setReadOnly(True)
        self.form_layout.addRow("Viện:", self.class_faculty_input)
        
        self.class_code_input = QLineEdit(self)
        self.class_code_input.setPlaceholderText("Nhập mã lớp")
        self.form_layout.addRow("Mã lớp:", self.class_code_input)
        
        self.module_combo = QComboBox(self)
        self.module_combo.currentIndexChanged.connect(self.fill_module_info)
        self.form_layout.addRow("Mã học phần:", self.module_combo)
        
        self.module_name_input = QLineEdit(self)
        self.module_name_input.setReadOnly(True)
        self.form_layout.addRow("Tên học phần:", self.module_name_input)
        
        self.day_of_week_input = QLineEdit(self)
        self.day_of_week_input.setPlaceholderText("Ví dụ: Thứ 2")
        self.form_layout.addRow("Ngày trong tuần:", self.day_of_week_input)
        
        self.time_input = QLineEdit(self)
        self.time_input.setPlaceholderText("Ví dụ: 08:00 - 10:00")
        self.form_layout.addRow("Thời gian:", self.time_input)
        
        self.weeks_input = QLineEdit(self)
        self.weeks_input.setPlaceholderText("Nhập số tuần")
        self.form_layout.addRow("Số tuần:", self.weeks_input)
        
        self.room_input = QLineEdit(self)
        self.room_input.setPlaceholderText("Nhập phòng học")
        self.form_layout.addRow("Phòng học:", self.room_input)
        
        self.registered_input = QLineEdit(self)
        self.registered_input.setPlaceholderText("Nhập số đăng ký")
        self.form_layout.addRow("Số đăng ký:", self.registered_input)
        
        self.max_capacity_input = QLineEdit(self)
        self.max_capacity_input.setPlaceholderText("Nhập sức chứa tối đa")
        self.form_layout.addRow("Sức chứa tối đa:", self.max_capacity_input)
        
        self.status_input = QComboBox(self)
        self.status_input.addItems(["Hoạt động", "Tạm ngừng", "Đã đóng"])
        self.status_input.setCurrentText("Hoạt động")
        self.form_layout.addRow("Trạng thái:", self.status_input)
        
        self.class_type_input = QLineEdit(self)
        self.class_type_input.setPlaceholderText("Ví dụ: Lý thuyết/Thực hành")
        self.form_layout.addRow("Loại lớp:", self.class_type_input)
        
        button_layout = QHBoxLayout()
        self.add_button = QPushButton("Thêm lớp", self)
        self.add_button.clicked.connect(self.add_class)
        button_layout.addStretch()
        button_layout.addWidget(self.add_button)
        button_layout.addStretch()
        self.form_layout.addRow(button_layout)
        
        self.form_container.hide()
        self.layout.addWidget(self.form_container)
        
        self.table = QTableWidget(self)
        self.table.setColumnCount(15)
        self.table.setHorizontalHeaderLabels([
            "Teacher ID", "Họ và tên", "Học kỳ", "Viện", "Mã lớp", "Mã học phần",
            "Tên học phần", "Ngày trong tuần", "Thời gian", "Số tuần", "Phòng học",
            "Số đăng ký", "Sức chứa tối đa", "Trạng thái", "Loại lớp"
        ])
        self.table.itemSelectionChanged.connect(self.on_class_selected)
        self.layout.addWidget(self.table)
        
        delete_layout = QHBoxLayout()
        self.delete_button = QPushButton("Xóa lớp đã chọn", self)
        self.delete_button.clicked.connect(self.delete_class)
        self.delete_button.setFixedWidth(200)
        delete_layout.addStretch()
        delete_layout.addWidget(self.delete_button)
        delete_layout.addStretch()
        self.layout.addLayout(delete_layout)
        
        self.setMinimumSize(800, 600)
        self.setWindowTitle("Quản lý lớp")
        self.setLayout(self.layout)
        
        self.load_teachers()
        self.load_modules()
        self.update_table()
    
    def toggle_registration_form(self):
        self.is_form_expanded = not self.is_form_expanded
        if self.is_form_expanded:
            self.form_container.show()
            self.toggle_form_button.setText("▲ Thêm lớp")
        else:
            self.form_container.hide()
            self.toggle_form_button.setText("▼ Thêm lớp")
    
    def load_teachers(self):
        teachers = self.controller.get_all_teachers()
        self.teacher_combo.clear()
        for teacher in teachers:
            self.teacher_combo.addItem(str(teacher[1]), teacher)
    
    def load_modules(self):
        modules = self.controller.get_all_modules()
        self.module_combo.clear()
        for module in modules:
            self.module_combo.addItem(str(module[1]), module)
    
    def fill_teacher_full_name(self):
        teacher = self.teacher_combo.currentData()
        if teacher:
            self.full_name_input.setText(teacher[2])
        else:
            self.full_name_input.clear()
    
    def fill_module_info(self):
        module = self.module_combo.currentData()
        if module:
            self.module_name_input.setText(module[2])
            name_institute = self.controller.get_training_institute_by_id(module[5])[2]
            self.class_faculty_input.setText(name_institute)
        else:
            self.module_name_input.clear()
            self.class_faculty_input.clear()
    
    def add_class(self):
        teacher = self.teacher_combo.currentData()
        if teacher is None:
            QMessageBox.warning(self, "Lỗi", "Vui lòng chọn giảng viên")
            return
        teacher_id = teacher[0]
        full_name = self.full_name_input.text()
        semester = self.semester_input.text()
        faculty = self.class_faculty_input.text()
        class_code = self.class_code_input.text()
        module = self.module_combo.currentData()
        if module is None:
            QMessageBox.warning(self, "Lỗi", "Vui lòng chọn học phần")
            return
        module_code = module[1]
        module_name = self.module_name_input.text()
        day_of_week = self.day_of_week_input.text()
        time_val = self.time_input.text()
        weeks = self.weeks_input.text()
        room = self.room_input.text()
        registered = self.registered_input.text()
        max_capacity = self.max_capacity_input.text()
        status = self.status_input.currentText()
        class_type = self.class_type_input.text()
        
        if all([teacher_id, full_name, semester, faculty, class_code, module_code,
                module_name, day_of_week, time_val, weeks, room, registered, max_capacity, status, class_type]):
            try:
                self.controller.add_class(
                    teacher_id, full_name, semester, faculty, class_code, module_code,
                    module_name, day_of_week, time_val, weeks, room, int(registered), int(max_capacity),
                    status, class_type
                )
                self.update_table()
                self.clear_inputs()
                QMessageBox.information(self, "Thành công", "Thêm lớp thành công!")
            except Exception as e:
                QMessageBox.critical(self, "Lỗi", f"Không thể thêm lớp: {str(e)}")
        else:
            QMessageBox.warning(self, "Lỗi nhập liệu", "Vui lòng điền đầy đủ thông tin bắt buộc")
    
    def delete_class(self):
        selected_row = self.table.currentRow()
        if selected_row >= 0:
            class_code = self.table.item(selected_row, 4).text()
            reply = QMessageBox.question(
                self, "Xác nhận xóa",
                f"Bạn có chắc chắn muốn xóa lớp có mã: {class_code}?",
                QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
                QMessageBox.StandardButton.No
            )
            if reply == QMessageBox.StandardButton.Yes:
                try:
                    self.controller.delete_class(class_code)
                    self.update_table()
                    QMessageBox.information(self, "Thành công", "Xóa lớp thành công!")
                except Exception as e:
                    QMessageBox.critical(self, "Lỗi", f"Không thể xóa lớp: {str(e)}")
        else:
            QMessageBox.warning(self, "Lỗi chọn", "Vui lòng chọn một lớp để xóa")
    
    def search_class(self):
        search_text = self.search_input.text().strip()
        if search_text:
            classes = self.controller.search_class_by_module_name(search_text)
            self.update_table(classes)
        else:
            classes = self.controller.get_all_classses()
            self.update_table(classes)
    
    def update_table(self, classes=None):
        self.table.setRowCount(0)
        if classes is None:
            classes = self.controller.get_all_classses()

        for row_number, cls in enumerate(classes):
            self.table.insertRow(row_number)
            for col, data in enumerate(cls):
                self.table.setItem(row_number, col, QTableWidgetItem(str(data)))
        self.table.resizeColumnsToContents()
    
    def clear_inputs(self):
        self.teacher_combo.setCurrentIndex(0)
        self.semester_input.clear()
        self.class_code_input.clear()
        self.day_of_week_input.clear()
        self.time_input.clear()
        self.weeks_input.clear()
        self.room_input.clear()
        self.registered_input.clear()
        self.max_capacity_input.clear()
        self.status_input.setCurrentIndex(0)
        self.class_type_input.clear()
    
    def on_class_selected(self):
        pass
