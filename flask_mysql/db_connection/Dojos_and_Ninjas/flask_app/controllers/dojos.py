from flask_app import app

from flask import Flask, render_template, redirect, request

from flask_app.models.dojo import Dojo

@app.route('/')
def index():
    return redirect('/dojo')

@app.route('/dojo')
def show():
    dojos = Dojo.get_all()
    return render_template('index.html', dojos=dojos)



@app.route('/create_dojo', methods=['POST'])
def create_dojo():
    print(request.form)
    data={
        "D_name": request.form['D_name'],
    }
    Dojo.save(data)
    return redirect('/')

# SO i think im having a database problem, I cannot connect to it for the life
# of me. Ill come back to it later

@app.route('/show/one/<int:id>')
def one(id):
    data ={
        "id": id
    }
    dojo = Dojo.get_one_with_ninjas(data)
    return render_template('show.html', dojo=dojo)