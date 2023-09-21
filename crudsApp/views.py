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


def create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        photo = request.FILES.get('photo')
        address = request.POST.get('address')
        numbers = request.POST.get('number')
        email = request.POST.get('email')
        birth_date = request.POST.get('birthday')
        religion = request.POST.get('religion')
        nationality = request.POST.get('nationality')
        marital_status = request.POST.get('marital')
        gender = request.POST.get('gender')
        blood_group = request.POST.get('blood')
        is_alive = request.POST.get('alive')
        if len(photo) != 0:
            prof = profile.objects.create(Name=name, Photo=photo, Address=address, Contact_numbers=numbers,
                                          Email_Address=email, Date_of_Birth=birth_date, Religion=religion,
                                          Nationality=nationality, Marital_status=marital_status, gender=gender,
                                          blood_group=blood_group, is_alive=is_alive)
            prof.save()
            return redirect('index')
        else:
            prof = profile.objects.create(Name=name, Address=address, Contact_numbers=numbers,
                                          Email_Address=email, Date_of_Birth=birth_date, Religion=religion,
                                          Nationality=nationality, Marital_status=marital_status, gender=gender,
                                          blood_group=blood_group, is_alive=is_alive)
            prof.save()
            return redirect('index')

    return render(request, 'create.html')
