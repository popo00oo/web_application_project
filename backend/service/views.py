from django.http import JsonResponse

from service.models import Lost, Notice
from serializers.service_serializer import NoticeSer, LostSer
from utils.base_view.base_view import BaseView
from utils.methods import return_response


class NoticeView(BaseView):
    model = Notice
    ser = NoticeSer
    allow_methods = ['get', 'post', 'patch', 'delete']

    def post(self, request, *args, **kwargs):
        if request.method.lower() not in self.allow_methods:
            response = return_response(status=False, error='method not allowed!')
            return JsonResponse(response)
        data = request.data
        data['user'] = request.user.id
        ser = self.ser(data=request.data)
        if ser.is_valid():
            ser.save()
            response = return_response(data=ser.data, info='add success！')
        else:
            response = return_response(status=False, error=ser.errors)
        return JsonResponse(response)


class LostListView(BaseView):
    model = Lost
    ser = LostSer
    allow_methods = ['get']
    get_filter = True
