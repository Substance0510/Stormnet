from django.shortcuts import render
from django.contrib.auth.models import User
from django.utils import timezone
from . models import Post


def main_page(request):
    return render(request, 'blog/main_page.html')


def post_list(request):
    authors = User.objects.all()
    user_choise = request.GET.get('authors_filter')
    selected_author = None
    if user_choise and user_choise != 'Все авторы':
        selected_author = User.objects.get(username=user_choise)
        posts = Post.objects.all().filter(author=selected_author).order_by('-published_date')
    else:
        posts = Post.objects.all().order_by('-published_date')
    return render(request, 'blog/post_list.html', {'posts': posts, 'authors': authors, 'author': selected_author})

def homework(request):
    name = request.GET.get('name')
    if name is None or name == '':
        name = 'John Doo'
    print(name)
    type = request.GET.get('type')
    if type is None or type == '':
        type = 'Unknown'
    humanoid = request.GET.get('humanoid')
    if humanoid is None or humanoid == '':
        humanoid = 'I don\'t know :('
    context = {'name': name,
               'name_lenght': len(name.replace(' ', '')),
               'name_reversed': name[::-1],
               'type': type,
               'humanoid': humanoid}
    return render(request, 'blog/homework.html', context=context)

def ded_moroz(request):
    return render(request, 'blog/ded_moroz.html')

def post(request):
    post_id = request.GET.get('id')
    selected_post = Post.objects.get(pk=post_id)
    context = {'id': post_id, 'selected_post': selected_post}
    return render(request, 'blog/post.html', context=context)