from django.views.generic import ListView

from .models import Post


class Homepage(ListView):
    http_method_name = ["get"]
    template_name = "home.html"
    model = Post
    context_object_name = "posts"
    queryset = Post.objects.all().order_by('-id')[0:30]
