
import re
from flask_app import app
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)
from flask import render_template, redirect, request, session, flash

from flask_app.models.user import User
from flask_app.models.recipe import Recipe



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():
    if not User.validate_user(request.form):
        return redirect('/')
    data ={
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email'],
        'password': bcrypt.generate_password_hash(request.form['password'])
    }
    id = User.save(data)
    session['user_id'] = id
    return redirect('/dashboard')

@app.route('/logging')
def logging():
    return render_template('Login.html')

@app.route('/login', methods=['POST'])
def login():
    user= User.get_by_email(request.form)

    if not user:
        flash("Invalid Email", "login")
        return redirect('/logging')
    if not bcrypt.check_password_hash(user.password, request.form['password']):
        flash("Invalid Password", "login")
        return redirect('/logging')
    session['user_id'] = user.id
    return redirect('/dashboard')

@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect('/')
    data ={
        'id': session['user_id']
    }
    return render_template("dash.html", user=User.get_by_id(data), recipes=Recipe.get_all())

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

# @app.route('/dojo/<int:id>')
# def show