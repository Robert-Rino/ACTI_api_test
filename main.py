# from google.appengine.ext import vendor

# Add any libraries installed in the "lib" folder.
# vendor.add('lib')

from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from config import config
import inspect
import logging
import json
import os

ENVIRONMENT = os.getenv('ENVIRONMENT', default='default')

app = Flask(__name__)
app.config.from_object(config[ENVIRONMENT])
db = SQLAlchemy(app)

class Recognize(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    image_b64 = db.Column(db.String)
    objectName = db.Column(db.String)
    score = db.Column(db.Integer)
    created = db.Column(db.Integer)

    def save(self):
        db.session.add(self)
        db.session.commit()

class Detection(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    image_b64 = db.Column(db.String)
    created = db.Column(db.Integer)

    def save(self):
        db.session.add(self)
        db.session.commit()

migrate = Migrate(app, db)
manager = Manager(app)

@app.route('/')
def hello_world():
    return 'Flask'

@app.route('/api/ACTi/facedata', methods=['POST'])
def facedata():
    print('Detection')
    body = request.form['']
    json_body = json.loads(body[2:-1])

    facedata = Detection(
        image_b64=json_body['Snapshot'],
        created=json_body['FirstTimestamp'])
    facedata.save()
    
    print(facedata.__dict__)
    return 'ok'

@app.route('/api/ACTi/persondata', methods=['POST'])
def persondata():
    print('Identification')
    body = request.form['']
    json_body = json.loads(body[2:-1])

    persondata = Recognize(
        objectName=json_body['ObjectName'],
        image_b64=json_body['Snapshot'],
        score=json_body['Score'],
        created=json_body['FirstTimestamp']
    )
    persondata.save()

    print(persondata.objectName, persondata.score)
    return 'ok'

# @app.route('/api/ACTi/persondata')
# def persondata_list():
#     print('get person data')
#     offset = request.args.get('offset')
#     json_body = json.loads(body[2:-1])

#     persondata = Recognize(
#         objectName=json_body['ObjectId'],
#         image_b64=json_body['Snapshot'],
#         created=json_body['FirstTimestamp']
#     )
#     persondata.save()

#     print(json_body)
#     return 'ok'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')