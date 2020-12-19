from django.shortcuts import render

from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView

from .models import Post
# Create your views here.

class BlogListView(ListView):
    model = Post
    template_name = 'blog/home.html'

class BlogDetailView(DetailView):
    model=Post
    template_name= 'blog/detalhe_post.html'

class BlogCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
     model = Post
     template_name = 'blog/post_new.html'
     form_class = Postform
     success_message = "%(field)s - criado com sucesso"
