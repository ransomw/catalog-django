from pdb import set_trace as st

from django.http import HttpResponseServerError
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.forms import model_to_dict
from django.core.urlresolvers import reverse

from .models import Category
from .models import Item
from .forms import ItemForm

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




# todo: remove duplicate add/edit code

@login_required
def item_add(request):
    def _render_form(form):
        return render(request, TEMPLATE_DIR + '/item_add_edit.html',
                      RequestContext(request,
                                     {'action': "Add",
                                      'form': form}))

    if request.method == 'GET':
        form = ItemForm()
        return _render_form(form)
    elif request.method == 'POST':
        form = ItemForm(request.POST)
        if not form.is_valid():
            return _render_form(form)
        item = form.save()
        item.user = request.user
        item.save()
        return HttpResponseRedirect(reverse('home'))


# todo: check users's ownership before allowing to modify
#       do not allow deleting items w/o associated users
#       ... perhaps use a decorator function that takes
#           a test function as an argument

@login_required
def item_edit(request, item_title):
    def _render_form(form):
        return render(request, TEMPLATE_DIR + '/item_add_edit.html',
                      RequestContext(request,
                                     {'action': "Edit",
                                      'form': form}))

    item = Item.objects.get(
        title__exact=item_title)
    if request.method == 'GET':
        # todo: read over model form code
        #       ... uncertain if this model_to_dict is the right way
        form = ItemForm(initial=model_to_dict(item), instance=item)
        return _render_form(form)
    elif request.method == 'POST':
        form = ItemForm(request.POST, instance=item)
        if not form.is_valid():
            return _render_form(form)
        item = form.save()
        item.user = request.user
        item.save()
        return HttpResponseRedirect(reverse('home'))


@login_required
def item_delete(request, item_title):
    if request.method == 'GET':
        return render(request, TEMPLATE_DIR + '/item_delete.html',
                      RequestContext(request,
                                     {}))
    elif request.method == 'POST':
        item = Item.objects.get(
            title__exact=item_title)
        item.delete()
        return HttpResponseRedirect(reverse('home'))
