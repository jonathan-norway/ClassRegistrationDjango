from django.contrib.auth.models import User
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.forms import UserCreationForm

from django.db import models
from django import forms


MAJOR_CHOICES = [
    ("CISC", "Computer Science"),
    ("CYBSEC", "Cyber Security"),
    ("MATH", "Mathematics"),
    ("PHYS", "Physics"),
    ("CHEM", "Chemistry"),
    ("BIO", "Biology"),
    ("PSYC", "Psychology"),
    ("REL", "Religion"),
    ("ECON", "Economy"),
    ("ACCO", "Accounting"),
    ("BUSN", "Business"),
    ("ART", "Arts and Crafts"),
    ("EXSC", "Exercise Science"),
    ("INTR", "International Relations"),
    ("POLS", "Political Science"),
]

class Student(models.Model):
    fullName = models.CharField(max_length=50)
    major = models.CharField(max_length=50)
    expectedGradDate = models.IntegerField(max_length=50)

class Class(models.Model):
    classId = models.IntegerField(max_length=50)
    className = models.CharField(max_length=50)
    subject = models.CharField(max_length=50)





