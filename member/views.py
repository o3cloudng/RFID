from django.shortcuts import render

from .models import Member
from .forms import MemberForm

# Create your views here.

def member(request):
    form = MemberForm(request.POST or None)
    context = {
        "form": form
    }
    if form.is_valid():
        firstname = form.cleaned_data.get("firstname")
        lastname = form.cleaned_data.get("lastname")
        email = form.cleaned_data.get("email")
        phone_number = form.cleaned_data.get("phone_number")
        address = form.cleaned_data.get("address")
        parent_guardian = form.cleaned_data.get("parent_guardian")
        tag_id = form.cleaned_data.get("tag_id")
        notify = form.cleaned_data.get("notify")

        print("Data: ", firstname, lastname, email)

        member_object = Member.objects.create(firstname=firstname,lastname=lastname,email=email,phone_number=phone_number,address=address,parent_guardian=parent_guardian, tag_id=tag_id, notify=notify)
        
        print("MEMBERS", member_object)
        context["object"] = member_object 
        context["created"] = True 
    return render(request, 'member/member.html', context = context)