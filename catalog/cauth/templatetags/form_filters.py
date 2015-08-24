from django import template

register = template.Library()

# todo: rename to cauth_extras

# @register.filter(name='addclass')
# def addclass(value, arg):
#     return value.as_widget(attrs={'class': arg})


@register.filter('makeinput')
def makeinput(value, arg):
    args = [a.strip() for a in arg.split(',')]
    return value.as_widget(attrs={
        'class': args[0],
        'placeholder': args[1]})
