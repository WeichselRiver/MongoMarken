from flask import Flask, render_template, redirect, url_for
from flask_pymongo import PyMongo
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, RadioField 
from wtforms.validators import DataRequired


app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/Briefmarken"
app.config['SECRET_KEY'] = "secretkey"

mongo = PyMongo(app)

class MyForm(FlaskForm):
    gebiete = [('AD Baden', 'AD Baden'), ('Berlin', 'Berlin') ]
    entwertungen = [('**', '**'), ('*', '*'), ('o', 'o')]

    gebiet = SelectField('Gebiet', choices=gebiete)
    michnr = IntegerField('MichNr')
    entwertung = RadioField('Entwertung', choices=entwertungen)
    anzahl = IntegerField('Anzahl', default = 0)

@app.route('/')
def home_page():
    marken = mongo.db.Berlin_West.find({})
    return render_template('index.html', marken=marken)


@app.route('/addStamp', methods =['GET', 'POST'])
def addStamp():
    
    form = MyForm()
    if form.validate_on_submit():

        mongo.db.Briefmarken.insert_one(
            {
            'Gebiet': form.gebiet.data,
            "MichNr" : form.michnr.data,
            "Entwertung" : form.entwertung.data,
            "Anzahl" : form.anzahl.data
            })
        return redirect(url_for('home_page'))
        
    return render_template('addStamp.html', form=form)



if __name__ == "__main__":
    app.run(debug=True)