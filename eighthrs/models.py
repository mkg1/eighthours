from django.db import models

# Create your models here.
class WorkDay(models.Model):
    date = models.DateTimeField()
    desk_time = models.IntegerField()
    target_intervals = models.IntegerField()
    location = models.CharField(max_length=100)
    description = models.TextField()

class Profile(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)

class Exercise(models.Model):
    exercise_type = models.ManyToManyField('ExerciseType', blank=True)
    reps = models.IntegerField()

class Workout(models.Model):
    work_day = models.OneToOneField('WorkDay')
        
