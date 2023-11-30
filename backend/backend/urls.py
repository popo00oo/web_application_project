from django.contrib import admin
from django.http import HttpResponse
from django.urls import path
from users.views import LoginView, RegisterView
from service.views import NoticeView, LostListView

urlpatterns = [
    path('', lambda request: HttpResponse('hello word!')),
    path('admin/', admin.site.urls),
    path('auth/login', LoginView.as_view()),
    path('auth/register', RegisterView.as_view()),
    path('service/notice', NoticeView.as_view()),
    path('service/lost', LostListView.as_view())
]
