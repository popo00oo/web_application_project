from rest_framework.pagination import PageNumberPagination


# 页码
class NumberPageFunc(PageNumberPagination):
    invalid_page_message = "当前页码无效！"
    page_query_param = 'page'  # get传参获取页码
    page_size = 20  # 每页默认显示数据量
    page_size_query_param = 'size'  # get传参获取指定数据量
    max_page_size = 100  # 每页最大数据显示条数

    def get_paginated_response(self, data):
        return {
            'count': self.page.paginator.count,
            'results': data
        }
