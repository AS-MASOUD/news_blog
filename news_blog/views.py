from django.views.generic import TemplateView
from django.views.generic import ListView
from blog.models import Post


class HomeView(TemplateView):
    template_name = 'home.html'


class BlogView(ListView):
    model = Post
    template_name = 'blogs.html'
