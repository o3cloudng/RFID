from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'index.html')


def login(request):
    return render(request, 'login.html')


def register(request):
    return render(request, 'register.html')


def logout(request):
    return render(request, 'logout.html')


def books(request):
    return render(request, 'books.html')


def books2(request):
    return render(request, 'books2.html')


def book_single(request):
    return render(request, 'book-single.html')


def contact(request):
    return render(request, 'contact.html')


def profile(request):
    return render(request, 'profile.html')
