from pdb import set_trace as st

from django.shortcuts import render

from .models import Category
from .models import Item

TEMPLATE_DIR = 'capp'

def home(request):
    categories = Category.objects.all()
    # todo: return only recent
    # todo: sort by modify time (desc)
    items = Item.objects.all()
    return render(request, TEMPLATE_DIR + '/home.html',
                  {'categories': categories,
                   'items': items})


def items_list(request, category_name):
    categories = Category.objects.all()
    # todo: errors on .get cases
    category = Category.objects.get(
        name__exact=category_name)
    # todo: use m2m relationship on category
    items = Item.objects.all().filter(
        category=category.pk)
    return render(request, TEMPLATE_DIR + '/items.html',
                  {'categories': categories,
                   'items': items,
                   'category': category})


def item_detail(request, category_name, item_title):
    item = Item.objects.get(
        title__exact=item_title)
    return render(request, TEMPLATE_DIR + '/item.html',
                  {'item': item})
