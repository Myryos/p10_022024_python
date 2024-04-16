from rest_framework.pagination import PageNumberPagination



class SoftDeskPagination(PageNumberPagination):
    max_page_size = 100