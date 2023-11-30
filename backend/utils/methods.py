import hashlib
from utils.pager.pager import NumberPageFunc


# 查
def get_data(model=None, is_query: bool = False, request=None, view=None, serClass=None, many: bool = True):
    if many:
        if is_query:
            queryset = model.order_by('-id')
        else:
            queryset = model.objects.all().order_by('-id')
        pg = NumberPageFunc()
        page_obj = pg.paginate_queryset(queryset, request, view)
        ser = serClass(page_obj, many=many)
        data = pg.get_paginated_response(ser.data)
    else:
        page_obj = model
        ser = serClass(instance=page_obj, many=many)
        data = ser.data
    return data


def return_response(status: bool = True, code: int = 200, data=None, info: str = '', error: str = ''):
    response = {
        'status': status,  # 请求状态
        'code': code,  # 请求标志 - 200/400
        'data': data,  # 请求内容 - dict
        'info': info,  # 提示信息 - str
        'errs': error  # 错误信息 - str
    }
    return response


def hash_pwd(password: str = ''):
    return hashlib.md5(password.encode('utf-8')).hexdigest()
