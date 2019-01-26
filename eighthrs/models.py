from django.db import models

# Create your models here.
# class WorkDay(models.Model):
#     date = models.DateTimeField()
#     desk_time = models.IntegerField()
#     target_intervals = models.IntegerField()
#     location = models.CharField(max_length=100)
#     description = models.TextField()
#     exercise = models.OneToManyField('Exercise')
#
class Profile(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    work_day = models.OneToManyFields('WorkDay')
# class Exercise(models.Model):
#     description = models.CharField(max_length=100)
#     exercise_type = models.ManyToManyField('ExerciseType', blank=True)
#     reps = models.IntegerField()
#
# class ExerciseType(models.Model):
#     description = models.CharField(max_length=50)
#
# class Workout(models.Model):
#     work_day = models.OneToOneField('WorkDay')
