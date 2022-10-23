from django.db import models
from PIL import Image
from django.core.files.uploadedfile import InMemoryUploadedFile
import os
from Img_Multi_Size.settings import BASE_DIR
import platform

def photo_path( filename):
    basefilename, file_extension = os.path.splitext(filename)
    MEDIA_ROOT = os.path.join(BASE_DIR,'thumnail')
        if platform.system() == 'Windows':
        return f'{MEDIA_ROOT}\{basefilename}{file_extension}'
    else:
        return f'{MEDIA_ROOT}/{basefilename}{file_extension}'



class DiffSize(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField()
    
       
    def save(self):
        super().save()  # saving image first
        img = Image.open(self.image.path)  # Open image using self
        new_img = img.thumbnail((300, 300))
        if platform.system() == 'Windows':
            x = photo_path(self.image.path.split('\\')[-1])   
        else:
            x = photo_path(self.image.path.split('/')[-1])    
        new_img.save(x)  # saving image at the same path

    def __str__(self):
        return self.name
