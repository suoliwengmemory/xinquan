"""xinquan URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.views.static import serve


import xadmin
from News.views import news, newsdet
from Contact.views import contact
from Goods.views import goods, goodsdet
from Index.views import index
from Lesson.views import lesson
from Show.views import show
from Store.views import store,storedet
from XQ.views import xq

from xinquan.settings import MEDIA_ROOT


urlpatterns = [
    url(r'^xadmin/', xadmin.site.urls),
    url(r'^index/$', index, name='index'),
    url(r'^show/$', show, name='show'),
    url(r'^xq/$', xq, name='xq'),
    url(r'^goods/$', goods, name='goods'),
    url(r'^goodsdet/(?P<pk>[0-9]+)/$', goodsdet, name='goodsdet'),
    url(r'^store/$', store, name='store'),
    url(r'^storedet/(?P<pk>[0-9]+)/$', storedet, name='storedet'),
    url(r'^lesson/$', lesson, name='lesson'),
    url(r'^news/$', news, name='news'),
    url(r'^newsdet/(?P<pk>[0-9]+)/$', newsdet, name='newsdet'),
    url(r'^contact/$', contact, name='contact'),
    url(r'^media/(?P<path>.*)$', serve, {"document_root": MEDIA_ROOT}),
    url(r'^ueditor/', include('DjangoUeditor.urls'))
]
