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

def how_it_works(request):
    return render(request, 'pages/how_it_works.html')

def login(request):
    return render(request, 'pages/login.html')

def client_login(request):
    return render(request, 'pages/client_login.html')

def login_tech_talent(request):
    return render(request, 'pages/login-as-tech-talent.html')