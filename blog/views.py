from django.shortcuts import render
from .models import Post
# Create your views here.

def list(request):
    data = {'Posts': Post.objects.all().order_by('price')}
    return render(request, 'blog/blog.html', data)

