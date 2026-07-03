from django.shortcuts import render

def home(request):
    return render(request, template_name='blog/home.html')

def contact(request):
    return render(request,template_name='blog/contact.html')
