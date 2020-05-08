from . import views
from django.urls import path

urlpatterns = [
    path('<str:username>/', views.user_profile_detail, name='profile'),
]
