from django.shortcuts import render, redirect
from django.contrib import messages
from users.forms import UserRegisterForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required
from users.models import Profile 
from forum.models import Post, Comment
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User 


def register(request):
    form = UserRegisterForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created!You are logged in now.')
            new_user = authenticate(username=form.cleaned_data['username'],
                                    password=form.cleaned_data['password1'],
                                    )
            login(request, new_user)
            
            return redirect('postregisterland')
        else:
            form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


def postregisterland(request):
    return render(request, 'users/landed.html')



def view_profile(request, pk):
    user = User.objects.get(pk = pk)
    posts = Post.objects.filter(author = user)
    context = {
        'user' : user,
        'posts' : posts
    }
    return render(request, 'users/viewprofile.html', context)



@login_required
def profile(request):
    posts_number, advice_number, upvotes_count = get_stats(request.user.id)
    print(posts_number)
    print(advice_number)
    print(upvotes_count)
    context = {
        'posts' : Post.objects.filter(author = request.user),
        'posts_number' : int(posts_number),
        'advice_number': advice_number,
        'upvotes_count': upvotes_count

    }
    return render(request, 'users/profile.html', context)

@login_required
def change_profile(request):
    form = ProfileUpdateForm(request.POST, request.FILES, instance = request.user.profile)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, f'Your profile had been updated')
            return redirect('profile')
    else:
       form = ProfileUpdateForm(instance = request.user.profile)
    return render(request, 'users/changeprofile.html', {'form': form})



def get_stats(profile_user): 
    user = User.objects.get(pk = profile_user)
    user_posts = Post.objects.filter(author= user)
    user_comments = Comment.objects.filter(author = user)
    posts_number = user_posts.count()
    advice_number = user_comments.count()
    upvotes_count = 0
    for post in user_posts:
        upvotes_count+= post.upvotes
    for comment in user_comments:
        upvotes_count += comment.upvotes
    return posts_number, advice_number, upvotes_count
