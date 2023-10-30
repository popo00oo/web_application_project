from django.views import View
from django.http import JsonResponse
from app01.models import UserInfo


class UserLurView(View):

    def put(self, request):
        res = {
            'code': 201,
            'msg': ' Successful！'
        }
        nid = request.data.get('nid')
        user_name = request.data.get('userName')
        user_sex = request.data.get('userSex')
        age = request.data.get('age')
        phone = request.data.get('phone')
        student_id = request.data.get('student_id')
        id_card = request.data.get('id_card')
        user_query = UserInfo.objects.filter(nid=nid)
        user_query.update(name=user_name, sex=user_sex, age=age, tel=phone, student_id=student_id, id_card=id_card)
        res['code'] = 200
        return JsonResponse(res)
