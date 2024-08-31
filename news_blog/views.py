from django.views.generic import TemplateView
from django.views.generic import View
from blog.models import Post
from django.core.paginator import Paginator
from django.shortcuts import render


class HomeView(TemplateView):
    template_name = 'home.html'


class BlogView(View):
    model = Post
    template_name = 'blogs.html'
    paginate_by = 9

    def get(self, request):
        posts = Post.objects.all()
        paginator = Paginator(posts, self.paginate_by)

        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        context = {
            'post_list': page_obj
        }

        return render(request, self.template_name, context)
