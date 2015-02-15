from django.conf.urls import patterns, url
from django.conf import settings
from django.conf.urls.static import static
from photo import views
from django.contrib import auth


urlpatterns = patterns('',
    url(r'^image/(?P<pk>\d+)/$', views.ImageView.as_view(),name='image-view'),
    url(r'^$', views.TopImage.as_view(),name ='Photo-top'),
    url(r'^author/$', views.ListAuthor.as_view(),name ='Author-List'),
    url(r'^author/(?P<pk>\d+)/', views.AuthorView.as_view(),name='author-view',),
    url(r'^image/$', views.ListImage.as_view(),name ='List-Photo'),
    url(r'^signup/$', views.AuthorCreate.as_view(), name = 'create-author'),
    url(r'^image/add/$', views.ImageCreate.as_view(), name = 'create-image'),
    url(r'update/(?P<pk>\d+)/$', views.ImageUpdate.as_view(),name='image-update'),
    url(r'^image/delete/(?P<pk>\d+)/$', views.ImageDelete.as_view(), name='image-delete'),
    url(r'^image/like/(?P<pk>\d+)/$', views.ImageLike),
    url(r'^signup/createuser/(?P<pk>\d+)/$', views.CreateUser, name = 'create-user'),
) 

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root = settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root = settings.MEDIA_ROOT)
