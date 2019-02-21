from django.shortcuts import render
from .models import Article,Comment

# Create your views here.

def get_all_articles(request):
    article=Article.objects.all()
    context={
        'articles':article
    }
    # return render(request, 'website_templates/index.html',context)
    return article

def get_comments(request,requested):
    for article in requested:
        comment=Comment.objects.filter(article_id=article.article_id)
        return comment
