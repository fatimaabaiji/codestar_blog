from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('post/<slug:slug>/', views.post_detail, name='post_detail'),
    path('event/<int:event_id>/', views.event_detail, name='event_detail'),  # Add this line
]