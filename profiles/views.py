from django.shortcuts import render
from .models import Profile
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from blog.models import Post

@login_required
def user_profile_detail(request, username):
    user = Profile.objects.get(user=User.objects.get(username=username))
    user_posts = Post.objects.filter(author=request.user)

    context = {'user_profile':user,
               'posts':user_posts}
    return render(request, 'profile/profile_detail.html', context)
