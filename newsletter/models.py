from django.db import models

class SignUp(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length= 120, blank=True, unique=True)
    birthdate = models.DateTimeField(blank=True)
    datecreated = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    def _unicode_(self):
        return self.email