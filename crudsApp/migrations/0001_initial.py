# Generated by Django 4.2.5 on 2023-09-16 02:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=20)),
                ('Photo', models.ImageField(upload_to='prof_pic/')),
                ('Address', models.TextField(max_length=40)),
                ('Contact_numbers', models.TextField(max_length=15)),
                ('Email_Address', models.EmailField(max_length=20)),
                ('Date_of_Birth', models.DateField()),
                ('Religion', models.CharField(choices=[('Islam', 'Islam'), ('Hindu', 'Hindu'), ('Cristian', 'Cristian'), ('Buddha', 'Buddha'), ('Other', 'Other')], max_length=20)),
                ('Nationality', models.TextField(max_length=20)),
                ('Marital_status', models.CharField(choices=[('Married', 'Married'), ('Unmarried', 'Unmarried'), ('Other', 'Other')], max_length=15)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], default='Male', max_length=10)),
                ('blood_group', models.CharField(choices=[('A+', 'A+'), ('A-', 'A-'), ('B+', 'B+'), ('B-', 'B-'), ('AB-', 'AB-'), ('AB+', 'AB+'), ('0-', '0-'), ('O+', 'O+')], default='A+', max_length=8)),
            ],
        ),
    ]
