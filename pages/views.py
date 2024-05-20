from django.shortcuts import render,get_object_or_404, redirect
from .models import Book
from .forms import BookForm

#from django.http import HttpResponse
# Create your views here. controles what appears and what not

def about(request):
     return render(request,'pages/about.html')

def signup(request):
     return render(request,'pages/signup.html')

def login(request):
     return render(request,'pages/login.html')


def homeuser(request):
    books = Book.objects.all()  
    return render(request, 'pages/homeuser.html', {'books': books})

def homeadmin(request):
    books = Book.objects.all()  
    return render(request, 'pages/homeadmin.html', {'books': books})

def bookpg(request):
     return render(request,'pages/bookpg.html')

# views.py

def addbook(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('homeadmin')  # Redirect after POST to avoid resubmitting the form
    else:
        form = BookForm()
    return render(request, 'pages/addbook.html', {'form': form})


def home(request):
    books = Book.objects.all()
    return render(request, 'pages/home.html', {'books': books})


def edit(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    if request.method == "POST":
        form = BookForm(request.POST, request.FILES, instance=book)
        if form.is_valid():
            form.save()
            return redirect('homeadmin')  # Replace with your book detail view
    else:
        form = BookForm(instance=book)
    return render(request, 'pages/edit.html', {'form': form, 'book': book})

def delete_book(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    book.delete()
    return redirect('homeadmin')