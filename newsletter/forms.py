from django import forms
from .models import SignUp

class SignUpForm(forms.ModelForm):
  class Meta:
      model = SignUp
      fields = ['name','email', 'birthdate']
  def clean_email(self):
      email = self.cleaned_data.get('email')
      email_base,provider = email.split("@")
      domain, extension = provider.split(".")
      if not extension == "edu":
	     raise forms.ValidationError("Please use a college email address")
      return email
  def clean_name(self):
        name = self.cleaned_data.get('name')
        if name:
          newname = name.replace(' ', '')
          if not newname.isalpha():
            raise forms.ValidationError("Please enter valid name")
        return name
  def clean_birthdate(self):
        birthdate = self.cleaned_data.get('birthdate')
        if birthdate:
          if birthdate.year > 2015:
		     raise forms.ValidationError("Invalid Year: Please enter birthdate before 2015")
          if birthdate.year > 2000:
             raise forms.ValidationError("You must be atleast 15 years old")		
        return birthdate
	#custom form without creating model
class ContactForm(forms.Form):
     full_name = forms.CharField(required=False)
     email = forms.EmailField()
     message = forms.CharField()
