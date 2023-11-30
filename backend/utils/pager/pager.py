from rest_framework.pagination import PageNumberPagination



class NumberPageFunc(PageNumberPagination):
    invalid_page_message = "Invalid page！"
    page_query_param = 'page'  # get page number
    page_size = 2000  # default display number
    page_size_query_param = 'size'
    max_page_size = 2000  # Mailman display each page

    def get_paginated_response(self, data):
        return {
            'count': self.page.paginator.count,
            'results': data
        }
