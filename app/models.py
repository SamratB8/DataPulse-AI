from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    password_hash = db.Column(db.String(256), nullable=False)
    archetype = db.Column(db.String(64), default='Wrangler')
    
    # Experience Counters
    data_engineering_xp = db.Column(db.Integer, default=0)
    machine_learning_xp = db.Column(db.Integer, default=0)
    deep_learning_xp = db.Column(db.Integer, default=0)
    mlops_xp = db.Column(db.Integer, default=0)

    # Relationships
    notebook_logs = db.relationship('NotebookLog', backref='user', lazy=True)
    quests = db.relationship('Quest', backref='user', lazy=True)
    arena_stats = db.relationship('MathArenaStat', backref='user', lazy=True)

class NotebookLog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    filename = db.Column(db.String(128), nullable=False)
    upload_time = db.Column(db.DateTime, default=datetime.utcnow)
    score = db.Column(db.Integer, default=0)

class Quest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    title = db.Column(db.String(128), nullable=False)
    description = db.Column(db.Text)
    is_completed = db.Column(db.Boolean, default=False)

class MathArenaStat(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    streak_days = db.Column(db.Integer, default=0)
    total_solved = db.Column(db.Integer, default=0)
    last_played = db.Column(db.DateTime, default=datetime.utcnow)