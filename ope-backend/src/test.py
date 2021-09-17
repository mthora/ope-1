import jwt
import datetime

token = jwt.encode(
                        {'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60), 'user_id': 1,
                         'role': 2}, key="123456", algorithm='HS256')

print(token)