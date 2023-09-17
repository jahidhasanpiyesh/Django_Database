from django.db import models


# Create your models here.

class profile(models.Model):
    RELIGION = (
        ('Islam', 'Islam'),
        ('Hindu', 'Hindu'),
        ('Cristian', 'Cristian'),
        ('Buddha', 'Buddha'),
        ('Other', 'Other'),
    )
    MARITAL_STATUS = (
        ('Married', 'Married'),
        ('Unmarried', 'Unmarried'),
        ('Other', 'Other'),
    )

    GENDER = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    )

    BLOOD_GROUP = (
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B-', 'B-'),
        ('AB-', 'AB-'),
        ('AB+', 'AB+'),
        ('0-', '0-'),
        ('O+', 'O+'),
    )

    Name = models.CharField(max_length=20)
    Photo = models.ImageField(upload_to='prof_pic/')
    Address = models.TextField(max_length=40)
    Contact_numbers = models.TextField(max_length=15)
    Email_Address = models.EmailField(max_length=20)
    Date_of_Birth = models.DateField()
    Religion = models.CharField(choices=RELIGION, max_length=20)
    Nationality = models.TextField(max_length=20)
    Marital_status = models.CharField(choices=MARITAL_STATUS, max_length=15)
    gender = models.CharField(choices=GENDER, max_length=10, default='Male')
    blood_group = models.CharField(choices=BLOOD_GROUP, max_length=8, default='A+')
