
from flask_app import app

from flask import Flask, render_template, redirect, request

from flask_app.models.user import User
from flask_app.models.recipe import Recipe



# @app.route('/recipe')
# def make_recipe():
#     users = User.get_all()
#     return render_template('new_ninja.html', users=users )

# @app.route('/create_recipe', methods=["POST"])
# def rec_created():
#     print(request.form)
#     data={
#         "name": request.form['name'],
#         "description": request.form['description'],
#         "instructions": request.form['instructions'],
#         "under": request.form['under'],
#         "user_id": request.form['user_id']
#     }
#     Recipe.save(data)

#     return redirect('/')