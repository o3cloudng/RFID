from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.views.generic.edit import FormView
from django.contrib import messages
from django.urls import reverse_lazy

from .models import Device
from .forms import DeviceForm

# Create your views here.
class DeviceList(ListView):
    model = Device
    context_object_name = "devices"
    paginate_by = 4
    template_name = 'device/devices.html'


class DeviceCreateForm(CreateView):
    template_name = 'device/add_device.html'
    model = Device
    form_class = DeviceForm
    # fields = ['firstname','lastname','email','tag_id','phone_number','parent_guardian','notify','address']
    success_url = reverse_lazy('device')
    success_message = "Device was created successfully"
    
   
    def form_valid(self, form):
        # form.instance.user = self.request.user
        messages.success(self.request, "The device was created successfully.")
        return super(DeviceCreateForm,self).form_valid(form)

# class MemberDetail(DetailView):
#     pass

class DeviceUpdate(UpdateView):
    model = Device
    form_class = DeviceForm
    template_name = 'device/add_device.html'
    success_message = "Device was updated successfully"
    
    def get_success_url(self):
        pk = self.kwargs["pk"]
        messages.success(self.request, "Device was updated successfully.")
        return reverse_lazy("device-update", kwargs={"pk": pk})

class DeviceDetail(DetailView):
    model = Device
    form_class = DeviceForm
    template_name = 'device/device_profile.html'

class DeviceDelete(DeleteView):
    model = Device
    template_name = 'device/confirm_delete.html'
    success_url = reverse_lazy('device')
    success_message = "Device deleted successfully"