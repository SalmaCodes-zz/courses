from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *


# Create your views here.

# '/'
def index(request):
    context = {
        'all_courses': Course.objects.all()
    }
    return render(request, 'courses/index.html', context)


# '/create', POST method that creates an 
def create(request):
    if request.method == 'POST':
        # Validate
        errors = Course.objects.basic_validator(request.POST)
        if len(errors):
            for tag, error in errors.iteritems():
                messages.error(request, error, extra_tags=tag)
        else:
            # Create Course object.
            Course.objects.create(
                name=request.POST['name'],
                desc=request.POST['desc']
            )
    return redirect('/')


# 'confirm/<id>' renders the delete confirmation page.
def confirm(request, id):
    context = {
        'course': Course.objects.get(id=id)
    }
    return render(request, 'courses/confirm.html', context)


# 'delete/<id>', method that deletes the course.
def delete(request, id):
    course = Course.objects.get(id=id)
    course.delete()
    return redirect('/')

