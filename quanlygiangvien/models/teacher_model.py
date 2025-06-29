from .database import Database

class TeacherModel(Database):
    def __init__(self):
        super().__init__()
        self.connect()
        self.create_table()

    def create_table(self):
        query = '''
            CREATE TABLE IF NOT EXISTS teachers (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                teacher_id TEXT NOT NULL,           -- Mã giáo viên
                full_name TEXT NOT NULL,            -- Họ và tên
                date_of_birth TEXT NOT NULL,        -- Ngày sinh
                gender TEXT NOT NULL,               -- Giới tính
                email TEXT NOT NULL,                -- Email
                address TEXT NOT NULL,              -- Địa chỉ
                phone_number TEXT NOT NULL,         -- Số điện thoại
                enrollment_year INTEGER NOT NULL,   -- Năm vào trường
                job_title TEXT NOT NULL,            -- Chức vụ
                education_level TEXT NOT NULL,      -- Trình độ học vấn
                learning_process TEXT NOT NULL,     -- Quá trình học tập
                intro TEXT NOT NULL,                -- Giới thiệu
                research_field TEXT NOT NULL,       -- Lĩnh vực nghiên cứu
                research_interests TEXT NOT NULL,   -- Các nghiên cứu quan tâm
                typical_scientific_works TEXT NOT NULL, -- Các công trình khoa học tiêu biểu
                prize TEXT NOT NULL,                -- Các giải thưởng
                faculty TEXT NOT NULL,              -- Khoa/Viện quản lý
                current_projects TEXT NOT NULL,     -- Các dự án hiện tại
                published_books TEXT NOT NULL,      -- Sách đã xuất bản
                status TEXT                        -- Trạng thái
            )
        '''
        self.execute(query)

    def add_teacher(self, teacher_id, full_name, date_of_birth, gender, email, address, phone_number, enrollment_year, job_title, education_level, learning_process, intro, research_field, research_interests, typical_scientific_works, prize, faculty, current_projects, published_books, status):
        query = '''
            INSERT INTO teachers (
                teacher_id, full_name, date_of_birth, gender, email, address, phone_number, enrollment_year, job_title, education_level, learning_process, intro, research_field, research_interests, typical_scientific_works, prize, faculty, current_projects, published_books, status
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        '''
        self.execute(query, (teacher_id, full_name, date_of_birth, gender, email, address, phone_number, enrollment_year, job_title, education_level, learning_process, intro, research_field, research_interests, typical_scientific_works, prize, faculty, current_projects, published_books, status))

    def get_all_teachers(self):
        query = 'SELECT * FROM teachers'
        return self.fetch_all(query)

    def get_teacher_by_id(self, teacher_id):
        query = 'SELECT * FROM teachers WHERE teacher_id = ?'
        return self.fetch_one(query, (teacher_id,))

    def search_teacher_by_name(self, name):
        query = 'SELECT * FROM teachers WHERE full_name LIKE ?'
        return self.fetch_all(query, (f'%{name}%',))
    
    def search_all_teacher_by_id(self, teacher_id):
        query = 'SELECT * FROM teachers WHERE teacher_id = ?'
        return self.fetch_all(query, (teacher_id,))
    
    def delete_teacher(self, teacher_id):
        query = 'DELETE FROM teachers WHERE id = ?'
        self.execute(query, (teacher_id,))
        
    def update_teacher(self, id, teacher_id, full_name, date_of_birth, gender, email, address, phone_number, enrollment_year):
        query = '''
            UPDATE teachers
            SET teacher_id = ?, full_name = ?, date_of_birth =?, gender = ?, email = ?, address = ?, phone_number = ?, enrollment_year = ?
            WHERE id = ?
        '''
        self.execute(query, (teacher_id, full_name, date_of_birth, gender, email, address, phone_number, enrollment_year, id))
            
    def update_teacher_info(self, id, teacher_id, job_title, education_level, research_field, research_interests, typical_scientific_works, prize, current_projects, published_books, status):
        query = '''
            UPDATE teachers
            SET teacher_id = ?, job_title = ?, education_level = ?, research_field = ?, research_interests = ?, typical_scientific_works = ?, prize = ?, current_projects = ?, published_books = ?, status = ?
            WHERE id = ?
        '''
        self.execute(query, (teacher_id, job_title, education_level, research_field, research_interests, typical_scientific_works, prize, current_projects, published_books, status, id))

    def fetch_all(self, query, params=None):
        self.cursor.execute(query, params) if params else self.cursor.execute(query)
        return self.cursor.fetchall()

    def fetch_one(self, query, params=None):
        self.cursor.execute(query, params) if params else self.cursor.execute(query)
        return self.cursor.fetchone()