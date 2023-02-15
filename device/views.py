from django.shortcuts import render

def device(self, request):
    return render(request, 'device/index.html')
