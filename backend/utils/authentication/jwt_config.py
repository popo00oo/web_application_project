import datetime
from django.utils.module_loading import import_string
from django.conf import settings as sys

# User table configuration
UserInfo = import_string('users.models.Users')

# jwt authentication configuration
JWT_AUTH = {
    'JWT_EXPIRATION_DELTA': datetime.timedelta(days=7),  # jwt expire
    "JWT_AUTH_HEADER_PREFIX": 'JWT'
}

# jwt authentication mode
JWT_AUTH_PORT = None  # request header
JWT_AUTH_COOKIE_KEY = 'JWT_TOKEN'  # cookie key authentication
JWT_AUTH_GET_KEY = 'AUTH_TOKEN'


SECRET_KEY = sys.SECRET_KEY

# token
TOKEN_START = 'JWT '
