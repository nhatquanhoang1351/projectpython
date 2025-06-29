from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QTableWidget, 
    QTableWidgetItem, QMessageBox, QFormLayout, QHBoxLayout, QGroupBox, QComboBox,
    QSplitter, QApplication, QScrollArea, QSizePolicy, QGridLayout
)
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import Qt, QSize

class CollapsibleBox(QWidget):
    def __init__(self, title="", parent=None):
        super(CollapsibleBox, self).__init__(parent)
        self.toggle_button = QPushButton(f"▼ {title}", self)
        self.toggle_button.setStyleSheet("""
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
        self.toggle_button.clicked.connect(self.on_toggle)
        
        self.content_area = QScrollArea()
        self.content_area.setWidgetResizable(True)
        self.content_area.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        self.content_area.setMaximumHeight(0)
        self.content_area.setMinimumHeight(0)
        
        self.content_widget = QWidget()
        self.content_layout = QVBoxLayout(self.content_widget)
        self.content_area.setWidget(self.content_widget)
        
        self.main_layout = QVBoxLayout(self)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.addWidget(self.toggle_button)
        self.main_layout.addWidget(self.content_area)
        
        self.is_collapsed = True
        
    def on_toggle(self):
        self.is_collapsed = not self.is_collapsed
        if self.is_collapsed:
            self.toggle_button.setText(f"▼ {self.toggle_button.text()[2:]}")
            self.content_area.setMaximumHeight(0)
        else:
            self.toggle_button.setText(f"▲ {self.toggle_button.text()[2:]}")
            self.content_area.setMaximumHeight(9999)
            
    def set_content_layout(self, layout):
        while self.content_layout.count():
            item = self.content_layout.takeAt(0)
            if item.widget():
                item.widget().deleteLater()
        
        container = QWidget()
        container.setLayout(layout)
        self.content_layout.addWidget(container)

class TeacherView(QWidget):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.updating_table = False  
        self.init_ui()
        
    def init_ui(self):

        main_layout = QVBoxLayout(self)
        
        search_box = CollapsibleBox("Tìm kiếm giảng viên")
        search_layout = QHBoxLayout()
        
        self.search_input = QLineEdit()
        self.search_input.setPlaceholderText("Nhập tên hoặc mã giảng viên")
        self.search_input.returnPressed.connect(self.search_teacher)
        
        self.search_button = QPushButton(QIcon("search_icon.png"), "Tìm kiếm")
        self.search_button.clicked.connect(self.search_teacher)
        
        search_layout.addWidget(self.search_input, 3)
        search_layout.addWidget(self.search_button, 1)
        
        search_box.set_content_layout(search_layout)
        search_box.on_toggle()  
        
        main_layout.addWidget(search_box)
        
        self.add_form_box = CollapsibleBox("Thêm giảng viên")
        
        form_grid = QGridLayout()
        form_grid.setColumnStretch(0, 1)
        form_grid.setColumnStretch(1, 1)
        form_grid.setColumnStretch(2, 1)
        form_grid.setColumnStretch(3, 1)

        self.teacher_id_input = QLineEdit()
        self.teacher_id_input.setPlaceholderText("Mã giảng viên")
        form_grid.addWidget(QLabel("Mã giảng viên:"), 0, 0)
        form_grid.addWidget(self.teacher_id_input, 0, 1)
        
        self.full_name_input = QLineEdit()
        self.full_name_input.setPlaceholderText("Họ và tên")
        form_grid.addWidget(QLabel("Họ và tên:"), 1, 0)
        form_grid.addWidget(self.full_name_input, 1, 1)
        
        self.date_of_birth_input = QLineEdit()
        self.date_of_birth_input.setPlaceholderText("Ngày sinh")
        form_grid.addWidget(QLabel("Ngày sinh:"), 2, 0)
        form_grid.addWidget(self.date_of_birth_input, 2, 1)
        
        self.gender_input = QLineEdit()
        self.gender_input.setPlaceholderText("Giới tính")
        form_grid.addWidget(QLabel("Giới tính:"), 3, 0)
        form_grid.addWidget(self.gender_input, 3, 1)
        
        self.email_input = QLineEdit()
        self.email_input.setPlaceholderText("Email")
        form_grid.addWidget(QLabel("Email:"), 4, 0)
        form_grid.addWidget(self.email_input, 4, 1)
        
        self.address_input = QLineEdit()
        self.address_input.setPlaceholderText("Địa chỉ")
        form_grid.addWidget(QLabel("Địa chỉ:"), 5, 0)
        form_grid.addWidget(self.address_input, 5, 1)
        
        self.phone_number_input = QLineEdit()
        self.phone_number_input.setPlaceholderText("Số điện thoại")
        form_grid.addWidget(QLabel("Số điện thoại:"), 0, 2)
        form_grid.addWidget(self.phone_number_input, 0, 3)
        
        self.enrollment_year_input = QLineEdit()
        self.enrollment_year_input.setPlaceholderText("Năm vào trường")
        form_grid.addWidget(QLabel("Năm vào trường:"), 1, 2)
        form_grid.addWidget(self.enrollment_year_input, 1, 3)
        
        self.job_title_input = QLineEdit()
        self.job_title_input.setPlaceholderText("Chức vụ")
        form_grid.addWidget(QLabel("Chức vụ:"), 2, 2)
        form_grid.addWidget(self.job_title_input, 2, 3)
        
        self.education_level_input = QLineEdit()
        self.education_level_input.setPlaceholderText("Trình độ học vấn")
        form_grid.addWidget(QLabel("Trình độ học vấn:"), 3, 2)
        form_grid.addWidget(self.education_level_input, 3, 3)
        
        self.learning_process_input = QLineEdit()
        self.learning_process_input.setPlaceholderText("Quá trình học tập")
        form_grid.addWidget(QLabel("Quá trình học tập:"), 4, 2)
        form_grid.addWidget(self.learning_process_input, 4, 3)
        
        self.status_input = QComboBox()
        self.status_input.addItems(["Đang dạy", "Tạm nghỉ", "Đã nghỉ"])
        self.status_input.setCurrentText("Đang dạy")
        form_grid.addWidget(QLabel("Trạng thái:"), 6, 0)
        form_grid.addWidget(self.status_input, 6, 1)
        
        self.faculty_input = QComboBox()
        form_grid.addWidget(QLabel("Khoa/Viện quản lý:"), 5, 2)
        form_grid.addWidget(self.faculty_input, 5, 3)
        
        extended_form_box = CollapsibleBox("Thông tin bổ sung (không bắt buộc)")
        extended_form_layout = QGridLayout()
        extended_form_layout.setColumnStretch(0, 1)
        extended_form_layout.setColumnStretch(1, 1)
        extended_form_layout.setColumnStretch(2, 1)
        extended_form_layout.setColumnStretch(3, 1)
        
        self.intro_input = QLineEdit()
        self.intro_input.setPlaceholderText("Giới thiệu")
        extended_form_layout.addWidget(QLabel("Giới thiệu:"), 0, 0)
        extended_form_layout.addWidget(self.intro_input, 0, 1)
        
        self.research_field_input = QLineEdit()
        self.research_field_input.setPlaceholderText("Lĩnh vực nghiên cứu")
        extended_form_layout.addWidget(QLabel("Lĩnh vực nghiên cứu:"), 1, 0)
        extended_form_layout.addWidget(self.research_field_input, 1, 1)
        
        self.research_interests_input = QLineEdit()
        self.research_interests_input.setPlaceholderText("Các nghiên cứu quan tâm")
        extended_form_layout.addWidget(QLabel("Các nghiên cứu quan tâm:"), 2, 0)
        extended_form_layout.addWidget(self.research_interests_input, 2, 1)
        
        self.typical_scientific_works_input = QLineEdit()
        self.typical_scientific_works_input.setPlaceholderText("Các công trình khoa học tiêu biểu")
        extended_form_layout.addWidget(QLabel("Các công trình khoa học tiêu biểu:"), 3, 0)
        extended_form_layout.addWidget(self.typical_scientific_works_input, 3, 1)
        
        self.prize_input = QLineEdit()
        self.prize_input.setPlaceholderText("Các giải thưởng")
        extended_form_layout.addWidget(QLabel("Các giải thưởng:"), 4, 0)
        extended_form_layout.addWidget(self.prize_input, 4, 1)
        
        self.current_projects_input = QLineEdit()
        self.current_projects_input.setPlaceholderText("Các dự án hiện tại")
        extended_form_layout.addWidget(QLabel("Các dự án hiện tại:"), 1, 2)
        extended_form_layout.addWidget(self.current_projects_input, 1, 3)
        
        self.published_books_input = QLineEdit()
        self.published_books_input.setPlaceholderText("Sách đã xuất bản")
        extended_form_layout.addWidget(QLabel("Sách đã xuất bản:"), 2, 2)
        extended_form_layout.addWidget(self.published_books_input, 2, 3)
        
        extended_form_box.set_content_layout(extended_form_layout)
        
        add_button_layout = QHBoxLayout()
        self.add_button = QPushButton("Thêm giảng viên")
        self.add_button.clicked.connect(self.add_teacher)
        add_button_layout.addStretch()
        add_button_layout.addWidget(self.add_button)
        add_button_layout.addStretch()
        
        form_container_layout = QVBoxLayout()
        
        form_grid_widget = QWidget()
        form_grid_widget.setLayout(form_grid)
        form_container_layout.addWidget(form_grid_widget)
        
        form_container_layout.addWidget(extended_form_box)
        
        button_widget = QWidget()
        button_widget.setLayout(add_button_layout)
        form_container_layout.addWidget(button_widget)
        
        self.add_form_box.set_content_layout(form_container_layout)
        main_layout.addWidget(self.add_form_box)
        
        data_splitter = QSplitter(Qt.Orientation.Vertical)
        data_splitter.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        
        self.table = QTableWidget()
        self.table.setColumnCount(10)
        self.table.setHorizontalHeaderLabels([
            "ID", "Mã giảng viên", "Họ và tên", "Ngày sinh", "Giới tính", 
            "Email", "Địa chỉ", "Số điện thoại", "Năm vào trường", "Chức vụ"
        ])
        self.table.itemSelectionChanged.connect(self.on_teacher_selected)
        self.table.horizontalHeader().setStretchLastSection(True)
        self.table.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        
        self.table.resizeColumnsToContents()
        self.table.setAlternatingRowColors(True)
        
        self.table.itemChanged.connect(self.on_item_changed)
        
        self.detail_box = CollapsibleBox("Thông tin chi tiết")
        self.detail_form_layout = QFormLayout()
        
        self.detail_widget = QWidget()
        self.detail_widget.setLayout(self.detail_form_layout)
        
        detail_container = QVBoxLayout()
        detail_container.addWidget(self.detail_widget)
        
        self.detail_box.set_content_layout(detail_container)
        
        data_splitter.addWidget(self.table)
        data_splitter.addWidget(self.detail_box)
        
        data_splitter.setSizes([600, 400])
        
        main_layout.addWidget(data_splitter, 1)  
        
        delete_layout = QHBoxLayout()
        self.delete_button = QPushButton("Xóa giảng viên đã chọn")
        self.delete_button.clicked.connect(self.delete_teacher)
        self.delete_button.setFixedWidth(200)
        delete_layout.addStretch()
        delete_layout.addWidget(self.delete_button)
        delete_layout.addStretch()
        
        delete_widget = QWidget()
        delete_widget.setLayout(delete_layout)
        main_layout.addWidget(delete_widget)
        
        self.load_training_institutes()
        self.update_table()
        
        self.setMinimumSize(800, 600)
        
    def load_training_institutes(self):
        training_institutes = self.controller.get_all_training_institutes()
        self.faculty_input.clear()
        for training_institute in training_institutes:
            self.faculty_input.addItem(training_institute[2], training_institute[0])
            
    def search_teacher(self):
        search_text = self.search_input.text().strip()
        print(search_text)
        if search_text:            
            teachers_by_id = self.controller.search_all_teacher_by_id(search_text)  
            teachers_by_name = self.controller.search_teacher_by_name(search_text)
            teachers = { teacher[0]: teacher for teacher in teachers_by_id + teachers_by_name}.values()
            self.update_table(list(teachers))
        else:
            teachers = self.controller.get_all_teachers()
            self.update_table(teachers)

    def add_teacher(self):
        teacher_id = self.teacher_id_input.text()
        full_name = self.full_name_input.text()
        date_of_birth = self.date_of_birth_input.text()
        gender = self.gender_input.text()
        email = self.email_input.text()
        address = self.address_input.text()
        phone_number = self.phone_number_input.text()
        enrollment_year = self.enrollment_year_input.text()
        job_title = self.job_title_input.text()
        education_level = self.education_level_input.text()
        learning_process = self.learning_process_input.text()
        intro = self.intro_input.text() or ""
        research_field = self.research_field_input.text() or ""
        research_interests = self.research_interests_input.text() or ""
        typical_scientific_works = self.typical_scientific_works_input.text() or ""
        prize = self.prize_input.text() or ""
        faculty = self.faculty_input.currentData()
        current_projects = self.current_projects_input.text() or ""
        published_books = self.published_books_input.text() or ""
        status = self.status_input.currentText()

        if all([teacher_id, full_name, date_of_birth, gender, email, address, phone_number, enrollment_year, job_title, education_level, learning_process]):
            try:
                self.controller.add_teacher(
                    teacher_id, full_name, date_of_birth, gender, email, address, 
                    phone_number, int(enrollment_year), job_title, education_level, 
                    learning_process, intro, research_field, research_interests, 
                    typical_scientific_works, prize, faculty, current_projects, 
                    published_books, status
                )
                self.update_table()
                self.clear_inputs()
                QMessageBox.information(self, "Thành công", "Thêm giảng viên thành công!")
            except Exception as e:
                QMessageBox.critical(self, "Lỗi", f"Không thể thêm giảng viên: {str(e)}")
        else:
            QMessageBox.warning(self, "Lỗi nhập liệu", "Vui lòng điền đầy đủ thông tin bắt buộc")

    def delete_teacher(self):
        selected_row = self.table.currentRow()
        if selected_row >= 0:
            teacher_id = self.table.item(selected_row, 0).text()
            reply = QMessageBox.question(self, "Xác nhận xóa", 
                                         f"Bạn có chắc chắn muốn xóa giảng viên có ID: {teacher_id}?",
                                         QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
                                         QMessageBox.StandardButton.No)
            if reply == QMessageBox.StandardButton.Yes:
                try:
                    self.controller.delete_teacher(int(teacher_id))
                    self.update_table()
                    QMessageBox.information(self, "Thành công", "Xóa giảng viên thành công!")
                except Exception as e:
                    QMessageBox.critical(self, "Lỗi", f"Không thể xóa giảng viên: {str(e)}")
        else:
            QMessageBox.warning(self, "Lỗi chọn", "Vui lòng chọn một giảng viên để xóa")
            
    def on_item_changed(self, item):
        if self.updating_table:
            return        
        
        row = item.row()
        id = self.table.item(row, 0).text() if self.table.item(row, 0) else ""
        teacher_id = self.table.item(row, 1).text() if self.table.item(row, 1) else ""
        full_name = self.table.item(row, 2).text() if self.table.item(row, 2) else ""        
        date_of_birth = self.table.item(row, 3).text() if self.table.item(row, 3) else ""
        gender = self.table.item(row, 4).text() if self.table.item(row, 4) else ""
        email = self.table.item(row, 5).text() if self.table.item(row, 5) else ""
        address = self.table.item(row, 6).text() if self.table.item(row, 6) else ""
        phone_number = self.table.item(row, 7).text() if self.table.item(row, 7) else ""
        enrollment_year = self.table.item(row, 8).text() if self.table.item(row, 8) else ""
        # column = item.column()
        
        # if column == 9:  
        #     try:
        #         id_value = int(self.table.item(row, 0).text())
        #         teacher_id = self.table.item(row, 1).text()
        #         new_job_title = item.text()
                
        #         teacher_info = self.controller.get_teacher_by_id(teacher_id)
                
        self.controller.update_teacher(
            id,
            teacher_id,
            full_name,  
            date_of_birth,  
            gender,  
            email,  
            address,  
            phone_number,  
            enrollment_year
        ) 
            
    def update_table(self, teachers=None):
        self.updating_table = True 
        self.table.setRowCount(0)
        if teachers is None:
            teachers = self.controller.get_all_teachers()
            
        for row_number, teacher in enumerate(teachers):
            self.table.insertRow(row_number)
            for column_number, data in enumerate(teacher[:10]):  
                self.table.setItem(row_number, column_number, QTableWidgetItem(str(data)))
        self.table.resizeColumnsToContents()
        
        if self.table.rowCount() == 0:
            if not self.detail_box.is_collapsed:
                self.detail_box.on_toggle()
            self.clear_detail_layout()
        self.updating_table = False 
    def on_teacher_selected(self):
        selected_row = self.table.currentRow()
        if selected_row >= 0:
            teacher_id = self.table.item(selected_row, 1).text()
            self.display_teacher_info(teacher_id)
            if self.detail_box.is_collapsed:
                self.detail_box.on_toggle()
        else:
            if not self.detail_box.is_collapsed:
                self.detail_box.on_toggle()

    def clear_detail_layout(self):
        while self.detail_form_layout.count():
            item = self.detail_form_layout.takeAt(0)
            if item.widget():
                item.widget().deleteLater()

    def display_teacher_info(self, teacher_id):
        teacher_info = self.controller.get_teacher_by_id(teacher_id)
        if teacher_info:
            self.clear_detail_layout()
            
            self.current_teacher_id = teacher_info[0]  
            self.current_teacher_code = teacher_id  
            
            button_layout = QHBoxLayout()
            self.edit_button = QPushButton("Chỉnh sửa")
            self.edit_button.clicked.connect(self.enable_editing)
            self.save_button = QPushButton("Lưu thay đổi") 
            self.save_button.clicked.connect(self.save_teacher_changes)
            self.save_button.setEnabled(False)
            
            button_layout.addWidget(self.edit_button)
            button_layout.addWidget(self.save_button)
            button_widget = QWidget()
            button_widget.setLayout(button_layout)
            self.detail_form_layout.addRow(button_widget)
            
            self.detail_inputs = {}
            
            labels_and_fields = [
                ("Chức vụ", teacher_info[9]),
                ("Trình độ học vấn", teacher_info[10]),
                ("Quá trình học tập", teacher_info[11]),
                ("Giới thiệu", teacher_info[12]),
                ("Lĩnh vực nghiên cứu", teacher_info[13]),
                ("Các nghiên cứu quan tâm", teacher_info[14]),
                ("Các công trình khoa học tiêu biểu", teacher_info[15]),
                ("Các giải thưởng", teacher_info[16]),
                ("Các dự án hiện tại", teacher_info[18]),
                ("Sách đã xuất bản", teacher_info[19]),
                ("Trạng thái", teacher_info[20])
            ]
            
            for label, value in labels_and_fields:
                if label == "Trạng thái":
                    input_field = QComboBox()
                    input_field.addItems(["Đang dạy", "Tạm nghỉ", "Đã nghỉ"])
                    input_field.setCurrentText(str(value))
                else:
                    input_field = QLineEdit()
                    input_field.setText(str(value))
                
                input_field.setEnabled(False)
                self.detail_inputs[label] = input_field
                self.detail_form_layout.addRow(QLabel(f"{label}:"), input_field)
            
            faculty_id = teacher_info[17]
            institute = self.controller.get_training_institute_by_id(faculty_id)
            value_text = institute[2] if institute else ""
            value = QLabel(value_text)
            self.detail_form_layout.addRow(QLabel("Khoa/Viện quản lý:"), value)
    def enable_editing(self):
        for input_field in self.detail_inputs.values():
            input_field.setEnabled(True)
        
        self.edit_button.setEnabled(False)
        self.save_button.setEnabled(True)

    def save_teacher_changes(self):
        try:
            job_title = self.detail_inputs["Chức vụ"].text()
            education_level = self.detail_inputs["Trình độ học vấn"].text()
            research_field = self.detail_inputs["Lĩnh vực nghiên cứu"].text()
            research_interests = self.detail_inputs["Các nghiên cứu quan tâm"].text()
            typical_scientific_works = self.detail_inputs["Các công trình khoa học tiêu biểu"].text()
            prize = self.detail_inputs["Các giải thưởng"].text()
            current_projects = self.detail_inputs["Các dự án hiện tại"].text()
            published_books = self.detail_inputs["Sách đã xuất bản"].text()
            status = self.detail_inputs["Trạng thái"].currentText()
            
            self.controller.update_teacher_info(
                self.current_teacher_id,
                self.current_teacher_code,
                job_title,
                education_level,
                research_field,
                research_interests,
                typical_scientific_works,
                prize,
                current_projects,
                published_books,
                status
            )
            
            self.update_table()
            self.display_teacher_info(self.current_teacher_code)
            
            for input_field in self.detail_inputs.values():
                input_field.setEnabled(False)
            
            self.edit_button.setEnabled(True)
            self.save_button.setEnabled(False)
            
            QMessageBox.information(self, "Thành công", "Cập nhật thông tin giảng viên thành công!")
        except Exception as e:
            QMessageBox.critical(self, "Lỗi", f"Không thể cập nhật thông tin giảng viên: {str(e)}")    
    def clear_inputs(self):
        for input_field in [
            self.teacher_id_input, self.full_name_input, self.date_of_birth_input,
            self.gender_input, self.email_input, self.address_input,
            self.phone_number_input, self.enrollment_year_input, self.job_title_input,
            self.education_level_input, self.learning_process_input, self.intro_input,
            self.research_field_input, self.research_interests_input,
            self.typical_scientific_works_input, self.prize_input, self.current_projects_input,
            self.published_books_input
        ]:
            input_field.clear()
            
        self.status_input.setCurrentText("Đang dạy")

    def resizeEvent(self, event):
        self.table.resizeColumnsToContents()
        QWidget.resizeEvent(self, event)
