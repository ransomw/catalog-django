from pdb import set_trace as st

from django.shortcuts import render
from django.template import RequestContext
from django.contrib.auth.decorators import login_required

from .models import Category
from .models import Item

TEMPLATE_DIR = 'capp'

def home(request):
    categories = Category.objects.all()
    # todo: return only recent
    # todo: sort by modify time (desc)
    items = Item.objects.all()
    return render(request, TEMPLATE_DIR + '/home.html',
                  RequestContext(request,
                        {'categories': categories,
                         'items': items}))


def items_list(request, category_name):
    categories = Category.objects.all()
    # todo: errors on .get cases
    category = Category.objects.get(
        name__exact=category_name)
    # todo: use m2m relationship on category
    items = Item.objects.all().filter(
        category=category.pk)
    return render(request, TEMPLATE_DIR + '/items.html',
                  RequestContext(request,
                                 {'categories': categories,
                                  'items': items,
                                  'category': category}))


def item_detail(request, category_name, item_title):
    item = Item.objects.get(
        title__exact=item_title)
    return render(request, TEMPLATE_DIR + '/item.html',
                  RequestContext(request,
                                 {'item': item}))


@login_required
def item_add(request):
    return render(request, TEMPLATE_DIR + '/item_add_edit.html',
                  RequestContext(request,
                                 {'action': "Add"}))


# todo: check users's ownership before allowing to modify
#       do not allow deleting items w/o associated users
#       ... perhaps use a decorator function that takes
#           a test function as an argument

@login_required
def item_edit(request, item_title):
    return render(request, TEMPLATE_DIR + '/item_add_edit.html',
                  RequestContext(request,
                                 {'action': "Edit"}))


@login_required
def item_delete(request, item_title):
    return render(request, TEMPLATE_DIR + '/item_delete.html',
                  RequestContext(request,
                                 {}))
