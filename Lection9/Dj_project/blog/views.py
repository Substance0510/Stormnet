from django.shortcuts import render
from django.utils import timezone
from . models import Post


def main_page(request):
    return render(request, 'blog/main_page.html')


def post_list(request):
    posts = Post.objects.all().order_by('-published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def homework(request):
    name = request.GET.get('name')
    if name is None:
        name = 'John Doo'
    print(name)
    type = request.GET.get('type')
    if type is None:
        type = 'Unknown'
    humanoid = request.GET.get('humanoid')
    if humanoid is None:
        humanoid = 'I don\'t know :('
    context = {'name': name,
               'name_lenght': len(name.replace(' ', '')),
               'name_reversed': name[::-1],
               'type': type,
               'humanoid': humanoid}
    return render(request, 'blog/homework.html', context=context)

def ded_moroz(request):
    return render(request, 'blog/ded_moroz.html')