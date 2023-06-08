from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('startup/', views.startup, name='startup'),
    path('talent/', views.talent, name='talent'),
    path('contact/', views.contact, name='contact'),
    path('blog/', views.blog, name='blog'),
    path('about/', views.about, name='about'),
    path('careers/', views.careers, name='careers')
]
