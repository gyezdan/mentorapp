from django.shortcuts import render, redirect
from django.contrib.auth.models import User 
from django.db.models import Q
from users.models import Profile
from mentors.models import MentorRequest
import pandas as pd
import geonamescache
from lists.list import countries

# Create your views here

def basic_search_people(request):
	if request.GET:
		query = request.GET.get('q')
		queryset = []
		queries = query.split(" ")

		for q in queries:
			profiles = Profile.objects.filter(Q(firstName__icontains = q)|Q(lastName__icontains = q))
			
			for profile in profiles:
				queryset.append(profile)

		queryset = list(set(queryset))
		print(queryset)
		context={
			'results' : queryset
			}

	else: 
		context = {
		'results' : Profile.objects.all()
		}

	return render(request, "mentors/results.html", context)

def advanced_search_people(request):

	profiles = Profile.objects.all()

	if request.GET: 
	    name_query = request.GET.get('fullname')
	    major_query = request.GET.get('major')
	    institute_query = request.GET.get('institute')
	    communities_query = request.GET.get('communities')
	    hs_city_query = request.GET.get('highschool_city')
	    hs_country_query = request.GET.get('highschool_country')
	    uni_city_query = request.GET.get('uni_city')
	    uni_country_query = request.GET.get('uni_country')
	    hs_grad_query = request.GET.get('highschool_grad')
	    uni_grad_query = request.GET.get('uni_grad')
	    interests_query = request.GET.get('prof_interests')

	    if name_query is not None:
	        profiles = profiles.filter(Q(firstName__icontains = name_query)|Q(lastName__icontains = name_query))

	    if major_query is not None:
	        profiles = profiles.filter(Q(major1__icontains = major_query)|Q(major2__icontains = major_query)|Q(minor1__icontains = major_query)|Q(minor1__icontains = major_query))
	        

	    if institute_query is not None:
	        profiles = profiles.filter(Q(priorInstitute__icontains = institute_query)|Q(currentInstitute__icontains = institute_query))
	        
	    if hs_city_query is not None:
	        profiles = profiles.filter(Q(homeCity__icontains = hs_city_query))

	    if hs_country_query is not None:
	        profiles = profiles.filter(Q(homeCountry__icontains = hs_country_query))

	    if uni_city_query is not None:
	        profiles = profiles.filter(Q(basedCity__icontains = uni_city_query))

	    if uni_country_query is not None:
	        profiles = profiles.filter(Q(basedCountry__icontains = uni_country_query))

	profiles = list(set(profiles))


	context = {
		'results' : profiles,
		'country_cat' : countries
		}

	return render(request, "mentors/advancedresults.html", context)


def send_mentor_request(request, pk):
	if request.method == 'POST':
		request = MentorRequest()
		request.request_from = request.user
		request.request_to = User.objects.get(pk = pk)
		request.request_message = request.POST.get('message')
		request.save()
		next = request.POST.get('next', '/')
		return HttpResponseRedirect(next)
