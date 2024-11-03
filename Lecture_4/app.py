from flask import Flask,render_template,url_for,redirect,flash
from forms import SignupForm, LoginForm

app = Flask(__name__)
app.config["SECRET_KEY"] = "this is our secret key"
@app.route('/')
@app.route('/home')

def home():
    return render_template("home.html",title="Home")

@app.route('/signup',methods=["GET","POST"])

def signup():
    form = SignupForm()
    if form.validate_on_submit():
        flash(f"Successfully Registered {form.username.data}!")
        return  redirect(url_for('home'))

    return render_template("signup.html",title="Signup",form=form)
    

@app.route('/login', methods=["GET","POST"])

def login():
    form = LoginForm()
    email = form.email.data
    pw = form.password.data
    if form.validate_on_submit():
        if email=="a@b.com" and pw == "12345":
            flash(f"Successfully logged in {email}")
            return redirect(url_for("home"))
        else:
            flash("Invalid Credentials")
    return render_template("login.html",title="Login",form=form)

if  __name__ == '__main__':
    app.run(debug=True)
