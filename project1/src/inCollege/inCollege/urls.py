"""inCollege URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from forum.views import forum_view, communities_forum_view, create_post, postDetail, upvote_post, upvote_comment
from users.views import register, profile, change_profile, postregisterland, view_profile
from chat.views import message_list, chat_view
from mentors.views import basic_search_people, advanced_search_people
from communities.views import community_view, search_community, add_community
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('forum/', forum_view, name = 'forum'),
    path('forum/myforum', communities_forum_view, name = 'myforum'),
    path('register/', register, name = 'register'),
    path('landed/', postregisterland, name = 'postregisterland'),
    path('login/', auth_views.LoginView.as_view(template_name = 'users/login.html'), name = 'login'),
    path('logout/', auth_views.LogoutView.as_view(template_name = 'users/logout.html'), name = 'logout'),
    path('profile/', profile, name = 'profile'),
    path('viewprofile/<int:pk>', view_profile, name = 'viewprofile'),
    path('updateprofile/', change_profile, name = 'changeprofile'),
    path('newpost/', create_post, name = 'createpost'),
    path('forum/postview/<int:pk>', postDetail, name = 'postview'),
    path('forum/postview/postlike/<int:pk>', upvote_post, name = 'postupvote'),
    path('forum/postview/commentlike/<int:pk>', upvote_comment, name = 'commentupvote'),
    path('', include('chat.urls')),
    path('mentors/', basic_search_people, name = 'mentorsearch'),
    path('mentors/advanced/', advanced_search_people, name = 'advancedsearch'),
    path('community/<int:pk>', community_view , name = 'community'),
    path('community/search/', search_community, name = 'community_search'),
    path('community/add/<int:pk>', add_community, name = 'add_community')
    ]


if settings.DEBUG == True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
