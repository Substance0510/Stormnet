from django.shortcuts import render
from django.utils import timezone
from . models import Post

# Create your views here.


def main_page(request):
    return render(request, 'blog/main_page.html', {})


def post_list(request):
    posts = Post.objects.all().order_by('-published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def homework(request):
    name = request.GET.get('name')
    type = request.GET.get('type')
    humanoid = request.GET.get('humanoid')
    context = {'name': name,
               'name_lenght': len(name),
               'name_reversed': name[::-1],
               'type': type,
               'humanoid': humanoid}
    return render(request, 'blog/homework.html', context=context)