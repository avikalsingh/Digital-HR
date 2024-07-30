from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=122)
    gender = models.CharField(max_length=122)
    address = models.TextField()
    contactno = models.IntegerField() 
    email = models.EmailField(max_length=122)
    message = models.TextField()
    date = models.DateField()


class JobSeeker(models.Model):
    name = models.CharField(max_length=122)
    gender = models.CharField(max_length=122)
    address = models.TextField()
    city = models.CharField(max_length=122)
    contactno = models.IntegerField() 
    email = models.EmailField(max_length=122)
    qualification = models.CharField(max_length=122)
    file = models.FileField(null=True, upload_to="resume/", max_length=250, default=None)
    date = models.DateField()


class Employee(models.Model):
    empid = models.CharField(max_length=10, primary_key=True)
    name = models.CharField(max_length=122)
    fname = models.CharField(max_length=122)
    mname = models.CharField(max_length=122)
    gender = models.CharField(max_length=122)
    address = models.TextField()
    city = models.CharField(max_length=122)
    contactno = models.IntegerField()
    email = models.EmailField(max_length=122)
    department = models.CharField(max_length=122)
    designation = models.CharField(max_length=122)
    dob = models.DateField()
    doj = models.DateField()
    salary = models.FloatField()

    def __str__(self):
        return (self.empid + " " + self.name)
    

class City(models.Model):
    city = models.CharField(max_length=122)

class Qualification(models.Model):
    qualification = models.CharField(max_length=122)
