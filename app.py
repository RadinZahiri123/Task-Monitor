from flask import Flask, flash, render_template, request, redirect, url_for, session
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
import uuid
import os

app = Flask(__name__)
app.secret_key = os.environ.get('my_secret_key')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C:/Users/radin/OneDrive/Pictures/Screenshots 1/JAVA/SoftwareDevelopment/TaskListTemp/instance/mydatabase.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Database models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)

class Task(db.Model):
    id = db.Column(db.String(36), primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    date = db.Column(db.String(10), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    completed = db.Column(db.Boolean, default=False)

@app.route('/', methods=['GET', 'POST'])
def index():
    if 'username' not in session:
        return redirect(url_for('login'))
    
    user = User.query.filter_by(username=session['username']).first()
    if user is None:
        flash('User not found. Please log in again.')
        return redirect(url_for('login'))

    if request.method == 'POST':
        task_name = request.form['task_name']
        task_date = request.form['task_date']
        task_id = str(uuid.uuid4())
        user = User.query.filter_by(username=session['username']).first()
        new_task = Task(id=task_id, name=task_name, date=task_date, user_id=user.id)
        db.session.add(new_task)
        db.session.commit()
        return redirect(url_for('index'))

    tasks = Task.query.filter_by(user_id=user.id).all()
    return render_template('index.html', tasks=tasks)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()

        if user and check_password_hash(user.password_hash, password):
            session['username'] = username
            return redirect(url_for('index'))
        else:
            error = 'Invalid username or password'
            flash(error)
            return render_template('LoginPage.html', error=error)

    return render_template('LoginPage.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        password_hash = generate_password_hash(password)
        new_user = User(username=username, email=email, password_hash=password_hash)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('login'))

    return render_template('Registration.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

@app.route('/add_task', methods=['GET', 'POST'])
def add_task():
    if 'username' not in session:
        return redirect(url_for('login'))
    
    if request.method == 'POST':
        task_name = request.form['task_name']
        task_date = request.form['task_date']
        task_id = str(uuid.uuid4())
        user = User.query.filter_by(username=session['username']).first()
        if user is None:
            flash('User not found. Please log in again.')
            return redirect(url_for('login'))
        new_task = Task(id=task_id, name=task_name, date=task_date, user_id=user.id)
        db.session.add(new_task)
        db.session.commit()
        return redirect(url_for('index')) 

    return render_template('add_task.html')

@app.route('/delete_task/<string:task_id>', methods=['GET'])
def delete_task_route(task_id):
    task = Task.query.get(task_id)
    db.session.delete(task)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/edit_task/<string:task_id>', methods=['GET', 'POST'])
def edit_task(task_id):
    if 'username' not in session:
        return redirect(url_for('login'))

    task = Task.query.get(task_id)
    if task is None:
        return "Task not found", 404

    if request.method == 'POST':
        task.name = request.form['task_name']
        task.date = request.form['task_date']
        db.session.commit()
        return redirect(url_for('index'))

    return render_template('edit_task.html', task=task)

@app.route('/toggle_complete/<string:task_id>', methods=['GET'])
def toggle_complete(task_id):
    task = Task.query.get(task_id)
    if task:
        task.completed = not task.completed
        db.session.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)