from django.shortcuts import render_to_response
from django.template import RequestContext
from django.shortcuts import get_object_or_404
from blog.models import Article


def home(request):
    articles = Article.objects.order_by('-created_at')
    return render_to_response("blog/home.html", {"articles": articles},
                              context_instance=RequestContext(request))


def article(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    return render_to_response("blog/article.html", {"article": article},
                              context_instance=RequestContext(request))
