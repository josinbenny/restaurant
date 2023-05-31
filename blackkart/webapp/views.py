from django.shortcuts import render

# Create your views here.
def webindex(req):
    return render(req,'index.html')

def webindex1(req):
    return render(req,'Home.html')