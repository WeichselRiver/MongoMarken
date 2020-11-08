from flask import render_template, url_for
from app import app, collect


@app.route('/', methods=['GET'])
def get_all():

    marken = collect.find()

    return render_template("index.html", marken = marken)


@app.route('/AD_BADEN', methods=['GET'])
def AD_Baden():
    marken = []
    return render_template("AD_Baden.html", marken = marken)


@app.route('/AD_Bayern', methods=['GET'])
def AD_Bayern():
    return render_template("AD_Bayern.html")

@app.route('/add_Satz', methods=['GET'])
def add_Satz():
    return "Add Satz"


# @app.route('/addStamp', methods=['GET', 'POST'])
# def add_Stamp():

#     form = Stamp()
#     if form.validate_on_submit():

#         ins = {
#             'id' : form.gebiet.data + str(form.michnr.data),
#             'Gebiet': form.gebiet.data,
#             'Jahrgang': form.jahrgang.data,
#             'Satz' : form.satz.data,
#             'MichNr': form.michnr.data,
#             'Entwertung': form.entwertung.data,
#             'Anzahl' : form.anzahl.data,
#             'Bild' : form.bild.data

#         }

#         collect.insert_one(ins)
#     return render_template('addStamp.html', form=form)


