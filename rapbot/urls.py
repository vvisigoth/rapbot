from django.conf.urls.defaults import patterns, include, url
from django.views.generic import DetailView
from raps.models import Rap
from rapbot import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^raps/$','raps.views.index'),
    #url(r'^post/(?P<post_id>\d+)/$', 'post.views.post'),
     # DetailView.as_view(
       # model = Rap,
       # template_name = 'raps/index.html')),
    # Examples:
    # url(r'^$', 'lilbbot.views.home', name='home'),
    # url(r'^lilbbot/', include('lilbbot.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
if settings.DEBUG:
  urlpatterns += patterns('',
    (r'^mymedia/(?P<path>.*)$', 'django.views.static.serve',
    {'document_root': settings.MEDIA_ROOT}),
    )

