from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy

from posts.models import Post
from django.views import generic


# Class Retrieve LIST
class IndexView(generic.ListView):
    # model = Post
    queryset = Post.objects.filter(status=True)
    template_name = "posts/index.html"
    context_object_name = "posts"


# Class Retrieve DETAIL
class PostDetailView(generic.DetailView):
    model = Post
    template_name = "posts/post_detail.html"
    context_object_name = "post"


# Class Create
class PostCreateView(generic.CreateView):
    model = Post
    template_name = "posts/post_create.html"
    fields = ["title", "content", "status", "category", "cover"]
    success_url = reverse_lazy("index-page")


# Class DELETE
class PostDeleteView(generic.DeleteView):
    model = Post
    success_url = reverse_lazy("index-page")


# Class Update
class PostUpdateView(generic.UpdateView):
    model = Post
    template_name = "posts/post_update.html"
    fields = ["title", "content", "status", "category", "cover"]
    success_url = reverse_lazy("index-page")


# CRUD = Create, Read(Retrieve), Update, Delete

# Retrieve
def index_view(request):
    posts = Post.objects.all()
    context = {
        "title": "Главная страница",
        "posts": posts,
    }
    return render(request, "posts/index.html", context=context)


# Retrieve
def post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    return render(request, "posts/post_detail.html", {"post": post})


def contacts(request):
    context = {
        "title": "Контакты"
    }
    return render(request, "posts/contacts.html", context)


def about(request):
    context = {
        "title": "О нас"
    }
    return render(request, "posts/about.html", context)


# def post_delete(request, pk):
#     if request.method == "POST":
#         post = Post.objects.get(pk=pk)
#         post.delete()
#         return reverse_lazy("index-page")
#     return render(request, "posts/post_delete.html")


def post_update(request, pk):
    return render(request, "posts/post_update.html")

#
# def post_create(request):
#     if request.method == "POST":
#         post = Post.objects.create(title=request.POST.get("zagolovok"))
#     return render(request, "posts/post_create.html")