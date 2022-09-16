
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

@app.route('/user/create_user', methods=['POST'])
def Create():
    if not User.validate_user(request.form):
        return redirect('/show/new_user')
    data ={
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email']
    }
    User.save(data)
    Create = User.get_last()
    id = Create.id
    return redirect(f'/show/one/{id}')


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