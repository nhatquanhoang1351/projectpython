from .database import Database

class ModuleModel(Database):
    def __init__(self):
        super().__init__()
        self.connect()
        self.create_table()

    def create_table(self):
        query = '''
            CREATE TABLE IF NOT EXISTS modules (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                module_code TEXT NOT NULL UNIQUE,   -- Mã học phần
                module_name TEXT NOT NULL,          -- Tên học phần
                duration INTEGER NOT NULL,          -- Thời lượng (giờ)
                credits TEXT NOT NULL,              -- Số tín chỉ
                faculty TEXT NOT NULL,              -- Viện quản lý
                type_module TEXT NOT NULL           -- Loại học phần
            )
        '''
        self.execute(query)

    def add_module(self, module_code, module_name, duration, credits, faculty, type_module):
        query = '''
            INSERT INTO modules (module_code, module_name, duration, credits, faculty, type_module)
            VALUES (?, ?, ?, ?, ?, ?)
        '''
        self.execute(query, (module_code, module_name, duration, credits, faculty, type_module))

    def get_all_modules(self):
        query = 'SELECT * FROM modules'
        return self.fetch_all(query)

    def get_module_by_id(self, module_id):
        query = 'SELECT * FROM modules WHERE id = ?'
        return self.fetch_one(query, (module_id,))

    def get_module_by_code(self, module_code):
        query = 'SELECT * FROM modules WHERE module_code = ?'
        return self.fetch_one(query, (module_code,))

    def search_module_by_name(self, module_name):
        query = 'SELECT * FROM modules WHERE module_name LIKE ?'
        return self.fetch_all(query, (f'%{module_name}%',))

    def delete_module(self, module_id):
        query = 'DELETE FROM modules WHERE id = ?'
        self.execute(query, (module_id,))

    def update_module(self, module_id, module_code, module_name, duration, credits, faculty, type_module):
        query = '''
            UPDATE modules
            SET module_code = ?, module_name = ?, duration = ?, credits = ?, faculty = ?, type_module = ?
            WHERE id = ?
        '''
        self.execute(query, (module_code, module_name, duration, credits, faculty, type_module, module_id))

    def fetch_all(self, query, params=None):
        self.cursor.execute(query, params) if params else self.cursor.execute(query)
        return self.cursor.fetchall()

    def fetch_one(self, query, params=None):
        self.cursor.execute(query, params) if params else self.cursor.execute(query)
        return self.cursor.fetchone()