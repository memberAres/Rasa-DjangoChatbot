from django import template
from datetime import date, timedelta

register = template.Library()

@register.filter()
def redcolor(value):
    if value > 0 :
        return 200-value*100
    elif value < 0 :
        return 200
@register.filter()
def greencolor(value):
    if value > 0 :
        return 200
    elif value < 0 :
        return 100+value*100
