from django import forms
from django.contrib import auth
from app01.models import UserInfo
from django.views import View
from django.http import JsonResponse


class LoginBaseForm(forms.Form):
    username = forms.CharField(error_messages={'required': 'Enter username！'})
    password = forms.CharField(error_messages={'required': 'Enter password！'})

    # Get the request object in the class
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super().__init__(*args, **kwargs)


class LoginForm(LoginBaseForm):

    # Global hook
    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = auth.authenticate(username=username, password=password)

        if not user:
            self.add_error('password', 'password error！')
            return self.cleaned_data
        self.cleaned_data['user'] = user
        return self.cleaned_data


class SignForm(LoginBaseForm):
    re_password = forms.CharField(error_messages={'required': 'please enter password！'})

    # Check  the user name already have or not
    def clean_username(self):
        username = self.cleaned_data.get('username')
        user_query = UserInfo.objects.filter(username=username)
        if user_query:
            self.add_error('username', 'username already registered ！')
        return self.cleaned_data

    # Check two times passwords are same or not
    def clean(self):
        password = self.cleaned_data.get('password')
        re_password = self.cleaned_data.get('re_password')
        if password != re_password:
            self.add_error('re_password', 'The two password entries are inconsistent！')
        return self.cleaned_data


def clean_form(form):
    err_dict: dict = form.errors
    err_valid = list(err_dict.keys())[0]
    err_msg = err_dict[err_valid][0]
    return err_valid, err_msg


class LoginView(View):
    def post(self, request):
        res = {
            'code': 425,
            'msg': 'Login successful！',
            'self': None
        }
        form = LoginForm(request.data, request=request)
        if not form.is_valid():
            res['self'], res['msg'] = clean_form(form)
            return JsonResponse(res)
        # Perform login operation
        user = form.cleaned_data.get('user')
        auth.login(request, user)
        res['code'] = 0
        return JsonResponse(res)


class SignView(View):
    def post(self, request):
        res = {
            'code': 425,
            'msg': 'Registered successfully!',
            'self': None
        }
        form = SignForm(request.data, request=request)
        if not form.is_valid():
            res['self'], res['msg'] = clean_form(form)
            return JsonResponse(res)
        user = UserInfo.objects.create_user(
            username=request.data.get('username'),
            password=request.data.get('password')
        )
        user.save()
        auth.login(request, user)
        res['code'] = 0
        return JsonResponse(res)
