from rest_framework.pagination import PageNumberPagination



class DefualPagination(PageNumberPagination):
    page_size = 10