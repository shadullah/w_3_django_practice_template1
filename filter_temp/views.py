from django.shortcuts import render, HttpResponse

# Create your views here.
def about(request):
    return HttpResponse("this is about of filter_temp")