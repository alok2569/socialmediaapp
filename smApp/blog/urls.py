from django.urls import path
from . import views

urlpatterns = [
path('',views.feeds,name='feeds'),
path('post/new/',views.post_new,name='post_new'),
path('feed_detail/<int:pk>/',views.feed_detail,name='feed_detail'),
path('feed_detail/<int:pk>/delete',views.delete_feed,name='delete_feed'),
path('feed_detail/<int:pk>/edit',views.feed_edit,name='feed_edit'),
path('profile',views.profile,name='profile'),
path('profile/edit',views.edit_profile,name='edit_profile'),
]