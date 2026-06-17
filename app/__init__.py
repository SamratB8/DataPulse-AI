import os
from flask import Flask
from .models import db

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'dev-secret-key-datapulse'
    
    # Configure local SQLite path binding directly to 'app/datapulse.db'
    basedir = os.path.abspath(os.path.dirname(__file__))
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'datapulse.db')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Initialize the SQLAlchemy instance
    db.init_app(app)

    # Register main routes blueprint
    from .routes import main_bp
    app.register_blueprint(main_bp)

    # Automatically run db.create_all() to build our SQLite tables
    with app.app_context():
        db.create_all()

    return app
