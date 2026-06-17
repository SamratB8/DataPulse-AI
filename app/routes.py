from flask import Blueprint, render_template, redirect, url_for, request, flash, session
from werkzeug.security import generate_password_hash, check_password_hash
from .models import db, User, Quest, NotebookLog, MathArenaStat

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    # Will render index layout when templates are ready
    return render_template('index.html') if 'index.html' else "DataPulse AI - Index"

@main_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        archetype = request.form.get('archetype', 'Wrangler')
        
        if User.query.filter_by(username=username).first():
            flash('Username already exists.')
            return redirect(url_for('main.register'))
            
        hashed_pw = generate_password_hash(password)
        new_user = User(username=username, password_hash=hashed_pw, archetype=archetype)
        db.session.add(new_user)
        db.session.commit()
        flash('Registration successful! Please log in.')
        return redirect(url_for('main.login'))
        
    return render_template('register.html')

@main_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password_hash, password):
            session['user_id'] = user.id
            flash('Logged in successfully.')
            return redirect(url_for('main.dashboard'))
            
        flash('Invalid credentials.')
        return redirect(url_for('main.login'))
        
    return render_template('login.html')

@main_bp.route('/logout')
def logout():
    session.pop('user_id', None)
    flash('You have been logged out.')
    return redirect(url_for('main.index'))

@main_bp.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        flash('Please log in to access the dashboard.')
        return redirect(url_for('main.login'))
        
    user = User.query.get(session['user_id'])
    quests = Quest.query.filter_by(user_id=user.id, is_completed=False).all()
    recent_logs = NotebookLog.query.filter_by(user_id=user.id).order_by(NotebookLog.upload_time.desc()).limit(5).all()
    
    return render_template('dashboard.html', user=user, quests=quests, recent_logs=recent_logs)
