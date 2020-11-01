from flask import Flask, render_template, redirect, url_for
import pymongo
import ssl
import datetime
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired
import conf


uri = "mongodb://marken:6kwieS9bXJhgqXJL9tvzdl7F4b4s8S37ZssSuhdfb4zQOUzNWYqcRMzPsd4HwxllXlnq1spJJ1J8GAZPoZ69JQ==@marken.mongo.cosmos.azure.com:10255/?ssl=true&replicaSet=globaldb&maxIdleTimeMS=120000&appName=@marken@&retrywrites=false"
client = pymongo.MongoClient(uri, ssl=True)

db = client.Berlin_West  # Select the database
collect = db.Container1  # Select the collection
saetze = db.Satz  # Select the collection


app = Flask(__name__)
app.config['SECRET_KEY'] = conf.secret_key


class Satz(FlaskForm):
    Beschreibung = StringField('Beschreibung', validators=[DataRequired()])
    Gebiet = StringField('Gebiet', validators=[DataRequired()])
    Jahrgang = IntegerField('Jahrgang')
    MichStart = IntegerField('MichStart')
    MichEnd = IntegerField('MichEnd')


@app.route('/', methods=['GET'])
def get_all():

    output = collect.find()
    tbl_satz = saetze.find()
    print(tbl_satz[0])
    #tbl_satz = [satz['Jahrgang'] for satz in saetze.find()]

    return render_template("index.html", marken=output, tbl_saetze=tbl_satz)


@app.route('/AD_Baden', methods=['GET'])
def AD_Baden():
    sets = saetze.aggregate([
        {"$group": {"_id": "$Jahrgang", "books": {"$push": "$$ROOT" }}}
    ])
 
    return render_template("AD_Baden.html", sets=sets)


@app.route('/AD_Bayern', methods=['GET'])
def AD_Bayern():
    return render_template("AD_Bayern.html")


@app.route('/addSatz', methods=['GET', 'POST'])
def add_Satz():

    form = Satz()
    if form.validate_on_submit():

        ins = {
            'Gebiet': form.Gebiet.data,
            'Beschreibung': form.Beschreibung.data,
            'Jahrgang': form.Jahrgang.data,
            'MichStart': form.MichStart.data,
            'MichEnd': form.MichEnd.data,

        }

        saetze.insert_one(ins)
    return render_template('addSatz.html', form=form)


if __name__ == "__main__":
    app.run(debug=True)

# TODO: Überschriften Tabelle **, *, o
