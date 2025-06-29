from .database import Database

class TrainingInstituteModel(Database):
    def __init__(self):
        super().__init__()
        self.connect()
        self.create_table()

    def create_table(self):
        query = '''
            CREATE TABLE IF NOT EXISTS training_institute (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                institute_id TEXT NOT NULL,         -- Mã viện
                name TEXT NOT NULL,                 -- Tên viện
                short_name TEXT NOT NULL,           -- Tên viết tắt
                address TEXT NOT NULL,              -- Địa chỉ
                phone_number TEXT NOT NULL,         -- Số điện thoại
                email TEXT NOT NULL,                -- Email liên hệ
                website TEXT,                       -- Website viện
                established_date TEXT,              -- Ngày thành lập
                head_of_institute TEXT,             -- Trưởng viện
                description TEXT,                   -- Mô tả ngắn gọn về viện
                status TEXT NOT NULL                -- Trạng thái hoạt động
            )
        '''
        self.execute(query)

    def add_institute(self, institute_id, name, short_name, address, phone_number, email, website, established_date, head_of_institute, description, status):
        query = '''
            INSERT INTO training_institute (
                institute_id, name, short_name, address, phone_number, email, website, established_date, head_of_institute, description, status
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        '''
        self.execute(query, (institute_id, name, short_name, address, phone_number, email, website, established_date, head_of_institute, description, status))

    def get_all_institutes(self):
        query = 'SELECT * FROM training_institute'
        return self.fetch_all(query)

    def get_institute_by_id(self, id):
        query = 'SELECT * FROM training_institute WHERE id = ?'
        return self.fetch_one(query, (id,))

    def search_institute_by_name(self, name):
        query = 'SELECT * FROM training_institute WHERE name LIKE ?'
        return self.fetch_all(query, (f'%{name}%',))
    
    def delete_institute(self, id):
        query = 'DELETE FROM training_institute WHERE id = ?'
        self.execute(query, (id,))

    def update_institute_info(self, id, institute_id, name, short_name, address, phone_number, email, website, established_date, head_of_institute, description, status):
        query = '''
            UPDATE training_institute
            SET institute_id = ?, name = ?, short_name = ?, address = ?, phone_number = ?, email = ?, website = ?,
                established_date = ?, head_of_institute = ?, description = ?, status = ?
            WHERE id = ?
        '''
        print("Đã update SQL trong model")
        self.execute(query, (institute_id, name, short_name, address, phone_number, email, website, established_date, head_of_institute, description, status, id))
        
    def fetch_all(self, query, params=None):
        if params:
            self.cursor.execute(query, params)
        else:
            self.cursor.execute(query)
        return self.cursor.fetchall()

    def fetch_one(self, query, params=None):
        if params:
            self.cursor.execute(query, params)
        else:
            self.cursor.execute(query)
        return self.cursor.fetchone()
