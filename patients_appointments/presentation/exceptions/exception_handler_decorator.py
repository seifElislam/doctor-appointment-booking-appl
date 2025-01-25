from functools import wraps
from rest_framework.response import Response
from .custom_exception import CustomException

def exception_handler_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except CustomException as e:
            return Response(
                {'error': str(e.message)},
                status=400
            )
    return wrapper