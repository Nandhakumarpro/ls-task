from django.shortcuts import render , redirect , reverse
from .models import Images , User
# Create your views here.
from .forms import imageAddForm, registerForm
from django.core.files.storage import FileSystemStorage
import os , glob
from PIL import  Image
import pandas as pd
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.http import HttpResponse, HttpResponseRedirect


def get_date_taken(path):
    try :
        return pd.datetime.strptime ( Image.open(path).getexif()[36867]  , '%Y:%m:%d %H:%M:%S')
    except Exception as e :
        print ( e )
        return pd.datetime.datetime.now( )

def refreshTemp (  ) :
    for i in glob.glob("temp/*"):
        os.remove(i)

def logoutUser( request )  :
    logout(request)
    return  HttpResponse("<h3 style='color:blue;'>Successfully Logged Out</h3>")

@login_required(login_url="/admin/login")
def imageAdd ( request ) :
    # print ( request.user )
    if request.method == "POST" :
        refreshTemp()
        form = imageAddForm ( request.POST , request.FILES  )
        if form.is_valid() :
            files = request.FILES.getlist("images")
            for f in files :
                fs = FileSystemStorage ( )
                filename = fs.save('temp/'+f.name ,f )
                y = os.listdir( "temp/" ) [0]
                date = get_date_taken( "temp/" + y )
                # print ( f"date = {date}")
                img = Images ( image = f, date = date , uploaded_by = request.user )
                img.save ( )
                # print ( "Successfully Saved" )
                refreshTemp()
            messages.success(request, 'Images added successfully')
            return redirect("image-add")
                # print ( fs.url(filename))
            # form.save ( )
        else :
            # print ( 'form not valid')
            form = imageAddForm ( )
    form = imageAddForm()
            
    return render( request , "imageForm.html" , {"form" :form } )


def Signup ( request ) :
    form = registerForm( request.POST )
    if form.is_valid() :
        user = User( username = form.cleaned_data.get("username") )
        user.set_password( form.cleaned_data.get("password") )
        user.is_staff = True
        user.save()
        messages.success(request , "Sign up Successful")
        return HttpResponseRedirect( "/admin/login?next=/app/image-add/" )
    else :
        form = registerForm ( )

    context = {
        "form" :form ,
      }
    return render ( request , "signup.html"  , context  )


