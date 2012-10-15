from django.conf.urls.defaults import patterns, include, url
from mysite.noteblog.views import *
from django.contrib import admin
from mysite.settings import *
admin.autodiscover()
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', main_page),
    url(r'^user/$', user_page),
    url(r'^user/(?P<parm1>.+)$', reply),
    url(r'^login/$', 'django.contrib.auth.views.login',{'template_name':'login.html'}),
    url(r'^register/$',register),
    url(r'^logout/$',logout_page),
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve',{'document_root': STATIC_ROOT }),
    #url(r'^notebook/$', 'mysite.notebook.views.index' ),
    #url(r'^blog/(?P<parm1>\w+)/(?P<parm2>\w+)/$', 'mysite.blog.views.index', ),
    #url(r'^information/(?P<parm1>.*)$', 'mysite.information.views.index' ),
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^mysite/', include('mysite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

