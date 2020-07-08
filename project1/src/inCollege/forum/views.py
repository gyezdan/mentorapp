from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.http import HttpResponseRedirect
from django.contrib import messages
from forum.models import Post, Comment
from users.models import Profile
from forum.forms import createPost, createComment
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView
from communities.models import Community
# Create your views here.

def forum_view(request):
	context = {
		'posts' : Post.objects.all().order_by('-date_posted')
	}
	return render(request,"forum/forum.html", context)


@login_required
def communities_forum_view(request):
	profile = Profile.objects.get(user = request.user)
	communities = profile.communities.all()
	posts = Post.objects.filter(communities__in = communities).order_by('-date_posted')
	print(posts)
	context = {
		'posts' : posts
	}
	return render(request,"forum/forum.html", context)


# @login_required
# def create_post(request):
# 	if request.method == 'POST':
# 		post = createPost(request.POST)
# 		if post.is_valid():
# 			p = post.save(commit = False)
# 			c1 = request.GET.get('community_1')
# 			c2 = request.GET.get('community_2')
# 			c3 = request.GET.get('community_3')
# 			c4 = request.GET.get('community_4')
# 			print(c1)
# 			add_communities(p, c1, c2, c3, c4) 
# 			p.author = request.user
# 			p.save()
# 			messages.success(request, f'Your post has been created!')
# 			return redirect('forum')
# 	else:
# 		post = createPost()
# 	return render(request, 'forum/newpost.html', {'post':post})


@login_required
def create_post(request):
	if request.method == 'POST':
		title = request.POST.get('title')
		print(title)
		content = request.POST.get('content')
		c1 = request.POST.get('community_1', default = None)
		c2 = request.POST.get('community_2', default = None)
		c3 = request.POST.get('community_3', default = None)
		c4 = request.POST.get('community_4', default = None)
		p = Post.objects.create(title = title, content = content, author = request.user)
		print(c2)
		add_communities(p, c1, c2, c3, c4) 
		p.author = request.user
		p.save()
		messages.success(request, f'Your post has been created!')
		return redirect('forum')
	return render(request, 'forum/newpost.html', {'communities' : Community.objects.all() })

@login_required
def postDetail(request, pk):
	post = Post.objects.get(pk = pk)
	if request.method == 'POST':
		newcomment = createComment(request.POST)
		if newcomment.is_valid():
				c = newcomment.save(commit = False) 
				c.author = request.user
				c.post = post
				c.save()
				messages.success(request, f'Your comment has been posted!')
				return HttpResponseRedirect(request.path_info)
	
	else:
		newcomment = createComment()

	comments = Comment.objects.filter(post = post)
	context = {'post' : post, 'comments' : comments, 'newcomment': newcomment}
	return render(request,'forum/postdetail.html', context)



def add_communities(post, community_1, community_2  , community_3, community_4):
	if community_1!= "":
		c = Community.objects.get(community_name = str(community_1))
		post.communities.add(c)

	if community_2!= "":
		c = Community.objects.get(community_name = str(community_2))
		post.communities.add(c)

	if community_3!= "":
		c = Community.objects.get(community_name = community_3)
		post.communities.add(c)

	if community_4 != "":
		c = Community.objects.get(community_name = community_4)
		post.communities.add(c)	


def upvote_post(request, pk):
	if request.method == 'POST':
		post = Post.objects.get(pk = pk)
		post.upvotes+=1
		post.save()
		next = request.POST.get('next', '/')
		return HttpResponseRedirect(next)

def upvote_comment(request, pk):
	if request.method == 'POST':
		comment = Comment.objects.get(pk = pk)
		comment.upvotes+=1
		comment.save()
		next = request.POST.get('next', '/')
		return HttpResponseRedirect(next)
