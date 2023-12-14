from django.shortcuts import HttpResponse, render

def home(request):
    # return HttpResponse("this is practice home")
    Movies= {'name': 'The Matrix'}
    return render(request, 'index.html', Movies)