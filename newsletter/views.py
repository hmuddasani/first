from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render
from django.template.context_processors import csrf
#import SignUpForm
from .models import SignUp
from .forms import SignUpForm, ContactForm

# Create your views here.

def home(request):
  title = "Sign Up Now"
  
  #add a form
  form = SignUpForm(request.POST or None)  
  context = {
              "title": title,
			  "form" : form,
			  }	 
			  
  if form.is_valid():
    instance = form.save(commit=False)
    instance.save()
    context = {
	           "title": "Thank You for registering",
			   }
  if request.user.is_authenticated and request.user.is_staff:
     queryset = SignUp.objects.all().order_by('-datecreated')#.filter(name="abc")
     context = {
           "queryset" : queryset}
  return render(request,'home.html', context)

def contact(request):
   title = "Contact Us"
   form = ContactForm(request.POST or None)
   # to send email
   #Subject = "Hello There"
   #Message = "This is the message"
   #from_emailid =  settings.EMAIL_HOST_USER
   #to_emailid = [from_emailid, 'harshitareddym@gmail.com']
   #send_mail(Subject, Message,from_emailid,to_emailid,fail_silently=False)   
   def clean_email(self):
      email = self.cleaned_data.get('email')
      email_base,provider = email.split("@")
      domain, extension = provider.split(".")
      if not extension == "edu":
         raise forms.ValidationError("Please use a college email address")
      return email
   def clean_full_name(self):
       full_name = self.cleaned_data.get('full_name')
       newname = full_name.replace(' ', '')
       if name:
         if not newname.isalpha():
				raise forms.ValidationError("Please enter valid name")
       return full_name
   context = {
              "form" : form,
			  "title" : title,
			  }
   
   return render(request, 'forms.html', context)
   
def about(request):
   return render(request, 'about.html' , {})