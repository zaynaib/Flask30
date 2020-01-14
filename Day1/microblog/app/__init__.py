from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# app is an instance of the Flask class
app = Flask(__name__)
app.config.from_object(Config)

#db object that represents the database
db = SQLAlchemy(app)
migrate = Migrate(app,db)


from app import routes, models