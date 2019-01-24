from django.db import models

# Create your models here.
class WorkDay(models.Model):
    date
    desk_timme
    target_intervals
class Profile(models.Model):
    name = models.CharField(max_length=100)
    height
    weight

class Exercise(models.Model):
    ex_type
    level
    reps
    sets
