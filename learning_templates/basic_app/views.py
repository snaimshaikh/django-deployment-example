from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,"basic_app/index.html")

def other(request):
    return render(request,"basic_app/other.html")

def templates(request):
    return render(request,"basic_app/template_tags.html")