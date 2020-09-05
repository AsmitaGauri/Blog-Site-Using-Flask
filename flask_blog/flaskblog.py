from flask import Flask,render_template,url_for,flash,redirect
# url_for accepts the name of the function you want to pass the control to
from forms import RegistrationForm,LoginForm
app=Flask(__name__)
# initializing flask


# to prevent the forms from forgery attacks we need to provide a secret key
# in cmd line
# import secrets
# secrets.token_hex(16)
app.config['SECRET_KEY']='9ae07d1837a5a3333786463b73ab6d0c'

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


if __name__=='__main__':
    app.run(debug=True)