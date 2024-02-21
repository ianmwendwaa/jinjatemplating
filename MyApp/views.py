from django.shortcuts import render
from django.http import HttpResponse

def karibu(request):
    return HttpResponse("<h2>Welcome to the concrete Django</h2>")


def home(request):
    return render(request, 'index.html')
def about(request):
    return render(request, 'about.html')
def contactus(request):
    return render(request, 'contactus.html')
def gallery(request):
    return render(request, 'gallery.html')
def services(request):
    return render(request, 'services.html')
