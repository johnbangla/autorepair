from django.shortcuts import render
from django.views.generic import View
from django.core.mail import send_mail
from django.contrib import messages
from .models import Project
# Create your views here.
def index(request):
   return render(request, 'index.html', {})

def about(request):
   return render(request, 'about.html', {})

def service(request):
   return render(request, 'services.html', {}) 
def project(request):
       projectlist = Project.objects.all()
       return render(request, 'project.html', {'projectlist': projectlist})     

def blog(request):
       return render(request, 'blog.html', {})   
def contact(request):
       return render(request, 'contact.html', {})   

class SendFormEmail(View):
    
    def  get(self, request):

        # Get the form data 
        name = request.GET.get('message-name', None)
        email = request.GET.get('message-email', None)
        message = request.GET.get('message', None)

        # Send Email
        send_mail(
            'Subject - Django Email Testing', 
            'Hello ' + name + ',\n' + message, 
            'tmth@jsoft.website', # Admin
            [
                email,
            ]
        ) 

        # Redirect to same page after form submit
        messages.success(request, ('Email sent successfully.'))
        return render(request,'index.html')