from django import template

register = template.Library()


@register.filter()
def loop(low: int, high: int) -> range:
    return range(low, high + 1)
