from sqlalchemy.exc import IntegrityError


def flask_adapter(request, composer, arg=None):
    try:
        body = request.get_json()
        files = []
        if request.files.getlist('files'):
            files = request.files.getlist('files')
        if body is None and arg is not None:
            body = arg
    except Exception as ex:
        print(ex);
        return {"data": None, "status": 400, "message": "Bad Request"}
    try:
        if request.files.getlist('files'):
            response = composer.route(body, files)
        else:
            response = composer.route(body)
    except IntegrityError:
        return {"data": None, "status": 409, "message": "Integrity Error"}
    return response
