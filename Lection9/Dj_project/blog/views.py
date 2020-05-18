from django.shortcuts import render
from django.contrib.auth.models import User, AnonymousUser
from django.utils import timezone, dateformat
from django.http import Http404, HttpResponseRedirect
# from django.template import RequestContext
from . models import Post, Comment
from .forms import CommentForm


def main_page(request):
    return render(request, 'blog/main_page.html')


def post_list(request):
    authors = User.objects.all()
    user_choise = request.GET.get('authors_filter')
    selected_author = None
    posts = Post.objects.all().filter(published_date__lte=timezone.now()).order_by('-published_date')
    max_date = dateformat.format(timezone.now(), 'Y-m-d')
    min_date = dateformat.format(posts.last().published_date, 'Y-m-d')
    archive_date = request.GET.get('archive_date')

    if user_choise and user_choise != 'Все авторы':
        selected_author = User.objects.get(username=user_choise)
        posts = Post.objects.all().filter(author=selected_author).filter(published_date__lte=timezone.now())\
            .order_by('-published_date')

    if archive_date:
        posts = Post.objects.all().filter(published_date__contains=archive_date).order_by('-published_date')

    context = {'posts': posts,
               'authors': authors,
               'author': selected_author,
               'max_date': max_date,
               'min_date': min_date,
               'archive_date': archive_date}
    return render(request, 'blog/post_list.html', context=context)

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
    if not Post.objects.filter(pk=post_id).exists():
        raise Http404
    selected_post = Post.objects.get(pk=post_id)
    comments = Comment.objects.all().filter(page_id=post_id).order_by('-created_date')

    if selected_post.published_date > timezone.now():
        raise Http404

    if request.method == 'POST':
        new_comment = CommentForm(request.POST)
        if new_comment.is_valid():
            post_comment = new_comment.save(commit=False)
            post_comment.page = selected_post
            # post_comment.author = AnonymousUser()
            # post_comment.author = request.user
            post_comment.save()
            return HttpResponseRedirect('?id=% s' % post_id)
        #new_comment = CommentForm()
    else:
        new_comment = CommentForm()
    context = {'id': post_id, 'selected_post': selected_post, 'comments': comments, 'new_comment': new_comment}
    return render(request, 'blog/post.html', context=context)


# def view_404(request, exception):
#     """
#     Page not found Error 404
#     """
#     response = render('404.html', context=RequestContext(request))
#     response.status_code = 404
#     return response
