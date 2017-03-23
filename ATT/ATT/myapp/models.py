from __future__ import unicode_literals
from django.db import models

# Create your models here.
 
class AppointmentsModel(models.Model):
	appointment_date = models.CharField(max_length=100)
	appointment_time = models.CharField(max_length=100)
	description = models.TextField(max_length=100)
	
	def __str__(self):
		return self.appointment_date
	
