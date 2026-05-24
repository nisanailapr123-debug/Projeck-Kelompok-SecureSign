"""
app.py
Main Flask Application
"""

import os

from flask import Flask

from config import Config
from database import init_db

from routes.auth import auth_bp
from routes.document import document_bp
from routes.sign import sign_bp
from routes.verify import verify_bp


# =====================================================
# CREATE APP
# =====================================================

def create_app():

    app = Flask(
        __name__,
        static_folder='static',
        template_folder='templates'
    )

    # =================================================
    # LOAD CONFIG
    # =================================================

    app.config.from_object(Config)

    # =================================================
    # INIT DATABASE
    # =================================================

    init_db(app)

    # =================================================
    # REGISTER BLUEPRINT
    # =================================================

    app.register_blueprint(auth_bp)
    app.register_blueprint(document_bp)
    app.register_blueprint(sign_bp)
    app.register_blueprint(verify_bp)

    # =================================================
    # CREATE REQUIRED FOLDERS
    # =================================================

    os.makedirs(
        app.config['UPLOAD_FOLDER'],
        exist_ok=True
    )

    os.makedirs(
        app.config['SIGNATURE_FOLDER'],
        exist_ok=True
    )

    os.makedirs(
        os.path.join(
            app.static_folder,
            'qrcodes'
        ),
        exist_ok=True
    )

    return app


# =====================================================
# RUN FLASK
# =====================================================

if __name__ == '__main__':

    app = create_app()

    app.run(
        host='0.0.0.0',
        port=5000,
        debug=True
    )