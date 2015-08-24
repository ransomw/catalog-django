from pdb import set_trace as st

from django.forms import ModelForm

from .models import Item

class ItemForm(ModelForm):

    class Meta:
        model = Item
        fields = [
            'title',
            'description',
            'category',
        ]
