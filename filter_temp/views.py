from django.shortcuts import render, HttpResponse

# Create your views here.
def about(request):
    # return HttpResponse("this is about of filter_temp")
    data = {'name': 'dollar mess', 'member': 10, 'living_rooms': [1,2,3,4], 'fees': [
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