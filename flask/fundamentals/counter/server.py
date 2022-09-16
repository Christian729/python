from flask import Flask, render_template, redirect, session
app = Flask(__name__)
app.secret_key = 'supersecret'

@app.route('/')
def index():
    if 'count' not in session:
        session ['count'] = 0
    else:
        session ['count'] += 1
    return render_template("Index.html")

@app.route('/destroy_session')
def reset():
    session.clear()
    return redirect('/')

@app.route('/add_two')
def add_two():
    session['count'] += 1
    return redirect('/')









if __name__== "__main__":
    app.run(debug=True)