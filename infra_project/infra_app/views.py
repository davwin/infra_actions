from django.http import HttpResponse

from rest_framework import status


def index(request):
    return HttpResponse('У меня получилось!', status=status.HTTP_200_OK)


def second_page(request):
    return HttpResponse('А это вторая страница', status=status.HTTP_200_OK)
