from flask import(
    Flask,
    render_template,
    redirect,
    flash,
    url_for,
    request,
    make_response
)
from forms import LoginForm

app = Flask(__name__)

app.config["SECRET_KEY"] = "secret_key"

@app.route('/')
@app.route('/home')

def home():
    return render_template("home.html",title="home")

@app.route('/login', methods = ['GET','POST'])

def login():
    form = LoginForm()
    if form.validate_on_submit():
        user_name = form.username.data
        response = make_response("")
        response.set_cookie("user_name",user_name)
        flash(f"Successfully logged in as {user_name.title()}!")
        next_url = request.args.get('next') or url_for("home")
        response.headers["Location"] = next_url
        response.status_code = 302
        return response
   
    return render_template("login.html",title="login",form=form)

@app.route('/about')

def about():
    username = request.cookies.get("user_name")
    if username is None:
        flash("Login Required")
        return redirect(url_for("login", next=request.url))
    else:
        flash(f"Hi {username}, have a good day!")
    return render_template("about.html",title="about")
@app.route('/contact')

def contact():
    username = request.cookies.get("user_name")
    if username is None:
        flash("Login Required")
        return redirect(url_for("login", next=request.url))
    else:
        flash(f"Hi {username}, have a good day!")
    return render_template("contact.html",title="contact")

if __name__ == "__main__":
    app.run(debug=True)
