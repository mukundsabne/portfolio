from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'index.html')

def forajax(request):
    # name = request.GET['name']
    # color = request.GET['color']
    return render(request,'home12.html')
