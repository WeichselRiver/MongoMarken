
from flask import Flask, jsonify
import ssl
import datetime
from flask_pymongo import PyMongo

app = Flask(__name__)


# client = pymongo.MongoClient(uri, ssl=True)
mongo = PyMongo(app)


@app.route('/', methods=['GET'])
def get_all():
  star = mongo.db.Container1
  output = []
  for s in star.find():
    output.append({'name' : s['MichNr']})
  return output



#collect = db.Container1 #Select the collection



# @app.route('/')
# def hello_world():
#     """Print 'Hello, world!' as the response body."""
#     return 'Hello, world!'


# @app.route('/')
# def home_page():
#     return str(collect.find_one())

# @app.route('/berlin_west')
# def berlin_west():
#     marken = db.Berlin_West.find()
#     return render_template('berlin_west.html', marken=marken, title = "Berlin West")


# @app.route('/addStamp', methods =['GET', 'POST'])
# def addStamp():
    
#     form = MyForm()
#     if form.validate_on_submit():

#         db.Berlin_West.insert_one(
#             {
#             'Gebiet': form.gebiet.data,
#             "MichNr" : form.michnr.data,
#             "Entwertung" : form.entwertung.data,
#             "Anzahl" : form.anzahl.data
#             })
#     return redirect(url_for('home_page'))

# if __name__ == '__main__':
#     app.run(debug=True)
        
#     return render_template('addStamp.html', form=form)



if __name__ == "__main__":
    app.run(debug=True)
# %%
