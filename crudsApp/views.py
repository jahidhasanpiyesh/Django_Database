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

    return render(request, "index.html")
