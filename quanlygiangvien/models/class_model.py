from .database import Database

class ClassModel(Database):
    def __init__(self):
        super().__init__()
        self.connect()
        self.create_table()

    def create_table(self):
        query = '''
            CREATE TABLE IF NOT EXISTS classes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                teacher_id TEXT NOT NULL,        -- Mã giáo viên
                full_name TEXT NOT NULL,         -- Họ và tên giảng viên
                semester TEXT NOT NULL,          -- Kỳ
                faculty TEXT NOT NULL,           -- Viện
                class_code TEXT NOT NULL,        -- Mã lớp
                module_code TEXT NOT NULL,       -- Mã học phần
                module_name TEXT NOT NULL,       -- Tên học phần
                day_of_week TEXT NOT NULL,       -- Thứ
                time TEXT NOT NULL,              -- Thời gian
                weeks TEXT NOT NULL,             -- Tuần
                room TEXT NOT NULL,              -- Phòng học
                registered INTEGER NOT NULL,     -- Số lượng đăng ký
                max_capacity INTEGER NOT NULL,   -- Số lượng tối đa
                status TEXT NOT NULL,            -- Trạng thái
                class_type TEXT NOT NULL         -- Loại lớp
            )
        '''
        self.execute(query)

    def add_class(self, teacher_id, full_name, semester, faculty, class_code, module_code, module_name, day_of_week, time, weeks, room, registered, max_capacity, status, class_type):
        query = '''
            INSERT INTO classes (
                teacher_id, full_name, semester, faculty, class_code, module_code, module_name, day_of_week, time, weeks, room, registered, max_capacity, status, class_type
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        '''
        self.execute(query, (teacher_id, full_name, semester, faculty, class_code, module_code, module_name, day_of_week, time, weeks, room, registered, max_capacity, status, class_type))

    def get_all_classes(self):
        query = 'SELECT * FROM classes'
        return self.fetch_all(query)

    def get_class_by_id(self, class_id):
        query = 'SELECT * FROM classes WHERE id = ?'
        return self.fetch_one(query, (class_id,))

    def get_class_by_class_code(self, class_code):
        query = 'SELECT * FROM classes WHERE class_code = ?'
        return self.fetch_one(query, (class_code,))

    def search_class_by_module_name(self, module_name):
        query = 'SELECT * FROM classes WHERE module_name LIKE ?'
        return self.fetch_all(query, (f'%{module_name}%',))
    
    def get_class_by_teacher_id(self, teacher_id):
        query = 'SELECT * FROM classes WHERE teacher_id = ?'
        return self.fetch_all(query, (teacher_id,))

    def delete_class(self, class_id):
        query = 'DELETE FROM classes WHERE id = ?'
        self.execute(query, (class_id,))

    def update_class(self, class_id, teacher_id, full_name, semester, faculty, class_code, module_code, module_name, day_of_week, time, weeks, room, registered, max_capacity, status, class_type):
        query = '''
            UPDATE classes
            SET teacher_id = ?, full_name = ?, semester = ?, faculty = ?, class_code = ?, module_code = ?, module_name = ?, day_of_week = ?, time = ?, weeks = ?, room = ?, registered = ?, max_capacity = ?, status = ?, class_type = ?
            WHERE id = ?
        '''
        self.execute(query, (teacher_id, full_name, semester, faculty, class_code, module_code, module_name, day_of_week, time, weeks, room, registered, max_capacity, status, class_type, class_id))

    def fetch_all(self, query, params=None):
        self.cursor.execute(query, params) if params else self.cursor.execute(query)
        return self.cursor.fetchall()

    def fetch_one(self, query, params=None):
        self.cursor.execute(query, params) if params else self.cursor.execute(query)
        return self.cursor.fetchone()