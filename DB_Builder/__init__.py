from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, migrate
from dotenv import load_dotenv

import os

app = Flask(__name__)

load_dotenv('./DB_Builder/.env')

app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

DB_USER= os.getenv('DB_USER')
DB_PASS= os.getenv('DB_PASS')
DB_URL= os.getenv('DB_URL')
DB_PORT= os.getenv('DB_PORT')
DB_NAME= os.getenv('DB_NAME')

app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql+psycopg2://{DB_USER}:{DB_PASS}@{DB_URL}:{DB_PORT}/{DB_NAME}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from DB_Builder.models import Users

