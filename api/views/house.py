from django.views import View
from django.http import JsonResponse
from app01.models import House


class HouseView(View):
    def get(self, request):
        res = {
            'code': 200,
            'msg': 'success',
            'data': []
        }

        house_list = House.objects.all()

        for house in house_list:
            res['data'].append({
                'nid': house.nid,
                'housing_no': house.housing_no,
                'building_no': house.building_no,
                'construction_area': house.construction_area,
                'using_area': house.using_area,
                'type': house.type,
                'location': house.location,
                'create_date': str(house.create_date)[:10],
                'user_name': house.user_name
            })

        return JsonResponse(res)

    def post(self, request):
        res = {
            'code': 200,
            'msg': 'success',
            'data': {}
        }
        housing_no = request.data.get('housing_no')
        building_no = request.data.get('building_no')
        construction_area = request.data.get('construction_area')
        using_area = request.data.get('using_area')
        type = request.data.get('type')
        addr = request.data.get('addr')
        location = request.data.get('location')
        user_name = request.data.get('user_name')

        House.objects.create(housing_no=housing_no, building_no=building_no, construction_area=construction_area,
                             using_area=using_area, type=type, addr=addr, location=location, user_name=user_name)

        return JsonResponse(res)

    def put(self, request):
        res = {
            'code': 200,
            'msg': 'success',
            'data': {}
        }
        nid = request.data.get('nid')
        house_obj = House.objects.filter(nid=nid)
        house_obj.update(**request.data)

        return JsonResponse(res)

    def delete(self, request):
        res = {
            'code': 200,
            'msg': 'success',
            'data': {}
        }
        nid = request.data.get('nid')
        house_query = House.objects.filter(nid=nid)
        house_query.delete()

        return JsonResponse(res)
