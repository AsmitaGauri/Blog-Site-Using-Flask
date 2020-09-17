
from flask import render_template,url_for,flash,redirect,request

from flaskblog.forms import RegistrationForm,LoginForm
from flaskblog import app,db,bcrypt
from flaskblog.models import User,Post
from flask_login import login_user,current_user,logout_user,login_required
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
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form=RegistrationForm()
    if form.validate_on_submit():
        hashed_pw=bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user=User(username=form.username.data,email=form.email.data,password=hashed_pw)
        db.session.add(user)
        db.session.commit()
        flash('You have successfully registered! Wohooooo!!','success')
        return redirect(url_for('login'))
    return render_template('register.html',title='Register',form=form)



@app.route('/login',methods=['GET','POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form=LoginForm()
    if form.validate_on_submit():
        user=User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password,form.password.data):
            login_user(user,remember=form.remember.data)
            flash('Login sucessfull, Wohoooo!!','success')
            request_page=request.args.get('next')

            return redirect(request_page) if request_page else redirect(url_for('home'))
        else:
            flash('Login unsucessful, Please check your email and password again','danger')
    return render_template('login.html',title='Login',form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route('/account')
@login_required
def account():
    return render_template('account.html',title="Account")
