from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.views.generic.edit import FormView
from django.contrib import messages
from django.urls import reverse_lazy

from .models import Member
from .forms import MemberForm

# Create your views here.
class MemberList(ListView):
    model = Member
    context_object_name = "members"
    paginate_by = 4
    template_name = 'member/members.html'


class MemberCreateForm(CreateView):
    template_name = 'member/add_member.html'
    model = Member
    form_class = MemberForm
    # fields = ['firstname','lastname','email','tag_id','phone_number','parent_guardian','notify','address']
    success_url = reverse_lazy('member')
    success_message = "Member was created successfully"
    
   
    def form_valid(self, form):
        # form.instance.user = self.request.user
        messages.success(self.request, "The member was created successfully.")
        return super(MemberCreateForm,self).form_valid(form)

# class MemberDetail(DetailView):
#     pass

class MemberUpdate(UpdateView):
    model = Member
    form_class = MemberForm
    template_name = 'member/add_member.html'
    success_message = "Member was updated successfully"
    
    def get_success_url(self):
        pk = self.kwargs["pk"]
        messages.success(self.request, "Member was updated successfully.")
        return reverse_lazy("member-update", kwargs={"pk": pk})

class MemberDetail(DetailView):
    model = Member
    form_class = MemberForm
    template_name = 'member/member_profile.html'

class MemberDelete(DeleteView):
    model = Member
    template_name = 'member/confirm_delete.html'
    success_url = reverse_lazy('member')
    success_message = "Member deleted successfully"


# class MemberList1(View):
#     def get(self, request):
#         # form = MemberForm()
#         members = Member.objects.all()
#         context = {
#             "members":members
#             }
#         print("CONTEXT", context)
#         return render(request, 'member/member.html', context)

#     def post(self, request):
#         form = MemberForm(request.POST or None)
#         context = {
#             "form": form
#         }
#         if form.is_valid():
#             firstname = form.cleaned_data.get("firstname")
#             lastname = form.cleaned_data.get("lastname")
#             email = form.cleaned_data.get("email")
#             phone_number = form.cleaned_data.get("phone_number")
#             address = form.cleaned_data.get("address")
#             parent_guardian = form.cleaned_data.get("parent_guardian")
#             tag_id = form.cleaned_data.get("tag_id")
#             notify = form.cleaned_data.get("notify")

#             print("Data: ", firstname, lastname, email)

#             member_object = Member.objects.create(firstname=firstname,lastname=lastname,email=email,phone_number=phone_number,address=address,parent_guardian=parent_guardian, tag_id=tag_id, notify=notify)
            
#             print("MEMBERS", member_object)
#             context["object"] = member_object 
#             context["created"] = True 
#         return render(request, 'member/member.html', context = context)

# class MemberDetails(View):
#     def get(self, request, pk):
#         member = Member.objects.get(id=pk)
#         context = {"members":members}
#         return render(request, 'member/member.html', context)

#     def post(self, request, pk):
#         member = Member.objects.get(id=pk)
#         member.firstname = request.POST.get("firstname")
#         member.lastname = request.POST.get("lastname")
#         member.email = request.POST.get("email")
#         member.phone_number = request.POST.get("phone_number")
#         member.address = request.POST.get("address")
#         member.parent_guardian = request.POST.get("parent_guardian")
#         member.tag_id = request.POST.get("tag_id")
#         member.notify = request.POST.get("notify")
#         member.save()
#         return render(request, 'member/member.html', context = context)


# class MemberDelete(View):
#     def get(self, request, pk):
#         member = Member.objects.get(id=pk)
#         context = { "member":member}
#         return render(request, 'member/member.html', context = context)

#     def post(self, request, pk):
#         member = Member.objects.get(pk=pk)
#         member.delete()
#         # context = {"members":members}
#         return redirect("members")

# def member(request):
#     form = MemberForm(request.POST or None)
#     context = {
#         "form": form
#     }
#     if form.is_valid():
#         firstname = form.cleaned_data.get("firstname")
#         lastname = form.cleaned_data.get("lastname")
#         email = form.cleaned_data.get("email")
#         phone_number = form.cleaned_data.get("phone_number")
#         address = form.cleaned_data.get("address")
#         parent_guardian = form.cleaned_data.get("parent_guardian")
#         tag_id = form.cleaned_data.get("tag_id")
#         notify = form.cleaned_data.get("notify")

#         print("Data: ", firstname, lastname, email)

#         member_object = Member.objects.create(firstname=firstname,lastname=lastname,email=email,phone_number=phone_number,address=address,parent_guardian=parent_guardian, tag_id=tag_id, notify=notify)
        
#         print("MEMBERS", member_object)
#         context["object"] = member_object 
#         context["created"] = True 
#     return render(request, 'member/member.html', context = context)