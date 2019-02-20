
from django import template
from datetime import date, timedelta


register = template.Library()


# Create your models here.

@register.filter(name='subtract')
def subtract(value, arg):
    return value - arg

