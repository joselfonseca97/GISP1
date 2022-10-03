from flask_restful import Resource
from . import controllerProyecto as controller

class EdificioApi(Resource):
    def get(self,id):
        return controller.getEdificioData(id)
class MedidasApi(Resource):
    def get(self):
        return controller.getMedidas()