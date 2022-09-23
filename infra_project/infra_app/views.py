from django.http import HttpResponse


def index(request):
    return HttpResponse('Путин объявил мобилизацию')


def second_page(request):
    return HttpResponse('Он ЁБНУТЫЙ')
