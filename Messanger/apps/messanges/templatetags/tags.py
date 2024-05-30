from django import template

register = template.Library()



@register.filter
def change_value(value, arg):
    value = arg
    return value