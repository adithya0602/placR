from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    is_admin=models.BooleanField('Is admin',default=False)
    is_recruiter=models.BooleanField('Is recruiter',default=False)
    is_student=models.BooleanField('Is student',default=False)

class Recruiter(models.Model):
    username=models.CharField(max_length=20)
    fname=models.CharField(max_length=20)
    lname=models.CharField(max_length=20)
    idno=models.IntegerField()
    email=models.EmailField(max_length=40)
    cname=models.CharField(max_length=30)
    password=models.CharField(max_length=20)
    def __str__(self):
        return self.username
class Student(models.Model):
    sname=models.CharField(max_length=20)
    fname=models.CharField(max_length=20)
    lname=models.CharField(max_length=20)
    email=models.EmailField(max_length=40)
    iname=models.CharField(max_length=30)
    pass1=models.CharField(max_length=20)
    def __str__(self):
        return self.sname
