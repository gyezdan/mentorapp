from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from users.models import Profile


class UserRegisterForm(UserCreationForm):
	email = forms.EmailField(required = True)
	class Meta:
	    model = User
	    fields = ['username',
		    'email',
		    'password1',
		    'password2',
			]


class ProfileUpdateForm(forms.ModelForm):
	class Meta: 
		model = Profile
		fields = ['firstName',
				'lastName',
				'profilePicture',
				'homeCity',
				'homeState',
				'homeCountry',
				'priorInstitute', 
				'priorGradYear', 
				'basedCity',
				'basedState',
				'basedCountry', 
				'currentInstitute',
				'currentGradYear', 
				'currentStatus', 
				'major1', 
				'major2',
				'minor1',
				'minor2' ]
