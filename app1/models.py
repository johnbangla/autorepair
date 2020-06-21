from django.db import models

# Create your models here.
class Project (models.Model):
	title = models.CharField(max_length=100)
	description = models.TextField()
	photo = models.ImageField(upload_to='pics')
