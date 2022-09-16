
from flask_app import app

from flask import Flask, render_template, redirect, request

from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja



@app.route('/ninjas')
def make_ninja():
    dojos = Dojo.get_all()
    return render_template('new_ninja.html', dojos=dojos )

@app.route('/create_ninja', methods=["POST"])
def nin_created():
    print(request.form)
    data={
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "age": request.form['age'],
        "dojo_id": request.form['dojo_id']
    }
    Ninja.save(data)

    return redirect('/')

# @app.route('/show/one/<int:id>')
# def one(id):
#     data ={
#         "id": id
#     }
#     return render_template('one.html', ninja=Ninja.get_one(data))
