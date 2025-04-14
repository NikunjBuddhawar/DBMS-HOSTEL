from django.shortcuts import render, redirect
from django.core.exceptions import ValidationError
from .forms import StudentForm
from .models import Room, Student
from datetime import date

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
