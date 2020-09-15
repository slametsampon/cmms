# coding=utf-8
from django.template import Library

register = Library()


@register.filter
def get_item(value_dict, key):
    return value_dict.get(key)

@register.filter
def get_count(value_dict):
    return len(value_dict)
