from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


app = Flask(__name__)
app.config.from_object(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:''@localhost/flask'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
app.app_context().push()
#CORS(app, resources={r"/*": {'origins': 'http://localhost:8080', "allow_headers": "Acces-Control-Allow-Origin"}})
CORS(app)
class Articles(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    body = db.Column(db.Text())
    date = db.Column(db.DateTime(), default=datetime.now())

    def __init__(self, title, body):
        self.title = title
        self.body = body
@app.route('/')
def home():
    return "HOME"
@app.route('/get', methods=['GET'])
def hello_world():  # put application's code here
    all_articles = Articles.query.all()

@app.route('/add', methods=['POST'])
def add_articles():
    title = request.json['title']
    body = request.json['body']

    article = Articles(title, body)
def resiter():
    return 'Register! '
if __name__ == '__main__':
    app.run()
