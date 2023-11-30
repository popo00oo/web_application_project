from django.http import JsonResponse
from rest_framework.views import APIView

from utils.methods import get_data, return_response


class BaseView(APIView):
    model = None
    ser = None
    get_filter = None
    allow_methods = ['get', 'post', 'put', 'patch', 'delete']

    def get(self, request, *args, **kwargs):
        if request.method.lower() not in self.allow_methods:
            response = return_response(status=False, error='method not allowed!')
            return JsonResponse(response)
        queryset = self.model
        is_query = False
        if self.get_filter:
            queryset = self.model.objects.filter(**request.query_params.dict()).all()
            is_query = True
        data = get_data(queryset, is_query, request, self, self.ser, True)
        response = return_response(data=data)
        return JsonResponse(response)

    def post(self, request, *args, **kwargs):
        if request.method.lower() not in self.allow_methods:
            response = return_response(status=False, error='method not allowed!')
            return JsonResponse(response)
        ser = self.ser(data=request.data)
        if ser.is_valid():
            ser.save()
            response = return_response(data=ser.data, info='add success！')
        else:
            response = return_response(status=False, error=ser.errors)
        return JsonResponse(response)

    def put(self, request, *args, **kwargs):
        if request.method.lower() not in self.allow_methods:
            response = return_response(status=False, error='method not allowed!')
            return JsonResponse(response)
        user_obj = self.model.objects.get(id=request.data.get('id'))
        ser = self.ser(instance=user_obj, data=request.data)
        if ser.is_valid():
            ser.save()
            response = return_response(data=ser.data, info='update success！')
        else:
            response = return_response(status=False, error=ser.errors)
        return JsonResponse(response)

    def delete(self, request, *args, **kwargs):
        if request.method.lower() not in self.allow_methods:
            response = return_response(status=False, error='method not allowed!')
            return JsonResponse(response)
        obj_id = request.data.get('id')
        if self.model.objects.filter(id=obj_id).delete():
            response = return_response(info='delete success！')
        else:
            response = return_response(status=False, error='delete error！')
        return JsonResponse(response)
