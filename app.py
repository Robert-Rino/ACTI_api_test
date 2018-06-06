from google.appengine.ext import vendor

# Add any libraries installed in the "lib" folder.
vendor.add('lib')

from flask import Flask, request
import inspect
import logging

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Flask'

@app.route('/api/ACTi/facedata', methods=['POST'])
def facedata():
    logging.info('be hit !')
    # logging.info(request.headers)
    # logging.info(request.)
    # logging.info(request.headers)
    # logging.info("from data {}".format(request.form))
    # logging.info("json data {}".format(request.json))
    return 'ok'

if __name__ == '__main__':
    app.run(debug=True, host='localhost')