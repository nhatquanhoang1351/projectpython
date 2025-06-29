from models.class_model import ClassModel
from controllers.teacher_controller import TeacherController
from controllers.module_controller import ModuleController
from controllers.training_institute_controller import TrainingInstituteController

class ClassController:
    def __init__(self):
        self.model = ClassModel()
        self.teacher_controller = TeacherController()
        self.module_controller = ModuleController()
        self.training_institute_controller = TrainingInstituteController()

    def add_class(self, teacher_id, full_name, semester, faculty, class_code, module_code, module_name, day_of_week, time, weeks, room, registered, max_capacity, status, class_type):
        self.model.add_class(teacher_id, full_name, semester, faculty, class_code, module_code, module_name, day_of_week, time, weeks, room, registered, max_capacity, status, class_type)
    def get_all_classses(self):
        return self.model.get_all_classes()
    def get_class_by_id(self, class_id):
        return self.model.get_class_by_id(class_id)
    def get_class_by_class_code(self, class_code):
        return self.model.get_class_by_class_code(class_code)
    def search_class_by_module_name(self, module_name):
        return self.model.search_class_by_module_name(module_name)
    def delete_class(self, class_id):
        self.model.delete_class(class_id)
    def update_class(self, class_id, teacher_id, full_name, semester, faculty, class_code, module_code, module_name, day_of_week, time, weeks, room, registered, max_capacity, status, class_type):
        self.model.update_class(class_id, teacher_id, full_name, semester, faculty, class_code, module_code, module_name, day_of_week, time, weeks, room, registered, max_capacity, status, class_type)
    def get_class_by_teacher_id(self, teacher_id):
        return self.model.get_class_by_teacher_id(teacher_id)
    def get_all_modules(self):
        return self.module_controller.get_all_modules()
    def get_all_teachers(self):
        return self.teacher_controller.get_all_teachers()
    def get_module_by_id(self, module_id):
        return self.module_controller.get_module_by_id(module_id)
    def get_training_institute_by_id(self, id):
        return self.training_institute_controller.get_institute_by_id(id)
    