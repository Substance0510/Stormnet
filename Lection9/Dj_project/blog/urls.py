from django.urls import path
from . import views

handler404 = 'blog.views.view_404'

urlpatterns = [
    path('', views.main_page, name='main_page'),
    path('blog/', views.post_list, name='post_list'),
    path('homework/', views.homework, name='homework'),
    path('ded/', views.ded_moroz, name='ded_moroz'),
    path('post/', views.post, name='post'),
]
