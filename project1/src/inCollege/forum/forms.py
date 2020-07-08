from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from users.models import Profile
from forum.models import Post, Comment


class createPost(forms.ModelForm):
	
	class Meta:
	    model = Post
	    fields = ['title',
		    'content']		

class createComment(forms.ModelForm):
	
	class Meta:
	    model = Comment
	    fields = ['commentcontent']		
