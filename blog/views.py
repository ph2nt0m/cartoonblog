from django.shortcuts import render, get_object_or_404

from django.http import HttpResponse
from .models import Post
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.
def BlogList(request, pk=None):
    q = request.GET.get("q",None)
    
    if pk is not None and q is None:
        post = get_object_or_404(Post, pk=pk)
        return render(request, "blogdetail.html", {"post":post})

    posts = Post.objects.all()
    if q is not None:
        lookup = Q(title__icontains=q) | Q(description__icontains=q)
        posts = posts.filter(lookup).distinct()
    page = request.GET.get('page', 1)
    paginator = Paginator(posts, 4) 
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return render(request, "bloglist.html", {"posts":posts})

    # return HttpResponse("<h1>Welcome Blog</h1>")