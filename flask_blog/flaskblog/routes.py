
from flask import render_template,url_for,flash,redirect

from flaskblog.forms import RegistrationForm,LoginForm
from flaskblog import app
from flaskblog.models import User,Post
posts=[
    {
        'author':"Asmita Gauri",
        'title':"BLog Post 1",
        'content':"First BLog Post",
        'date_posted':"August 29th 2020"
    },
    {
        'author':"Gauri Asmita",
        'title':"BLog Post 2",
        'content':"Second BLog Post",
        'date_posted':"August 30th 2020"
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html',posts=posts)


@app.route("/about")
def about():
    return render_template('about.html',title='About')


@app.route('/register',methods=['GET','POST'])
def register():
    form=RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!','success')
        return redirect(url_for('home'))
    return render_template('register.html',title='Register',form=form)



@app.route('/login',methods=['GET','POST'])
def login():
    form=LoginForm()
    if form.validate_on_submit():
        if form.email.data=='admin@gmail.com' and form.password.data=='password':
            flash('You have been logged in!','success')
            return redirect(url_for('home'))
        else:
            flash('Login unsucessful, Please check your password and email again','danger')
    return render_template('login.html',title='Login',form=form)
