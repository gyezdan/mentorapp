from django.db import models
from django.contrib.auth.models import User
from multiselectfield import MultiSelectField
# Create your models here.

STATUS_CHOICES = (('A', 'Accepted'),
              ('R', 'Rejected'))

class MentorRequest(models.Model):
	request_from = models.OneToOneField(User, on_delete = models.CASCADE, related_name = 'sentby' )
	request_to = models.OneToOneField(User, on_delete = models.CASCADE, related_name = 'receivedby')
	request_status = MultiSelectField(choices=STATUS_CHOICES)
	request_message = models.CharField(default = '', blank = True, null = True, max_length=120)
