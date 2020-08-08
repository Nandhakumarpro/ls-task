from  django.urls import path , include
from . import  views
urlpatterns = [
    path( "image-add/" , views.imageAdd , name = "image-add") ,
    path ("logout/" , views.logoutUser , name="logout") ,
    path("signup/" , views.Signup , name= "signup") ,
]