from flask import render_template, redirect, request, session, flash
from flask_app import app
from flask_app.models.thought import Thought
from flask_app.models.user import User
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)


@app.route('/thoughts')
def thoughts():
    if 'user_id' not in session:
        return redirect('/logout')
    else:
        data={
            "id": session['user_id']
        }
        user= User.get_by_id(data)
        thoughts = Thought.get_all()
        return render_template('dash.html', user=user, thoughts=thoughts)

@app.route('/create/thought', methods=['POST'])
def create_thought():
    if 'user_id' not in session:
        return redirect('/logout')
    if not Thought.validate_thought(request.form):
        return redirect('/thoughts')
    data={
        "description": request.form['description'],
        "user_id": session['user_id']
    }
    Thought.save(data)
    print(data)
    return redirect('/dashboard')

# @app.route('/show/edit/<int:id>')
# def edit(id):
#     if 'user_id' not in session:
#         return redirect('/logout')
#     else:
#         data={
#             "id": session['user_id']
#         }
#         user= User.get_by_id(data)
#     data ={
#         "id": id
#     }
#     return render_template('edit.html', thought=Thought.get_one(data),user=user, thoughts=thoughts)

# added a delete
@app.route('/show/delete/<int:id>')
def delete(id):
    data ={
        "id": id
    }
    Thought.delete_one(data)
    return redirect('/dashboard')

@app.route('/show/one/<int:id>')
def thought(id):
    if 'user_id' not in session:
        return redirect('/logout')
    else:
        data={
            "id": session['user_id']
        }
    dog={
        "id": id
    }
    user= User.get_one_with_thoughts(dog)
    
    return render_template('one.html', logged_user= User.get_by_id(data), user=user)

    # at this point i didnt really know what to do next, i got very stuck with implementing 
    # different associated classes. Im sure i made some simple mistakes but im just not seeing it at the moment