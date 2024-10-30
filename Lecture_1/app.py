from flask import Flask

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return "<h1>WElcome to HOMEpage !</h1>"

@app.route('/about')

def about():
    return "<h1>WElcome to About Page !</h1>"

@app.route('/welcome/<name>')

def welcome(name):
    return f"HI {name.title()}, hello!"

@app.route('/add/<int:num>')

def add(num):
    return f"Input is {num}, output is {num+10}"


@app.route('/add_two/<int:num1>/<int:num2>')

def add_two(num1,num2):
    return f"Input is {num1}+{num2}, output is {num1+num2}"


if __name__ == '__main__':
    app.run(debug=True)