# custom_filters.py
from django import template

register = template.Library()

@register.filter
def get_item(dictionary, key):
    """Fetch the value for a given key from the dictionary."""
    if isinstance(dictionary, dict):
        return dictionary.get(key)
    return None 
