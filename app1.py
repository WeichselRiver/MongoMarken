from flask import Flask, render_template, redirect, url_for
import pymongo
import ssl
import datetime
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired



client = pymongo.MongoClient(uri, ssl=True)

db = client.Berlin_West   #Select the database
collect = db.Container1 #Select the collection
saetze = db.Satz #Select the collection


app = Flask(__name__)
app.config['SECRET_KEY'] = "secretkey"



class Satz(FlaskForm):
    Beschreibung = StringField('Beschreibung', validators=[DataRequired()])
    Gebiet = StringField('Gebiet', validators=[DataRequired()])
    Jahrgang = IntegerField('Jahrgang')
    MichStart = IntegerField('MichStart')
    MichEnd = IntegerField('MichEnd')


@app.route('/', methods=['GET'])
def get_all():

    output = collect.find()
    tbl_satz = saetze. 


    return render_template("index.html", marken = output, tbl_saetze = tbl_satz)

@app.route('/addSatz', methods=['GET', 'POST'])
def add_Satz():

    form = Satz()
    if form.validate_on_submit():

        ins = {
            'Gebiet' : form.Gebiet.data,
            'Beschreibung' : form.Beschreibung.data,
            'Jahrgang' : form.Jahrgang.data,
            'MichStart' : form.MichStart.data,
            'MichEnd' : form.MichEnd.data,

        }

        saetze.insert_one(ins)
    return render_template('addSatz.html', form = form)


if __name__ == "__main__":
    app.run(debug=True)

#TODO: Überschriften Tabelle **, *, o