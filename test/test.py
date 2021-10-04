import jwt
import datetime
secret='hz66OCkDtv8G6D'
token = jwt.encode({'user': 'user', 'exp' : datetime.datetime.utcnow() + datetime.timedelta(minutes=5)}, secret)
print(token)
print(type(token))