from django import template
import re

register = template.Library()


@register.filter
def search(value):
    pattern = "(\/login\/\?next\=)(.*?$)"

    if re.search(pattern, value):
        return True

