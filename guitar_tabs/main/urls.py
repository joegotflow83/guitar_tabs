from django.conf.urls import url

from main import views


urlpatterns = [
    url(r'^$', views.Search.as_view(), name='index'),
    url(r'^(?P<url>.*)/$', views.Tabs.as_view(), name='tabs'),
]
