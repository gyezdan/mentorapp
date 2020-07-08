from django.shortcuts import render
from .models import Community
from forum.models import Post
from users.models import Profile
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required



def community_view(request, pk):
	community = Community.objects.get(pk = pk)
	context = {
	'community' : community,
		'community_posts' : Post.objects.filter(communities = community).order_by('-date_posted')
	}
	return render(request,"communities/community.html", context)



def search_community(request):
	
	communities = Community.objects.all()

	if request.GET: 
	    name_query = request.GET.get('community_search')
	   
	    if name_query is not None:
	        communities = communities.filter(Q(community_name__icontains = name_query))
	   
	communities = list(set(communities))

	context = {
		'results' : communities
		}

	return render(request, "communities/search.html", context)


@login_required
def add_community(request, pk):
	if request.method == 'POST':
		community = Community.objects.get(pk = pk)
		profile = Profile.objects.get(user = request.user)
		profile.communities.add(community)
		next = request.POST.get('next', '/')
		return HttpResponseRedirect(next)
