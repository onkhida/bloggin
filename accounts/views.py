from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm, RegisterForm
from django.contrib.auth.models import User
from profiles.models import Profile

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            print(cd)
            user = authenticate(request, username=cd['username'], password=cd['password'])

            if user is not None:
                if user.is_active:
                    login(request, user)
                    print('<h2>Successful Login</h2>')
                    return redirect('post_list')

                else:
                    print('<h2>De-activated account</h2>')

            else:
                print('<h2>Invalid Login</h2>')

    else:
        form = LoginForm()

    return render(request, 'accounts/login.html', {'form':form})

def user_register(request):
    print(request.user)
    if request.user.is_authenticated == False:
        if request.method == "POST":
            form = RegisterForm(request.POST)
            if form.is_valid():
                cd = form.cleaned_data
                if cd['password1'] == cd['password2']:
                    created_user = User(username=cd['username'],
                                email=cd['email'])
                    created_user.set_password(cd['password1'])
                    created_user.save()

                    # create a profile for the user upon sign up
                    Profile.objects.create(user=created_user, bio='Hi there. I\'m using Bloggin\'')

                    return redirect('login')
                else:
                    print('Passwords must match')
                    HttpResponse('<h1>Passwords must match</h1>')
            else:
                print('Fill in the fields well')
                HttpResponse('<h1>Fill in the fields well</h1>')

        else:
            form=RegisterForm()

    else:
        return redirect('logout')

    return render(request, 'accounts/register.html',{'form':form})
