from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ContactForm
from django.contrib import messages
from .models import Teacher

# Create your views here.

def home(request):
    teachers = Teacher.objects.distinct('speciality')
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'form has been sent')
            return redirect('home')
        else:
            messages.error(request, 'something went wrong. Please try again!')
    context = {
        'form' : form,
        'teachers' : teachers
    }
    return render(request, 'home/index.html', context)

def about(request):

    return render(request, 'home/about.html')

def teacher(request):
    teachers = Teacher.objects.all()
    context = {
        'teachers' : teachers
    }
    return render(request, 'home/teacher.html', context)