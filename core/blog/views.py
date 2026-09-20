from django.shortcuts import render
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
    DetailView,
    TemplateView,
    RedirectView,
    ListView,
    DeleteView,
    FormView,
    CreateView,
    UpdateView,
    DeleteView,
)
from .forms import CreatePostForm
from django.http import HttpResponse


# Create your views here.
# class MyTemplateView(TemplateView):
#     template_name = "blog/template_view.html"

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context["name"] = "MOHSEN"
#         return context


# class MyRedirectView(RedirectView):
#     url = "https://www.djangoproject.com/"

#     def get_redirect_url(self, *args, **kwargs):
#         article_id = kwargs["article_id"]

#         print(article_id)

#         return article_id


class PostListView(LoginRequiredMixin, ListView):
    model = Post
    queryset = Post.objects.filter(status=True)
    # paginate_by = 2
    context_object_name = "articles"


class PostDetailView(LoginRequiredMixin, DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    template_name = "blog/contact.html"
    form_class = CreatePostForm
    success_url = "/blog/post/"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    form_class = CreatePostForm
    template_name = "blog/contact.html"
    success_url = "/blog/post/"


class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = "/blog/post/"
