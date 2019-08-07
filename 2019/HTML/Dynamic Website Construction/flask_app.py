
# A very simple Flask Hello World app for you to get started with...

from flask import Flask, render_template, flash, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config["SECRET_KEY"] = "P@55w0rd";
SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://{username}:{password}@{hostname}/{databasename}".format(
    username="<username>",
    password="<password>",
    hostname="<hostname>",
    databasename="<databasename>",
)
app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
app.config["SQLALCHEMY_POOL_RECYCLE"] = 299
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

class Comment(db.Model):
    __tablename__ = "comments"
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(4069))

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        return '<User {}>'.format(self.username)

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

user=None

@app.route('/')
@app.route("/index")
def hello_world():
    title = None
    posts = [
        {
            'author' : {'username': "Bob"},
            'body' : "I like cats!"
        },
        {
            'author': {'username': "Karen"},
            'body' : "I also like cats!"
        }
    ]
    return render_template("index2.html", user=user, title=title, posts=posts)


@app.route("/bar")
def bar():
    return "Go away"

@app.route("/login2", methods=['GET', 'POST'])
def login2():
    form = LoginForm()
    if form.validate_on_submit():
        flash(f"Login requested for user {form.username.data}")
        return redirect("/index")
    return render_template("login2.html", title="Sign in", form = form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash(f"Login request for user {form.username.data}, remember_me={form.remember_me.data}")
        user = {'username': form.username.data}
        return redirect(url_for('hello_world'))
    return render_template("login.html", title="sign in", form=form)
