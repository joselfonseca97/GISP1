import jwt
import os
import inspect
from dotenv import load_dotenv
from functools import wraps
from flask import request
from api.common.error import buildErrorResponse

load_dotenv()


def token_required(f):
    """
    Decorator to check if the token is valid
    """
    @wraps(f)
    def decorator(*args, **kwargs):
        token = None
        if 'Authorization' in request.headers:
            token = request.headers['Authorization'].replace('Bearer ', '')
        if not token:
            return buildErrorResponse("Token is missing", 401)

        try:
            jwt.decode(token, os.getenv("SECRET_KEY"), algorithms="HS256")
            return f(*args, **kwargs)
        except:
            return buildErrorResponse("Token is invalid", 401)

    return decorator


def role_required(roles):
    """"
    Check if a user has the required role given in the argument array
    """
    def wrapper(f):
        @wraps(f)
        def decorator(*args, **kwargs):
            token = None
            if 'Authorization' in request.headers:
                token = request.headers['Authorization'].replace('Bearer ', '')

            if not token:
                return buildErrorResponse("Token is missing", 401)

            try:
                payload = jwt.decode(token, os.getenv("SECRET_KEY"), algorithms="HS256")
                if payload['role'] not in roles:
                    return buildErrorResponse("You don't have the required role", 403)
                return f(*args, **kwargs)
            except:
                return buildErrorResponse("Token is invalid", 401)

        return decorator

    return wrapper
