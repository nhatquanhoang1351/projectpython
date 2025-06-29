from models.module_model import ModuleModel
from controllers.training_institute_controller import TrainingInstituteController

class ModuleController:
    def __init__(self):
        self.model = ModuleModel()
        self.training_institute_controller = TrainingInstituteController()
        
    def add_module(self, module_code, module_name, duration, credits, faculty, type_module):
        self.model.add_module(module_code, module_name, duration, credits, faculty, type_module)
        
    def get_all_modules(self):
        return self.model.get_all_modules()
    
    def get_module_by_id(self, module_id):
        return self.model.get_module_by_id(module_id)
    
    def get_module_by_code(self, module_code):
        return self.model.get_module_by_code(module_code)
    
    def search_module_by_name(self, module_name):
        return self.model.search_module_by_name(module_name)
    
    def delete_module(self, module_id):
        self.model.delete_module(module_id)
        
    def update_module(self, module_id, module_code, module_name, duration, credits, faculty, type_module):
        self.model.update_module(module_id, module_code, module_name, duration, credits, faculty, type_module)
    
    def fetch_all_training_institute(self):
        return self.training_institute_controller.get_all_institutes()