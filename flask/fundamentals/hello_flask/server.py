from flask import Flask, render_template
app = Flask(__name__)

@app.route('/main_page')
def index():
    return "Hello World!"

@app.route('/account/<int:acct_num>')
def account(acct_num):
    return "Account #" + str(acct_num)

@app.route('/faq')
def faq():
    return render_template("faq.html")

@app.route('/hello/<string:banana>/<int:num>')
def hello(banana,num):
    return render_template("hello.html", banana=banana,num= num)


@app.route('/lists')
def render_lists():
    # Soon enough, we'll get data from a database, but for now, we're hard coding data
    student_info = [
        {'name' : 'Michael', 'age' : 35},
        {'name' : 'John', 'age' : 30 },
        {'name' : 'Mark', 'age' : 25},
        {'name' : 'KB', 'age' : 27}
    ]
    return render_template("lists.html", random_numbers = [3,1,5], students = student_info)

if __name__ == "__main__":
    app.run(debug=True)