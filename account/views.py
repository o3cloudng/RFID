from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.views.generic.edit import FormView
from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

from .models import User
from .forms import UserForm

# Create your views here.
class UserList(LoginRequiredMixin, ListView):
    login_url = '/login/'
    model = User
    context_object_name = "users"
    paginate_by = 4
    template_name = 'user/index.html'


class UserCreateForm(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    template_name = 'user/add_user.html'
    model = User
    form_class = UserForm
    # fields = ['firstname','lastname','email','tag_id','phone_number','parent_guardian','notify','address']
    success_url = reverse_lazy('user')
    success_message = "User was created successfully"
    
   
    # def form_valid(self, form):
    #     form.instance.user = self.request.user
    #     messages.success(self.request, "The User was created successfully.")
    #     return super(UserForm,self).form_valid(form)

# class UserDetail(DetailView):
#     pass

class UserUpdate(LoginRequiredMixin, UpdateView):
    login_url = '/login/'
    model = User
    form_class = UserForm
    template_name = 'user/add_user.html'
    success_message = "User was updated successfully"
    
    def get_success_url(self):
        pk = self.kwargs["pk"]
        messages.success(self.request, "User was updated successfully.")
        return reverse_lazy("user-update", kwargs={"pk": pk})

class UserDetail(LoginRequiredMixin, DetailView):
    login_url = '/login/'
    model = User
    form_class = UserForm
    template_name = 'user/user_profile.html'

class UserDelete(LoginRequiredMixin, DeleteView):
    login_url = '/login/'
    model = User
    # template_name = 'member/confirm_delete.html'
    success_url = reverse_lazy('user:user')
    success_message = "User deleted successfully"


@login_required(login_url='/login/')
def user_profile(request):
    return render(request, 'user/my_profile.html')

@login_required(login_url='/login/')
def login(request):
    return render(request, 'login.html')

@login_required(login_url='/login/')
def register(request):
    return render(request, 'register.html')


# def logout(request):
#     return render(request, 'logout.html')


# def books(request):
#     return render(request, 'books.html')


# def books2(request):
#     return render(request, 'books2.html')


# def book_single(request):
#     return render(request, 'book-single.html')


# def contact(request):
#     return render(request, 'contact.html')


# def profile(request):
#     return render(request, 'profile.html')
