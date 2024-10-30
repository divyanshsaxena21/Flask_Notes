import time

from flask import Flask,redirect,url_for

app = Flask(__name__)

@app.route('/')

def home():
    return "<h1> Welcome to Home Page </h1>"



@app.route('/passed/<sname>/<int:marks>')

def passed(sname,marks):
    return f"Congrats {sname.title()} you have passed {marks}"

@app.route('/fail/<sname>/<int:marks>')

def fail(sname,marks):
    return f"Sorry {sname.title()} you have failed {marks}"

@app.route('/score/<name>/<int:num>')

def score(name,num):
    if (num<30):
        time.sleep(1)
        #redirect user to page called fail
        return redirect(url_for('fail',sname=name,marks=num))
    else:
        time.sleep(1)
        #redirect to a page called pass
        return redirect(url_for('passed',sname=name,marks=num))

if __name__ == '__main__':
    app.run(debug=True)