
from django.shortcuts import render, HttpResponse
from files.models import *
from django.contrib import messages
from django.shortcuts import redirect

def home(request):
# Create your views here.

    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        content = request.POST['content']
        print(name,email,phone,content)

        if len(name)<2 or len(email)<5 or len(content)<3:
            messages.error(request, "Please fill the form Correctly")
        else:
            contact = Contact(name=name, email=email, phone=phone, content=content)
            contact.save()
            messages.success(request, ": Sent, Thank You.")
    return render(request,'chartapp/aboutus.html')

