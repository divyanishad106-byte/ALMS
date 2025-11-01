# models.py – defines database tables (as per synopsis)
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    preferences = models.JSONField(default=dict, blank=True)
    progress = models.JSONField(default=dict, blank=True)

class Course(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)

class Module(models.Model):
    course = models.ForeignKey(Course, related_name='modules', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField()
    order = models.IntegerField(default=0)

class Assessment(models.Model):
    module = models.ForeignKey(Module, related_name='assessments', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    questions = models.JSONField(default=list)

class Feedback(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    module = models.ForeignKey(Module, null=True, blank=True, on_delete=models.SET_NULL)
    rating = models.IntegerField(default=5)
    comments = models.TextField(blank=True)