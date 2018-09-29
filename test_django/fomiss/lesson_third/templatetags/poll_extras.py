from django import  template

register = template.Library()

@register.filter (name = "my_lower_filter")
def my_lover_filter(value):
    return value.lower()

