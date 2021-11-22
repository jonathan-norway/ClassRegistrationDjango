from django import forms

#Resources:
# https://docs.djangoproject.com/en/3.2/ref/forms/fields/
# https://docs.djangoproject.com/en/3.2/topics/forms/
# : MAYBE ITS EASIER TO CREATE FORM FROM MODEL??
# https://docs.djangoproject.com/en/3.2/topics/forms/modelforms/
# : We need signup form

class SignUpForm(forms.Form):
    user_id = forms.IntegerField(auto_id=True) #
    full_name = forms.CharField(max_length=100, label="Enter Full Name")
    email = forms.EmailField(max_length=100, label="Enter email")
    date_of_birth = forms.DateTimeField(label="enter date of birth")
    # : add timestamp for user creation.
    # : validate that email is not already associated with another account
    signup_date = forms.DateTimeField(auto_now_add=True)



# We need login form




# We need class registration form




#https://simpleisbetterthancomplex.com/tutorial/2017/02/18/how-to-create-user-sign-up-view.html