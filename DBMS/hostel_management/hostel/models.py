from django.db import models
from django.core.exceptions import ValidationError

class Room(models.Model):
    room_number = models.CharField(max_length=10, unique=True)
    capacity = models.IntegerField()
    is_occupied = models.BooleanField(default=False)

    def __str__(self):
        return self.room_number


class Student(models.Model):
    name = models.CharField(max_length=100)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    joining_date = models.DateField()

    def save(self, *args, **kwargs):
        if self.room and self.room.student_set.count() >= self.room.capacity:
            raise ValidationError(f"Room {self.room.room_number} is already at full capacity.")
        super(Student, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
