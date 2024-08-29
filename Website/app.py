from flask import Flask, request, redirect, url_for, render_template, session, flash
from werkzeug.utils import secure_filename
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import os
from config import Config

app = Flask(__name__)
app.config.from_object('config.Config')
db = SQLAlchemy(app)

# Ensure the uploads directory exists
if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    resume = db.Column(db.String(120), nullable=True)
    job_title = db.Column(db.String(120), nullable=True)
    experience = db.Column(db.String(120), nullable=True)
    skills = db.Column(db.String(250), nullable=True)
    cover_letter = db.Column(db.Text, nullable=True)

    def __repr__(self):
        return f'<User {self.name}>'

@app.route('/')
def index():
    if 'user_id' in session:
        user = User.query.get(session['user_id'])
        if user.job_title:
            return redirect(url_for('view_submission'))
        else:
            return redirect(url_for('job_details'))
    return redirect(url_for('login'))

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']

        existing_user = User.query.filter_by(email=email).first()
        if existing_user is None:
            hashed_password = generate_password_hash(password, method='pbkdf2:sha256')
            new_user = User(name=name, email=email, password=hashed_password)
            db.session.add(new_user)
            db.session.commit()
            session['user_id'] = new_user.id
            return redirect(url_for('job_details'))
        else:
            flash("User already exists! Please log in.", "warning")
            return redirect(url_for('login'))
    
    return render_template('signup.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                session['user_id'] = user.id
                return redirect(url_for('index'))
            else:
                flash("Incorrect password. Please try again.", "danger")
        else:
            flash("User does not exist. Please sign up.", "warning")
    
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('user_id', None)
    return redirect(url_for('login'))

@app.route('/job_details', methods=['GET', 'POST'])
def job_details():
    if 'user_id' not in session:
        return redirect(url_for('login'))

    user = User.query.get(session['user_id'])
    
    # Prevent user from filling out the form again if already filled
    if user.job_title:
        flash("You have already submitted your job application. You cannot change it.", "warning")
        return redirect(url_for('view_submission'))

    if request.method == 'POST':
        # Filling out the job details form and uploading resume
        user.job_title = "Software Engineer"
        user.experience = request.form['experience']
        user.skills = request.form['skills']
        user.cover_letter = request.form['cover_letter']
        
        file = request.files['resume']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)
            user.resume = filename
        
        db.session.commit()
        flash("Job details submitted successfully!", "success")
        return redirect(url_for('view_submission'))
    
    return render_template('job_details.html')

@app.route('/view_submission')
def view_submission():
    if 'user_id' not in session:
        return redirect(url_for('login'))

    user = User.query.get(session['user_id'])
    return render_template('view_submission.html', user=user)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
