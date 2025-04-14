# admin.py

from django.contrib import admin
from .models import Student, Room

# Register the models
admin.site.register(Student)
admin.site.register(Room)
