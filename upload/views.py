from django.shortcuts import render,redirect 
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.models import User
from .forms import BookForm
from .models import Book


def book_list(request):
    books=Book.objects.filter(user=request.user)
    return render(request,'book_list.html',{
        'books':books})


def upload_book(request):
    if request.method=="POST":
        form=BookForm(request.POST,request.FILES)
        if form.is_valid():
            doc=Book(Teacher_Name=request.POST['Teacher_Name'],Class=request.POST['Class'],Subject_Name=request.POST['Subject_Name'],Description=request.POST['Description'],Content=request.FILES['Content'],user=request.user)
            doc.save()
            return redirect('upload')
    else:
        form=BookForm()
        
    return render(request,'upload_book.html', {
        'form':form
    })

def delete_book(request,pk):
    if request.method == 'POST':
        book=Book.objects.get(pk=pk)
        book.delete()
    return redirect('upload')
