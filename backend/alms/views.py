# views.py – logic layer (skeleton)
from django.shortcuts import render
from .models import Course, Module, Feedback

def home(request):
    return render(request, "home.html")

def dashboard(request):
    courses = Course.objects.all()
    return render(request, "dashboard.html", {"courses": courses})

def feedback(request):
    feedbacks = Feedback.objects.all()
    return render(request, "feedback.html", {"feedbacks": feedbacks})