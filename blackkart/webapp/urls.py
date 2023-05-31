from django.urls import path
from webapp import views

urlpatterns=[
    path('webindex/',views.webindex,name='webindex'),
    path('webindex1/',views.webindex1,name='webindex1')
]