from django.shortcuts import render_to_response
from django.template import RequestContext  # TODO: is this needed?
from blog.models import Article


def home(request):
    articles = Article.objects.order_by('created_at')
    return render_to_response("blog/home.html", {"articles": articles},
                              context_instance=RequestContext(request))


def article(request, article_id):
    return render_to_response("blog/article.html", {},
                              context_instance=RequestContext(request))
