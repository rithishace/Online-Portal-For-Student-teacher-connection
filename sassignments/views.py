from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from .forms import SolutionForm,view_assignment_form
from .models import Solution,view_assignment
from assignment.models import Assignment
# Create your views here.

def view_ass(request):
    form=view_assignment_form(request.POST)
    if request.method=="POST":
        
        if form.is_valid():
            form.save()

    
    s=Assignment.objects.filter(Assignment_Code=request.POST.get('Assignment_Code'))
    return render(request,'view_ass.html',{
        's':s,'form':form})

def upload_solution(request):
    form=SolutionForm(request.POST,request.FILES)
    if request.method=="POST":
        if form.is_valid():
            form.save()
            return redirect('view')
    
    else:
        form=SolutionForm()

    return render(request,'solution.html',{
        'form':form })    
