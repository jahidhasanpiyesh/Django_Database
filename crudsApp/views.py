import os
from django.shortcuts import render, redirect

from .models import *


# Create your views here.


def index(request):
    prof = profile.objects.all()
    return render(request, "index.html", locals())


def delete(request, id):
    prof = profile.objects.get(id=id)
    if prof.Photo != 'images.png':
        os.remove(prof.Photo.path)
    prof.delete()
    return redirect('index')
