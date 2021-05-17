from django.views.generic import ListView
from django.shortcuts import render

from articles.models import Article

class ArticleListView(ListView):
    model = Article
    template_name = 'articles/news.html'
    ordering = '-published_at'


