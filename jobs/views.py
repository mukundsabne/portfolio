from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'index.html')

def forajax(request):
    return render(request,'home1.html')
