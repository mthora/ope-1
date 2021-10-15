from sqlalchemy.exc import IntegrityError


def flask_adapter(request, composer, arg=None):
    try:
        body = request.get_json()
        if body is None and arg is not None:
            body = arg
    except:
        return {"data": None, "status": 400, "message": "Bad Request"}
    try:
        response = composer.route(body)
    except IntegrityError:
        return {"data": None, "status": 409, "message": "Integrity Error"}
    return response
