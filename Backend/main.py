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
from api import EdificiosApi,AcerasApi,ZonasVerdesApi,ZonasSegurasApi,RutasEvacuacionApi,VialidadApi,MedidasApi


#from api import UserApi, users_bp
#from api.schemas.schema_user import POST_SCHEMA, PATCH_SCHEMA
from api.common.error import buildErrorResponse


# Initialize server
load_dotenv()
app = Flask(__name__, static_url_path='')
swagger = Swagger(app)

CORS(app)
api = Api(app, catch_all_404s=True)

#app.register_blueprint(users_bp)

# Routes

#Edificios
api.add_resource(EdificiosApi,'/edificios',endpoint="get_post_edificios")
api.add_resource(EdificiosApi,'/edificios/<id>',endpoint="get_post_edificio")
#Aceras
api.add_resource(AcerasApi,'/aceras',endpoint="get_post_aceras")
#ZonasVerdes
api.add_resource(ZonasVerdesApi,'/zonasVerdes',endpoint="get_post_zonasVerdes")
#zonasSeguras
api.add_resource(ZonasSegurasApi,'/zonasSeguras',endpoint="get_post_zonasSeguras")
#RutasEvacuacion
api.add_resource(RutasEvacuacionApi,'/rutasEvacuacion',endpoint="get_post_rutasEvacuacion")
#Vialidad
api.add_resource(VialidadApi,'/vialidad',endpoint="get_post_vialidad")
#Medidas Iniciales
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
