from models.training_institute_model import TrainingInstituteModel

class TrainingInstituteController:
    def __init__(self):
        self.model = TrainingInstituteModel()
        
    def add_institute(self, institute_id, name, short_name, address, phone_number, email, website, established_date, head_of_institute, description, status):
        self.model.add_institute(institute_id, name, short_name, address, phone_number, email, website, established_date, head_of_institute, description, status)

    def get_all_institutes(self):
        return self.model.get_all_institutes()
    
    def get_institute_by_id(self, id):
        return self.model.get_institute_by_id(id)
    
    def search_institute_by_name(self, name):
        return self.model.search_institute_by_name(name)
    
    def delete_institute(self, id):
        self.model.delete_institute(id)
        
    def update_institute_info(self, id, institute_id, name, short_name, address, phone_number, email, website, established_date, head_of_institute, description, status):
        self.model.update_institute_info(id, institute_id, name, short_name, address, phone_number, email, website, established_date, head_of_institute, description, status)
        