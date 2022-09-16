from flask import Flask, render_template, redirect, request, session
# import the class from friend.py
from user import User
app = Flask(__name__)
app.secret_key = "mysecretisasecret"


@app.route("/")
def index():

    return render_template("index.html")

@app.route('/create_user', methods=["POST"])
def create_friend():
    
        session["name"]= request.form["name"],
        session["location"]= request.form["location"],
        session["lang"]= request.form["lang"],
        session["comment"]= request.form["comment"]

    return redirect('/result')
            
@app.route('/result')
def show():
    return render_template('result.html') 

if __name__ == "__main__":
    app.run(debug=True)