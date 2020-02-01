from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

# Create your views here.
def index(request):
    now = datetime.now()
    return render(
        request,
        'HelloDjango/index.html',
        {
            'title' : 'Hello Django!',
            'heading' : 'Hello World!',
            'date' : str(now.strftime('%A, %d-%b-%Y')),
        }
    )

