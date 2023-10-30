import datetime
from app01.models import UserInfo
from django.http import JsonResponse


# Get  the number of registered users for seven days
def get_seven_data(request):
    today = datetime.date.today()
    seven_data = {
        'date': [],
        'login_data': [],
        'sign_data': []
    }
    for i in range(6, -1, -1):
        date = today - datetime.timedelta(days=i)

        login_count = UserInfo.objects.filter(last_login__year=date.year,
                                              last_login__month=date.month,
                                              last_login__day=date.day).count()

        sign_count = UserInfo.objects.filter(date_joined__year=date.year,
                                             date_joined__month=date.month,
                                             date_joined__day=date.day).count()
        seven_data['date'].append(date.strftime('%m-%d'))
        seven_data['login_data'].append(login_count)
        seven_data['sign_data'].append(sign_count)
    return JsonResponse(seven_data)



