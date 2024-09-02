from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.views import View
from django.views.generic import ListView
from blog.models import Post
from .forms import CustomUserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth import logout
from django.shortcuts import redirect, render

from .models import CustomUser


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


def custom_logout_view(request):
    logout(request)
    return redirect('home')


class UserProfile(View):
    model = Post
    template_name = 'user_profile.html'
    paginate_by = 6
    # context_object_name = 'post_list'

    # def get_queryset(self):
    #     # Get the user's posts
    #     user_id = self.kwargs.get('pk')
    #     user_profile = CustomUser.objects.get(id=user_id)
    #     return Post.objects.filter(author=user_profile).order_by('-date')
    #
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     user_id = self.kwargs.get('pk')
    #     user_profile = CustomUser.objects.get(id=user_id)
    #     context['profile'] = user_profile
    #     return context

    def get(self, request, pk):
        # user = request.user  # Get the currently logged-in user
        user_profile = CustomUser.objects.get(id=pk)
        user_posts = Post.objects.filter(author=user_profile).order_by('-date')

        # Pagination setup
        paginator = Paginator(user_posts, self.paginate_by)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        context = {
            'profile': user_profile,
            'post_list': page_obj,  # Pass paginated posts
        }

        return render(request, self.template_name, context)
