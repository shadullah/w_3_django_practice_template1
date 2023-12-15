from django.shortcuts import render, HttpResponse
import datetime

# Create your views here.
def about(request):
    # return HttpResponse("this is about of filter_temp")
    # filter_data={}
    data = {'name': 'dollar mess', 'list': ['django','is','fun'], 'member': 10, "living":datetime.datetime.now(), 'living_rooms': [1,2,3,4], 'fees': [
        {
            'id': 1,
            'name': ['Khaled', 'muztahid'],
            'fee': 2600 
        },
        {
            'id': 2,
            'name': ['saki', 'al-amin', 'walid'],
            'fee': 1550 
        }
    ]}
    return render(request, 'filter_temp/inside_temp_filter.html', data)