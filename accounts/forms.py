from django import forms
from .models import User

class UserForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder':'Enter Password', 'required':'required'}))
    confirm_password = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder':'Confirm Password', 'required':'required'}))
    class Meta:
        model = User
        fields = ["first_name","last_name","username", "email", "image"]

        widgets = {
                'first_name': forms.TextInput(attrs={'class': 'form-control','placeholder':'Enter First Name', 'required':'required'}),
                'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Enter Last Name', 'required':'required'}),
                'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Enter a Username', 'required':'required'}),
                'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder':'Enter your Email', 'required':'required'}),
                'image': forms.FileInput(attrs={'class': 'form-control', 'placeholder':'Upload your Profile Picture', 'required':'required'}),
                # 'password': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder':'Enter Password', 'required':'required'}),
                # 'confirm_password': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder':'Confirm Password', 'required':'required'}),
            }
    
  

from django import forms
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model

class PasswordChangeForm(forms.Form):
    new_password = forms.CharField(
        label='New Password',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder':'Enter New Password', 'required':'required'}),
    )
    
    confirm_password = forms.CharField(
        label='Confirm Password',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder':'Confirm New Password', 'required':'required'}),
    )

    def clean(self):
        cleaned_data = super().clean()
        new_password = cleaned_data.get("new_password")
        confirm_password = cleaned_data.get("confirm_password")

        # Check if the new password and confirm password match
        if new_password and confirm_password:
            if new_password != confirm_password:
                raise forms.ValidationError("The two password fields must match.")
            
            # Validate the new password using Django's built-in password validators
            try:
                validate_password(new_password)  # This validates the new password using Django's validators
            except ValidationError as e:
                self.add_error("new_password", e)  # Add the error to the 'new_password' field

        return cleaned_data
