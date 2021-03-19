from django import template

register = template.Library()


@register.filter
def get_index(array, i):
    return array[i]
