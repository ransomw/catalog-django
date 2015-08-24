from django import template

register = template.Library()

@register.filter('makeinput')
def makeinput(value, arg):
    args = [a.strip() for a in arg.split(',')]
    attrs = {'class': args[0]}
    if len(args) > 1:
        attrs.update({'placeholder': args[1]})
    if False: # todo XXX
        attrs.update({'value': ''})
    return value.as_widget(attrs=attrs)
