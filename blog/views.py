from django.views.generic import TemplateView, CreateView, DetailView
from django.views.generic.edit import UpdateView, DeleteView
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


class PostUpdateView(UpdateView):
    model = Post
    template_name = 'post_update.html'
    fields = ['title', 'excerpt', 'body', 'photo']


class PostDeleteView(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('blogs')
