import time

from flask import Flask,redirect,url_for

app = Flask(__name__)

@app.route('/')

def home():
    return "<h1> Welcome to Home Page </h1>"



@app.route('/passed')

def passed():
    return "Congrats you have passed"

@app.route('/fail')

def fail():
    return "Sorry you have failed"

@app.route('/score/<name>/<int:num>')

def score(name,num):
    if (num<30):
        time.sleep(1)
        #redirect user to page called fail
        return redirect(url_for('fail'))
    else:
        time.sleep(1)
        #redirect to a page called pass
        return redirect(url_for('passed'))

if __name__ == '__main__':
    app.run(debug=True)