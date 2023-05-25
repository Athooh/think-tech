from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'pages/index.html')

def startup(request):
    return render(request, 'pages/startup.html')

def contact(request):
    return render(request, 'pages/contact.html')