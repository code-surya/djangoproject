# from urllib import request

from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
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


class CreateNewPost(LoginRequiredMixin, CreateView):
    model = Post
    template_name = "feed/create.html"
    fields = ['text']
    success_url = "/"



    def dispatch(self, request, *args, **kwargs):
        self.request = request
        return super().dispatch(request, *args, **kwargs)




    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.author = self.request.user
        obj.save
        return super().form_valid(form)

    def post(self, request, *args, **kwargs):
        post = Post.objects.create(
            text=request.POST.get("text"),
            author=request.user,
        )
        return render(
            request,
            "includes/post.html",
            {
                "post":post,
                "show_detail_link": True,
            },
            content_type="application/html"
        )
