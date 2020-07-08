from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from communities.models import Community 
from mentors.models import MentorRequest
# Create your models here.

class Profile(models.Model): 
	user = models.OneToOneField(User, on_delete = models.CASCADE)
	firstName = models.CharField(default = '', blank = True, null = True, max_length=120) 
	lastName = models.CharField(default = '', blank = True, null = True, max_length=120)
	email = models.EmailField(default = '', blank = True, null = True)
	profilePicture = models.ImageField(default = 'default.png', blank = True, null = True)
	homeCity = models.CharField(default = '', blank = True, null = True, max_length=120)
	homeState = models.CharField(default = '', blank = True, null = True, max_length=120)
	homeCountry = models.CharField(default = '', blank = True, null = True, max_length=120)
	priorInstitute = models.CharField(default = '', blank = True, null = True, max_length=120)
	priorGradYear = models.PositiveSmallIntegerField(null = True, default = 0)

	basedCity = models.CharField(default = '', blank = True, null = True, max_length=120)
	basedState = models.CharField(default = '', blank = True, null = True, max_length=120)
	basedCountry = models.CharField(default = '', blank = True, null = True, max_length=120)
	currentInstitute = models.CharField(default = '', blank = True, null = True, max_length=120)
	currentGradYear = models.PositiveSmallIntegerField(blank = True, null = True, default = 0); 
	
	currentStatus = models.CharField(default = '', blank = True, null = True, max_length=120)

	major1 = models.CharField(default = '', blank = True, null = True, max_length=120)
	major2 = models.CharField(default = '', blank = True, null = True, max_length=120)
	minor1 = models.CharField(default = '', blank = True, null = True, max_length=120)
	minor2 = models.CharField(default = '', blank = True, null = True, max_length=120)

	communities = models.ManyToManyField(Community)
	requests = models.ManyToManyField(MentorRequest)
	mentors = models.ManyToManyField(User, related_name = 'mentors')


	def __str__(self):
		return f'{self.user.username} Profile'





