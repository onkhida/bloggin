from . import views
from django.urls import path
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/', views.user_login, name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='accounts/logout.html'), name='logout'),
    path('register/', views.user_register, name='register'),

]
