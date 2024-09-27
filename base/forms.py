from django import forms
from django.contrib.auth.models import User
from allauth.account.forms import SignupForm


class CustomSignupForm(SignupForm):
    first_name = forms.CharField(max_length=30, label="First Name")
    last_name = forms.CharField(max_length=30, label="Last Name")

    def save(self, request):
        # Ensure you call the parent's save method
        user = super(CustomSignupForm, self).save(request)
        # Add additional fields to the user object
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()
        return user
