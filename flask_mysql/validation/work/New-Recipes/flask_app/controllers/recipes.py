
from flask import render_template, redirect, request, session, flash
from flask_app import app
from flask_app.models.recipe import Recipe
from flask_app.models.user import User
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)


@app.route('/recipes')
def recipes():
    if 'user_id' not in session:
        return redirect('/logout')
    else:
        data={
            "id": session['user_id']
        }
        user= User.get_by_id(data)
        recipes = Recipe.get_all
        return render_template('new_r.html', user=user, recipes=recipes)

@app.route('/create/recipe', methods=['POST'])
def create_recipe():
    if 'user_id' not in session:
        return redirect('/logout')
    if not Recipe.validate_recipe(request.form):
        return redirect('/recipes')
    data={
        "name": request.form['name'],
        "description": request.form['description'],
        "instructions": request.form['instructions'],
        "created_on": request.form['created_on'],
        "under": request.form['under'],
        "user_id": session['user_id']
    }
    Recipe.save(data)
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
    return render_template('edit.html', recipe=Recipe.get_one(data),user=user, recipes=recipes)

@app.route('/show/update', methods=['POST'])
def update():
    if not Recipe.validate_recipe(request.form):
        update = Recipe.get_last()
        id = update.id
        return redirect(f'/show/edit/{id}')
    Recipe.update(request.form)
    
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
    return render_template('one.html', recipe=Recipe.get_one(data),user=user, recipes=recipes)