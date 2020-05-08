from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.http import HttpResponse
from django.utils.text import slugify
from .models import Post
from .forms import PostCreateForm
from django.contrib.auth.decorators import login_required

def post_list(request):
    context = {
     'posts': Post.objects.all()
    }
    return render(request, 'blog/post_list.html', context)

def post_detail(request, id):
    context = {
        'post': get_object_or_404(Post, id=id)
    }

    return render(request, 'blog/post_detail.html', context)

@login_required
def post_create(request):
    if request.method == 'POST':
        form = PostCreateForm(request.POST, request.FILES)
        print(form)
        print(request.POST)
        print(request.GET)
        print(form.is_valid())
        print(request.FILES)
        # print(request.POST.get('thumbnail').url)
        if form.is_valid():
            cd = form.cleaned_data
            new_post = form.save(commit=False)
            new_post.author = request.user
            new_post.slug = slugify(new_post.title)
            new_post.save()
            return redirect('post_list')
        else:
            return HttpResponse('Please fill in the fields correctly')

    else:
        form = PostCreateForm()

    context = {
        'form':form,
    }

    return render(request, 'blog/post_create.html', context)
