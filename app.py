
from database import create_tables
from Seed import seed_all
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os
from sqlalchemy import event
from sqlalchemy.engine import Engine

from isolation_test import isolation_test
from performance_tests import performance_test_create_users

load_dotenv()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URL")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

@event.listens_for(Engine, "connect")
def set_search_path(dbapi_connection, connection_record):
    cursor = dbapi_connection.cursor()
    cursor.execute('SET search_path TO "Venture"')
    cursor.close()

if __name__ == "__main__":
    #create_tables()
    #seed_all()
    isolation_test()
    #performance_test_create_users()





