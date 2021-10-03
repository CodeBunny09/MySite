from django import template
from ..models import Author

register = template.Library()

@register.simple_tag
def author():
    return Author