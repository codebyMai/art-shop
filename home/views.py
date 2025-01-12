from django.shortcuts import render

# Create your views here.
def index(request):
    """ Index page view """
    return render(request, 'home/index.html')

def about(request):
    """ About page view """
    return render(request, 'home/about.html')    
