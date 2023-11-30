import datetime, jwt
from rest_framework.authentication import BaseAuthentication
from rest_framework import exceptions
from utils.authentication import jwt_config
from utils.methods import return_response


class JwtAuthentication(BaseAuthentication):
    # Token authentication
    def authenticate(self, request):
        # needs to verify the token
        auth = get_auth(request)
        if not auth:
            response = return_response(status=False, error='No token!')
            raise exceptions.AuthenticationFailed(response)
        if auth[0].lower() != jwt_config.TOKEN_START.lower().strip():
            response = return_response(status=False, error='token wrong!')
            raise exceptions.AuthenticationFailed(response)
        if len(auth) == 1:
            response = return_response(status=False, error='error token!')
            raise exceptions.AuthenticationFailed(response)
        elif len(auth) > 2:
            response = return_response(status=False, error='error token!')
            raise exceptions.AuthenticationFailed(response)

        token = auth[1]
        result = parse_payload(token)
        if not result['status']:
            raise exceptions.AuthenticationFailed(result)
        user_obj = jwt_config.UserInfo.objects.filter(id=result['data']['id']).first()
        if not user_obj or not user_obj.is_active:
            result = return_response(status=False, error='invalid token!')
            raise exceptions.AuthenticationFailed(result)
        return user_obj, token


def get_auth(request):
    # Get Token
    authorization = request.META.get('HTTP_AUTHORIZATION', '')
    if jwt_config.JWT_AUTH_PORT:
        if jwt_config.JWT_AUTH_PORT == 'Cookie':
            authorization = request.COOKIES.get(jwt_config.JWT_AUTH_COOKIE_KEY)
        if jwt_config.JWT_AUTH_PORT == 'Get':
            authorization = request.query_params.get(jwt_config.JWT_AUTH_GET_KEY)
    auth = authorization.split()
    return auth


def create_jwt_token(payload: dict, timeout: int = 7):
    # Create jwt token
    SALT = jwt_config.SECRET_KEY
    payload['exp'] = datetime.datetime.utcnow() + datetime.timedelta(days=timeout)
    token = jwt_config.TOKEN_START + jwt.encode(payload, SALT, algorithm="HS256")
    return token


def parse_payload(token: str):
    #Verifies the token and obtains the payload
    try:
        verified_payload = jwt.decode(token, jwt_config.SECRET_KEY, algorithms=["HS256"])
        result = return_response(data=verified_payload)
    except exceptions.NotAcceptable:
        result = return_response(status=False, error='token expired!')
    except jwt.DecodeError:
        result = return_response(status=False, error='token fail!')
    except jwt.InvalidTokenError:
        result = return_response(status=False, error='wrong token!')
    return result
