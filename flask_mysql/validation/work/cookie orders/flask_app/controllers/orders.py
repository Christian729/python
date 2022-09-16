from flask_app import app

from flask import render_template, redirect, request

from flask_app.models.order import Order



@app.route('/')
def index():
    return redirect('/show')

@app.route('/show')
def show():
    return render_template('index.html', orders=Order.get_all())

@app.route('/show/new_order')
def new_page():
    
    return render_template('create.html')

@app.route('/user/create_order', methods=['POST'])
def Create():
    if not Order.validate_order(request.form):
        return redirect('/show/new_order')
    data ={
        'name': request.form['name'],
        'cookie_type': request.form['cookie_type'],
        'num_box': request.form['num_box']
    }
    Order.save(data)

    return redirect('/')

#new code

@app.route('/show/edit/<int:id>')
def edit(id):
    data ={
        "id": id
    }
    return render_template('edit.html', order=Order.get_one(data))

@app.route('/show/one/<int:id>')
def one(id):
    data ={
        "id": id
    }
    return render_template('one.html', order=Order.get_one(data))

@app.route('/show/update', methods=['POST'])
def update():
    print(request.form)
    id= request.form['id']
    data = {
        "id": id,
        "name": request.form['name'],
        "cookie_type": request.form["cookie_type"],
        'num_box': request.form['num_box']
    }
    if not Order.validate_order(request.form):
        return redirect(f'/show/edit/{id}')
    Order.update(data)
    return redirect('/')  

@app.route('/show/delete/<int:id>')
def delete(id):
    data ={
        "id": id
    }
    Order.delete_one(data)
    return redirect('/')