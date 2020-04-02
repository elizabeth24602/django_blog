{"filter":false,"title":"urls.py","tooltip":"/django_blog/urls.py","undoManager":{"mark":1,"position":1,"stack":[[{"start":{"row":15,"column":0},"end":{"row":30,"column":1},"action":"remove","lines":["from django.conf.urls import url","from django.contrib import admin","","urlpatterns = [","    url(r'^admin/', admin.site.urls),","]","","from django.conf.urls import url","from .views import get_posts, post_detail, create_or_edit_post","","urlpatterns = [","    url(r'^$', get_posts, name='get_posts'),","    url(r'^(?P<pk>\\d+)/$', post_detail, name='post_detail'),","    url(r'^new/$', create_or_edit_post, name='new_post'),","    url(r'^(?P<pk>\\d+)/edit/$', create_or_edit_post, name='edit_post')","]"],"id":4}],[{"start":{"row":15,"column":0},"end":{"row":26,"column":1},"action":"insert","lines":["from django.conf.urls import url, include","from django.contrib import admin","from django.views.generic import RedirectView","from django.views.static import serve","from .settings import MEDIA_ROOT","","urlpatterns = [","    url(r'^admin/', admin.site.urls),","    url(r'^$', RedirectView.as_view(url='posts/')),","    url(r'^posts/', include('posts.urls')),","    url(r'^media/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT})","]"],"id":5}]]},"ace":{"folds":[],"scrolltop":11,"scrollleft":0,"selection":{"start":{"row":26,"column":1},"end":{"row":26,"column":1},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"hash":"b5f8e59dff8cae9f15c7d0edd2221e89feeaad3d","timestamp":1585578185738}