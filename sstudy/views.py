from django.shortcuts import render
from django.contrib.auth.models import User
from .forms import StudentForm
from .models import Student
from upload.models import Book
# Create your views here.

def sbook_list(request):
    form=StudentForm(request.POST)
    if request.method=="POST":
        
        if form.is_valid():
            form.save()
    
    sc=Book.objects.filter(Class=request.POST.get('Class'),Subject_Name=request.POST.get('Subject_Name'))
    return render(request,'sstudy_list.html',{
        'sc':sc,'form':form})

def student_home(request):
    return render(request,'student_home.html')
    
