"""
Definition of views.
"""

from datetime import datetime
from django.shortcuts import render
from django.http import HttpRequest

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
        }
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )

def catalog(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/catalog.html',
        {
            'title':'Catalog',
            'message':'Your catalog page.',
            'year':datetime.now().year,
        }
    )



def Registration(request):
   return render(request, 'app/Registration.html')


def kitchen(request):
   return render(request, 'app/kitchen.html')

def food(request):
   return render(request, 'app/food.html')

def serve(request):
   return render(request, 'app/serve.html')

def go(request):
   return render(request, 'app/go.html')

def hom(request):
   return render(request, 'app/hom.html')