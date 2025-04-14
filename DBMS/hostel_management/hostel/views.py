from django.shortcuts import render, redirect
from django.core.exceptions import ValidationError
from .forms import StudentForm
from .models import Room, Student
from datetime import date
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .forms import LoginForm, RegisterForm
from django.contrib.auth import logout


# Login View
def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('booking')  # Replace with your homepage URL name
        else:
            return render(request, 'hostel/login.html', {'form': form, 'error': 'Invalid credentials'})
    else:
        form = LoginForm()
    return render(request, 'hostel/login.html', {'form': form})

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to login after registration
        else:
            return render(request, 'hostel/register.html', {'form': form, 'error': 'Error in registration'})
    else:
        form = RegisterForm()
    return render(request, 'hostel/register.html', {'form': form})

def booking_view(request):
    error_message = None

    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            try:
                student = form.save(commit=False)
                student.joining_date = date.today()  # Set today's date
                student.save()
                return redirect('success')
            except ValidationError as e:
                error_message = e.messages[0]
    else:
        form = StudentForm()

    return render(request, 'hostel/booking.html', {'form': form, 'error': error_message})


def success_view(request):
    return render(request, 'hostel/success.html')


def logout_view(request):
    logout(request)  # Logs the user out
    return redirect('login')  # Redirect to the login page after logout
