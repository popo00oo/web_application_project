from django.urls import path
from api.views import login, admin_data, user, house

urlpatterns = [
    path('login/', login.LoginView.as_view()),
    path('sign/', login.SignView.as_view()),
    path('get_seven_data/', admin_data.get_seven_data),  # Get 7 days user registration
    path('userlur/', user.UserLurView.as_view()),
    path('house/', house.HouseView.as_view())
]
