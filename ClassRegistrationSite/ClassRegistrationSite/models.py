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

class UserRegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    date_of_birth = forms.DateField()
    year_started = forms.IntegerField()
    student_status = forms.ChoiceField(choices=[("FR", "Freshman"), ("SO", "Sophomore"), ("JR", "Junior"), ("SR", "Senior"), ("GR", "Grad Student")])
    major = forms.ChoiceField(choices=MAJOR_CHOICES)

    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'password1', 'password2', 'date_of_birth', 'year_started', 'student_status', 'major' ]

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]
        user.date_of_birth = self.cleaned_data["date_of_birth"]
        user.year_started = self.cleaned_data["year_started"]
        user.student_status = self.cleaned_data["student_status"]
        user.major = self.cleaned_data["major"]
        if commit:
            user.save()
        return user





