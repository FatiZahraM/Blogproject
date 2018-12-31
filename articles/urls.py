from django.urls import path
from .import views

app_name = 'articles'

urlpatterns = [
    path('article_list/', views.article_list, name='list'),
    path('article_create/', views.article_create, name='create'),
    path('<slug>/', views.article_detail, name='detail'),
]
