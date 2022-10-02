import jwt
from cloudant import Cloudant
import os

username = os.getenv('CLOUDANT_USERNAME')
api_key = os.getenv('CLOUDANT_API_KEY')
SECRET_KEY = os.getenv('SECRET_KEY')

class Auth:

    def __open_db(self, db_name, client):
        db = client.create_database(db_name, throw_on_exists=False)
        return db

    def __open_client(self):
        client = Cloudant.iam(username,
                              api_key,
                              connect=True)

        return client

    def get_db(self, db_name):
        client = self.__open_client()
        db = self.__open_db(db_name, client)
        return db

    def generate_token(self, user_id, role):
        token = jwt.encode({'user_id': user_id, 'role': role}, SECRET_KEY, algorithm="HS256")
        return token


auth = Auth()
