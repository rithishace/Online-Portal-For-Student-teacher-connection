from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from .forms import AssignmentForm,view_assignment_form
from .models import Assignment
from sassignments.models import Solution  
#from upload.models import Book
import random
import string
# Create your views here.

def assignment_upload(request):
    form=AssignmentForm(request.POST,request.FILES)
    letter=string.ascii_letters+string.digits
    unique=''.join((random.choice(letter) for i in range(6)))
    
    if request.method=="POST":
        
        if form.is_valid():
            doc=Assignment(Assignment_Code=str(unique),Grade=request.POST['Grade'],Subject_Name=request.POST['Subject_Name'],Description=request.POST['Description'],Content=request.FILES['Content'],user=request.user)
            doc.save()
            
    
    else:
        form=AssignmentForm()

    assignments=Assignment.objects.filter(user=request.user)
    return render(request,'assignment.html',{
        'assignments':assignments,'form':form})


def delete_assignment(request,pk):
    if request.method == 'POST':
        book=Assignment.objects.get(pk=pk)
        book.delete()
    return redirect('assignment')

def view_ass(request):
    form=view_assignment_form(request.POST)
    if request.method=="POST":
        
        if form.is_valid():
            form.save()
    
    pr=Solution.objects.filter(Assignment_Code=request.POST.get('Assignment_Code'))
    return render(request,'view_soln.html',{
        'pr':pr,'form':form})

def delete_solution(request,pk):
    if request.method == 'POST':
        book=Solution.objects.get(pk=pk)
        book.delete()
    return redirect('ViewSolution')
