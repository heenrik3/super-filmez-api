from fastapi import Request, status
from fastapi.responses import JSONResponse
from fastapi.exceptions import *

class Error(Exception):
    def __init__(self, message: str, code: int):
        self.message = message
        self.code = code


def errorPackage():
    return { 
            'code': status.HTTP_400_BAD_REQUEST,
            'content': {
                    'status': 'fail',        
                    'message': 'Algum erro ocorreu.'
                }
            }


def constructGenericError():
    error = errorPackage()
    error['code'] = status.HTTP_500_INTERNAL_SERVER_ERROR
    error['content']['status'] = 'error'

    return error


async def exceptionHandler(req: Request, err):
    if isinstance(err, Error):
        error = errorPackage()
        error['code'] = err.code
        error['content']['message'] = err.message

    else:
        error = constructGenericError()
    
    return JSONResponse(
        status_code = error.get('code'),
        content = error.get('content')
    )
    