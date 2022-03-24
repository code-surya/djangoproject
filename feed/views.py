from tempfile import template
from django.views.generic import ListView, DetailView

from .models import Post

class Homepage(ListView):
    http_method_name = ["get"]
    template_name = "feed/home.html"
    model = Post
    context_object_name = "posts"
    queryset = Post.objects.all().order_by('-id')[0:30]

class PostDetailView(DetailView):
    http_method_name = ["get"]
    template_name = "feed/detail.html"
    model = Post
    context_object_name = "post"