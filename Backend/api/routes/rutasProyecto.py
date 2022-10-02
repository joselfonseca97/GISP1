from flask.helpers import make_response
from flask import request
from flask_restful import Resource
from flask_expects_json import expects_json
from . import controllerProyecto as controller
from api.common.error import buildErrorResponse, CustomError
from decorate_all_methods import decorate_all_methods
from api.common.decorators import token_required

class EdificiosApi(Resource):
    def get(self):
        return controller.getEdificios()
class AcerasApi(Resource):
    def get(self):
        return controller.getAceras()
class ZonasVerdesApi(Resource):
    def get(self):
        return controller.getZonasVerdes()
class ZonasSegurasApi(Resource):
    def get(self):
        return controller.getZonasSeguras()
class RutasEvacuacionApi(Resource):
    def get(self):
        return controller.getRutasEvacuacion()
class VialidadApi(Resource):
    def get(self):
        return controller.getVialidad()
class MedidasApi(Resource):
    def get(self):
        return controller.getMedidas()