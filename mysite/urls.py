from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('blog.urls')),
url(r'^$', views.post_list, name='post_list'),
]
