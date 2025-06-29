from models.teacher_model import TeacherModel
from controllers.training_institute_controller import TrainingInstituteController

class TeacherController:
    def __init__(self):
        self.model = TeacherModel()
        self.training_institute_controller = TrainingInstituteController()

    def add_teacher(self, teacher_id, full_name, date_of_birth, gender, email, address, phone_number, enrollment_year, job_title, education_level, learning_process, intro, research_field, research_interests, typical_scientific_works, prize, faculty, current_projects, published_books, status):
        self.model.add_teacher(teacher_id, full_name, date_of_birth, gender, email, address, phone_number, enrollment_year, job_title, education_level, learning_process, intro, research_field, research_interests, typical_scientific_works, prize, faculty, current_projects, published_books, status)

    def get_all_teachers(self):
        return self.model.get_all_teachers()
    
    def get_teacher_by_id(self, teacher_id):
        return self.model.get_teacher_by_id(teacher_id)

    def search_teacher_by_name(self, name):
        return self.model.search_teacher_by_name(name)

    def search_all_teacher_by_id(self, teacher_id):
        return self.model.search_all_teacher_by_id(teacher_id)

    def delete_teacher(self, teacher_id):
        self.model.delete_teacher(teacher_id)
    def update_teacher(self, id, teacher_id, full_name, date_of_birth, gender, email, address, phone_number, enrollment_year):
        self.model.update_teacher(id, teacher_id, full_name, date_of_birth, gender, email, address, phone_number, enrollment_year)    
        
    def update_teacher_info(self, id, teacher_id, job_title, education_level, research_field, research_interests, typical_scientific_works, prize, current_projects, published_books, status):
        self.model.update_teacher_info(id, teacher_id, job_title, education_level, research_field, research_interests, typical_scientific_works, prize, current_projects, published_books, status)
    def get_all_training_institutes(self):
        return self.training_institute_controller.get_all_institutes()
    
    def get_training_institute_by_id(self, training_institute_id):
        return self.training_institute_controller.get_institute_by_id(training_institute_id)