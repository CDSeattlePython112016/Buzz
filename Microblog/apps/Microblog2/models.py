from __future__ import unicode_literals

from django.db import models

class User(models.Model):
	first_name = models.CharField(max_length=45)
	last_name = models.CharField(max_length=45)

# Create your models here.
