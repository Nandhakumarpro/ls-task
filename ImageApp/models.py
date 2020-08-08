from django.db import models
from PIL import Image

from django.contrib.auth.models import  User
from django.db import models

def uploadPath ( instance , filename) :

    return f"Images/{instance.date.strftime('%d-%m-%Y')}/{filename}"


class Images( models.Model ) :
    uploaded_by = models.ForeignKey( User , on_delete=models.SET_NULL , null=True )
    image = models.ImageField (  upload_to=uploadPath , null=False  )
    date = models.DateField ( null=False  )

    class Meta :
        verbose_name = 'Image'
        verbose_name_plural = "Images"
        db_table = "images"



