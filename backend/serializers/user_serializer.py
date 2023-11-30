from rest_framework import serializers
from users.models import Users
from rest_framework.validators import UniqueValidator
from utils.methods import hash_pwd


class LoginSer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ['id', 'username']


class RegisterSer(serializers.ModelSerializer):
    username = serializers.CharField(validators=[
        UniqueValidator(
            queryset=Users.objects.all(),
            message='This username has already been registered'
        )
    ])

    def validate_password(self, value):
        return hash_pwd(value)

    class Meta:
        model = Users
        fields = ['username', 'password']
