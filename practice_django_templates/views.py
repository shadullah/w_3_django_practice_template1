from django.shortcuts import HttpResponse

def home(request):
    return HttpResponse("this is practice home")