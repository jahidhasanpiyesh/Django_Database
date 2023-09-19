from django.shortcuts import render
from .models import *


# Create your views here.


def index(request):
    # try to first way >>>>>>>>>>
    # total_profile = profile.objects.all()
    # for i in total_profile:
    #     print(f'profile is : {i} phone number is :{i.Contact_numbers} and Email is : {i.Email_Address} ')

    # try to 2nd wey >>>>>>>>>>>  All data show to backend terminal
    # total_profile = profile.objects.filter(is_alive=False)
    # for i in total_profile:
    #     print(f'profile is : {i} phone number is :{i.Contact_numbers} and Email is : {i.Email_Address} ')

    # try to 3rd wey >>>>>>>>>>>  Robot Adrita fixing data backend output show ?
    # total_profile = profile.objects.get(Name= "Robot Adrita")
    # print(total_profile.Email_Address)

    # backend unit data press to add all info >>>>>?
    # prof = profile.objects.create(Name="Rana", Address="mymensing,valuka", Contact_numbers="01798845625",
    #                               Email_Address="rana@gmail.com", Date_of_Birth="1996-09-23",
    #                               Religion="Islam", Nationality="Bangladeshi", gender="Female", blood_group="AB-",
    #                               is_alive=False)
    # prof.save()

    # use to all() and get() and filter() three functions/method
    # prof = profile.objects.get(Name="Robot Adrita")
    prof = profile.objects.all()
    return render(request, "index.html", locals())
