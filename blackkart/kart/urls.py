from django.urls import path
from kart import views


urlpatterns = [
    path('indexpag/',views.indexpag,name="indexpag"),
    path('categorypage/',views.categorypage,name="categorypage"),
    path('savecategory/',views.savecategory,name="savecategory"),
    path('displaycategory/',views.displaycategory,name="displaycategory"),
    path('addproduct/',views.addproduct,name="addproduct"),
    path('saveproduct/',views.saveproduct,name="saveproduct"),
    path('displayproductpage/',views.displayproductpage,name="displayproductpage"),
    path('editcategorypage/<int:dataid>/',views.editcategorypage,name="editcategorypage"),
    path('updatecategorypage/<int:dataid>/',views.updatecategorypage,name="updatecategorypage"),
    path('deletecategory/<int:dataid>/',views.deletecategory,name="deletecategory"),
    path('editproduct/<int:dataid>/',views.editproduct,name="editproduct"),
    path('updateproduct/<int:dataid>/',views.updateproduct,name="updateproduct"),
    path('deleteproduct/<int:dataid>/',views.deleteproduct,name="deleteproduct"),
    path('adminlogin/',views.adminlogin,name="adminlogin"),
    path('adminpage/',views.adminpage,name="adminpage"),
    path('adminlogout/',views.adminlogout,name="adminlogout"),
]