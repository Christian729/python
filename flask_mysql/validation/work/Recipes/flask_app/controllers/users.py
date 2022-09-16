from flask_app import app
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)
import re
from flask import render_template, redirect, request, session, flash

from flask_app.models.user import User



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register')
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

@app.route('/login', methods=['POST'])
def login():
    user= User.get_by_email(request.form)

    if not user:
        flash("Invalid Email", "login")
        return redirect('/')
    if not bcrypt.check_password_hash(user.password, request.form['password']):
        flash("Invalid Password", "login")
        return redirect('/')
    session['user_id'] = user.id
    return redirect('/dashboard')


@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect('/logout')
    data ={
        'id': session['user_id']
    }
    return render_template("dash.html", user=User.get_by_id(data))

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')








@app.route('/show/edit/<int:id>')
def edit(id):
    data ={
        "id": id
    }
    return render_template('edit.html', user=User.get_one(data))

@app.route('/show/one/<int:id>')
def one(id):
    data ={
        "id": id
    }
    return render_template('one.html', user=User.get_one(data))

@app.route('/show/update', methods=['POST'])
def update():
    User.update(request.form)
    update = User.get_last()
    id = update.id
    return redirect(f'/show/one/{id}')  

@app.route('/show/delete/<int:id>')
def delete(id):
    data ={
        "id": id
    }
    User.delete_one(data)
    return redirect('/')