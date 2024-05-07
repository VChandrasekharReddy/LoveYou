from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from . import Templates

# Create your views here.
from django.shortcuts import render

def index(request):
    if not request.session.get('popup_shown', False):
        request.session['popup_shown'] = True  # Set session variable to indicate popup has been shown
        show_popup = True
    else:
        show_popup = False

    return render(request, 'home.html', {'show_popup': show_popup})

def Flames(request):
    return HttpResponse(loader.get_template('Flames.html').render())
                        
def about(request):
    return HttpResponse(loader.get_template('about.html').render({'name':'chandra'},request))

def wishes(request):
    return HttpResponse(loader.get_template('wishes.html').render())