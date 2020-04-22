from flask import Flask,render_template
from config import Config
from forms import CreateFilmForm, UpdateFilmForm, ConfirmDelete
from flask_pymongo import PyMongo, DESCENDING
import os


app = Flask(__name__)
app.config['MONGO_DBNAME']= 'films'
app.config["MONGO_URI"]= "mongodb://admin:Andreea983@cluster0-shard-00-00-xnfne.mongodb.net:27017,cluster0-shard-00-01-xnfne.mongodb.net:27017,cluster0-shard-00-02-xnfne.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true&w=majority"
mongo=PyMongo(app)
@app.route('/')
@app.route('/index')
def index():
    films=mongo.db.films.films.find()


    return render_template('index.html',films=films)


if __name__ == '__main__':
    app.run()
