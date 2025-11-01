# admin.py – placeholder for admin registration
from django.contrib import admin
from .models import User, Course, Module, Assessment, Feedback

admin.site.register([User, Course, Module, Assessment, Feedback])