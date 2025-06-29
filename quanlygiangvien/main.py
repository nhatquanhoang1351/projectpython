import sys
from PyQt6.QtWidgets import QMainWindow, QApplication, QLabel, QListWidgetItem, QWidget, QGridLayout
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QIcon, QPixmap, QFont

from main_ui import Ui_MainWindow
from controllers.teacher_controller import TeacherController
from controllers.module_controller import ModuleController
from controllers.class_controller import ClassController
from controllers.training_institute_controller import TrainingInstituteController

from views.teacher_view import TeacherView
from views.module_view import ModuleView
from views.class_view import ClassView
from views.training_institute_view import TrainingInstituteView
from views.login import LoginWindow  

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.setWindowIcon(QIcon("./icon/Logo.png"))
        self.setWindowTitle("Quản lý giảng viên")

        self.title_label = self.ui.title_label
        self.title_label.setText("Quản lý giảng viên")

        self.title_icon = self.ui.title_icon
        self.title_icon.setText("")
        self.title_icon.setPixmap(QPixmap("./icon/Logo.png"))
        self.title_icon.setScaledContents(True)

        self.side_menu = self.ui.listWidget
        self.side_menu.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.side_menu_icon_only = self.ui.listWidget_icon_only
        self.side_menu_icon_only.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.side_menu_icon_only.hide()

        self.menu_btn = self.ui.menu_btn
        self.menu_btn.setText("")
        self.menu_btn.setIcon(QIcon("./icon/close.svg"))
        self.menu_btn.setIconSize(QSize(30, 30))
        self.menu_btn.setCheckable(True)
        self.menu_btn.setChecked(False)

        self.main_content = self.ui.stackedWidget

        self.menu_list = [
            {
                "name": "Quản lý viện đào tạo",
                "icon": "./icon/training.svg"
            },
            {
                "name": "Quản lý thông tin giảng viên",
                "icon": "./icon/teacher.svg"
            },
            {
                "name": "Quản lý học phần",
                "icon": "./icon/module.svg"
            },
            {
                "name": "Quản lý lớp",
                "icon": "./icon/classes.svg"
            },
            {
                "name": "Đăng xuất",
                "icon": "./icon/logout.svg"
            }
        ]

        self.init_list_widget()
        self.init_stackwidget()
        self.init_single_slot()

    def init_single_slot(self):
        self.menu_btn.toggled['bool'].connect(self.side_menu.setHidden)
        self.menu_btn.toggled['bool'].connect(self.title_label.setHidden)
        self.menu_btn.toggled['bool'].connect(self.side_menu_icon_only.setVisible)
        self.menu_btn.toggled['bool'].connect(self.title_icon.setHidden)

        self.side_menu.currentRowChanged['int'].connect(self.main_content.setCurrentIndex)
        self.side_menu_icon_only.currentRowChanged['int'].connect(self.main_content.setCurrentIndex)
        self.side_menu.currentRowChanged['int'].connect(self.side_menu_icon_only.setCurrentRow)
        self.side_menu_icon_only.currentRowChanged['int'].connect(self.side_menu.setCurrentRow)
        self.menu_btn.toggled.connect(self.button_icon_change)

        self.side_menu.itemClicked.connect(self.on_menu_item_clicked)

    def on_menu_item_clicked(self, item):
        if item.text() == "Đăng xuất":
            self.close()
            self.login_window.show()

    def init_list_widget(self):
        self.side_menu_icon_only.clear()
        self.side_menu.clear()

        for menu in self.menu_list:
            item = QListWidgetItem()
            item.setIcon(QIcon(menu.get("icon")))
            item.setSizeHint(QSize(40, 40))
            self.side_menu_icon_only.addItem(item)
            self.side_menu_icon_only.setCurrentRow(0)

            item_new = QListWidgetItem()
            item_new.setIcon(QIcon(menu.get("icon")))
            item_new.setText(menu.get("name"))
            self.side_menu.addItem(item_new)
            self.side_menu.setCurrentRow(0)

    def init_stackwidget(self):
        widget_list = self.main_content.findChildren(QWidget)
        for widget in widget_list:
            self.main_content.removeWidget(widget)
            
        training_institute_controller = TrainingInstituteController()
        training_institute_view = TrainingInstituteView(training_institute_controller)
        self.main_content.addWidget(training_institute_view)
        
        teacher_controller = TeacherController()
        teacher_view = TeacherView(teacher_controller)
        self.main_content.addWidget(teacher_view)
        
        module_controller = ModuleController()
        module_view = ModuleView(module_controller)
        self.main_content.addWidget(module_view)         
           
        class_controller = ClassController()
        class_view = ClassView(class_controller)
        self.main_content.addWidget(class_view)

        
        # statics_controller = StatisticsController()
        # statics_view = StatisticsView(statics_controller)
        # self.main_content.addWidget(statics_view)   
        
        # predict_view = PredictView()
        # self.main_content.addWidget(predict_view)
        
        # registration_controller = RegistrationSubjectController()
        # registration_view = RegistrationSubjectView(registration_controller)
        # self.main_content.addWidget(registration_view)   


    def button_icon_change(self, status):
        if status:
            self.menu_btn.setIcon(QIcon("./icon/open.svg"))
        else:
            self.menu_btn.setIcon(QIcon("./icon/close.svg"))


if __name__ == '__main__':
    app = QApplication(sys.argv)

    with open("style.qss") as f:
        style_str = f.read()

    app.setStyleSheet(style_str)

    login_window = LoginWindow(on_login_success=lambda: main_window.show())
    main_window = MainWindow()
    main_window.login_window = login_window  

    login_window.show()

    sys.exit(app.exec())