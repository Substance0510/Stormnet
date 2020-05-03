from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_page, name='main_page'),
    path('blog/', views.post_list, name='post_list'),
    path('homework/', views.homework, name='homework'),
    path('ded/', views.ded_moroz, name='ded_moroz'),
]