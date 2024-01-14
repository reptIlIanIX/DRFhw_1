from rest_framework.pagination import PageNumberPagination


class CoursePagination(PageNumberPagination):
    page_size = 3
    page_query_param = 'page_size'
    max_page_size = 30
