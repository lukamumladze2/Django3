from django.http import HttpResponse

def blog_home(request):
    return HttpResponse("Hello from blog app!")