from django.db import models

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=122)
    email=models.CharField(max_length=122)
    phone=models.CharField(max_length=22)
    message=models.TextField()
    

    def _str_(self):
        return self.name 
    
