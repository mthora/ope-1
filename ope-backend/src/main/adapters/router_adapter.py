from sqlalchemy.exc import IntegrityError


def flask_adapter(request, composer):
    try:
        body = request.get_json()
        print("body", body)
        print("composer", composer)
    except:
        return {"data": None, "status": 400, "message": "Bad Request"}
    try:
        response = composer.route(body)
    except IntegrityError:
        return {"data": None, "status": 409, "message": "Integrity Error"}
    return response
