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


# FIX WITH APPROPRIATE WIDGETS
# CHECK /signup to see form
# Need better styling
class UserRegisterForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'First Name'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Last Name', 'class': 'email-field'}))
    date_of_birth = forms.DateField(label="Date of Birth",widget=forms.SelectDateWidget( attrs={'placeholder':'Date of Birth'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'placeholder': 'Email'}))
    year_started = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder':'Year Started'}))
    student_status = forms.ChoiceField(widget=forms.Select(attrs={'placeholder': 'Computer Science', 'class':'select-field'}),choices=[("FR", "Freshman"), ("SO", "Sophomore"), ("JR", "Junior"), ("SR", "Senior"), ("GR", "Grad Student")], initial="FR")
    major = forms.ChoiceField(widget=forms.Select(attrs={'class':'select-field'}), choices=MAJOR_CHOICES, initial='Computer Science')
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Confirm Password'}))


    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'password1', 'password2', 'date_of_birth', 'year_started', 'student_status', 'major' ]
        help_texts = {
            'username': None,
            'email': None,
            'password1': None,
            'password2': None,
        }

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





