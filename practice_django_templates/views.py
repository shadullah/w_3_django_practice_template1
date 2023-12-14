from django.shortcuts import HttpResponse, render

def home(request):
    # return HttpResponse("this is practice home")
    return render(request, 'index.html')