from django.db import models

class	Post(models.Model):	
    title	=	models.CharField(max_length=200)	
    content	=	models.TextField(default="test")	
    created_at	=	models.DateTimeField(auto_now_add=True)	
def	__str__(self):	
    return	self.title

# Create your models here.
