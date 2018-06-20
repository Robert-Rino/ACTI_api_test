# from google.appengine.ext import vendor

# Add any libraries installed in the "lib" folder.
# vendor.add('lib')

from flask import Flask, request
import inspect
import logging

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Flask'

@app.route('/api/ACTi/facedata', methods=['POST'])
def facedata():
    print('be hit !')
    print(request.data)
    print("from data {}".format(request.form))
    print("json data {}".format(request.json))
    return request.data

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')