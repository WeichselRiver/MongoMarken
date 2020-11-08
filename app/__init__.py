from flask import Flask, render_template, redirect, url_for
import pymongo
import ssl
import datetime
from flask_wtf import FlaskForm
from flask_wtf.file import FileField
from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config.from_object("config.Config")

client = pymongo.MongoClient(app.config['DB_URL'], ssl=True)


db = client.Berlin_West  # Select the database

collect = db.Container1  # Select the collection


from app import views
