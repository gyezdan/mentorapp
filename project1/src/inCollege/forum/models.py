from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from communities.models import Community 
# Create your models here.

class Post(models.Model):
	title = models.CharField(max_length = 120)
	content = models.TextField()
	date_posted = models.DateTimeField(default=timezone.now)
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	communities = models.ManyToManyField(Community)
	upvotes = models.IntegerField(default = 0)

	def __str__(self):
		return self.title


class Comment(models.Model):
	commentcontent = models.CharField(max_length = 1200)
	date_posted = models.DateTimeField(default=timezone.now)
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	post = models.ForeignKey(Post, on_delete = models.CASCADE)
	upvotes = models.IntegerField(default = 0)