from . import views
from django.urls import path

urlpatterns = [
    path('make/', views.post_create, name='post_create'),
    path('<int:id>/', views.post_detail, name='post_detail'),
    path('', views.post_list, name='post_list'),

]
