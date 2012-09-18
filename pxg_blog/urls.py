from django.conf.urls.defaults import *
from django.contrib import admin
admin.autodiscover()

handler500 = 'djangotoolbox.errorviews.server_error'

urlpatterns = patterns('',
     url(r'^admin/', include(admin.site.urls)),
    ('^$', 'blog.views.home'),
    (r'^article/(?P<article_id>\d+)$', 'blog.views.article'),
)
