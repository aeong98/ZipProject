from django.shortcuts import render, redirect

# Create your views here.
def home(request):
    return render(request,'home.html')

def curation(request):
    return render(request,'curator_page.html')

def sh_page(request):
    return render(request,'curator_page1.html')

def zip_page(request):
    return render(request,'curator_page2.html')