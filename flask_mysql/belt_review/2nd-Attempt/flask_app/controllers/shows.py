
from flask import render_template, redirect, request, session, flash
from flask_app import app
from flask_app.models.show import Show
from flask_app.models.user import User
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)


@app.route('/shows')
def shows():
    if 'user_id' not in session:
        return redirect('/logout')
    else:
        data={
            "id": session['user_id']
        }
        user= User.get_by_id(data)
        shows = Show.get_all
        return render_template('new_s.html', user=user, shows=shows)

@app.route('/create/show', methods=['POST'])
def create_show():
    if 'user_id' not in session:
        return redirect('/logout')
    if not Show.validate_show(request.form):
        return redirect('/shows')
    data={
        "s_name": request.form['s_name'],
        "network": request.form['network'],
        "release_date": request.form['release_date'],
        "description": request.form['description'],
        "user_id": session['user_id']
    }
    Show.save(data)
    print(data)
    return redirect('/dashboard')

@app.route('/show/edit/<int:id>')
def edit(id):
    if 'user_id' not in session:
        return redirect('/logout')
    else:
        data={
            "id": session['user_id']
        }
        user= User.get_by_id(data)
    data ={
        "id": id
    }
    return render_template('edit.html', show=Show.get_one(data),user=user, shows=shows)

@app.route('/show/delete/<int:id>')
def delete(id):
    data ={
        "id": id
    }
    Show.delete_one(data)
    return redirect('/dashboard')

@app.route('/show/update', methods=['POST'])
def update():
    if not Show.validate_show(request.form):
        update = Show.get_last()
        id = update.id
        return redirect(f'/show/edit/{id}')
    Show.update(request.form)
    
    return redirect('/dashboard')  

@app.route('/show/one/<int:id>')
def one(id):
    if 'user_id' not in session:
        return redirect('/logout')
    else:
        data={
            "id": session['user_id']
        }
        user= User.get_by_id(data)
    data ={
        "id": id
    }
    return render_template('one.html', show=Show.get_one(data),user=user, shows=shows)