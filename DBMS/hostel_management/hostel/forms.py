from django import forms
from .models import Student, Room

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'room']

    def __init__(self, *args, **kwargs):
        super(StudentForm, self).__init__(*args, **kwargs)
        self.fields['room'].queryset = Room.objects.all()
