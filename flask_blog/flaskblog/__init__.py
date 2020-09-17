from flask import Flask
# url_for accepts the name of the function you want to pass the control to
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
app=Flask(__name__)
# initializing flask

# In databse we are gonna use sqlite which has data structure in form of classes also callled as models.
# to prevent the forms from forgery attacks we need to provide a secret key
# in cmd line
# import secrets
# secrets.token_hex(16)



app.config['SECRET_KEY']='9ae07d1837a5a3333786463b73ab6d0c'
app.config['SQLALCHEMY_DATABASE_URI']="sqlite:///site.db"

db=SQLAlchemy(app)
bcrypt=Bcrypt(app)
login_manager=LoginManager(app)
login_manager.login_view='login'
login_manager.login_message_category="info"
from flaskblog import routes
