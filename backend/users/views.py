from rest_framework.views import APIView
from django.http import JsonResponse

from serializers.user_serializer import LoginSer, RegisterSer
from users.models import Users
from utils.base_view.base_view import BaseView
from utils.authentication.jwt_auth import create_jwt_token
from utils.methods import return_response, get_data, hash_pwd


# user login view
class LoginView(APIView):
    authentication_classes = []
    permission_classes = []
    throttle_classes = []

    def post(self, request):
        data = request.data
        if not data:
            response = return_response(status=False, error='username or password error!')
            return JsonResponse(response)
        data['is_active'] = True
        data['password'] = hash_pwd(data['password'])
        user_obj = Users.objects.filter(**data).first()
        if user_obj:
            data = get_data(model=user_obj, serClass=LoginSer, many=False)
            data['token'] = create_jwt_token({'id': user_obj.id})
            response = return_response(data=data)
        else:
            response = return_response(status=False, error='username or password error!')
        return JsonResponse(response)


# register view
class RegisterView(BaseView):
    authentication_classes = []
    permission_classes = []
    throttle_classes = []
    model = Users
    ser = RegisterSer
    allow_methods = ['post']
