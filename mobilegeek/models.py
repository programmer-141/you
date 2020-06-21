from django.db import models

# Create your models here.

class content(models.Model):
	heading = models.CharField(max_length=200)
	about_topic = models.TextField()
	image=models.ImageField(upload_to='photos',null=True)
	
	
