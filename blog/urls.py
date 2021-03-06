from django.urls import path, include
from . import views
from django.contrib import admin

urlpatterns = [
    path('', views.post_list, name = 'post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('post/delete/<int:pk>/', views.confirm_delete, name='confirm_delete'),
    path('comment/<int:pk>/approve/', views.comment_approve, name='comment_approve'),
    path('comment/<int:pk>/remove/', views.comment_remove, name='comment_remove'),
    path('account/profile/', views.profile_page, name='profile_page'),
    path('account/profile/delele', views.delete_user, name = 'delete_user'),
]

