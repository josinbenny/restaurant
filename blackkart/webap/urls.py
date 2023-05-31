from django.urls import path
from webap import views

urlpatterns = [
    path('homepage1/',views.homepage1,name='homepage1'),
]