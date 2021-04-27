from django import template

register = template.Library()

@register.filter()
def color(value):
    value = float(value)
    if value < 0:
        return '#008000'
    elif 0 <= value <= 1:
        return '#ffffff'
    elif 1 < value <= 2:
        return 'ff9999'
    elif 2 < value <= 5:
        return '#ff6666'

    return '#ff0000'