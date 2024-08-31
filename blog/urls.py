from django.urls import path
from .views import PostNewView, PostDetailView, PostUpdateView, PostDeleteView


urlpatterns = [
    path('post/new', PostNewView.as_view(), name='post_new'),
    path('post/<int:pk>', PostDetailView.as_view(), name='post_detail'),
    path('post/update/<int:pk>', PostUpdateView.as_view(), name='post_update'),
    path('post/delete/<int:pk>', PostDeleteView.as_view(), name='post_delete'),
]