from django.shortcuts import render_to_response
from django.template import RequestContext  # TODO: is this needed?


def home(request):
    return render_to_response("blog/home.html", {},
                              context_instance=RequestContext(request))


def article(request, article_id):
    return render_to_response("blog/article.html", {},
                              context_instance=RequestContext(request))
