from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Community(models.Model): 
	community_name = models.CharField(blank = False, null = False, max_length=120) 

	