from cgi import test
import os
from turtle import end_poly
# Flask imports
from flasgger import Swagger
from flask import Flask, jsonify, make_response, render_template, request
from flask_cors import CORS
from flask_expects_json import expects_json
from flask_restful import Api

# Local imports
from dotenv import load_dotenv
from jsonschema import ValidationError

# Local imports
from api import EdificioApi,MedidasApi
from api.common.error import buildErrorResponse

# Initialize server
load_dotenv()
app = Flask(__name__, static_url_path='')
swagger = Swagger(app)

CORS(app)
api = Api(app, catch_all_404s=True)

# EndPoints

#Get data from specific building
api.add_resource(EdificioApi,'/edificio/<id>',endpoint="get_post_edificio")

#Get data for all buildings
api.add_resource(MedidasApi,'/medidas',endpoint="get_post_medidas")

@app.route('/')
def index():
    return render_template('index.html')

@app.errorhandler(400)
def bad_request(error):
    if isinstance(error.description, ValidationError):
        original_error = error.description
        return make_response(jsonify({'error': original_error.message}), 400)
    # handle other "Bad Request"-errors
    return error

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
