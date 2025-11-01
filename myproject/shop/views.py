from django.http import HttpResponse


def shop_home(request):
    return HttpResponse("Hello from shop app!")