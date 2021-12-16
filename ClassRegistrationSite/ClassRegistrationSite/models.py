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
## FOR MAME
# OneToOne relationship to user
# Fullname
# Major
# Expected Grad.Year


class Class(models.Model):
# ManyToMany relationship
# classID AutoField
# classname
# subject



