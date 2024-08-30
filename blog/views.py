from django.views.generic import TemplateView, CreateView, DetailView
from .models import Post
from .forms import PostForm
from django.urls import reverse_lazy


class PostNewView(CreateView):
    model = Post
    template_name = 'post_new.html'
    form_class = PostForm
    success_url = reverse_lazy('blog_detail')


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog_detail.html'
