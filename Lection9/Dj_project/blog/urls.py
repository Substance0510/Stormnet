from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.main_page, name='main_page'),
    path('blog/', views.post_list, name='post_list'),
    path('homework/', views.homework, name='homework'),
    re_path(r'^ded/$', views.ded_moroz, name='ded_moroz'),
    path('post/<int:post_id>', views.post, name='post'),
    path('logout/', views.logout_view, name='logout'),
    path('login/', views.login_view, name='login'),
    path('registration/', views.registration_view, name='registration')
]
