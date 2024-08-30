from django.urls import path
from .views import PostNewView, PostDetailView


urlpatterns = [
    path('post/new', PostNewView.as_view(), name='post_new'),
    path('post/<int:pk>', PostDetailView.as_view(), name='post_detail'),
]