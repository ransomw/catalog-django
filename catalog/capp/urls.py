from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^(?P<category_name>.+)/items$',
        views.items_list,
        name='items_list'),
    url(r'^(?P<category_name>.+)/(?P<item_title>.+)$',
        views.item_detail,
        name='item_detail')
    # url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail')
]
