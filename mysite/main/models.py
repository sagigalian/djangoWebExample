from django.db import models

# Create your models here.

class Person(models.Model):
	name = models.CharField(max_length=200, default="")
	phone = models.CharField(max_length=200, default="")
	email = models.CharField(max_length=200, default="")

	def __str__(self):
		return self.name