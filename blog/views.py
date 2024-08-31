from django.views.generic import TemplateView, CreateView, DetailView, View, FormView
from django.views.generic.edit import UpdateView, DeleteView
from .models import Post
from .forms import PostForm, CommentForm
from django.urls import reverse_lazy, reverse
from django.views.generic.detail import SingleObjectMixin


class PostNewView(CreateView):
    model = Post
    template_name = 'post_new.html'
    form_class = PostForm

    def get_success_url(self):
        # Redirect to the detail page of the created post
        return reverse_lazy('post_detail', kwargs={'pk': self.object.pk})

    # success_url = reverse_lazy('blog_detail')


class CommentGet(DetailView):
    model = Post
    template_name = 'blog_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CommentForm()
        return context


class CommentPost(SingleObjectMixin, FormView):
    model = Post
    form_class = CommentForm
    template_name = 'blog_detail.html'

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        comment = form.save(commit=False)
        comment.post = self.object
        comment.author = self.request.user
        comment.save()
        return super().form_valid(form)

    def get_success_url(self):
        post = self.get_object()
        return reverse('post_detail', kwargs={'pk': post.pk})


class PostDetailView(View):
    def get(self, request, *args, **kwargs):
        view = CommentGet.as_view()
        return view(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        view = CommentPost.as_view()
        return view(request, *args, **kwargs)


class PostUpdateView(UpdateView):
    model = Post
    template_name = 'post_update.html'
    fields = ['title', 'excerpt', 'body', 'photo']


class PostDeleteView(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('blogs')
