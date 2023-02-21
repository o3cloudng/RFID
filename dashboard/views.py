from django.shortcuts import render
from django.contrib.auth import login, authenticate  # add to imports
from django.contrib.auth.decorators import login_required
from . import forms
from django.shortcuts import redirect



@login_required(login_url='/login/')
def dashboard(request):
    return render(request, 'dashboard/index.html')




def login_page(request):
    form = forms.LoginForm()
    message = ''
    if request.method == 'POST':
        form = forms.LoginForm(request.POST)
        print("FORM: ", request.POST.get("email"))
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['email'],
                password=form.cleaned_data['password'],
            )
            if user is not None:
                login(request, user)
                # message = f'Hello {user.email}! You have been logged in'
                return redirect('dashboard')
            else:
                message = 'Login failed!'
    return render(
        request, 'dashboard/login.html', context={'form': form, 'message': message})