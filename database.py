import pymysql
pymysql.install_as_MySQLdb()
import pymysql as MySQLdb
from flask import g, current_app

def get_db():
    """Ambil koneksi database dari context aplikasi."""
    if 'db' not in g:
        g.db = MySQLdb.connect(
            host=current_app.config['MYSQL_HOST'],
            user=current_app.config['MYSQL_USER'],
            passwd=current_app.config['MYSQL_PASSWORD'],
            db=current_app.config['MYSQL_DB'],
            charset='utf8mb4'
        )
    return g.db

def close_db(e=None):
    db = g.pop('db', None)
    if db is not None:
        db.close()

def init_db(app):
    """Inisialisasi tabel database jika belum ada."""
    app.teardown_appcontext(close_db)

    with app.app_context():
        # Buat database jika belum ada
        conn = MySQLdb.connect(
            host=app.config['MYSQL_HOST'],
            user=app.config['MYSQL_USER'],
            passwd=app.config['MYSQL_PASSWORD'],
            charset='utf8mb4'
        )
        cursor = conn.cursor()
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {app.config['MYSQL_DB']} CHARACTER SET utf8mb4")
        conn.select_db(app.config['MYSQL_DB'])

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id         INT AUTO_INCREMENT PRIMARY KEY,
                username   VARCHAR(80)  NOT NULL UNIQUE,
                password   VARCHAR(255) NOT NULL,
                public_key TEXT         NOT NULL,
                private_key TEXT        NOT NULL,
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP
            ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS documents (
                id         INT AUTO_INCREMENT PRIMARY KEY,
                user_id    INT          NOT NULL,
                filename   VARCHAR(255) NOT NULL,
                file_hash  TEXT         NOT NULL,
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (user_id) REFERENCES users(id)
            ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS signatures (
                id          INT AUTO_INCREMENT PRIMARY KEY,
                document_id INT  NOT NULL,
                user_id     INT  NOT NULL,
                signature   TEXT NOT NULL,
                created_at  DATETIME DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (document_id) REFERENCES documents(id),
                FOREIGN KEY (user_id)     REFERENCES users(id)
            ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4
        """)

        conn.commit()
        cursor.close()
        conn.close()
