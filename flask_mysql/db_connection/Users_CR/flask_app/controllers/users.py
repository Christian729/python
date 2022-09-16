
from flask_app import app

from flask import render_template, redirect, request

from flask_app.models.user import User



@app.route('/')
def index():
    return redirect('/show')

@app.route('/show')
def show():
    return render_template('index.html', users=User.get_all())

@app.route('/show/new_user')
def new_page():
    
    return render_template('create.html')

@app.route('/user/create_user', methods=['post'])
def Create():
    User.save(request.form)
    return redirect('/')

