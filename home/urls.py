from django.urls import path
from . import views

urlpatterns=[
    path('',views.index,name='index'),
    path('index/',views.index,name='index'),
    path('category/',views.category,name='category'),
    path('contact/',views.contact,name='contact'),
    path('single/',views.single,name='single'),
]