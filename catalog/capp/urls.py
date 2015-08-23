from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    # todo: item titles and category names cannot be 'item'
    url(r'^item/new$',
        views.item_add,
        name='item_add'),
    url(r'^(?P<category_name>.+)/items$',
        views.items_list,
        name='items_list'),
    url(r'^(?P<item_title>.+)/edit$',
        views.item_edit,
        name='item_edit'),
    url(r'^(?P<item_title>.+)/delete$',
        views.item_delete,
        name='item_delete'),
    # todo: item titles cannot be 'items', 'edit', or 'delete'
    url(r'^(?P<category_name>.+)/(?P<item_title>.+)$',
        views.item_detail,
        name='item_detail')
    # url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail')
]
