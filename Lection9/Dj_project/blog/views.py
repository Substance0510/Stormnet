from django.shortcuts import render, redirect
from django.contrib.auth.models import User, Group, AnonymousUser
from django.utils import timezone, dateformat
from django.http import Http404, HttpResponseRedirect, HttpResponseNotFound, HttpResponse
from datetime import datetime
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from . models import Post, Comment
from . forms import CommentForm, SignUpForm


def main_page(request):
    return render(request, 'blog/main_page.html')


def post_list(request):
    authors = User.objects.all().filter(is_staff=True)
    user_choise = request.GET.get('authors_filter')
    posts = Post.objects.all().filter(published_date__lte=timezone.now()).order_by('-published_date')
    value_date_max = max_date = dateformat.format(timezone.now(), 'Y-m-d')
    value_date_min = min_date = dateformat.format(posts.last().published_date, 'Y-m-d')
    archive_date_start = request.GET.get('archive_date_start')
    archive_date_stop = request.GET.get('archive_date_stop')
    get_params = request.GET

    # Чтобы работали фильтры одновременно с пагинацией, нам нужно передавать строку фильтров в GET,
    # при этом убирая параметр page из строки (.urlencode() - метод QuerySet для преобразования его в строку):
    url_params = '&'.join(['%s=%s' % (k, v) for k, v in get_params.items() if k != 'page'])
    url_params = '&' + url_params if url_params else url_params

    if archive_date_start and archive_date_stop:
        archive_date_start = datetime.strptime(archive_date_start, '%Y-%m-%d')
        archive_date_stop = datetime.strptime(archive_date_stop + ' 23:59:59', '%Y-%m-%d %H:%M:%S')
        posts = posts.filter(published_date__gte=archive_date_start,
                                          published_date__lte=archive_date_stop).order_by('-published_date')
        value_date_min = dateformat.format(archive_date_start, 'Y-m-d')
        value_date_max = dateformat.format(archive_date_stop, 'Y-m-d')

    if user_choise and user_choise != 'Все авторы':
        selected_author = User.objects.get(username=user_choise)
        posts = posts.filter(author=selected_author).order_by('-published_date')
    else:
        selected_author = None

    # Pagination block:
    paginator = Paginator(posts, 6)
    page = request.GET.get('page')
    try:
        pag_posts = paginator.page(page)
    except PageNotAnInteger:
        # Если страница не является целым числом, поставим первую страницу
        pag_posts = paginator.page(1)
    except EmptyPage:
        # Если страница больше максимальной, доставить последнюю страницу результатов
        pag_posts = paginator.page(paginator.num_pages)

    context = {'posts': pag_posts,
               'authors': authors,
               'selected_author': selected_author,
               'max_date': max_date,
               'min_date': min_date,
               'archive_date_start': archive_date_start,
               'archive_date_stop': archive_date_stop,
               'value_date_min': value_date_min,
               'value_date_max': value_date_max,
               'url_params': url_params,
               }

    return render(request, 'blog/post_list.html', context=context)

def homework(request):
    name = request.GET.get('name')
    if name is None or name == '':
        name = 'John Doo'
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


def post(request, post_id):
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
            post_comment.author = request.user
            post_comment.save()
            return HttpResponseRedirect(post_id)
    else:
        new_comment = CommentForm()
    context = {'id': post_id, 'selected_post': selected_post, 'comments': comments, 'new_comment': new_comment}
    return render(request, 'blog/post.html', context=context)


def view_404(request, exception):
    """
    Page not found Error 404
    """
    return render(request, 'blog/404.html')


def login_view(request):
    redirect_to = request.GET.get('next')
    if request.method == 'POST':
        user_form = AuthenticationForm(data=request.POST)
        if user_form.is_valid():
            user = user_form.get_user()
            login(request, user)
            return HttpResponseRedirect(redirect_to)
    else:
        user_form = AuthenticationForm()
    return render(request, 'blog/login_form.html', context={'user_form': user_form})


def logout_view(request):
    redirect_to = request.GET.get('next')
    if request.method == 'POST':
        logout(request)
    return HttpResponseRedirect(redirect_to)


def registration_view(request):
    redirect_to = request.GET.get('next')
    if request.method == 'POST':
        reg_form = SignUpForm(request.POST)
        if reg_form.is_valid():
            user = reg_form.save()
            default_group = Group.objects.get(name='user_group')
            default_group.user_set.add(user)
            login(request, user)
            return HttpResponseRedirect(redirect_to)
    else:
        reg_form = SignUpForm()
    context = {'reg_form': reg_form}
    return render(request, 'blog/registration.html', context=context)