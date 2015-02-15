from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import auth
from photo import views

urlpatterns = patterns('',
    url(r'^polls/', include('polls.urls', namespace = "polls")),
    url(r'^photo/', include('photo.urls', namespace = "photo")),
    url(r'^signups/',include('signups.urls', namespace = "signups")),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login', name = 'mysite_login'),
    url(r'^accounts/logout/$', views.logout_view, name='mysite_logout'),

    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root = settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root = settings.MEDIA_ROOT)