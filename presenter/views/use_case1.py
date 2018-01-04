from django.http import HttpResponse

def index(request):
    return HttpResponse("Use case 1 example.")