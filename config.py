import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'signdoc-secret-key-ganti-di-production'
    
    # Konfigurasi MySQL (XAMPP default)
    MYSQL_HOST     = os.environ.get('MYSQL_HOST', 'localhost')
    MYSQL_USER     = os.environ.get('MYSQL_USER', 'root')
    MYSQL_PASSWORD = os.environ.get('MYSQL_PASSWORD', '')
    MYSQL_DB       = os.environ.get('MYSQL_DB', 'signdoc2')
    
    # Folder penyimpanan
    BASE_DIR        = os.path.abspath(os.path.dirname(__file__))
    UPLOAD_FOLDER   = os.path.join(BASE_DIR, 'uploads')
    SIGNATURE_FOLDER = os.path.join(BASE_DIR, 'signatures')
    
    # Ekstensi file yang diizinkan
    ALLOWED_EXTENSIONS = {'pdf', 'txt', 'docx', 'png', 'jpg'}
    
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16 MB
