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

def guide(request):
    return render(
        request,
        'HelloDjango/guide.html',
        {
            'title' : 'Learn Django',
            'heading' : 'Learn Django with Visual Studio',
            'content' : {
                'Create a project and solution' : 'https://docs.microsoft.com/en-us/visualstudio/python/learn-django-in-visual-studio-step-01-project-and-solution?view=vs-2019',
                'Create a Django app' : 'https://docs.microsoft.com/en-us/visualstudio/python/learn-django-in-visual-studio-step-02-create-an-app?view=vs-2019',
                'Server static files and pages' : 'https://docs.microsoft.com/en-us/visualstudio/python/learn-django-in-visual-studio-step-03-serve-static-files-and-add-pages?view=vs-2019',
                'Use the Django Web Project template' : 'https://docs.microsoft.com/en-us/visualstudio/python/learn-django-in-visual-studio-step-04-full-django-project-template?view=vs-2019',
                'Authenticate users' : 'https://docs.microsoft.com/en-us/visualstudio/python/learn-django-in-visual-studio-step-05-django-authentication?view=vs-2019',
                'Use the Polls Django Web Project template' : 'https://docs.microsoft.com/en-us/visualstudio/python/learn-django-in-visual-studio-step-06-polls-django-web-project-template?view=vs-2019',
            }
        }
    )
