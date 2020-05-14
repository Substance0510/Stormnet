from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING)
    # on_delete=models.CASCADE - удаляет записи пользователя при далении самого пользователя.
    # blank=True - допускает отсутствие автора. null=True - заполняется пустая колонка значением null.
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(default=timezone.now)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class Comment(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, auto_created=True, on_delete=models.DO_NOTHING)
    created_date = models.DateTimeField(auto_now=True)
    text = models.TextField(max_length=1000)
    page = models.ForeignKey(Post, on_delete=models.DO_NOTHING)

    def __str__(self):
        return '%s, %s' % (self.author, self.created_date)
