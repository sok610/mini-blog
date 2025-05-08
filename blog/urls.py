from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('create/', views.post_create, name='post_create'),
    path('delete/<int:post_id>/', views.post_delete, name='post_delete'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('signup/', views.user_signup, name='signup'),
    path('my-posts/', views.my_posts, name='my_posts'),
    path('edit/<int:post_id>/', views.post_edit, name='post_edit'),
]