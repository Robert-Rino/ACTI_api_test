# from google.appengine.ext import vendor

# Add any libraries installed in the "lib" folder.
# vendor.add('lib')

from flask import Flask, request
import inspect
import logging
import json

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Flask'

@app.route('/api/ACTi/facedata', methods=['POST'])
def facedata():
    print('Detection')
    body = request.form['']
    # print(body[1:])
    json_body = json.loads(body[2:-1])
    print(json_body)
    return 'ok'

@app.route('/api/ACTi/persondata', methods=['POST'])
def persondata():
    print('Identification')
    body = request.form['']
    json_body = json.loads(body[2:-1])
    print(json_body)
    return 'ok'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')