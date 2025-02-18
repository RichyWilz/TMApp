# Create your views here.
from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserForm
from django.contrib.auth import password_validation
from django.core.exceptions import ValidationError
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.password_validation import validate_password
from .forms import PasswordChangeForm
# from .models import User


# Create your views here.

def login_view(request):
    if request.user.is_authenticated:
        return redirect("home")

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        form.fields['username'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Username'})
        form.fields['password'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Password'})

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            if username and password:
                user = authenticate(request, username=username, password=password)
                # Check if authentication is successful
                if user is not None:

                    login(request, user)
                    
                    messages.success(request, f"You are now logged in as {user}.")
                    return redirect('home')
                else:
                    messages.error(request, "Invalid username or password provided.")
            else:
                messages.error(request, "Username and password must be provided.")
        else:
            messages.error(request, "Invalid username or password provided. Please try again.")

    else:
        form = AuthenticationForm()

    # Ensure the form is always rendered if the conditions above don't redirect
    return render(request, 'login.html', {'form': form})


@login_required
def logout_view(request):
    logout(request)
    return redirect('login')  # Redirect to the login page after logout


def password_reset(request):
    if request.method == "POST":
        form = PasswordChangeForm(request.POST)
        if form.is_valid():
            new_password = form.cleaned_data["new_password"]

            # Manually validate the password against the validators
            try:
                validate_password(new_password, user=request.user)  # user=request.user ensures the password is validated for the current user
                user = request.user  # This is your custom user model
                user.set_password(new_password)  # This will hash the password
                user.save()

                # Update session auth hash to keep the user logged in
                update_session_auth_hash(request, user)

                messages.success(request, "Your password has been updated successfully.")
                return redirect("profile")  # Redirect to a profile or dashboard page
            except Exception as e:
                form.add_error("new_password", str(e))  # Add the validation error to the form
        else:
            messages.error(request, "There was an error updating your password. Please try again.")
    else:
        form = PasswordChangeForm()

    return render(request, "password_reset.html", {"form": form})




def signup(request):
    if request.method == 'GET':
        form = UserForm()

    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES)

        if form.is_valid():
            user = form.save(commit=False)
            password = form.cleaned_data['password']
            confirm_password = form.cleaned_data['confirm_password']

            # Ensure the passwords match
            if password != confirm_password:
                form.add_error('confirm_password', 'Passwords do not match')
            else:
                # Set password and validate it
                user.set_password(password)
                
                # Manually trigger password validation
                try:
                    password_validation.validate_password(password, user)
                except ValidationError as e:
                    # Add all password validation errors to the form
                    for error in e.messages:
                        form.add_error('password', error)

                # If there are no password validation errors, save the user
                if not form.errors:
                    user.save()
                    messages.success(request, "You're Account Has Been Created Successfully")
                    return redirect('home')

    return render(request, 'signup.html', {'form': form})
