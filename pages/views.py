from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'pages/index.html')

def startup(request):
    return render(request, 'pages/startup.html')

def talent(request):
    return render(request, 'pages/talent.html')

def contact(request):
    return render(request, 'pages/contact.html')

def blog(request):
    return render(request, 'pages/blog.html')

def about(request):
    return render(request, 'pages/about.html')

def careers(request):
    return render(request, 'pages/careers.html')