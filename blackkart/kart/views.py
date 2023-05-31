from django.shortcuts import render,redirect
from kart.models import kartdb,productdb
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User

# Create your views here.
def indexpag(req):
    return render(req,'indexpage.html')
def categorypage(req):
    return render(req,'Addcategory.html')
def savecategory(req):
    if req.method=="POST":
        na=req.POST.get('category')
        de=req.POST.get('description')
        img=req.FILES['image']
        obj=kartdb(Name=na,Description=de,Image=img)
        obj.save()
        return redirect(categorypage)
def displaycategory(req):
    data=kartdb.objects.all()
    return render(req,'displaycategory.html', {"data":data})
def editcategorypage(req,dataid):
    data=kartdb.objects.get(id=dataid)
    return render(req,'editcategory.html', {"data":data})
def updatecategorypage(req,dataid):
    if req.method=="POST":
        na = req.POST.get('productname')
        de = req.POST.get('productdesc')
        try:
            img=req.FILES['image']
            fs=FileSystemStorage()
            file=fs.save(img.name,img)
        except MultiValueDictKeyError:
            file=kartdb.objects.get(id=dataid).Image
        kartdb.objects.filter(id=dataid).update(Name=na,Description=de,Image=file)
        return redirect(displaycategory)


def deletecategory(req,dataid):
    data=kartdb.objects.get(id=dataid)
    data.delete()
    return redirect(displaycategory)

def addproduct(req):
    data=kartdb.objects.all()
    return render(req,'addproduct.html',{'data':data})
def saveproduct(req):
    if req.method=="POST":
        cat=req.POST.get('category')
        na=req.POST.get('product')
        qty=req.POST.get('qty')
        pr=req.POST.get('price')
        des=req.POST.get('description')
        im=req.FILES['image']
        obj=productdb(Category=cat,Productname=na,Quantity=qty,Price=pr,Description=des,Image=im)
        obj.save()
        return redirect(addproduct)

def displayproductpage(req):
    data=productdb.objects.all()
    return render(req,'displayproduct.html',{"data":data})

def editproduct(req,dataid):
    data=productdb.objects.get(id=dataid)
    da = kartdb.objects.all()
    return render(req,'editproductpage.html',{'data':data, 'da':da})

def updateproduct(req,dataid):
    if req.method=="POST":
        cat = req.POST.get('category')
        na = req.POST.get('product')
        qty = req.POST.get('qty')
        pr = req.POST.get('price')
        des = req.POST.get('description')
        try:
            im=req.FILES['image']
            fs=FileSystemStorage()
            file=fs.save(im.name,im)
        except MultiValueDictKeyError:
            file=productdb.objects.get(id=dataid).Image
        productdb.objects.filter(id=dataid).update(Category=cat,Productname=na,Quantity=qty,Price=pr,Description=des,Image=file)
        return redirect(displayproductpage)

def deleteproduct(req,dataid):
    data=productdb.objects.get(id=dataid)
    data.delete()
    return redirect(displayproductpage)

def adminlogin(req):
    return render(req,'loginpage.html')
def adminpage(req):
    if req.method=="POST":
        usrnme=req.POST.get('username')
        psswrd=req.POST.get('password')
        if User.objects.filter(username__contains=usrnme).exists():
            user=authenticate(username=usrnme,password=psswrd)
            if user is not None:
                login(req,user)
                req.session['username']=usrnme
                req.session['password']=psswrd
                return redirect(indexpag)
            else:
                return redirect(adminlogin)
        else:
            return redirect(adminlogin)
def adminlogout(req):
    del req.session['username']
    del req.session['password']
    return redirect(adminlogin)